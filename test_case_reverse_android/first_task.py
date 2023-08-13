import subprocess
from androguard.core.bytecodes import apk
import os
from dotenv import load_dotenv

### Будем получать необходимы нам данные 2 способами, через AAPT и с помошью библиотеки "androguard"
### И сравнивать результаты полученные с использованием разных методов

def get_package_name_by_AAPT():
    command = ['aapt', 'dump', 'badging', os.path.abspath('Dingtone_v6.1.0.apk')]
    process = subprocess.run(command, capture_output=True, text=True, shell=True)
    return process.stdout[process.stdout.find("package: name='")+15:33]


def get_main_activity_by_AAPT():
    command = ['aapt', 'dump', 'badging', os.path.abspath('Dingtone_v6.1.0.apk')]
    process = subprocess.run(command, capture_output=True, text=True, shell=True)
    start_index = process.stdout.find("activity: name=")
    return process.stdout[start_index+16: start_index+58]


def get_list_of_permission_by_AAPT():
    command = ['aapt', 'dump', 'badging', os.path.abspath('Dingtone_v6.1.0.apk')]
    process = subprocess.run(command, capture_output=True, text=True, shell=True)
    start_index = process.stdout.find("uses-permission:")
    lst_of_permissions = process.stdout[start_index:1839].strip().split(sep='\n')
    return(len(lst_of_permissions))


if __name__ == '__main__':
    load_dotenv()
    os.environ['PATH'] =  os.getenv('PATH_TO_AAPT')
    a = apk.APK('Dingtone_v6.1.0.apk')
    
    assert get_package_name_by_AAPT() == a.get_package()
    print("package_name приложения =",a.get_package())
    
    assert get_main_activity_by_AAPT()==a.get_main_activity()
    print('main_activity =',a.get_main_activity())
    
    assert get_list_of_permission_by_AAPT()==len(a.get_permissions())
    print('количество запрашиваемых разрешений =',len(a.get_permissions()))
    
# ну и самое простое - чтение документации
# переходим на сайт - https://dingtone.en.uptodown.com/android/download/101360663
# получаем необходимую информацию.

# так же можно использовать приложение на телефоне APK Viewer