from selenium import webdriver
from bs4 import BeautifulSoup
import time
from merchant.amazon_product_page import AmazonProductPage


def main():
    amzn = AmazonProductPage("https://www.amazon.com/LG-27GL83A-B-Ultragear-Compatible-Monitor/dp/B07YGZL8XF")
    amzn_price = amzn.get_product_price()
    amzn_product_name = amzn.get_product_name()
    amzn_availability = amzn.get_product_availability()
    if amzn_availability:
        print(f"The product ({amzn_product_name}) is {amzn_price}")
    else:
        print(f"The product ({amzn_product_name}) is not available")

    

if __name__ == '__main__':
    main()



