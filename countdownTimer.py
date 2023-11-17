import time

def startCountDown(t):
    while t > 0:
        min, sec = divmod(t, 60)
        time_print = "{:02d} : {:02d}".format(min, sec)
        print(time_print)
        time.sleep(1)
        t -= 1

sec = int(input("Enter the seconds needed in timer: "))
startCountDown(sec)