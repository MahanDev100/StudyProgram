import os

path = "C:\\Users\\Administrator\\Desktop\\System\\study_program.txt"

subjects_dict = {"1": "Math", "2": "Science", "3": "Geography"}
hours_dict = {"1": "1h", "2": "2h", "3": "3h", "4": "4h"}

while True:
    menu = input("1.Add new subject\n2.Show today program\n3.Exit\n")
    
    if menu == '1':
        sub_name = input("Enter your new subject : \n1.Math\n2.Science\n3.Geography\n")
        if sub_name in subjects_dict:
            sub_time = input("Enter your new subject study time :\n1.1h\n2.2h\n3.3h\n4.4h\n")
            if sub_time in hours_dict:
                day = input("Today is (day of week) : ")
                with open(path, "a", encoding="utf-8") as file:
                    file.write(f"{day}: {subjects_dict[sub_name]},{hours_dict[sub_time]}\n")
                print("Your subject has been added :)")
            else:
                print("Invalid time!")
        else:
            print("Invalid subject!")
    
    elif menu == '2':
        with open(path, "r", encoding="utf-8") as Read:
            content = Read.read()
            print(content)
    
    elif menu == '3':
        break