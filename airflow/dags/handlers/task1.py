import yfinance as yf
import datetime as dt
from dynamodb.base import DynamoDB
from settings import settings


def task1_handler():
    # download today data
    dynamo = DynamoDB(settings.dynamodb_table_name,
                      settings.dynamodb_partition_key,
                      None,
                      cursor=None)
    key = settings.dynamodb_partition_key

    amazon = yf.Ticker("AMZN")
    apple = yf.Ticker("AAPL")

    dynamo.put({
        f"{key}": "AMZN",
        "dayHigh": str(amazon.info['dayHigh']),
        "dayLow": str(amazon.info['dayLow']),
        "timestamp": (dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
    })

    dynamo.put({
        f"{key}": "AAPL",
        "dayHigh": str(apple.info['dayHigh']),
        "dayLow": str(apple.info['dayLow']),
        "timestamp": (dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
    })


# python -m handlers.task1
if __name__ == "__main__":
    task1_handler()
