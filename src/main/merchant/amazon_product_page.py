from selenium import webdriver
from bs4 import BeautifulSoup
import logging as logger

class AmazonProductPage:
    def __init__(self, url):
        self.url = url
        self.soup_var = BeautifulSoup(self.go_to_amazon_link().page_source, "lxml")

    def go_to_amazon_link(self):
        driver = webdriver.Edge(r"C:\Users\Samson\Desktop\Projects\msedgedriver.exe")
        driver.get(self.url)
        return driver

    def get_product_price(self):
        price = self.soup_var.find(id="newBuyBoxPrice").string
        if "$" in price:
            logger.info(f"Price({price}) was found on the Amazon product page")
            return price
        else:
            logger.warning("Unable to determine price from Amazon product page using id(newBuyBoxPrice)")
            return None

    def get_product_name(self):
        name = self.soup_var.find(id="productTitle").string.strip()
        if len(name) > 0:
            logger.info(f"The Amazon product name is {name}")
            return name
        else:
            logger.warning("Unable to get the product's name from Amazon product page using id(productTitle)")
            return None


    def get_product_availability(self):
        availability = self.soup_var.find(id="availability").find("span").string
        if "in stock" in availability.lower():
            logger.info(f"The Amazon product name is in stock.")
            return True
        else:
            logger.warning("Unable to get the product's availability from Amazon product page using id(availability)")
            return False

    @staticmethod
    def get_page_soup(driver):
        return BeautifulSoup(driver.page_source, "lxml")

