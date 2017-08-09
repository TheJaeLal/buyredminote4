"""Before running...
Install selenium
sudo pip3 install selenium

Download firefox_binary and place it in the directory

Then execute the following command in the shell script
export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()

note_4_2GB_url = 'https://www.flipkart.com/\
	redmi-note-4-black-32-gb/p/itmeqe48hrakfuuj\
	?pid=MOBEQ98MMWX5R8RE'

note_4_3GB_url = 'https://www.flipkart.com/\
	redmi-note-4-black-32-gb/p/itmeqe4htst9587b\
	?pid=MOBEQ98THNGR4FD5'

out_of_stock_selector = '#container > div > \
	div:nth-child(2) > div > div > div > \
	div._1GRhLX._3N5d1n > div > div._2Cl4hZ > \
	div.RIBRtX > div._3xgqrA'

buy_now_selector = '#container > div > \
	div:nth-child(2) > div > div > div > \
	div._1GRhLX._3N5d1n > div > \
	div._3S6yHr._2S3f06 > div._1k1QCg._3QNwd7 > \
	ul > li:nth-child(2) > form > button'

# enter_email_selector = '._2zrpKA'
# enter_password_selector = 'div._39M2dM:nth-child(2) > input:nth-child(1)'
driver.get(note_4_2GB_url)

while True: 
	try:
		driver.find_element_by_css_selector(out_of_stock_selector)
	except NoSuchElementException:
		break

	SCROLL_PAUSE_TIME = 1
	REFRESH_PAUSE_TIME = 2

	# Wait to load page
	time.sleep(SCROLL_PAUSE_TIME)

	#Scroll to the bottom
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# Wait to load page
	time.sleep(SCROLL_PAUSE_TIME)

	#Scroll up
	driver.execute_script("window.scrollTo(0, 0);")

	print('Out of Stock!')

	# Wait before Refresh
	time.sleep(REFRESH_PAUSE_TIME)

	# Refresh the web page
	driver.refresh()

print('In Stock!!')
# buy_button = driver.find_element_by_css_selector(buy_now_selector)
# buy_button.click()