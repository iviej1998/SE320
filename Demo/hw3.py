""" The purpose of this assignment is to:
1. Use an API to fetch real-world financial data
2. Process and extract relevant
3. Compute basic statistical measures
4. Handle and present results in a structured manner """

from requests import get
import requests
import statistics #for median calculation
import json

def download_data(ticker: str) -> dict:
    """ this function retrieves historical stock data from a financial API
    Arguments: 
        ticker (str): Stock ticker symbol ('AAPL' for Apple)
        
    Returns
        dict: A dictionary containing historical stock data 
        """
    API_KEY = "O2BLZOXG5A45JG5I" #given key from Alpha Vantage
    BASE_URL = "https://www.alphavantage.co/query"
    
    parameters = {
        "function": "TIME_SERIES_DAILY", #specify which type of financial data to retrieve
        "symbol" : ticker,
        "apikey" : API_KEY,
        "outputsize": "full" # fetches all available historic data
    }
    
    #use a try block to handle potential errors when making an API request
    try:
        #send a GET request to the API
        response = get(BASE_URL, params = parameters)
        #raise HTTPError for bad responses
        response.raise_for_status()
        #parse the response body and convert to JSON format
        data = response.json()
        
        #print API response for debugging
        print(f"API Response for {ticker}: {data}")
        
        if "Time Series (Daily)" not in data:
            raise ValueError(f"Invalid API Response for ticker: {ticker}")
        
        return data["Time Series (Daily)"]
    
    except requests.exceptions.RequestException as e: #base exception i the requests library that catches all types of request related errors
        print(f"Error fetching data for {ticker}: {e}")
        return {} #return dictionary