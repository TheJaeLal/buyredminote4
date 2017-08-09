"""Before running...
Install selenium
sudo pip3 install selenium
"""
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
import time,sys,os,platform

#Take email and password from command line
email = sys.argv[1]
password = sys.argv[2]


#Returns the Path to appropriate GeckoDriver based on the type of system 
def find_system_driver():
	myOS = sys.platform
	#32bit or 64bit
	arch = platform.architecture()[0]

	if myOS.startswith('linux') and arch.startswith('32'):
		return '/GeckoDriver/Linux/32/'	
	elif myOS.startswith('linux') and arch.startswith('64'):
		return '/GeckoDriver/Linux/64/'
	elif myOS == 'darwin':
		return '/GeckoDriver/MacOS/'
	elif myOS.startswith('win') and arch.startswith('32'):
		return '\\GeckoDriver\\Windows\\32\\'
	elif myOS.startswith('win') and arch.startswith('64'):
		return '\\GeckoDriver\\Windows\\64\\'
	else:
		raise Exception('Unknown Operating System or Platform Architecture!')

def Set_Path_For_Firefox():
	pwd = os.environ['PWD']
	path_to_gecko = pwd+find_system_driver()
	new_path = os.environ['PATH']+':'+path_to_gecko
	os.environ['PATH'] = new_path

def Out_of_Stock(driver,out_of_stock_selector):
	try:
		driver.find_element_by_css_selector(out_of_stock_selector)
	except NoSuchElementException:
		return False

	SCROLL_PAUSE_TIME = 1

	# Wait to load page Before Scrolling
	time.sleep(SCROLL_PAUSE_TIME)

	#Scroll down to Bottom
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	# Wait to load page
	time.sleep(SCROLL_PAUSE_TIME)

	#Scroll up
	driver.execute_script("window.scrollTo(0, 0);")

	print('Out of Stock!')

	return True

def checkout(driver,buy_now_selector,email,password):
	print('Your credentials are as follows :')
	print('email:{} password:{}'.format(email,password))
	buy_button = driver.find_element_by_css_selector(buy_now_selector)
	buy_button.click()

def main():

	#Set the path to locate Gecko Driver for firefox..
	Set_Path_For_Firefox()

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

	enter_email_selector = '._2zrpKA'
	enter_password_selector = 'div._39M2dM:nth-child(2) > input:nth-child(1)'

	driver.get(note_4_2GB_url)

	while Out_of_Stock(driver,out_of_stock_selector): 

		REFRESH_PAUSE_TIME = 2

		# Wait before Refresh
		time.sleep(REFRESH_PAUSE_TIME)

		# Refresh the web page
		driver.refresh()

	print('********Congrats In Stock!!*********')
	checkout(driver,buy_now_selector,email,password)


#***********Main Ends***********

if __name__== "__main__":
	main()