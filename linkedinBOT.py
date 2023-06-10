import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

def create_driver():
    """
    Create a new instance of the Chrome WebDriver.
    
    Returns:
        WebDriver: The Chrome WebDriver instance.
    """
    return webdriver.Chrome()

def login(email, password):
    """
    Perform login operation on LinkedIn.
    
    Args:
        email (str): The email address for login.
        password (str): The password for login.
    """
    if not driver.get_window_size()['width'] == driver.execute_script('return window.innerWidth') and not driver.get_window_size()['height'] == driver.execute_script('return window.innerHeight'):
        driver.maximize_window()
    time.sleep(5)
    
    # Find the email and password fields and enter the credentials
    email_field = driver.find_element(By.ID, 'username')
    pw_field = driver.find_element(By.ID, 'password')
    
    email_field.clear()
    pw_field.clear()
    
    email_field.send_keys(email)
    pw_field.send_keys(password)
    
    # Click the login button
    login_btn = driver.find_element(By.XPATH, '//button[starts-with(@class,"btn__primary")]')
    login_btn.click()

def search(keyword):
    """
    Perform a search operation on LinkedIn.
    
    Args:
        keyword (str): The search keyword.
    """
    if not driver.get_window_size()['width'] == driver.execute_script('return window.innerWidth') and not driver.get_window_size()['height'] == driver.execute_script('return window.innerHeight'):
        driver.maximize_window()
    time.sleep(5)
    
    # Find the search field and enter the keyword
    search_field = driver.find_element(By.CLASS_NAME, 'search-global-typeahead__input')
    search_field.clear()
    search_field.send_keys(keyword)
    search_field.send_keys(Keys.ENTER)

def connect(count):
    """
    Connect with LinkedIn users based on the search results.
    
    Args:
        count (int): The number of connections to make.
    """
    if not driver.get_window_size()['width'] == driver.execute_script('return window.innerWidth') and not driver.get_window_size()['height'] == driver.execute_script('return window.innerHeight'):
        driver.maximize_window()
    time.sleep(5)
    
    current = 0
    while current < count:
        wait = WebDriverWait(driver, 10)
        people_ctg = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@class,"search-reusables__filter-pill-button")]')))
        if people_ctg[0].get_attribute("id") == '':
            people_ctg[0].click()
        
        time.sleep(5)
        
        d = driver.find_elements(By.CLASS_NAME, 'artdeco-button__text')
        for i in d:
            if i.text == 'Connect':
                i.click()
                send = driver.find_element(By.XPATH, '//button[contains(@class,"artdeco-button--primary")]')
                is_clickable = EC.element_to_be_clickable((By.XPATH, '//button[contains(@class,"artdeco-button--primary")]'))(driver)
                cross = driver.find_element(By.XPATH, '//button[starts-with(@class,"artdeco-modal__dismiss")]')
                if is_clickable and current < count:
                    send.click()
                    current+=1
                else:
                    cross.click()


        
        time.sleep(5)
        
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Click the next button for pagination
        next_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class,"artdeco-pagination__button--next")]')))
        next_btn.click()
        
        print(f"Successfully connected to {current} people. {count - current} connections remaining...")

# Create a new instance of the Chrome WebDriver
driver = create_driver()

url = 'https://www.linkedin.com/login'
driver.get(url)

# Perform login
login('YOUR-EMAIL-ID', 'YOUR-PASSWORD')

# Perform search
search('-KEYWORD-')

# Connect with LinkedIn users
connect(10)

# Close the WebDriver
driver.close()
