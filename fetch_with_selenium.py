import time
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
    ChromeDriverManager().install())
url = 'https://tsdr.uspto.gov/#caseNumber=79315695&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch'
driver.get(url)
time.sleep(1)
documents = driver.find_elements_by_xpath(
    '/html/body/div[4]/div[4]/div[6]/div[2]/ul/li[2]/a')
documents[0].click()
element = driver.find_elements_by_xpath(
    '/html/body/div[4]/div[4]/div[6]/div[3]/ul/li[2]/div[2]/div[1]/div[2]/table/tbody/tr[1]')
print(element[0].text)
time.sleep(2)
driver.close()
