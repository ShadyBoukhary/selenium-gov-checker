import requests
import json
from urllib.request import Request, urlopen
from selenium import webdriver
import time
import smtplib, ssl


def send_email():
    port = 465 # SSL port
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    

    context = ssl.create_default_context()
    print("Sending email.")

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, "password")
        server.sendmail(sender_email, receiver_email, message)


def find_available():
    driver.get(site)
    # click radio button
    inputs = driver.find_elements_by_xpath("//input[@name='planning' and @value='21029']")
    if inputs:
        driver.set_window_size(1920, 1080)

        next_button = inputs[0]
        time.sleep(0.2)
        next_button.click()
        # click submit button
        buttons = driver.find_elements_by_xpath("//input[@type='submit']")
        if buttons:
            submit_button = buttons[0]
            submit_button.click()
            time.sleep(0.2)
            html = driver.page_source
            if "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement." in html:
                print("Not available\n")
            elif "502 Bad Gateway" not in html:
                print("Available")
                return True
        else:
            print("Submit button not found.")
    else:
        print("Radio Button not found.")
        
    return False

def main():

    while not find_available():
        driver.set_window_size(1280, 720)
        time.sleep(60)
        print("Checking availability")
        pass
    send_email()
    driver.stop_client()

if __name__ == "__main__":
    site= "http://www.essonne.gouv.fr/booking/create/14056/1"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-check-certificate')
    options.add_argument("--test-type")
    options.add_argument('headless')
    options.add_argument('--disable-extensions')
    options.add_argument('--profile-directory=Default')
    options.add_argument("--incognito")
    options.add_argument("--disable-plugins-discovery")
    options.add_argument("--start-maximized")    
    driver = webdriver.Chrome('./chromedriver', options=options)
    message = """\
Subject: Shady Boukhary Automated Message

You can now visit the website and renew your residence permit."""
    main()
