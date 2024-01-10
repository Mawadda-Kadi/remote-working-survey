import gspread 

from google.oauth2.service_account import Credentials 

SCOPE = [ 
    "https://www.googleapis.com/auth/spreadsheets", 
    "https://www.googleapis.com/auth/drive.file", 
    "https://www.googleapis.com/auth/drive" 
    ] 

CREDS = Credentials.from_service_account_file('creds.json') 

SCOPED_CREDS = CREDS.with_scopes(SCOPE) 

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS) 

# to open the spread sheet 
SHEET = GSPREAD_CLIENT.open('remote_working_survey')
 
# to select a single worksheet 
responses_sheet = SHEET.worksheet('questions&responses') 

# to get all values form a single worksheet  
data = responses_sheet.get_all_values() 

""" Functions """

def validate_numeric_input(num):
    """ Function to validate numeric input """
    while True:
        try:
            user_input = int(input(num))
            return user_input
        except ValueError:
            print("Please enter a valid numeric value\n")

def validate_input_range(num, min_value, max_value):
    """ Function to validate input within a specified range """
    while True:
        # to ensure first that the input is an int
        user_input = validate_numeric_input(num)
        # to ensure that the input is within the specified range
        try:
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a value between {min_value} and {max_value}\n")
        except ValueError:
            print("Please enter a valid numeric value\n")

def update_worksheet(data, worksheet):
    """
    Receives a list of responses to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    # to map numeric responses to their corresponding labels
    mapped_data = [LABELS.get(key, {}).get(value, value) for key, value in data.items()]
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(mapped_data)
    print(f"{worksheet} worksheet updated successfully\n")


""" Survey Questions and Validation """

""" This is the questions list. Each question is represented as a tuple,
where the first element is a unique identifier for the question, the second
element is the text of the question, and the third element is a validation 
function """

questions = [
    ("employee_id", "Please enter your employee ID (numeric format only): ", validate_numeric_input),
    ("satisfaction", "How would you rate your overall satisfaction with working from home?\n1. Very Satisfied\n2. Satisfied\n3. Neutral\n4. Dissatisfied\n5. Very Dissatisfied\n", lambda x: validate_input_range("Enter your choice (1-5): ", 1, 5)),
    ("remote_work_setup", "Which of the following best describes your remote work setup?\n1. Dedicated home office\n2. Shared workspace with others\n3. No dedicated workspace\n", lambda x: validate_input_range("Enter your choice (1-3): ", 1, 3)),
    ("technical_issues", "How often do you encounter technical issues while working from home?\n1. Rarely or never\n2. Occasionally\n3. Frequently\n", lambda x: validate_input_range("Enter your choice (1-3): ", 1, 3)),
    ("work_life_balance_challenges", "Have you experienced challenges in maintaining work-life balance while working from home?\n1. Yes\n2. No\n", lambda x: validate_input_range("Enter your choice (1-2): ", 1, 2)),
    ("productivity_improvement", "Have you experienced an improvement in your productivity since working from home?\n1. Yes\n2. No\n3. No change\n", lambda x: validate_input_range("Enter your choice (1-3): ", 1, 3)),
    ("work_model_preference", "Would you prefer a hybrid work model (a mix of remote and in-office work) in the future?\n1. Yes, I prefer a hybrid model\n2. No, I prefer fully remote work\n3. No, I prefer fully in-office work\n4. Undecided\n", lambda x: validate_input_range("Enter your choice (1-4): ", 1, 4)),
    ("average_daily_work_hours", "On average, how many hours per day do you work remotely? [Numeric value in hours]\n", lambda x: validate_input_range("Enter the number of hours: ", 1, 24)),
    ("experience_years", "How many years of experience do you have in your current role? [Positive integer value]\n", lambda x: validate_input_range("Enter the number of years: ", 1, float('inf')))
]

# to define a dictionary to map numeric responses to labels
LABELS = {
    'satisfaction': {1: 'Very Satisfied', 2: 'Satisfied', 3: 'Neutral', 4: 'Dissatisfied', 5: 'Very Dissatisfied'},
    'remote_work_setup': {1: 'Dedicated home office', 2: 'Shared workspace with others', 3: 'No dedicated workspace'},
    'technical_issues': {1: 'Rarely or never', 2: 'Occasionally', 3: 'Frequently'},
    'work_life_balance_challenges': {1: 'Yes', 2: 'No'},
    'productivity_improvement': {1: 'Yes', 2: 'No', 3: 'No change'},
    'work_model_preference': {1: 'Yes, I prefer a hybrid model', 2: 'No, I prefer fully remote work', 3: 'No, I prefer fully in-office work', 4: 'Undecided'},
    'average_daily_work_hours': 'Numeric value in hours',
    'experience_years': 'Positive integer value'
}

# to collect survey responses
responses = {}

""" to iterate through each question and present it to the user using
the input function, and then validiate the user's input based on the 
provided validation function """

for question_id, question, validation_function in questions:
    print(question)
    user_response = validation_function(question)
    responses[question_id] = user_response

print(responses)

""" Write responses to the sheet """
response_values = {key: responses.get(key, "") for key in ["employee_id", "satisfaction", "remote_work_setup", ]}
update_worksheet(response_values, 'questions&responses')

print("Survey response recorded successfully.../n")



