import random
import os
import socket
import time
start_menu = True
connecting_menu = False
game_menu = False
list_of_cart = []
turn = True
tedad_card = 5
tedad_card_harif = 5
win = False
lose = False
seek = 1
hostname =input("what is your IP: ")
port = int(input("port: "))
while True:
    if start_menu:
        print("----------------------------")
        print("|    welcome to bazi (s)   |")
        print("----------------------------")
        print(f"hostname: {hostname}")
        print("[1]Start                    ")
        print("[2]Exit                     ")
        harecat = int(input(">> "))
        if harecat == 1:
            start_menu = False
            connecting_menu = True
        elif harecat == 2:
            break
    elif connecting_menu :
        ip = hostname
        os.system("cls")
        print("connecting ...")
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((ip,port))
        print("waiting for client ...")
        server.listen(1)
        con, add = server.accept()
        print("connected")
        connecting_menu = False
        game_menu = True
        for a in range(5):
            list_of_cart.append(random.randint(1,9))
    elif win:
        print("      __________        ")
        print("  /---|         |---\   ")
        print("  \---|   WIN   |---/   ")
        print("       \       /        ")
        print("        \     /         ")
        print("        |     |         ")
        print("        |     |         ")
        print("        -------         ")
        time.sleep(5)
        quit()
    elif lose:
        print("      __________        ")
        print("     /           \      ")
        print("    /   []   []   \     ")
        print("    |      |      |     ")
        print("    |    _____    |     ")
        print("    \   /     \   /     ")
        print("     \___________/      ")
        print("         LOSE           ")
        time.sleep(5)
        quit()
    elif game_menu:
        if turn:
            print("-------------------------")
            print("|   what is your move?  |")
            print("-------------------------")
        elif turn == False :
            print("-------------------------")
            print("|     Turn player 1     |")
            print("-------------------------")

        if tedad_card_harif == 5:
            print("  1    2    3    4    5  ")
            print(" [?]  [?]  [?]  [?]  [?] ")
        if tedad_card_harif == 4:
            print("  1    2    3    4   ")
            print(" [?]  [?]  [?]  [?]  ")
        if tedad_card_harif == 3:
            print("  1    2    3 ")
            print(" [?]  [?]  [?]")
        if tedad_card_harif == 2:
            print("  1    2 ")
            print(" [?]  [?]")
        print("\n\n")
        if tedad_card == 5:
            print(f" [{list_of_cart[0]}]  [{list_of_cart[1]}]  [{list_of_cart[2]}]  [{list_of_cart[3]}]  [{list_of_cart[4]}] ")
        if tedad_card == 4:
            print(f" [{list_of_cart[0]}]  [{list_of_cart[1]}]  [{list_of_cart[2]}]  [{list_of_cart[3]}]")
        if tedad_card == 3:
            print(f" [{list_of_cart[0]}]  [{list_of_cart[1]}]  [{list_of_cart[2]}]")
        if tedad_card == 2:
            print(f" [{list_of_cart[0]}]  [{list_of_cart[1]}]")
        print(" ")
        print("[1]Delete cart  [5]Shuffle")
        print("[2]Chenge Card  [6]Restart")
        print(f"[3] 11 !!!      [7]seek({seek})")
        print("[4]Refresh      [8] 21 !!!")
        har = int(input(">> "))
        if har == 1 and turn:
            sel = int(input("choose card number: "))
            list_of_cart.pop(sel-1)
            tedad_card -= 1
            turn = False
            con.send("1  ".encode())
        elif har == 2 and turn:
            sel = int(input("choose card number: "))
            sel_h = int(input("choose card number harif: "))
            con.send(f"2{list_of_cart[sel-1]}{sel_h-1}".encode())
            data = con.recv(1024).decode()
            list_of_cart[sel-1]=int(data)
            turn = False
        elif har == 3 and turn:
            if sum(list_of_cart) == 11:
                con.send("3  ".encode())
                win = True
                turn = False
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
                print("------You Win!!!-----")
                time.sleep(0.2)
            else:
                print("hanoz magmoee cart haye shoma 11 nashode ast")
                time.sleep(1)
        elif har == 5 and turn:
            random.shuffle(list_of_cart)
            con.send("5  ".encode())
            turn = False
        elif har == 6 and turn:
            con.send("6  ".encode())
            print("waiting for sending request ...")
            answer = con.recv(1024).decode()
            if answer == "y":
                list_of_cart = []
                for a in range(5):
                    list_of_cart.append(random.randint(1,9))
                tedad_card = 5
                tedad_card_harif = 5
                print("---------Reset---------")
                time.sleep(2)
                turn = False
            else:
                print("----reset cancel shod----")
                time.sleep(2)
        elif har == 7 and turn and seek > 0:
            seek -= 1
            s_n = int(input("Choose card number : "))
            con.send(f"7{s_n-1} ".encode())
            print("please waiting for seeking ...")
            j_s = con.recv(1024).decode()
            print("Succsesful")
            print(f"the card {s_n} is : [{j_s}]")
            time.sleep(3)
            turn = False
        elif har == 8 and turn:
            if sum(list_of_cart) == 21:
                seek += 1
                for i in list_of_cart:
                    list_of_cart.pop(0)
                    list_of_cart.append(random.randint(1,9))
                con.send("8  ".encode())
                turn = False
                print("------seek + 1------")
                time.sleep(2)
        elif turn == False:
            data = con.recv(1024).decode()
            if data[0] == "1":
                tedad_card_harif -= 1
                turn = True
                print("------Delete card!!!-----")
                time.sleep(2)
            if data[0] == "2":
                sele = list_of_cart[int(data[2])]
                list_of_cart[int(data[2])] = int(data[1])
                con.send(f"{sele}".encode())
                turn = True
                print("------Change Card!!!-----")
                time.sleep(2)
            if data[0] == "3":
                lose = True
                turn = False
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
                print("------You Lose!!!-----")
                time.sleep(0.2)
            if data[0] == "5":
                turn = True
                print("------Shuffle!!!-----")
                time.sleep(2)
            if data[0] == "6":
                an = input("are you ok for reset (y,n): ")
                if an == "y":
                    turn = True
                    con.send("y".encode())
                    list_of_cart = []
                    for a in range(5):
                        list_of_cart.append(random.randint(1,9))
                    tedad_card_harif = 5
                    tedad_card = 5
                    print("---------Reset---------")
                    time.sleep(2)
                else:
                    con.send("n".encode())
                    print("----reset cancel shod----")
                    time.sleep(2)
            if data[0] == "7":
                ss = int(data[1])
                con.send(f"{list_of_cart[ss]}".encode())
                print("-------Seeking-------")
                time.sleep(3)
                turn = True
            if data[0] == "8":
                turn = True
                print("------ 21 !!! ------")
                time.sleep(2)
    time.sleep(0.1)
    os.system("cls")
