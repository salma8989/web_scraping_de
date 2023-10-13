from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from helpers import init, write_to_bigquery
import pandas as pd
import time

DATASET_ID = "dibimbing_de_batch2" # NOTE: use underscore, don't use dash (-)
TABLE_ID = "hospitals"

def main(driver_path: str, path_to_visit: str, keyword: str, creds_path: str):
    location_names = []
    location_addresses = []

    # NOTE: FOR EASINESS PURPOSES ON COLLAB, UNCOMMENT THIS LINE AND COMMENT THE LINES BELOW
    driver = init(
        driver_path=driver_path,
        headless=True,
        detach=False
    )

    # NOTE: FOR VISUALIZATION PURPOSES ON TEXT EDITOR, UNCOMMENT THIS LINE AND COMMENT THE LINES ABOVE
    # driver = init(
    #     driver_path=driver_path,
    #     headless=False,
    #     detach=True
    # )
    driver.get(path_to_visit)

    # wait for 5 seconds
    time.sleep(5)

    search_bar_xpath = '//*[@id="searchboxinput"]'
    search_el = driver.find_element(By.XPATH, search_bar_xpath)
    search_el.click()
    search_el.send_keys(keyword)
    search_el.send_keys(Keys.ENTER)

    # YOU CAN COPY AND PASTE THIS xpath INTO Chrome DevTools > elements to get the selected element
    time.sleep(5)
    scroll_xpath = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'
    scroll_el = driver.find_element(By.XPATH, scroll_xpath)
    init_wait = WebDriverWait(driver, timeout=30)

    print("Waiting the initial text to be displayed before doing infinite scroll")
    init_wait.until(lambda _: scroll_el.is_displayed())

    while True:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", driver.find_element(By.XPATH, scroll_xpath))
        # new_height = driver.execute_script("return arguments[0].scrollTop;", driver.find_element(By.XPATH, scroll_xpath))
        # print(f"new height {new_height}")

        most_bottom_el = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[last()]')

        if most_bottom_el.text.strip().lower() == 'anda telah mencapai akhir daftar.':
            break
    
    locations_el = driver.find_elements(By.XPATH, '//*[@class="Nv2PK tH5CWc THOPZb "]')
    print(f"There are {len(locations_el)} locations found with '{keyword}' keyword")
    
    for loc_element in locations_el:
        name_el = loc_element.find_element(By.XPATH, ".//a[contains(@href, 'google.co.id')]")
        name = name_el.get_attribute('aria-label')
        address_el = loc_element.find_element(By.XPATH, './/div[@class="bfdHYd Ppzolf OFBs3e "]//div[contains(@class, "fontBodyMedium")]/div[4]/div[1]')

        location_names.append(name)
        location_addresses.append(address_el.text)
    
    df = pd.DataFrame({
        "name": location_names,
        "address": location_addresses,
        "keyword": [keyword for _ in range(len(location_names))]
    })
    write_to_bigquery(df, DATASET_ID, TABLE_ID, creds_path)
    print(f"Successfully write to {DATASET_ID}.{TABLE_ID}!")


driver_path = "web_scraping/chromedriver"
path_to_visit = "https://www.google.co.id/maps"
keyword = 'Hospital near jakarta'
creds_path = "creds/scraping-key-sa.json"
main(driver_path, path_to_visit, keyword, creds_path)