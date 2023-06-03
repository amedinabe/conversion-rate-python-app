import datetime
import sys

def check_arguments(args):
    """
    Function that will check if there are enough input arguments provided (ie exactly 3) and will return the input arguments if it is the case.
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    args: list
        The function receives the input arguments list args created in the main.py

    Pseudo-code
    ----------
    if longitude of arguments is equal to 3
	    return True
    else
	    return False
    
    Returns
    -------
    False / True: Boolean
        The function returns a Boolean result (False or True) based on the longitude of the arguments.
    """

    # check number of arguments
    if len(args) == 3:
        return True  
    else: 
        return False

def check_date(date):
    """
    Function that will check if the provided date is valid and will return the value True if that is the case. 
    Otherwise the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    date: str
        The function receives the first input argument from the arguments list args created in the main.py

    Pseudo-code
    ----------
    Create a Boolean variable as True
    try:
	    Assign variables year, month, day from the date split by hyphen
	    use datatime library to check if year, month, day variables 
        can assemble a valid date.
    except with a value error:
        Assign False to Boolean variable
    
    if Boolean variable is equal to True then:
	    if year's longitude equal to 4 and month's longitude equal to 2 and day's longitude equal to 2:
		    return True
	    else:
		    return False
    else:
	    return False

    Returns
    -------
    False / True: Boolean
        The function returns a Boolean result (False or True) based on the date validity format.
    """
    #check if the provided date is valid
    
    isValidDate = True
    try:
        year, month, day = date.split('-')
        datetime.datetime(int(year), int(month), int(day))
        
    except ValueError:
        isValidDate = False

    if isValidDate == True:
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            return True
        else: 
            return False
    else:
        return False
    
        
    