from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
# chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome(executable_path=os.environ.get(
# "CHROMEDRIVER_PATH"), options=chrome_options)

# options = Options()
# options.headless = True
driver = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)
url = 'https://tsdr.uspto.gov/#caseNumber=79315695&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch'
driver.get(url)
