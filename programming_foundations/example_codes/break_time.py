import webbrowser
import time

breaks = 3
break_count = 0

print("This program started on "+ time.ctime())

while breaks < breaks:
    
    time.sleep(10)
    webbrowser.open("http://www.google.com")
    break_count += 1
