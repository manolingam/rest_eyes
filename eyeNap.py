import os
import schedule
import time
import sys

def execute_command():
    os.system(r'start /min "" %windir%\System32\rundll32.exe powrprof.dll,SetSuspendState Standby')

if len(sys.argv) > 1:             
    schedule.every(int(sys.argv[1])).minutes.do(execute_command)
                
while True:
    schedule.run_pending()
    time.sleep(1)

