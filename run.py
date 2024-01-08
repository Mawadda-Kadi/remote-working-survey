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
responses_sheet = SHEET.worksheet('questions & responses') 

# to get all values form a single worksheet  
data = responses_sheet.get_all_values() 

""" Survey Questions and Validation """

""" This is the questions list. Each question is represented as a tuple,
where the first element is a unique identifier for the question, the second
element is the text of the question, and the third element is a validation 
function """

questions = [
    ("employee_id", "Please enter your employee ID (numeric format only): ", validate_numeric_input),
    ("satisfaction", "How would you rate your overall satisfaction with working from home?\n1. Very Satisfied\n2. Satisfied\n3. Neutral\n4. Dissatisfied\n5. Very Dissatisfied\n", lambda x: validate_input_range("Enter your choice (1-5): ", 1, 5)),
    ("remote_work_setup", "Which of the following best describes your remote work setup?\n1. Dedicated home office\n2. Shared workspace with others\n3. No dedicated workspace\n", lambda x: validate_input_range("Enter your choice (1-3): ", 1, 3))
]

# to collect survey responses
responses = {}

""" to iterate through each question and present it to the user using
the input function, and then validiate the user's input based on the 
provided validation function """

for question_id, question, validation_function in questions:
    user_response = validate_function(question)
    responses[question_id] = user_response




