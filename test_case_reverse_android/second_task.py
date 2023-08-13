import subprocess
import os
from dotenv import load_dotenv
from androguard.core.bytecodes import apk

### Реализуем методы получения активити настроек разработчика

## 1 метод
# открываем документацию по аддресу - https://developer.android.com/reference/android/provider/Settings#ACTION_APPLICATION_DEVELOPMENT_SETTINGS
# видим что что Activity Action для настроек разработчика выглядит так "android.settings.APPLICATION_DEVELOPMENT_SETTINGS"

def open_dev_activity(): # открывает настройки разработчика на телефоне
    os.environ['PATH'] =  os.getenv('PATH_TO_ADB')
    command = ['adb', 'shell', 'am', 'start', '-a', 'com.android.settings.APPLICATION_DEVELOPMENT_SETTINGS']
    subprocess.run(command)

## 2 метод
# выташить из телефона файл Settings.apk через ADB, открыть его с помошью "androguard" и вывести список Activities по ключ. слову

def get_activityes_by_androguard():
    a = apk.APK('Settings.apk')
    print('Cписок активити связанных с режимом разработчика:', list(filter(lambda x: 'evelop' in x, a.get_activities())))


if __name__ == '__main__':
    load_dotenv()
    open_dev_activity()
    get_activityes_by_androguard()
    
## 3 метод
# открываем файл Settings.apk в AndroidStudio, находим там AndroidManifest.XML, 
# видим - android:name="com.android.settings.Settings$DevelopmentSettingsDashboardActivity"
# и у этого поля видим тег <action android:name="com.android.settings.APPLICATION_DEVELOPMENT_SETTINGS" />
# c помошью которого мы открываем настройки для разработчиков на телефоне через ADB
# делаем вывод что активити называется "DevelopmentSettingsDashboardActivity"
# Это же имя мы и получаем через "androguard.get_activities()"