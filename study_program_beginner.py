import os
path = "C:\\Users\\Administrator\\Desktop\\System\\study_program.txt"
while True :
    menu = input("1.Add new subject\n2.Show today program\n3.Exit")
    if menu == '1' :
        while True :
            sub_name = input("Enter your new subject : \n1.Math\n2.Science\n3.Geography\n")
            if sub_name == "1" :
                sub_time = input("Enter your new subject study time :\n1.1h\n2.2h\n3.3h\n4.4h\n")
                if sub_time == "1" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Math:
                        Math.write(day + ": Math,1h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "2" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Math:
                        Math.write(day + ": Math,2h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "3" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Math:
                        Math.write(day + ": Math,3h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "4" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Math:
                        Math.write(day + ": Math,4h\n")
                        print("Your subject has been added :) ")
                        break
            if sub_name == "2" :
                sub_time = input("Enter your new subject study time :\n1.1h\n2.2h\n3.3h\n4.4h\n")
                if sub_time == "1" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Science:
                        Science.write(day + ": Science,1h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "2" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Science:
                        Science.write(day + ": Science,2h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "3" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Science:
                        Science.write(day + ": Science,3h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "4" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Science:
                        Science.write(day + ": Science,4h\n")
                        print("Your subject has been added :) ")
                        break
            if sub_name == "3" :
                sub_time = input("Enter your new subject study time :\n1.1h\n2.2h\n3.3h\n4.4h\n")
                if sub_time == "1" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Geography:
                        Geography.write(day + ": Geography,1h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "2" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Geography:
                        Geography.write(day + ": Geography,2h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "3" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Geography:
                        Geography.write(day + ": Geography,3h\n")
                        print("Your subject has been added :) ")
                        break
                elif sub_time == "4" :
                    day = input("Today is (day of week) : ")
                    with open(path , "a") as Geography:
                        Geography.write(day + ": Geography,4h\n")
                        print("Your subject has been added :) ")
                        break
    elif menu == '2' :
        with open(path, "r") as Read:
            content = Read.read()
            print(content)
            break
    elif menu == '3' :
        break