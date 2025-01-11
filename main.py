import random

my2d_list=[[random.randint(0,90),random.randint(0,90),random.randint(0,90)],
           [random.randint(0,90),'Bingo',random.randint(0,90)],
           [random.randint(0,90),random.randint(0,90),random.randint(0,90)]]

def rows():
    for row in my2d_list:
        print(row)
rows()