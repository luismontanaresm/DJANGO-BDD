from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def before_all(context):
	
	context.browser = webdriver.Firefox()
	context.browser.implicitly_wait(1)
	context.server_url = 'http://localhost:8000'

def after_all(context):
	# Explicitly quits the browser, otherwise it won't once tests are done
	context.browser.quit()

def before_feature(context, feature):
	# Code to be executed each time a feature is going to be tested
	pass
