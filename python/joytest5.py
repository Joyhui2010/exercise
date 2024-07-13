"""
题目：格式化当前时间输出，暂停一秒输出，并格式化当前时间。
类似：
2023-10-21 17:48:40
2023-10-21 17:48:41
"""
import datetime
from time import sleep
# from datebase import one hanshu

# 获取当前日期和时间
current_datetime = datetime.datetime.now()
formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Formatted date and time: {formatted}")
# print(current_datetime)
print(formatted)

sleep(1)  # 暂停1秒

current_datetime = datetime.datetime.now()
formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(f"Formatted date and time: {formatted}")
# print(current_datetime)
print(formatted)



# from datetime import timedelta
# delta = timedelta(seconds=1)
# future_date = current_datetime + delta
# formatted = future_date.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted)

# print(future_date)
