# Remote Working Survey Analysis

Thank you all for participating in our survey. Your insights are valuable in understanding the nuances of remote working.

## Overview

This Python-based project is designed to collect and analyze survey data related to remote working. Utilizing Google Sheets API for data storage and management, and incorporating statistical analysis with the scipy library, this application provides insights into the impacts and challenges of remote working.

The live link can be found here: [Remote Working Survey](https://remote-working-survey-7d3459fee416.herokuapp.com/)

The Google Spreadsheet link: [Google Sheet](https://docs.google.com/spreadsheets/d/188cmXlzrPtkhoqi-mFS6WpQ_FLD8M2zr_rruXRsZfAc/edit#gid=0)

![python overwiew](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/4bc1c794-c541-4e88-a9c5-73746ebb615e)

## How to Participate in the Survey

Participating in the Remote Working Survey is a straightforward process. Follow these steps to complete the survey:

### Accessing the Survey

Visit the survey link [Remote Working Survey](https://remote-working-survey-7d3459fee416.herokuapp.com/)

### Starting the Survey

The survey app will be running automatically once you enter.

### Answering Questions

The survey consists of 10 questions covering various aspects of remote working.

Read each question carefully and provide your response. Responses require only numeric inputs.

### Input Validation

The survey includes input validation for accurate data collection. If an input is not valid (for example, non-numeric input where a number is expected), you will be prompted to re-enter the correct data.

Make sure to answer all required questions to proceed to the next section.

### Completing the Survey

After answering all the questions, you can review your responses.

Your responses will be submitted in the Google Spreadsheet and you will receive a confirmation message.

### Analysing Data

The new data will be analysed and calculated, then you may view a summary of general survey results.

### Confidentiality and Data Use

Be assured that your responses will be kept confidential and used solely for the purposes outlined in the survey introduction.

## Site Owner Goals

The primary goals of this project are:

1. **Provide Insightful Data Analysis**: Offer users comprehensive analysis of remote working trends and impacts.
![python analysis report](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/4e61ef5d-213d-4a78-bc31-cc30827773cc)

2. **User-Friendly Experience**: Ensure that the application is easy to navigate and use, even for those with limited technical background.
3. **Promote Data-Driven Decisions**: Assist organizations and individuals in making informed decisions based on the analysis provided.
4. **Encourage Community Involvement**: Create an open-source platform that encourages collaboration and contributions from the wider community.

## User Stories

- **As a remote worker**, I want to participate in surveys so that I can share my experiences and challenges.
- **As a team leader**, I want to understand the common issues faced in remote working to improve my team's productivity and work-life balance.
- **As a data analyst**, I need a tool that can provide detailed analysis of survey data to identify trends in remote working.
- **As a project contributor**, I want clear documentation and easy-to-understand code to contribute effectively to the project.

## Logic Flow

The application follows a structured logic flow:

1. **Survey Initiation**: The user starts the survey and responds to various questions, with input validation at each step.
2. **Data Storage**: Responses are securely transmitted and stored in Google Sheets.
3. **Data Analysis**: Upon completion of the survey, the application performs statistical analysis on the collected data.
4. **Result Presentation**: Analyzed data is presented to the user in an understandable format, highlighting key insights and trends.
5. **Continuous Operation**: The application loops back, allowing for new survey participation or analysis of updated data.

## Features

### Survey Data Collection

Interactive survey questionnaire with validation to ensure accurate data collection.

Questions covering various aspects of remote working, such as satisfaction, technical issues, and work-life balance.

### Google Sheets API Integration

Data storage and retrieval using Google Sheets, enabling easy access and management of survey responses.

Automated data updating for both responses and analysis results.

The Google Spreadsheet link: [Google Sheet](https://docs.google.com/spreadsheets/d/188cmXlzrPtkhoqi-mFS6WpQ_FLD8M2zr_rruXRsZfAc/edit#gid=0)

![responses sheet](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/f5f6e1fc-c8e1-4427-83c8-331b575a82df)
![data analysis sheet](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/27472410-6754-4644-b968-f0cc706bb002)

### Data Analysis

Comprehensive analysis of survey data, including calculation of percentages, averages, and correlations.

Use of `scipy.stats.pearsonr` for calculating correlations between different survey aspects.



### User Interface

- Console-based interaction for survey participation and viewing analysis results.

![python analysis report](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/4e61ef5d-213d-4a78-bc31-cc30827773cc)

- Clear instructions and feedback provided to the user throughout the application.

![python input validation](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/8fcc330e-34c3-4a17-bd8c-bebf86fa0e30)

### Error Handling and Validation

- Robust error handling and input validation for reliable application performance.
- Ensures data integrity and accuracy.

![python input validation](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/8fcc330e-34c3-4a17-bd8c-bebf86fa0e30)

### Security

- Secure handling of sensitive information, such as API credentials, using best practices.

## Data Model

The Remote Working Survey Analysis application is built on a robust data model that ensures efficient data collection, storage, and analysis. Here's an overview of our data model:

### Survey Structure

- **Questions**: The survey comprises various questions designed to gather comprehensive information on remote working experiences. Questions are formatted as multiple-choice, numeric input, or free text, depending on the nature of the data being collected.
- **Response Options**: For multiple-choice questions, each option is assigned a unique identifier for easy analysis and interpretation.

### Data Storage

- **Google Sheets Integration**: Responses are directly stored in a Google Sheets spreadsheet. Each response corresponds to a row, with columns representing different questions.
- **Worksheets**: The spreadsheet is divided into different worksheets for responses and data analysis. This separation ensures organized and efficient data handling.
![responses sheet](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/f5f6e1fc-c8e1-4427-83c8-331b575a82df)
![data analysis sheet](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/27472410-6754-4644-b968-f0cc706bb002)

### Data Processing

- **Input Validation**: Responses are validated at the point of entry to ensure data integrity. This includes checks for valid numeric values, required fields, and appropriate response formats.

![python survey responses](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/3f6d27fd-8f03-41f1-a3b3-93d405a5a5fa)

- **Data Mapping**: Numeric responses are mapped to corresponding textual labels using a predefined dictionary. This enhances the readability and interpretability of the data during analysis.

### Data Analysis

- **Statistical Analysis**: Utilizing Python libraries such as `scipy`, the application performs various statistical analyses including averages, percentages, and correlation calculations.
- **Dynamic Analysis**: The analysis is dynamically updated as new survey data is entered, providing real-time insights.

### Security and Privacy

- **Confidentiality**: Personal information (ID Number) is handled with utmost confidentiality and is not used for any purpose other than the stated objectives of the survey.
- **Data Access Control**: Access to the data is restricted and managed through Google Sheets' sharing and access control features.

### Future Enhancements

- **Adaptive Questionnaires**: Plans to implement dynamic questionnaires where questions adapt based on previous responses.
- **Advanced Analytics**: Incorporation of more sophisticated data analysis techniques for deeper insights.

## Bugs Fixed

- **Displaying Corresponding Labels for Numeric Responses**:
  - **Bug**: Numeric responses in the survey were not correctly displaying their corresponding labels.
  - **Fix**: Implemented a mapping mechanism using a labels dictionary to translate numeric responses into understandable text.

- **Handling Non-numeric Data in Analysis**:
  - **Bug**: Encountered issues with non-numeric data during analysis, leading to errors.
  - **Fix**: Converted relevant data into numeric values to facilitate accurate analysis.

- **Preserving Headers in Data Analysis Sheet**:
  - **Bug**: The header row was being cleared when updating the second worksheet (data_analysis).
  - **Fix**: Modified the `update_worksheet` function to clear and update the worksheet while preserving the header row.

- **Adapting `update_worksheet` for Different Sheet Requirements**:
  - **Bug**: The `update_worksheet` function was not adequately handling the specific needs of different worksheets.
  - **Fix**: Refined the function to cater to the unique update requirements of both the 'responses' and 'data_analysis' worksheets, ensuring appropriate data handling for each.

- **Long Question Text Display in Console**:
  - **Bug**: Long survey question text was not displaying correctly, getting cut off in the console.
  - **Fix**: Integrated newline characters (\n) within survey questions to ensure proper display across all environments.

- **Compliance with Python's PEP 8 Style Guide**:
  - **Bug**: Code lines exceeded the recommended length, affecting readability.
  - **Fix**: Reformatted long lines manually to comply with PEP 8 style guidelines, improving code readability and maintenance.

- **Environment-Specific Display Issues**:
  - **Bug**: Discrepancies in text display between local and Heroku environments.
  - **Fix**: Adjusted text formatting to ensure consistent display across different platforms, including Heroku web applications and local consoles.

- **Error Handling in Survey Question Processing**:
  - **Bug**: A code error caused a failure in processing certain survey questions.
  - **Fix**: Corrected the structure and syntax in the survey question processing logic, preventing runtime errors.

## Testing

### PEP8 Compliance Testing

- **Tools Used**: PEP8 Online checker.
- **Process**: `run.py` Python file in our project was rigorously checked using the PEP8 Online tool.
- **Outcome**: It was confirmed to be PEP8 compliant with no errors reported.
- **Screenshots**: Provided below for evidence of PEP8 compliance.
![python validator](https://github.com/Mawadda-Kadi/love-maths/assets/151715427/f8725e5a-695a-4892-8f7f-f462e7e61af9)

### Input Testing

Extensive input testing was conducted to ensure accurate data collection and user interaction:

- **Survey Responses**:
  - **Test Case**: Validation of survey responses, including numeric inputs and range inputs.
  - **Method**: Used custom validation functions to check for valid numeric input and correct selection from available options.
  - **Result**: The application correctly handles invalid inputs and prompts the user for re-entry.

- **Google Sheets API Integration**:
  - **Test Case**: Ensuring that data is accurately sent to and retrieved from Google Sheets.
  - **Method**: Conducted tests to submit sample survey data and then fetch it.
  - **Result**: Data was successfully updated and retrieved, confirming the API integration's functionality.

- **Statistical Analysis with built-in functions and `scipy`**:
  - **Test Case**: Correct application of statistical methods to the survey data.
  - **Method**: Implemented unit tests to validate the output of statistical functions like correlation calculations.
  - **Result**: All functions returned expected results, validating our analysis algorithms.

### User Experience Testing

To ensure a seamless and user-friendly experience:

- **Participants**: A group of users representing the target audience was asked to complete the survey.
- **Focus**: Checking for ease of use, clarity of instructions, and overall user satisfaction.
- **Outcome**: Feedback was positive, with minor suggestions leading to subsequent interface improvements.


## Libraries and Technologies Used

### Python Libraries
- `gspread`: To allow communication with Google Sheets.
- `google.oauth2.service_account`: Used to validate credentials and grant access to Google service accounts.
- `Scipy`: For statistical analysis.

### Technologies Used
- Python
- Google Sheets API

### Programs Used
- **GitHub**: Used for version control.
- **GitPod**: Used as a code editor.
- **Heroku**: Used to deploy the live project.
- **PEP8 Online**: Used to validate all the Python code.

## Deployment

The site was deployed via Heroku, and the live link can be found here: [Remote Working Survey](https://remote-working-survey-7d3459fee416.herokuapp.com/)

### Steps for Deployment
1. Log in to Heroku or create an account.
2. On the main page, click the button labelled 'New' in the top right corner and select "Create New App" from the drop-down menu.
3. Enter a unique and meaningful app name and select your region.
4. Click on the 'Create App' button.
5. In the 'Settings' tab, scroll down to 'Config Vars'.
6. Click 'Reveal Config Vars' and enter `PORT` into the Key box and `8000` into the Value box. Click the 'Add' button.
7. Input `CREDS` and the content of your Google Sheet API creds file as another config var and click 'Add'.
8. Scroll down to the 'Buildpacks' section, click 'Add Buildpack', select Python, and click 'Save Changes'.
9. Repeat the previous step to add node.js. (Note: The Buildpacks must be in the correct order. If not, click and drag them to move into the correct order.)
10. Go to the 'Deploy' tab.
11. Select GitHub as the deployment method and confirm the connection.
12. Search for the repository name and click 'Connect'.
13. Scroll to the bottom of the deploy page and choose either 'Enable Automatic Deploys' for automatic deploys or 'Deploy Branch' to deploy manually. (Note: Manually deployed branches will need re-deploying each time the repo is updated.)
14. Click 'View' to view the deployed site. The site is now live and operational.

## Credits

### Educational Websites
- [Love Sandwiches Walkthrough Project](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/58d3e90f9a2043908c62f31e51c15deb/)
- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [How to Create an Excel Data Entry Form in 10 Minutes Using Python](https://www.youtube.com/watch?v=svcv8uub0D0)
- [How to Use Python Lambda Functions](https://realpython.com/python-lambda/)
- [Python Validation](https://www.educba.com/python-validation/)
- [Map in Python: An Overview on Map Function in Python](https://www.simplilearn.com/tutorials/python-tutorial/map-in-python)
- [Python Map Function](https://www.youtube.com/watch?v=7e1u54GcgKE)
- [Mapping over values in a python dictionary](https://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary)
- [Python – Mapping key values to Dictionary](https://www.geeksforgeeks.org/python-mapping-key-values-to-dictionary/)
- [How to Calculate Correlation Between Variables in Python](https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/)
- [How to clear a range in google sheet via gspread](https://stackoverflow.com/questions/58876935/how-to-clear-a-range-in-google-sheet-via-gspread)
- [Is there an operator to calculate percentage in Python?](https://stackoverflow.com/questions/5997987/is-there-an-operator-to-calculate-percentage-in-python)
- [Count Function In Python](https://www.simplilearn.com/tutorials/python-tutorial/count-in-python)
- [Python statistics.mean() Method](https://www.w3schools.com/python/ref_stat_mean.asp)

### Contents
- [Survey’s questions based on Employee engagement](https://www.charliehr.com/blog/remote-working-survey-questions/)
- [word-Py/README.md](https://github.com/AliOKeeffe/word-Py/blob/main/README.md#logic-flow) (applied similar structure and the same deployment method was taken)

## Acknowledgements
I am immensely grateful to my mentor, Antonio Rodriguez, for his invaluable support and guidance in my project. His expertise in refining the code and fixing bugs and also in writing the exit code has been crucial to the project's success. His mentorship has not only enhanced the project but also significantly contributed to my professional growth.

