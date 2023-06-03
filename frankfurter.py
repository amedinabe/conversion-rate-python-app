from datetime import date
from api import call_get

class Frankfurter:
    """
    Class that manages API calls to Frankfurter. It will be used to store the URLS to the relevant endpoints. It will also automatically call the Currencies endpoint and store the return list of available currency codes.

    Attributes
    ----------
    base_url : str
        Base url to Frankfurter API
    currencies_url : str
        Frankfurter endpoint for extracting currencies list
    historical_url : str
        Frankfurter endpoint for extracting historical currencies conversion rates
    currencies: list
        List of available currency codes
    """
    def __init__(self):
        #store the URLS to the relevant endpoints
        self.base_url = "https://api.frankfurter.app"
        self.currencies_url = self.base_url + "/currencies"
        self.historical_url = self.base_url + "/"
        #automatically call the Currencies endpoint and store the return list of available currency codes.
        self.currencies = self.get_currencies_list()

    def get_currencies_list(self):
        """
        Method that will get the list of available currencies and returns it as a Python list.

        Parameters
        ----------
        self: 
            The function receives all self parameters from the CurrencyConverter class

        Pseudo-code
        ----------
        Create a variable "response" to save the result from the call_get function
        Create a variable to save the list of available currencies from the response
        get the python list from the json
        return the python list

        Returns
        -------
        list:
            Contains all the currencies fetched from the server


        """
        
        #get the list of available currencies
        response = call_get(self.currencies_url)
        #get the json from the response
        currency_list = response.json()
        #get the python list from the json
        python_list = currency_list.keys()
        
        return python_list

    def check_currency(self, currency):
        """
        Method that will check if a provided currency code is valid and return True if that is the case.
        Otherwise it will return False.

        Parameters
        ----------
        self: 
            The function receives all self parameters from the CurrencyConverter class
        
        currency:

        Pseudo-code
        ----------
        if currency is in currencies list:
            return True
        else:
            return False

        Returns
        -------
        currency
        """
        
        #check if a provided currency code is valid
        return currency in self.currencies
         

    def get_historical_rate(self, from_currency, to_currency, from_date, amount=1):
        """
        Method that will call the historical API endpoint in order to get the conversion rate for a given dates and currencies. It will return an requests.models.Response object.

        Parameters
        ----------
        self: 
            The function receives all self parameters from the CurrencyConverter class
        
        from_currency:
            code for the origin currency
        
        to_currency:
            code for the destination currency
        
        from_date:
            Date reference to download the currency history
        

        Pseudo-code
        ----------
        return the object response from the call_get function

        Returns
        -------
        object: response
            object response from call_get function
        """
        
        #call the historical API endpoint - return an requests.models.Response object
        return call_get(self.historical_url+from_date)