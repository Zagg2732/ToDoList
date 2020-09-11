import os

## DailyList는 매일 할일(routine)식으로 저장됩니다.

list_name = 'Daily.txt'

def make_list () :
    open_list = open( list_name, 'w', encoding= 'utf-8')
    input_command = None
    check_list = []

    while input_command != "exit" :
        input_command = input("명령어 입력 add : 리스트 추가  undo : 추가한 리스트 취소 exit : 저장 및 종료\n")
        if input_command == "add":
            check_list.append(input("추가할 리스트를 입력해주세요. ex) 1. 빨래하기\n>>>>"))
            check_list.sort()
            print(check_list)


        elif input_command == "undo":
            check_list.pop()

        elif input_command == "exit":
            for i in check_list:
                open_list.write(i+"\n")
            print("리스트 만들기 종료")
            print("저장 경로 -> " + os.getcwd() + "\\" + list_name)

        else :
            print(input_command + " 명령어가 없습니다 다시 입력해주세요")


    open_list.close()

warning = input("이 코드를 실행하면 기존에 저장된 %s의 내용물이 사라지고 다시 입력합니다. 그래도 계속 하시겠습니까? (Y/N)\n" % list_name)
if warning == "Y":
    make_list()