import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDemo:
    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)

    def test_wei(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, "// *[ @ id = 'indexTop'] / div[2] / aside / a[1]").click()  ##立即登录
        sleep(5)
        self.driver.get_cookies()
        self.driver.find_element(By.XPATH, "//*[@id='menu_customer']").click()  ##点击客户联系
        sleep(2)

    # def teardown_method(self, method):
    #     self.driver.quit()

    def test_cookies(self):
        cookies = self.driver.get_cookies()
        print(cookies)
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

        self.driver.delete_all_cookies()
        with open("cookie.json", "r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)
