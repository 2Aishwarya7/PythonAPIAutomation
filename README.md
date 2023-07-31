# Python-API Automation Framework

## Integration Test Cases for RESTfull Booker
URL-https://restful-booker.herokuapp.com/apidoc/index.html

1. Verify GET, POST, PACTH, DELETE, PUT
1. Response Body, Headers, Status Code. 
2. Auth - Basic Auth, Cookie Based Auth.
3. JSON Schema Validation.

## Tech Stack/Packages (Required Packages)
1.Request Module
2.Pytest,Pytest-html
3.Allure Report
4.Faker-CSV JSON 
5. Run via Command line-Jenkins

### P.S - DB Connection(in future)

##Install pip packkes
- 'pip install requests pytest pytest-html faker allure-pytest jsonschema'
- 'pip install requirements.txt'

##How to run Locally and see the Report?
'pytest tests/* -s -v --alluredir=./reports --html=report.html'

##How to run via Jenkins
