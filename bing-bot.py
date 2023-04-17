import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CREDENTIALS_FILE = 'credentials.txt'


def read_credentials(file_path):
    with open(file_path, 'r') as f:
        email = f.readline().strip()
        password = f.readline().strip()
    return email, password


def initialize_webdriver():
    print('Opening Chrome...')
    driver = webdriver.Chrome()
    return driver


def login(driver, email, password):
    print('Accessing Bing login page...')
    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d3CFF6759C2BD66F7277775AFC3FD6733&wp=MBI_SSL&lc=1033&CSRFToken=637a2c3c-48c1-43e6-a31e-23bc25b39a50&aadredir=1')

    print('Entering email...')
    email_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'i0116'))
    )
    email_element.clear()
    email_element.send_keys(email)

    print('Clicking Next...')
    next_button = driver.find_element(By.ID, 'idSIButton9')
    next_button.click()

    print('Entering password...')
    time.sleep(1)
    password_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'i0118'))
    )
    password_element.clear()
    password_element.send_keys(password)

    print('Clicking Sign In...')
    sign_in_button = driver.find_element(By.ID, 'idSIButton9')
    sign_in_button.click()

    print('Checking for Stay Signed In prompt...')
    time.sleep(1)
    confirm_button = driver.find_element(By.ID, 'idSIButton9')
    confirm_button.click()
    print('Logged in successfully...')

def generate_random_query():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 10)))

def perform_random_searches(driver, num_searches):
    print(f'Performing {num_searches} random searches...')
    for i in range(num_searches):
        random_query = generate_random_query()
        print(f'Searching: {random_query}')
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'sb_form_q'))
        )
        search_box.clear()
        search_box.send_keys(random_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(0.8, 1.4))

def main():
    email, password = read_credentials(CREDENTIALS_FILE)
    driver = initialize_webdriver()
    login(driver, email, password)
    perform_random_searches(driver, 35)
    print("Success!")

if __name__ == '__main__':
    main()

