import yfinance as yf
from datetime import datetime, timedelta


def get_close(index, days):
    """
    Returns the closing prices of an index over a certain number of days.

    Parameters:
    index (str): The ticker symbol of the index (e.g. '^GSPC' for the S&P 500).
    days (int): Number of days for which the data should be retrieved.

    Returns:
    pandas.series: A series of closing prices.
    """
    # Calculation of the start date based on the number of days
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=days)).strftime('%Y-%m-%d')

    # Download data for the specified index and time period
    data = yf.download(index, start=start_date, end=end_date)

    # Return of the closing prices
    return data['Close']
