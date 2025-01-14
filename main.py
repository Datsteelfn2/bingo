import random

my2d_list=[[random.randint(0,90),random.randint(0,90),random.randint(0,90)],
           [random.randint(0,90),'Bingo',random.randint(0,90)],
           [random.randint(0,90),random.randint(0,90),random.randint(0,90)]]
def card():
    for row in my2d_list:
        for item in row:
            print(f"{item:^5}", end=' | ')
        print()
card()
while True:
    guess=int(input("Guess a number:> "))
    for row in range(len(my2d_list)):
        for item in range(len(my2d_list[row])):
            if my2d_list[row][item]==guess:
                my2d_list[row][item]="X"
                card()
    exit=input("Would you like to exit the program:> ")
    if exit.strip().lower()[0]=="y":
        break
    
print("Youve exited the program")