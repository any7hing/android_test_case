from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from dotenv import load_dotenv
import os
from selenium.common.exceptions import NoSuchElementException

## Браузер должен быть последней версии. При первом запуске теста - иметь вид описанный в Readme.
## После первого прогона, можно запускать многократно

def test_google_chrome():
    capabilities = {
        'platformName': 'Android',
        'deviceName': os.getenv('DEVICE_NAME'),

    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    driver.implicitly_wait(1)

    try:
    
        digit1_btn = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Chrome')
        digit1_btn.click()
        
    except (NoSuchElementException,):
        pass
    
    finally:
            search_box_text = driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/search_box_text')
            search_box_text.click()
        
            find_text = driver.find_element(by=AppiumBy.ID, value ='com.android.chrome:id/url_bar')
            find_text.click()
            find_text.send_keys('собака')
            
            buff = driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
            buff.click()
            
            for _ in range(10):
                driver.swipe(470, 2000, 470, 400, 400)
            el = driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().textContains("обак").clickable(true)')
            el.click()
            
            sleep(3)
            driver.press_keycode(4)
            driver.press_keycode(4)
        
if __name__ == '__main__':
    load_dotenv()
    test_google_chrome()
