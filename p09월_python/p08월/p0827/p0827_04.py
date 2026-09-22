import datetime
now=datetime.datetime.now()
print()
print(now.year)
print(now.month)

# # format
# # 123-> 5자리 빈 공백 0으로 채워서 출력하시오.
# print("{:05d}".format(123)) # 00123
# print("{:05,d}".format(123456789)) # ,를 넣으면 천 단위 숫자 표시 가능 123,456,789
# print("{:02d}".format(8)) # 08

# 월을 출력하는데, 1,2,3..... 9월까지는 01월, 02월, 03월.... 이런식으로 출력하고 10월, 11월, 12월은 10월, 11월, 12월로 출력하시오.

# print("{:02d}월".format(now.month))
# print("{:02d}월,{:02d}월,{:02d}월,{:02d}월,{:02d}월,{:02d}월,{:02d}월,{:02d}월,{:02d}월".format(1,2,3,4,5,6,7,8,9))
# print("{:02d}분".format(now.minute))

# 2026년 8월 27일 11시 57분 20초
print(now)
f_date=now.strftime("%y--%m--%d")
print(f_date)

print(now)
f_date=now.strftime("%y년--%m월--%d일")
print(f_date)

print(now)
f_date = now.strftime("%Y년%m월%d일 %H시%M분%S초")
print(f_date)

print(now)
f_date = now.strftime("%Y년M월%D일 %H시%M분%S초")
print(f_date)

print("{}년{}월{}일 {}시{}분{}초".format(\
    now.year,now.month,now.day,now.hour,\
    now.minute,now.second))

