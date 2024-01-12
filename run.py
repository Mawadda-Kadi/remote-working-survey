import gspread
from google.oauth2.service_account import Credentials
from scipy.stats import pearsonr

# Connect to the Google Spreadsheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


""" Functions """


def collect_survey_responses(questions):
    """
    Function to collect survey responses
    """
    responses = {}

    """ A for loop to iterate through each question and present it to
    the user using the input function, and then validiate the user's
    input based on the provided validation function """

    for question_id, question, validation_function in questions:
        print(question)
        user_response = validation_function(question)
        responses[question_id] = user_response
        print("\n--------------------------\n")

    print("\nSurvey Responses")
    print("================\n")
    print(responses)
    print("-------------------------\n")
    return responses


def validate_numeric_input(prompt):
    """
    Function to validate numeric input
    """
    while True:
        try:
            user_input = int(input(""))
            return user_input
        except ValueError:
            print("\nPlease enter a valid numeric value")


def validate_input_range(prompt, min_value, max_value):
    """
    Function to validate input within a specified range
    """
    while True:
        # Ensure first that the input is an int
        user_input = validate_numeric_input(prompt)
        # Ensure that the input is within the specified range
        try:
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"\nPlease enter a value between {min_value} and {max_value}")
        except ValueError:
            print("\nPlease enter a valid numeric value")


def update_worksheet(data, worksheet_name):
    """ Function to update a specified worksheet with new data and
    appropriately handles both worksheets based on their unique
    requirements """

    worksheet = SHEET.worksheet(worksheet_name)

    if worksheet_name == 'responses':
        # Map numeric responses to their corresponding labels and append
        mapped_data = [LABELS.get(key, {}).get(value, value) for key, value in data.items()]
        worksheet.append_row(mapped_data)

    elif worksheet_name == 'data_analysis':
        # Clear and update 'data_analysis' worksheet
        total_rows = len(worksheet.get_all_values())
        if total_rows > 1:
            range_to_clear = f'A2:Z{total_rows}'
            worksheet.batch_clear([range_to_clear])
        # Initialize a list to store formatted rows
        formatted_rows = []
        for key, values in data.items():
            if isinstance(values, dict):
                # For data with subcategories
                for sub_key, sub_value in values.items():
                    formatted_rows.append([f"{key} - {sub_key}", sub_value])
            else:
                # For single numeric values
                formatted_rows.append([key, values])
        worksheet.insert_rows(formatted_rows, 2)
    print(f"{worksheet_name} worksheet updated successfully\n")


def fetch_data(sheet):
    """
    Function to get all data from a particular
    worksheet, excluding the header row
    """
    return sheet.get_all_records(default_blank=0)


