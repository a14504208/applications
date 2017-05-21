#! python3
from pyperclip import copy, paste
import time

recent_str = ''
while True:
    temp = paste()
    if recent_str != temp:
        recent_str = temp
        if '.' in recent_str:
            recent_str = recent_str[recent_str.find('.') + 1:]
            copy(recent_str)
    time.sleep(0.1)
        

