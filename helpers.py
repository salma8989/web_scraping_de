from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import pandas_gbq
from google.oauth2 import service_account


def init(driver_path: str, headless: bool, detach: bool) -> webdriver.Chrome:
    service = Service(executable_path=driver_path)
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option("detach", detach) # to keep driver "alive"

    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def write_to_bigquery(df: pd.DataFrame, dataset_id: str, table_id: str, creds_path: str):
    # NOTE: please refer to this docs for writing to BigQuery
    # https://googleapis.dev/python/pandas-gbq/latest/writing.html
    creds = service_account.Credentials.from_service_account_file(creds_path)
    pandas_gbq.to_gbq(df, f"{dataset_id}.{table_id}", credentials=creds, if_exists="replace")