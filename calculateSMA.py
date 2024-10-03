def calculate_sma(data, period):
    """
    Calculates the Simple Moving Average (SMA) over a certain period of time.

    Parameters:
    data (pandas.Series): The closing prices (or similar data) as a pandas series.
    period (int): The number of days over which the SMA should be calculated.

    Returns:
    float: The calculated SMA value.
    returns -1 if there is not enough data available
    """
    # Check whether sufficient data is available
    if len(data) < period:
        return -1

    # If the data set contains more values, only use the last "period" days
    relevant_data = data.tail(period)

    # Calculation of the SMA
    sma = relevant_data.mean()

    return sma


def calculate_sma_dif(sma, data):
    """
    Calculates the difference between the SMA and the last closing price in the data.

    Parameters:
    sma (float): The Simple Moving Average (SMA).
    data (pandas.series): The closing prices (or similar data) as a pandas series.

    Returns:
    float: The difference between the last closing price and the SMA.
    """

    # Retrieve the last value in the data (the last closing price)
    last_value = data.iloc[-1]

    # Calculate the difference
    difference = last_value - sma

    return difference
