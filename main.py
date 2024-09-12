from gettext import install

import manager as manager
import pip
import selenium as selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up WebDriver (make sure you have the correct path for the chromedriver)
driver = webdriver.Chrome()

# Open amazon.in
driver.get("https://www.amazon.in")

# Search for 'LG Soundbar'
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("LG Soundbar")
search_box.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(3)

# Get all product containers on the page
products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

product_data = []

# Loop through the products and collect names and prices
for product in products:
    try:
        # Extract product name
        name = product.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
    except:
        name = "Unknown Product"

    try:
        # Extract price (if available)
        price_whole = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text.replace(',', '')
        price_fraction = product.find_element(By.XPATH, ".//span[@class='a-price-fraction']").text
        price = float(price_whole + '.' + price_fraction)
    except:
        # Handle missing price
        price = 0.0

    # Store in list as a tuple (price, name)
    product_data.append((price, name))

# Sort product data by price
sorted_products = sorted(product_data, key=lambda x: x[0])

# Print sorted products
for price, name in sorted_products:
    print(f"{price} - {name}")

# Close the browser
driver.quit()