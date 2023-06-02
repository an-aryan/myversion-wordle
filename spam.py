import pyautogui, time, datetime
  
time.sleep(2)
flag = True
count = 0
while flag == True:
    
    # to display the time at which the message is sent 
    pyautogui.typewrite("spam") 
    pyautogui.press("enter")
    time.sleep(1)
    if count == 25:
        flag = False
    count = count + 1
