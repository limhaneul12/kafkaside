import datetime
import time
import os
import logger

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# 현재 시각하는 시간 설정
start_time = datetime.datetime.now()

# 로그
logging = logger.log()

option_chrome = webdriver.ChromeOptions()
option_chrome.add_argument('headless')
option_chrome.add_argument("disable-gpu")
option_chrome.add_argument("disable-infobars")
option_chrome.add_argument("--disable-extensions")


# 속도
prefs = {'profile.default_content_setting_values'
         : {'cookies': 2, 'images': 2, 'plugins': 2, 'popups': 2, 'geolocation': 2, 'notifications': 2,
            'auto_select_certificate': 2, 'fullscreen': 2, 'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
            'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 'ppapi_broker': 2,
            'automatic_downloads': 2, 'midi_sysex': 2, 'push_messaging': 2, 'ssl_cert_decisions': 2,
            'metro_switch_to_desktop': 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
            'durable_storage': 2}
         }

option_chrome.add_experimental_option('prefs', prefs)

# chromedriver_path
web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=option_chrome)
data = web_driver.get("https://www.naver.com")

def scroll_injection_around() -> None:
   pass


class GoogleUtilityDriver:
   def __init__(self, driver=web_driver) -> None:
      self.xpath = None
      self.url = f"https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
      self.driver = driver
   
   def page(self) -> None:
      self.driver.get(self.url)
      return self.driver.page_source
      

if __name__ == "__main__":
   a = GoogleUtilityDriver()
   a.page()
