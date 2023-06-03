#import libraries
import sys
from currency import CurrencyConverter
from checks import check_arguments, check_date

if __name__ == "__main__":
    print("Launching app")
    """
    Main logics of the program.

    Pseudo-code
    ----------
    Extract the input arguments
    Remove the first argument (name of Python script)
    Check there are 3 items in the remaining list of argument (using your defined check_arguments() function)
    Check the validity of the input date (using your defined check_date() function)
    Instantiate an object from your defined CurrencyConverter class with the verified 2 currency codes and date
    Check the validity of the 2 currency codes (using your defined check_currencies() method from CurrencyConverter class)
    Extract the historical rate and calculate its inverse rate (using your defined get_historical_rate() method from CurrencyConverter class)
    """

    #Extract the input arguments and Remove the first argument
    args = sys.argv[1:]

    #Checking that there are 3 items in the remaining list of argument
    is_lenght_valid = check_arguments(args)
    if is_lenght_valid == False: 
        print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2>")
        sys.exit(0)
    
    #Checking the validity of the input date
    is_date_valid = check_date(args[0])
    if is_date_valid == False:
        print("Provided date is invalid")
        sys.exit(0)
    
    
    #Instantiate an object from your defined CurrencyConverter class with the verified date
    currency = CurrencyConverter(from_currency = args[1], to_currency = args[2], date = args[0])
    
    #Checking the validity of the 2 currency codes
    is_currency_valid = currency.check_currencies()
    if is_currency_valid == False:
        sys.exit(0)
        
    #Extract the historical rate and calculate its inverse rate
    #call get_historical_rate
    currency.get_historical_rate()
    
    #print values
    print(f"The conversion rate on {currency.date} from {currency.from_currency} to {currency.to_currency} was {currency.rate}. The inverse rate was {currency.inverse_rate}") 