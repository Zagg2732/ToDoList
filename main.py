import Lists
import os


command = ""
Lists.lists()
print("-----------------")
while command != "exit" :
    command = input("커맨드입력 \n리스트 선택 및 수정 : set \n수정하지 않고 넘어가기 : pass \n>>>> ")

    if command == "set" :
        Lists.set_list()

    elif command == "pass" :
        break

command = ""
while command != "exit" :
    command = input("커맨드입력\n오늘 한일 : done 남은 일만 보기 : remain \n한일 초기화 : clear 한일 모두 초기화 : clearA\n>>>> ")

    if command == "done" :
        txt_name = Lists.choose()
        print(txt_name)
        check_list = Lists.open_txt(txt_name)
        print(check_list)
        done = input("몇 번째 할일을 했습니까?       뒤로가기 : undo\n>>>> ")
        if done == "undo" :
            pass
        else:
            done = int(done)
            print(check_list[done - 1] + " 가 한일에 추가됩니다.")
            done_list = Lists.open_txt("Done" + str(txt_name))
            done_list.append(check_list[done - 1])
            Lists.write_text("Done" + str(txt_name),done_list)

    elif command == "remain" :
        txt_name = Lists.choose()
        print(Lists.current_list(txt_name))

    elif command == "clear" :
        check_list = []
        txt_name = Lists.choose()
        Lists.write_text("Done"+str(txt_name),check_list)

    elif command == "clearA" :
        check_list = []
        for i in range(Lists.done_txt_types) :
            erase = open(i, w, encoding= 'utf-8')
            erase.close()
    else:
        print("명령어를 잘못 입력하셨습니다.")









