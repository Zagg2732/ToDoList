import os
import datetime
import re
import Dday

## DailyList는 매일 할일(routine)식으로 저장됩니다.


def set_list () :

    number = int(input("세팅할 Text파일 번호 입력: ")) #번호를 받아서 ToDoList의 텍스트이름 받아옴
    if number == 1 :
        txt_name = "D-Day.txt"
    elif number == 2 :
        txt_name = "Daily.txt"
    elif number == 3 :
        txt_name = "Today.txt"

    #warning = input("이 코드를 실행하면 기존에 저장된 %s의 내용물이 사라지고 다시 입력합니다. 그래도 계속 하시겠습니까? (Y/N)\n" % txt_name)
    #if warning == "Y":
    open_list = open(txt_name , 'r', encoding='utf-8')
    check_list = []

    for line in open_list:
        data = line.strip()
        check_list.append(data)


    input_command = None

    while input_command != "exit":
        input_command = input("%s 리스트를 불러왔습니다. %s \n add : 리스트 추가 list : 리스트 출력 \nundo : 추가한 리스트 "
                              "취소 del : 특정 리스트 삭제 exit : 저장 및 뒤로가기\n>>>> " %(txt_name, check_list))
        if input_command == "add":
            if txt_name == "D-Day.txt" :
                check_list.append(Dday.set_dday("D-Day.txt"))

            else : check_list.append(input("추가할 리스트를 입력해주세요. ex) 1. 빨래하기\n>>>> "))
            check_list.sort()

        elif input_command == "list":
            print(check_list)

        elif input_command == "del" :
            done = int(input("삭제할 리스트 번호를 입력해주세요\n"))
            check_list.pop(done - 1)
            print(check_list)


        elif input_command == "undo":
            check_list.pop()

        elif input_command == "exit":
            write_list = open(txt_name, 'w', encoding='utf-8')
            for i in check_list:
                write_list.write(i + "\n")
            print("리스트 만들기 종료")
            print("저장 경로 -> " + os.getcwd() + "\\" + txt_name)

        else:
            print(input_command + " 명령어가 없습니다 다시 입력해주세요")


    else :
        return False

def load_txt(txt_name) :
    load_txt = open(txt_name , 'r', encoding='utf-8')
    print("------%s------" % txt_name[:-4])
    for x in load_txt :
        print(x.strip())

def lists() :
    print("List 목록을 불러옵니다.")
    file_list = os.listdir("./")
    txt_list = [x for x in file_list if x.endswith(".txt")] #경로내의 모든 텍스트 폴더 찾기
    i = 1
    for x in txt_list :
        print(str(i) + "번 : " + x)
        i += 1
    for x in txt_list :
        load_txt(x)

