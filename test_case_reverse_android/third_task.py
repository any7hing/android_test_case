from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from time import sleep
from dotenv import load_dotenv
import os
from selenium.common.exceptions import NoSuchElementException

## При выполнении пользовался: Appium server GUI, Genimotion, Appium inspector, Virtyal Box, Android Studio

def test_google_chrome():
    capabilities = {
        'platformName': 'Android',
        'deviceName': os.getenv('DEVICE_NAME'),
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)

    try:
    
        digit1_btn = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Chrome"]')
        digit1_btn.click()
        sleep(1)
    except (NoSuchElementException,):
        pass
    
    finally:
        
        find_text = driver.find_element(by=AppiumBy.ID, value ='com.android.chrome:id/url_bar')
        find_text.click()
        sleep(1)  
        find_text.send_keys('собака')
        buff = driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView')
        buff.click()
        sleep(1)
        for _ in range(8):
            driver.swipe(470, 2000, 470, 400, 400)
        sleep(1)
        el = driver.find_element(by=MobileBy.ANDROID_UIAUTOMATOR, value='new UiSelector().textContains("собак")')
        if el is None:
            for _ in range(2):
                driver.swipe(470, 2000, 470, 400, 400)
                el.click()
        else:
            el.click()
        sleep(3)
        driver.press_keycode(4)
        driver.quit()


if __name__ == '__main__':
    load_dotenv()
    test_google_chrome()
