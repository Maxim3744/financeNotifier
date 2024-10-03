import getData
import calculateSMA
import createMessage
import sendWAMessage


def main():
    close_values = getData.get_close('^GSPC', 300)
    close_values_2x = getData.get_close('DBPG.DE', 300)
    sma = calculateSMA.calculate_sma(close_values, 200)
    dif = calculateSMA.calculate_sma_dif(sma, close_values)
    message = createMessage.create_message(close_values_2x, dif, 'S&P 500 2x')
    sendWAMessage.send_whatsapp_message(message)


if __name__ == "__main__":
    main()
