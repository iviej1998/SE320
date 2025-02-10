""" The purpose of this assignment is to:
1. Use an API to fetch real-world financial data
2. Process and extract relevant
3. Compute basic statistical measures
4. Handle and present results in a structured manner """

from requests import get

def download_data(ticker: str) -> dict:
    """ this function retrieves historical stock data from Nasdaq"""