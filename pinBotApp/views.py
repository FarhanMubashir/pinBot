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


    chrome_options = Options()


    chrome_options.add_argument("download.default_directory=C:/Downloads")
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=chrome_options)


    driver.get("https://www.nmc.org.uk/registration/search-the-register/")

    element = driver.find_element('id','PinNumber')
    time.sleep(3)
    element.send_keys(pin)
    loginbtn = driver.find_element('id','searchRegisterButton')
    warning = driver.find_element('id','validationSummary').text
    cook = driver.find_element('id',"CybotCookiebotDialogBodyButtonAccept").click()
    time.sleep(3)
    loginbtn.click()
    time.sleep(3)

    if warning == 'please verify you are not a robot':
        loginbtn.click()
        time.sleep(2)

    try:
        
        clickView = driver.find_element(by=By.CLASS_NAME, value="more-link").click()

        time.sleep(3)

        download = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div/div/div[2]/ul/li[2]/a').get_attribute('href')
        time.sleep(3)

        print(download,'_________________')
        # download.click()
        # print(download.text,'________download')


        time.sleep(3)

        name = driver.find_element(by=By.XPATH, value='//*[@id="main"]/div/div/div/div[3]/div[1]/dl[1]/dd').text

        context = {
            'name': name,
            'data': download,
        }

        print(name,'here it is')

        time.sleep(3)

        return render(request,'result.html',context)
    
    except:
        pass
        return redirect('/')