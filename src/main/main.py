from selenium import webdriver


def main():
    driver = webdriver.Chrome("C:\\Users\\Haysus\\Desktop\\Python Project\\chromedriver.exe")
    driver.get("google.com")

if __name__ == '__main__':
    main()