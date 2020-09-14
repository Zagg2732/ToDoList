import Lists
import os
command = ""
Lists.lists()


while command != "exit" :
    command = input("커맨드입력 . 리스트 선택 및 수정 : set 종료 : exit \n>>>> ")

    if command == "set" :
        Lists.set_list()

    elif command == "exit" :
        break




