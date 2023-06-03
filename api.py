from urllib import response
import requests
import sys

def call_get(url: str) -> requests.models.Response:
    """
    Function that will call the API endpoint (input parameter) and return its response as a requests.models.Response object
    In case of an error, the program will exit and display the relevant message provided in the assignment brief

    Parameters
    ----------
    url: str
        url to call the API endpoint

    Pseudo-code
    ----------
    Create a variable "response" to call the API endpoint and save the result

    if status code from response is equal to 200:
        return response
    else:
        print "There is an error with Frankfurter API"
        exit from the program
    

    Returns
    -------
    object: response
        response from the API

    """
    
    # call the API endpoint
    response = requests.get(url)
    
    # validate the response
    if response.status_code == 200:
        #return its response as a requests.models.Response object
        return response
    else:
        print("There is an error with Frankfurter API")
        sys.exit(0)