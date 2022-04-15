import sys,time,random

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*5.0/typing_speed)
    print ("")

slow_type("Hello cruel world. My name is Brandon. I am married to a BEAUTIFUL BUTTERFLY! BABY COME HERE!!!!")

