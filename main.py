#스크립트 클래스로서 DdayList,DailyList, TodayList 를 이용해 할일을 체크합니다.
list_input = None

open_list = open('Daily.txt', 'r', encoding='utf-8')

daily_list = []

for line in open_list:
    data = line.strip()
    daily_list.append(data)
    
open_list.close()
print("체크 리스트 : " + str(daily_list))



while list_input != "x" :
    list_input = input("명령어를 입력해주세요.\ndone : 한일(체크리스트에서 삭제)\nprint : 리스트 출력\nadd : 리스트추가\n"
                       "save : 현재 체크리스트를 저장\nexit : 종료하기\n>>>>")

    if list_input == "add":
        open_list = open('DailyDone.txt', 'w')

        daily_list.append(input("추가할 리스트를 입력해주세요\n"))
        daily_list.sort()
        print(daily_list)

    elif list_input == "done" :
        done = int(input("삭제할 리스트 번호를 입력해주세요\n"))
        daily_list.pop(done - 1)
        print(daily_list)
        
    elif list_input == "print" :
        for i in daily_list :
            print(i)

    elif list_input == "exit":
        print("프로그램을 종료합니다")

    elif list_input == "save" :
        save = open('Daily.txt', 'w', encoding='utf-8')
        save.write(daily_list)

    else:
        print(list_input + " 라는 명령어가 없습니다. \n")