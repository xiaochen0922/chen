# import pytest
#
# if __name__ == '__main__':
#     pytest.main()
# import requests
# import time
# import datetime
# start = time.time()  # 请求前记录时间
# #
# url_path = "https://api.lichidental.com/lichidental-web/product/single/detail?pdCode=PDC0854&productSku=300443&coupon=true&channel=APP"
# response = requests.get(url=url_path,headers={"USERID":"ca520250ed85477a9fac7b2d7a7f0e13"})
# end = time.time()  # 请求后记录时间
# # 输出响应时间
# #
# # dt=datetime.datetime.fromtimestamp(start)
# # dt2=datetime.datetime.fromtimestamp(end)
# response_time = end - start
# #
# data_str1 = str(response_time)
# # print(dt)
# # print(dt2)
# print(f"加了参数响应时间: {response_time}秒")
# print(response.text)  # 使用response.text打印响应文本
# with open('D:\\pythonfile\\pytest_demo\\优化后的.txt', 'a') as file:
#     file.write(f"加参数响应时间: {data_str1}秒 \n")
#
# start2 = time.time()
# url_path2 = "https://api.lichidental.com/lichidental-web/product/single/detail?pdCode=PDC0854&productSku=300443&channel=APP"
# response2 = requests.get(url=url_path2,headers={"USERID":"ca520250ed85477a9fac7b2d7a7f0e13"})
# end2 = time.time()  # 请求后记录时间
# response_time2 = end2 - start2
# data_str = str(response_time2)

# print(f"没加参数响应时间: {response_time2}秒")
# print(response2.text)  # 使用response.text打印响应文本
# with open('D:\\pythonfile\\pytest_demo\\优化后的.txt', 'a') as file:
#     file.write(f"没加参数响应时间: {data_str}秒 \n")


# start3 = time.time()
# url_path3 = "https://test.api.lichidental.com/lichidental-web/home/mid/component/detail/list"
# response3 = requests.get(url=url_path3,headers={"USERID":"ca520250ed85477a9fac7b2d7a7f0e13"})
# end3 = time.time()  # 请求后记录时间
# response_time3= end3 - start3
# print(f"响应时间: {response_time3}秒")
# print(response3.json())
# import os
# print (os.getcwd()+'\main_run.py')

# months=[
# 'January','February','March',
# 'April','May','June','July','August','September','October','November','December']
#
# endings=['st','nd','rd']+17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']
# weekdays='-二三四五六七'
# month=int(input('输入月份数字:'))
# day=int(input('输入第几天数字:'))
# weekday=int(input('输入星期几数字:'))
#
# month=months[month-1]
# ordinal= endings[day-1]
# weekday=weekdays[weekday-1]
# print(month +''+str(day)+ordinal+','+weekday)


print(0)