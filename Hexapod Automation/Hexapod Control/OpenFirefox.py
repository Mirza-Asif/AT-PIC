import pyautogui
import time
import os

# Path to Firefox executable
firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

# Launch Firefox
os.startfile(firefox_path)
time.sleep(10)  # Wait for Firefox to open

# Type the IP address
pyautogui.typewrite("192.168.0.254")
pyautogui.press("enter")  # Press Enter key to navigate to the IP address

time.sleep(20)
pyautogui.press("tab")
pyautogui.typewrite("Administrator")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("right")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)
