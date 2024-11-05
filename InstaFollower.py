from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import getenv
from time import sleep


load_dotenv(dotenv_path=".env")
username= getenv("mail")
password = getenv("password")
URL="https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.driver = self.driver_initialization()

    def driver_initialization(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--start-maximized")

        inner_driver = webdriver.Chrome(options=chrome_options)

        return inner_driver

    def login(self):
        self.driver.get(URL)
        # cookies ista
        self.driver.find_element(By.XPATH, value="//button[@class='_a9-- _ap36 _a9_1']").click()
        sleep(1)
        # login with fb button
        self.driver.find_element(By.XPATH, value="//span[@class='_ab37']").click()
        sleep(2)
        # cookies facebook
        self.driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[3]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div/span/span').click()
        sleep(1)
        email_box = self.driver.find_element(By.ID, value="email")
        login_box = self.driver.find_element(By.ID, value="pass")

        email_box.send_keys(username)
        login_box.send_keys(password, Keys.TAB, Keys.TAB, Keys.ENTER)
        sleep(3)

        # continue as username

        self.driver.find_element(By.XPATH, value="//button[@class='_42ft _4jy0 layerConfirm _1-ag _4jy6 _4jy1 selected _51sy']").click()
        sleep(10)



    def find_followers(self):
        print("follower")
        pass

    def follow(self):
        print("folow")
        pass