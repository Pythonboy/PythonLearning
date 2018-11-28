import random
import ctypes
import time
import os

path = "D:\\Image\\";
while True:
	file = os.listdir(path);
	filepath = path + random.choice(file);
	ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)
	time.sleep(60*60);