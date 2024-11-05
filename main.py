from selenium import webdriver
from selenium.common import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import getenv
from time import sleep
from InstaFollower import InstaFollower

bot = InstaFollower()

bot.find_followers()
bot.follow()
bot.login()