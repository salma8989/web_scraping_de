Kang Okza, saya coba run gmaps python, tidak bisa running. muncul :

1. PS C:\Users\asusa\OneDrive\Documents\web_scraping> & C:/Users/asusa/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/asusa/OneDrive/Documents/web_scraping/gmap.py
Traceback (most recent call last):
  File "c:\Users\asusa\OneDrive\Documents\web_scraping\gmap.py", line 82, in <module>
    main(driver_path, path_to_visit, keyword, creds_path)
  File "c:\Users\asusa\OneDrive\Documents\web_scraping\gmap.py", line 16, in main
    driver = init(
  File "c:\Users\asusa\OneDrive\Documents\web_scraping\helpers.py", line 17, in init
    driver = webdriver.Chrome(service=service, options=chrome_options)
  File "C:\Users\asusa\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\selenium\webdriver\chrome\webdriver.py", line 45, in __init__
    super().__init__(
  File "C:\Users\asusa\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\selenium\webdriver\chromium\webdriver.py", line 51, in __init__
    self.service.path = DriverFinder.get_path(self.service, options)
  File "C:\Users\asusa\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\selenium\webdriver\common\driver_finder.py", line 44, in get_path    
    raise NoSuchDriverException(f"Unable to locate or obtain driver for {options.capabilities['browserName']}")
selenium.common.exceptions.NoSuchDriverException: Message: Unable to locate or obtain driver for chrome; For documentation on this error, please visit: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location

2. dimana file creds/scraping-key-sa.json? dapatnya bagaimana?
ini untuk bisa load ke bigquery?

3. tugas : file salma_web_scraping.py
versi chrome: 117.0.5938.152


