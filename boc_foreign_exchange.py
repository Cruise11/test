import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 获取命令行参数
date = sys.argv[1]
currency_code = sys.argv[2]

# 设置浏览器选项
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无头模式，不打开浏览器窗口
options.add_argument('--disable-gpu')  # 禁用GPU加速

# 打开网页
driver = webdriver.Chrome(options=options)
driver.get("https://www.boc.cn/sourcedb/whpj/")

# 输入日期
date_input = driver.find_element_by_id("erdat")
date_input.clear()
date_input.send_keys(date)

# 选择货币
currency_select = driver.find_element_by_id("pjname")
currency_select.send_keys(currency_code)

# 点击查询按钮
query_button = driver.find_element_by_class_name("searchBut")
query_button.click()

# 获取现汇卖出价
price = driver.find_element_by_xpath("//tr[position()>1]/td[5]").text

# 打印到result.txt文件中
with open("result.txt", "w") as f:
    f.write(f"日期: {date}\n货币代号: {currency_code}\n现汇卖出价: {price}")

driver.quit()