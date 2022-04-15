import sys,time,random
from Functions import menu

typing_speed = 50 #wpm
def slow_type_input(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2.0/typing_speed)
    input("")

def slow_type_menu(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2.0/typing_speed)
        menu()



import sys,time,random

typing_speed = 50 #wpm
def slow_type_title(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.1/typing_speed)
    print ("")

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2.0/typing_speed)
    print("")