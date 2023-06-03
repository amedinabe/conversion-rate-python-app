import sys
from frankfurter import Frankfurter

class CurrencyConverter:
    """
    Class that represents a Currency conversion object. It will be used to store the input arguments (currency codes, date) and also other information required (amount, rate, inverse rate, instantiation of Frankfurter class).

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    api : Frankfurter
        Instance of Frankfurter class
    """
    def __init__(self, from_currency, to_currency, date):
        # define self parameters
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.date = date
        self.amount = None
        self.rate = None
        self.inverse_rate = None
        #instantiation of Frankfurter class
        self.frankfurter = Frankfurter()


    def check_currencies(self):
        """
        Method that will check if currency codes stored in the class attributes are valid.
        Otherwise the program will exit and display the relevant message provided in the assignment brief

        Parameters
        ----------
        self: 
            The function receives all self parameters from the CurrencyConverter class

        Pseudo-code
        ----------
        Create a Boolean variable "is_valid" as False

        Create a boolean variable to save the checked from_currency. It will generate a frankfurter object from the class Frankfurter and access the method check_currency  to evaluate the currency.

        Create a boolean variable to save the checked to_currency. Generate a frankfurter object,  access the method check_currency and evaluate the currency.

        if checked from_currency and check to_currency are false:
            print from_currency and to_currency are not valid currency codes
        elif checked from_currency is false:
            print from_currency is not a valid currency code
        elif check to_currency is false:
            print to_currency is not a valid currency code
        else:
            assign is_valid to True
        return is_valid

        Returns
        -------
        is_valid: Boolean
            The function returns a Boolean result (False or True) based on the currency code's validity.
        """
        #check if currency codes stored in the class attributes are valid
        is_valid = False
        is_from_currency_valid = self.frankfurter.check_currency(self.from_currency)
        is_to_currency_valid = self.frankfurter.check_currency(self.to_currency)
        
        if not is_from_currency_valid and not is_to_currency_valid:
            print(f"{self.from_currency} and {self.to_currency} are not valid currency codes")   
        elif not is_from_currency_valid:
            print(f"{self.from_currency} is not a valid currency code")
        elif not is_to_currency_valid:
            print(f"{self.to_currency} is not a valid currency code")
        else:
            is_valid = True
            
        return is_valid
    
    
    def reverse_rate(self):
        """
        Method that will calculate the inverse rate from the value stored in the class attribute, round it to 4 decimal places and save it back in the class attribute inverse_rate.

        Parameters
        ----------
        self: 
            The function receives all self parameters from the CurrencyConverter class

        Pseudo-code
        ----------
        if parameter self.rate from CurrencyConverter is different from cero:
            Save parameter inverse_rate as a result of applying round_rate function to 1/ self.rate
        else:
            inverse_rate equal to cero
        return empty

        Returns 
        -------
        The function doesn't return a result. It is saving the self parameter inverse_rate from the CurrencyConverter class
        """
        # calculate the inverse rate, use round_rate and save inverse rate
        if self.rate != 0:
            self.inverse_rate = self.round_rate(1/self.rate)
        else:
            self.inverse_rate = 0
        return 


    def round_rate(self, rate):
        """
        Method that will round an input argument to 4 decimals places.

        Parameters
        ----------
        self: 
            The function receives all self parameters from the CurrencyConverter class
        rate: float
            The function receives a rate to round

        Pseudo-code
        ----------
        return the round rate with 4 decimals

        Returns
        -------
        round_rate: float with 4 decimals
        """

        #round rate to 4 decimal
        return round(rate, 4)
        

    def get_historical_rate(self):
        """
        Method that will call the Frankfurter API and get the historical conversion rate for the currencies (rounded to 4 decimals) and date stored in the class attributes.
        Then it will calculate the inverse rate and will exit by displaying the relevant message provided in the assignment brief

        Parameters
        ----------
        self: 
            The function receives all self parameters from the CurrencyConverter class

        Pseudo-code
        ----------
        Create a variable json_conversion_rate to save the dictionary from the response object calling the method get_historical_rate of the Frankfurter class with from_currency, to_currency and date as parameters

        get the dictionary of the historical rates

        Calculate the rate as rate to_currency/ rate from_currency

        Save the rate parameter with 4 decimals

        calculate the inverse rate 
        
        return empty

        Returns
        -------
        The function doesn't return a result. It is saving the self parameter rate from the CurrencyConverter class
        """

        # => To be filled by student
        #call the Frankfurter API - dict object with base, date and rates 
        json_conversion_rate = self.frankfurter.get_historical_rate(self.from_currency, self.to_currency, self.date).json()
        #get the historical conversion rate - dict with the rates
        historical_conversion_rate = json_conversion_rate.get("rates")
        #get rate
        rate = historical_conversion_rate.get(self.to_currency) / historical_conversion_rate.get(self.from_currency)
        self.rate = self.round_rate(rate)
        #calculate the inverse rate
        self.reverse_rate()
        return
        
        