def create_message(close, dif, name):
    """
    Creates a message with the closing prices, and the difference between the last closing price and the SMA.

    Parameters:
    close (pandas.Series): The closing prices.
    name (str): The name of the index
    dif (float): The difference between the last closing price and the SMA.

    Returns:
    str: The message containing the data.
    """

    standard_message = f"{name}\n" \
                       f"Der Schlusskurs beträgt {close.iloc[-1]:.2f}\n" \
                       f"Der Abstand des SMA zum Basiswert beträgt {dif:.2f}"

    return standard_message
