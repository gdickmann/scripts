import os
import datetime

import subprocess
import shlex

def main():
    print('Follow the format: 03:00, 20:30, 12:00, 00:00')
    shutdown = input('Shutdown at: ')

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if shutdown == now:
            os.system("shutdown /s /t 1")


if __name__ == '__main__':
    main()
