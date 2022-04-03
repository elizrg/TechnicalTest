import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Functions:

    def openBrowserChrome(self, link, title):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(link)
        assert "No results found." not in driver.page_source
        assert title in driver.title
        print(title)
        return title

    def searchWord(self, word):
        textbox = driver.find_element(By.NAME, "q")
        textbox.clear()
        textbox.send_keys(word)
        textbox.submit()

        time.sleep(10)

        # check results
        results = driver.find_element(By.XPATH, "//*[contains(text(),'Cerca de')]")
        results.click()

        # results on the browser
        resultsword = results.text
        resultsnumber = re.findall(r'\d+\,\d+\,\d+', resultsword)

        # convert list to string
        resultstring = "".join(resultsnumber)

        # remove ','
        transformed_result = resultstring.replace(",", "")

        # convert string to int
        resultsInt = int(transformed_result)

        print("Results on the browser: ", resultsword)

        if resultsInt != 0:
            print("Different to zero")
        else:
            print("Equals to zero")

        driver.close()
        return resultsInt


