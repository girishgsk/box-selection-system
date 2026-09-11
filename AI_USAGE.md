# AI Usage

## AI Tool Used

ChatGPT was used as a development assistant during the assignment.

## Areas Where AI Was Used

AI assistance was used for:

- Django project setup guidance
- Django REST Framework API structure
- Serializer design
- API validation
- Initial implementation ideas for the box recommendation algorithm
- Test case suggestions
- Debugging test failures
- README/documentation structure
- GitHub Actions configuration

## Important Prompts / Questions

Examples of prompts used during development:

- How should I structure a small Django REST API for this assignment?
- How should I model products and boxes in Django?
- How can I validate the product quantity in Django REST Framework?
- How should I implement a box recommendation algorithm that considers dimensions, rotation, quantity and weight?
- How should I test the recommendation API?
- Why is my quantity test failing?
- How should I prepare the Django project for GitHub submission?

## Accepted AI Output

AI-generated suggestions were used for parts of the Django API structure, serializer validation, test structure, documentation structure and the heuristic packing approach.

All generated code was reviewed, executed and tested locally before being retained.

## Modified / Rejected Output

Some generated suggestions were modified after testing.

For example, an initial test expected two laptops to require a Medium Box. After implementing the 3D packing logic and testing the actual dimensions, it was determined that two laptops can fit inside the Small Box by stacking them.

The test expectation was therefore corrected rather than changing the algorithm to satisfy an incorrect test.

## AI Mistakes / Limitations

One important issue identified during verification was that an initial test assumption did not match the physical dimensions of the products and boxes.

The AI-assisted implementation also uses a heuristic packing strategy rather than an exact optimal 3D bin-packing algorithm.

## Verification

AI-generated code was verified by:

- Running Django system checks
- Running the Django test suite
- Manually testing the API with curl
- Checking expected HTTP status codes
- Checking product rotation
- Checking quantity handling
- Checking box weight limits
- Checking the no-suitable-box scenario

Final test result:

10 tests passed successfully.