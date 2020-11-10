from time import sleep


def simpleCountdown(seconds, message="Waiting..."):
    while seconds > 0:
        print(f"\n [{seconds}] {message}", end='\r')
        seconds -= 1
        sleep(1)
