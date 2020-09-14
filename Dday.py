import datetime
# D-Day 목표를 출력하는 리스트입니다.

#D-Day 목표날짜가 포함된 세팅 만들기
def set_dday(txt_name):
    goal = (input("추가할 %s 목표를 입력해주세요. ex) 1. 빨래하기\n>>>>" % txt_name[:-4]))
    year = int(input("목표년도(숫자만) : "))
    month = int(input("목표 월(숫자만) : "))
    day = int(input("목표 일(숫자만) : "))
    hour = int(input("목표 시(숫자만) : "))
    return goal + " 목표일 :"+ str(datetime.datetime(year, month, day, hour))[:-6] + "시"

# 목표 D-Day 리스트와 몇번째 목표인지 번호를 받고 며칠 남았는지 계산해줌
def remain_days(list,index) :

    slices = list[index-1]

    nyear = int(slices[-14:-10])  # 년도
    nmonth = int(slices[-9:-7])  # 월
    nday = int(slices[-6:-4])  # 일
    nhour = int(slices[-3:-1])  # 시

    goal_day = datetime.datetime(nyear, nmonth, nday, nhour)
    today = datetime.datetime.now()

    return goal_day - today