def analyze_data(all_responses):
    """
    Function to perform analysis on all survey responses
    """
    analysis_results = {}
    num_responses = len(all_responses)

    print("Responses Data is being analyzed ...\n")

    # Calculate percentage of 'Yes' and 'No' responses for work_life_balance_challenges and productivity_improvement
    yes_no_questions = ['work_life_balance_challenges', 'productivity_improvement']
    for question in yes_no_questions:
        yes_count = sum(1 for response in all_responses if response.get(question) == 'Yes')
        no_count = sum(1 for response in all_responses if response.get(question) == 'No')
        total = yes_count + no_count

        # Avoid division by zero
        if total > 0:
            yes_percentage = (yes_count / total) * 100
            no_percentage = (no_count / total) * 100
        else:
            yes_percentage = no_percentage = 0

        analysis_results[f'{question} Yes Percentage'] = yes_percentage
        analysis_results[f'{question} No Percentage'] = no_percentage

    # Satisfaction Analysis
    satisfaction_counts = {label: sum(1 for response in all_responses if response.get('satisfaction') == label) for label in LABELS['satisfaction'].values()}
    analysis_results['Satisfaction Counts'] = satisfaction_counts

    # Remote Work Setup Analysis
    remote_work_setup_counts = {label: sum(1 for response in all_responses if response.get('remote_work_setup') == label) for label in LABELS['remote_work_setup'].values()}
    analysis_results['Remote Work Setup Counts'] = remote_work_setup_counts

    # Technical Issues Analysis
    technical_issues_counts = {label: sum(1 for response in all_responses if response.get('technical_issues') == label) for label in LABELS['technical_issues'].values()}
    analysis_results['Technical Issues Counts'] = technical_issues_counts

    # Work-Life Balance Challenges Analysis
    work_life_balance_counts = {label: sum(1 for response in all_responses if response.get('work_life_balance_challenges') == label) for label in LABELS['work_life_balance_challenges'].values()}
    analysis_results['Work-Life Balance Challenges Counts'] = work_life_balance_counts

    # Productivity Improvement Analysis
    productivity_improvement_counts = {label: sum(1 for response in all_responses if response.get('productivity_improvement') == label) for label in LABELS['productivity_improvement'].values()}
    analysis_results['Productivity Improvement Counts'] = productivity_improvement_counts

    # Work Model Preference Analysis
    work_model_preference_counts = {label: sum(1 for response in all_responses if response.get('work_model_preference') == label) for label in LABELS['work_model_preference'].values()}
    analysis_results['Work Model Preference Counts'] = work_model_preference_counts

    # Average Daily Work Hours Analysis
    total_work_hours = sum(response.get('average_daily_work_hours', 0) for response in all_responses)
    average_daily_work_hours = total_work_hours / num_responses if num_responses > 0 else 0
    analysis_results['Average Daily Work Hours'] = average_daily_work_hours

    analysis_results['Average Daily Work Hours'] = average_daily_work_hours

    # Work Duration Analysis
    work_duration_counts = {label: sum(1 for response in all_responses if response.get('work_duration') == label) for label in LABELS['work_duration'].values()}
    analysis_results['Work Duration Counts'] = work_duration_counts

    # Experience Years Analysis
    total_experience_years = sum(response.get('experience_years', 0) for response in all_responses)
    average_experience_years = total_experience_years / num_responses if num_responses > 0 else 0
    analysis_results['Average Experience Years'] = average_experience_years

    analysis_results['Average Experience Years'] = average_experience_years

    # Convert textual responses to numeric values
    satisfaction_numeric = [1 if res['satisfaction'] == 'Very Satisfied' else
                            2 if res['satisfaction'] == 'Satisfied' else
                            3 if res['satisfaction'] == 'Neutral' else
                            4 if res['satisfaction'] == 'Dissatisfied' else
                            5 for res in all_responses]

    productivity_numeric = [1 if res['productivity_improvement'] == 'Yes' else 0 for res in all_responses]

    # Calculate correlation
    if satisfaction_numeric and productivity_numeric:
        correlation = pearsonr(satisfaction_numeric, productivity_numeric)[0]
        analysis_results['Satisfaction-Productivity Improvement Correlation'] = correlation

    print("Responses Data analyzed successfully\n")

    return analysis_results


