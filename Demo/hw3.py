""" The purpose of this assignment is to:
1. Use an API to fetch real-world financial data
2. Process and extract relevant
3. Compute basic statistical measures
4. Handle and present results in a structured manner """

from requests import get

def download_data(ticker: str) -> dict:
    """ this function retrieves historical stock data from a financial API
    Arguments: 
        ticker (str): Stock ticker symbol ('AAPL' for Apple)
        
    Returns
        dict: A dictionary containing historical stock data 
        """
    API_KEY = "CYURPUAWDOKMLFJP" #given key from Alpha Vantage
    BASE_URL = f"https://www.alphavantage.co/query"
    
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED", #specify which type of financial data to retrieve
        "symbol" : ticker,
        "apikey" : API_KEY,
        "outputsize": "full" # fetches all available historic data
    }
    
    #use a try block to handle potential errors when making an API request
    try:
        #send a GET request to the API
        response = get(BASE_URL)
        #print to a JSON file
        print(response.json())
        #raise HTTPError for bad responses
        response.raise_for_status()
        #parse the response body and convert to JSON format
        data = response.json()
        
        if "Time Series (Daily)" not in data:
            raise ValueError("Invalid API Response. Check your API key or ticker")
        
        return data["Time Series (Daily)"]
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return {}
    
    #example usage

    
    #CYURPUAWDOKMLFJP