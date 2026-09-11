# AI Usage

1. AI Tool Used:-

ChatGPT Free was used as a development assistant during the assignment.

## Areas Where AI Was Used

AI assistance was used for:

- I have made this project in my new device so i have to set up the Env firstly to run the django project.
- First to understand what the Assessment is, and what I have to develop
- Django project setup
- Django REST Framework API structure
- Serializer design
- API validation
- Implementation ideas for the box recommendation algorithm
- Test case file creation
- Debugging test failures
- README/documentation structure

## Important Prompts / Questions

Examples of prompts used during development:

- Give me the detail of Assessement 
- Check the env of the new device so later there is no any env related issues
- like which version of the python is needed in the django and then download the necessary modules and packages
- About the assessment, the algorithm 
- the working of the api, how to test 
- how to test the api fastly -- with the curl command
- How should I test the recommendation API?
- Why is my quantity test failing?
- How should I prepare the Django project for GitHub submission?

## Accepted AI Output

AI-generated suggestions were used for parts of the Django API structure, serializer validation, test structure, documentation structure and the heuristic packing approach.

All generated code was reviewed, executed and tested locally before being retained.

## Modified / Rejected Output

Some generated suggestions were modified after testing.

For example: an initial test expected two laptops to require a Medium Box. After implementing the 3D packing logic and testing the actual dimensions, it was determined that two laptops can fit inside the Small Box by stacking them.
- due to this we able to make the 3d logic

The test expectation was therefore corrected rather than changing the algorithm to satisfy an incorrect test.

## AI Mistakes / Limitations

One important issue identified during verification was that an initial test assumption did not match the physical dimensions of the products and boxes.

## Verification

AI-generated code was verified by:

- Running Django system checks
- Running the Django test suite
- Manually testing the API with curl and Postman
- Checking product rotation
- Checking quantity handling
- Checking box weight limits
- Checking the no-suitable-box scenario
- All the test cases are in the test.py file

Final test result:

10 tests passed successfully.