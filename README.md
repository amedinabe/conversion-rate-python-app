# Currency Converter App

## Description
The currency converter is a python program that takes a date and two currency codes as input arguments and returns the rate and inverse rate based on the Frankfurter app.
The program works with specific date and currency code formats. Several scenarios were implemented for invalid parameters. 
Unit tests will assure the code's functionality and verify it works as intended. 
In future developments, the app is expected to receive an amount and convert it to the given currency. 

## How to Setup
To config the development environment and run the program, you would need to follow the next steps:
1. Unzip the code folder
2. Open the IDE of preference
3. Use Python 3.8.10
4. Install the package requests==2.28.1 and validators==0.20.0
Note: The converter uses datetime and sys built-in Python modules. 


## How to Run the Program
Follow the next steps:
1. Open a terminal
2. Navigate to the project folder
3. use the statement "python main.py <date> <currency1> <currency2>" to execute the currency converter
Using the date format: YYYY-MM-DD and valid currency codes based on the Frankfurter app.
Example: <python main.py 2021-07-16 GBP AUD>

## Project Structure
The following is the list of files for this project:
1. main.py: The orchestration file is used for running the code with the given date and currency codes.
2. checks.py: script that checks currencies and date validity.
3. api.py: script that makes the API calls and returns the response
4. frankfurter.py: script that manages Api call to Frankfurter endpoints.
5. currency.py: script that contains the class used for extracting currency conversion rate and calculating the inverse rate
6. test_checks.py: script for test checks.py
7. test_frankfurter.py: script for test frankfurter.py
8. test_api.py: python script for test api.py
9. test_currency.py: script for test currency.py

## Citations
Ensari, H. (2022). Frankfurter API. Retrieved from Frankfurter API: https://www.frankfurter.app/docs/#usage


