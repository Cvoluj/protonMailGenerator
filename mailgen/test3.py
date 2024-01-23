import time
import pyautogui
from PIL import Image
import pyautogui
import sys
import time
import random
import string
import webbrowser
import ctypes
import re


CF_TEXT = 1

kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p

codeAvailable =  False
def get_code(codeAvailable):
    user32.OpenClipboard(0)
    while codeAvailable != True:

        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('shiftright')
        pyautogui.press('j')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('ctrlleft')
        pyautogui.typewrite(
            "var verificationCode = document.querySelector('.messages-list pre')?.innerText.match(/\\b\d{6}\\b/)?.[0];"
            "var tempTextarea = document.createElement('textarea');"
            "tempTextarea.value = verificationCode;document.body.appendChild(tempTextarea);"
            "tempTextarea.select();document.execCommand('copy');document.body.removeChild(tempTextarea);"
        )
        time.sleep(5)
        pyautogui.typewrite('\n')
        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('shiftright')
        pyautogui.press('j')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('ctrlleft')
        
        time.sleep(1)
        try:
            if user32.IsClipboardFormatAvailable(CF_TEXT):
                data = user32.GetClipboardData(CF_TEXT)
                data_locked = kernel32.GlobalLock(data)
                text = ctypes.c_char_p(data_locked)
                value = text.value
                value = value.decode('utf-8')
                kernel32.GlobalUnlock(data_locked)
                if re.match(r'\d{6}', value):
                    codeAvailable = True
        finally:
            user32.CloseClipboard()


time.sleep(3)
get_code(codeAvailable=codeAvailable)
