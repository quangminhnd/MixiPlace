import selenium
import os
import selenium.webdriver as sw
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import threading
import time
#from msedge.selenium_tools import Edge, EdgeOptions
#import shutil
#shutil.rmtree('D:\\Edge Data\\')
#os.makedirs("D:\\Edge Data\\")


credentials = [
    ("HVS_1", "H0vietsang2005"),
    ("Express_Ad5978","VNvodich9901"),
    ("Traditional_Name5952","AAbb123456cc"),
    ("daddypunz","-j-PTS!rSt3Lc7D")
    ]





import urllib.request

def read_to_string(target_url):
    with urllib.request.urlopen(target_url) as response:
        return response.read().decode('utf-8').strip()
    
js = read_to_string("https://raw.githubusercontent.com/LiquidRekto/rplacevnhideout/master/us.js")

def login(driver: sw.Edge | sw.Chrome | sw.Firefox, username: str, password: str):
    # Đăng nhập vào reddit
    try:
        username_box = driver.find_element(By.ID, "loginUsername")
        password_box = driver.find_element(By.ID, "loginPassword")
        username_box.clear()
        username_box.send_keys(username)
        password_box.clear()
        password_box.send_keys(password)
        # Bấm nút đăng nhập
        password_box.send_keys(Keys.ENTER)

        # r/place canvas là một iframe, source là https://garlic-bread.reddit.com.
        # ID của iframe này thay đổi sau mỗi reload, phải fetch lại
        time.sleep(5)
    
        driver.execute_script(js)
    except Exception as e:
        driver.delete_all_cookies()

        print(e)



N = len(credentials)   # Number of browsers to spawn
thread_list = list()

# Start test
for i in range(N):
    edge_options = sw.Edge.EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_experimental_option("detach", True)
    edge_options.add_argument("-inprivate")

    # Set the path of the profile ending with User Data, not the profile folder
    #edge_options.add_argument(f"--user-data-dir=D:\\Edge Data\\{i}")

    # Specify the actual profile folder
    #edge_options.add_argument(f"profile-directory=My_Profile_{i}")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver = sw.Edge(executable_path='MicrosoftWebDriver.exe',options=edge_options)
    driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2Fr%2Fplace%2F%3Fscreenmode%3Dfullscreen%26cx%3D168%26cy%3D245%26px%3D19")
    
    t = threading.Thread(name='Test {}'.format(i), target=login, args=[driver,credentials[i][0],credentials[i][1]])
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    

# Wait for all threads to complete
#for thread in thread_list:
#    thread.join()

print('Test completed!')