def print_analysis_report(analysis_results):
    """
    Function to print the analysis report through iterating over the
    analysis_results dictionary. For each entry:
    If the value is a dictionary (for categories with subcategories),
    the category and then each subcategory are printed with its count.
    If the value is a single number,
    the category and its value are printed directly.
    """
    print("Survey Analysis Report")
    print("======================\n")

    for key, value in analysis_results.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  - {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")

        #Separator line
        print("----------------------------------")

    print("\nEnd of Report\n")


""" Survey Questions and Validation """

""" This is the questions list. Each question is represented as a tuple,
where the first element is a unique identifier for the question, the second
element is the text of the question, and the third element is a validation
function """

questions = [
    ("employee_id", "Please enter your employee ID (numeric format only): \n", validate_numeric_input),
    ("satisfaction", "How would you rate your overall satisfaction with working from home?\n1. Very Satisfied\n2. Satisfied\n3. Neutral\n4. Dissatisfied\n5. Very Dissatisfied\n", lambda x: validate_input_range("Enter your choice (1-5): ", 1, 5)),
    ("remote_work_setup", "Which of the following best describes your remote work setup?\n1. Dedicated home office\n2. Shared workspace with others\n3. No dedicated workspace\n", lambda x: validate_input_range("Enter your choice (1-3): ", 1, 3)),
    ("technical_issues", "How often do you encounter technical issues while working from home?\n1. Rarely or never\n2. Occasionally\n3. Frequently\n", lambda x: validate_input_range("Enter your choice (1-3): ", 1, 3)),
    ("work_life_balance_challenges", "Have you experienced challenges in maintaining work-life balance while working from home?\n1. Yes\n2. No\n", lambda x: validate_input_range("Enter your choice (1-2): ", 1, 2)),
    ("productivity_improvement", "Have you experienced an improvement in your productivity since working from home?\n1. Yes\n2. No\n3. No change\n", lambda x: validate_input_range("Enter your choice (1-3): ", 1, 3)),
    ("work_model_preference", "Would you prefer a hybrid work model (a mix of remote and in-office work) in the future?\n1. Yes, I prefer a hybrid model\n2. No, I prefer fully remote work\n3. No, I prefer fully in-office work\n4. Undecided\n", lambda x: validate_input_range("Enter your choice (1-4): ", 1, 4)),
    ("average_daily_work_hours", "On average, how many hours per day do you work remotely? [Numeric value in hours]\n", lambda x: validate_input_range("Enter the number of hours: ", 1, 24)),
    ("work_duration", "How long have you worked remotely?\n1. Less than 6 months\n2. 6 months to 1 year\n3. 1 year to 2 years\n4. More than 2 years\n", lambda x: validate_input_range("Enter your choice (1-4): ", 1, 4)),
    ("experience_years", "How many years of experience do you have in your current role? [Value in years]\n", lambda x: validate_input_range("Enter the number of years: ", 0, 60))
]

# Define a dictionary to map numeric responses to labels
LABELS = {
    'satisfaction': {1: 'Very Satisfied', 2: 'Satisfied', 3: 'Neutral', 4: 'Dissatisfied', 5: 'Very Dissatisfied'},
    'remote_work_setup': {1: 'Dedicated home office', 2: 'Shared workspace with others', 3: 'No dedicated workspace'},
    'technical_issues': {1: 'Rarely or never', 2: 'Occasionally', 3: 'Frequently'},
    'work_life_balance_challenges': {1: 'Yes', 2: 'No'},
    'productivity_improvement': {1: 'Yes', 2: 'No', 3: 'No change'},
    'work_model_preference': {1: 'Yes, I prefer a hybrid model', 2: 'No, I prefer fully remote work', 3: 'No, I prefer fully in-office work', 4: 'Undecided'},
    'work_duration': {1: 'Less than 6 months', 2: '6 months to 1 year', 3: '1 year to 2 years', 4: 'More than 2 years'}
}


def main():
    """
    Run all program functions
    """
    responses = collect_survey_responses(questions)
    update_worksheet(responses, 'responses')
    all_responses = fetch_data(RESPONSES_SHEET)
    analysis_results = analyze_data(all_responses)
    update_worksheet(analysis_results, 'data_analysis')
    print_analysis_report(analysis_results)


# Ensure to be executed only when the script is run directly
if __name__ == "__main__":

    # Add Credentials
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

    # Open the spreadsheet
    SHEET = GSPREAD_CLIENT.open('remote_working_survey')
    # Select a single worksheet
    RESPONSES_SHEET = SHEET.worksheet('responses')
    DATA_ANALYSIS_SHEET = SHEET.worksheet('data_analysis')

    print("\nWelcome to Remote Working Survey Analysis\n")

    # Program Exit
    exit_survey = False
    while exit_survey is False:
        main()
        user_input = input("Thank you for your participation.\nEnter 'exit' to close the program, any key to restart: \n")
        exit_survey = user_input.lower() == 'exit'
