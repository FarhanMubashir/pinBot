from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Create your views here.


def index(request):
    return render(request,'index.html')



def apicall(request):
    if request.method == 'POST':
        pin = request.POST['pin']
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.nmc.org.uk/registration/search-the-register/")

    element = driver.find_element('id','PinNumber')
    time.sleep(5)
    element.send_keys(pin)
    loginbtn = driver.find_element('id','searchRegisterButton')
    warning = driver.find_element('id','validationSummary').text
    cook = driver.find_element('id',"CybotCookiebotDialogBodyButtonAccept").click()
    time.sleep(5)
    loginbtn.click()
    time.sleep(5)

    if warning == 'please verify you are not a robot':
        loginbtn.click()
        time.sleep(5)

    try:
        
        clickView = driver.find_element(by=By.CLASS_NAME, value="more-link").click()

        time.sleep(5)

        download = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div/div/div[2]/ul/li[2]/a')
        time.sleep(7)

        download.click()
        print(download.text,'________download')

        time.sleep(5)
    
    except:
        pass

    return redirect('/')