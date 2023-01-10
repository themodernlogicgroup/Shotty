import sys
import os
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
import datetime
import colorama
from colorama import Fore, Style

OUTPUT = 'outputs'
INPUT_FILE = sys.argv[1]

# date time function

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S-{fname}'):
        return datetime.datetime.now().strftime(fmt).format(fname=fname)

# Try logic 

try:
   file = open(INPUT_FILE, "r")
except IOError:
   print(Fore.RED + "there was an error reading the file")
   sys.exit()

if len(sys.argv) > 3:
    if len(sys.argv) < 4:
        print(Fore.RED + "ERROR: Missing folder name. eg: --out <folder_name")
        sys.exit()
    else:
        OUTPUT = sys.argv[3]


fileData = tuple(file.readlines())
file.close()

if len(fileData) <= 0:
    print(Fore.RED + "ERROR: File is empty! Please data into the file")
    sys.exit()

# URL Parser

def urlParser(url):
    o = urlparse(url)
    if len(o.scheme) == 'http' or len(o.scheme) == 'https':
        return url
    elif len(o.path) <= 0:
        return False
    else:
        return 'http://' + o.path

# take screenshots with chrome


def takeScreeshot(url):
    if len(url) == 0:
        return False
    else:
        u = urlParser(url.strip())
        if u:
            if not os.path.exists(OUTPUT):
                os.makedirs(OUTPUT)
            
            chrome_options = Options()
            chrome_options.add_argument("--headless") 
            driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
            driver.set_window_size(1280, 1024) 
            driver.get(u)
            driver.save_screenshot(os.getcwd() + '/' +OUTPUT + '/screenshot-' + urlparse(url).path + '.png')  
            return True
        else:
            return False

if len(fileData) > 0:
    for url in fileData:
        result = takeScreeshot(url)
        if result:
            print(url.strip() + Fore.GREEN + ' is ready.')
sys.exit()