from selenium import webdriver
from bs4 import BeautifulSoup
import time
	


def main():
    driver = webdriver.Edge(r"C:\Users\Haysus\Desktop\Python Project\msedgedriver.exe")
    driver.get("https://www.newegg.com/amd-ryzen-9-3900x/p/N82E16819113103?quicklink=false")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    product_price = soup.find(string="\"Buy New\"").find_parent(class_="product-pane").find(class_="price-current").find("strong").string
    time.sleep(2)
    print("Price is this: " + product_price)
    

if __name__ == '__main__':
    main()



