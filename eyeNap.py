import os
import schedule
import time
import sys

# Lock worksystem: Rundll32.exe User32.dll,LockWorkStation
# Shutdown: Shutdown.exe -s -t 00
# Sleep: rundll32.exe powrprof.dll,SetSuspendState 0,1,0
# Hibernate: rundll32.exe PowrProf.dll,SetSuspendState
# Restart: Shutdown.exe -r -t 00
# Turn off hiberante & standby: powercfg -hibernate off && start /min "" %windir%\System32\rundll32.exe powrprof.dll,SetSuspendState Standby

def execute_command():
    os.system(r'start /min "" %windir%\System32\rundll32.exe powrprof.dll,SetSuspendState Standby')

if len(sys.argv) > 1:             
    schedule.every(int(sys.argv[1])).minutes.do(execute_command)
                
while True:
    schedule.run_pending()
    time.sleep(1)

