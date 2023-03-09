# """点击榜"""
# from selenium import webdriver
# from lxml import etree
# from selenium.webdriver.common.by import By
# import time

# import random
# import re
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

# # 导入mysql操作类别
# # option.add_argument('--headless')
# # 无头模式
# option = webdriver.ChromeOptions()
# # 允许root模式允许google浏览器
# option.add_argument('--no-sandbox')
# # option.add_argument('--headless')
# option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
# option.add_argument('--disable-blink-features=AutomationControlled')
# driver = webdriver.Chrome(executable_path=r"C:\Users\walker\Documents\chromedriver_win32\chromedriver.exe",chrome_options=option)
# # 隐藏对selenium的检测
# # //滑块解决
# # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
# #   "source": """
# #     Object.defineProperty(navigator, 'webdriver', {
# #       get: () => undefined
# #     })
# #   """
# # })
# def getImgUrl(imgStr:str)->str:
#     try:
#         p1=re.compile(r'[(](.*?)[)]', re.S) 
#         return re.findall(p1,imgStr)[0]
#     except:
#         return ""
# if __name__=="__main__":
#     driver.get("https://s.1688.com/selloffer/offer_search.htm?keywords=%CD%E0%D7%D3&spm=a26352.13672862.searchbox.input&beginPage=1#sm-filtbar")
#     # /html/body/div[1]/div/div[7]/div[4]/div/div/ul/div[2]/div/div[1]/div/a/div
#     # https://www.coder.work/article/2283103
#                                          #/html/body/div[1]/div/div[7]/div[4]/div/div/ul/div[2]/div/div[1]/div/a/div
#     img_url=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[7]/div[4]/div/div/ul/div[1]/div/div[1]/div/a/div').get_attribute('style')
#     print(getImgUrl(img_url))

from urllib import parse
s1=b"%D0%AC%D7%D3"
# 
s1.decode("utf-8")
s="鞋子"
# a=parse.quote(s.encode('gbk'))
# print(a)
b=str(parse.unquote(s1))
print(b)