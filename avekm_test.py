#!/usr/bin/python3
#coding=utf-8

'''
 avekm界面自动化测试示例
'''


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException


def log(msg):
    '''
    错误输出
    :param msg: 消息信息
    :return:
    '''
    print(msg)

def avekm_login(browser, url):
    browser.get(url)

    # 输入用户名和密码
    browser.find_element(By.ID, "userName").send_keys(
        "administrator")
    browser.find_element(By.ID, "password").send_keys(
        "administrator")

    # “登录”按钮没有id属性，就改用classname属性搜索
    browser.find_element(By.CLASS_NAME, "login_button").send_keys(
        Keys.ENTER)

    try:
        # 等待打开页面
        WebDriverWait(browser, 5, 0.5).until(
            EC.title_is(r'欢迎您：系统管理员')
        )
    except TimeoutException as e:
        log("登录失败")
        return -1

    log("登录成功")

    # 跳转到知识管理页面
    # 鼠标双击，调用http://10.0.0.158:8090/avekm/platform/ui/edo/edo.js
    browser.find_element_by_xpath(
        r'//*[@id="grid|1001|domainName"]/div').click()


    return 0


if __name__=="__main__":
    browser = webdriver.Chrome()

    ret = avekm_login(browser,
                      r'http://10.0.0.158:8090/avekm/index.jsp')

    browser.quit()

    # try:
    #     ret = avekm_login(browser,
    #         r'http://10.0.0.158:8090/avekm/index.jsp')
    # except Exception as e:
    #     log('str(Exception):\t' + str(Exception))
    #     log('str(e):\t\t'+str(e))
    # finally:
    #     browser.quit()


