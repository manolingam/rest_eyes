from optparse import OptionParser
import os

parser = OptionParser()

def get_arguments():
    parser = OptionParser(conflict_handler="resolve")
    parser.add_option('-i', '--interval', dest = 'interval', help = 'Time interval in 20 or 40 minutes')
    return parser.parse_args()

def input_validation(param, msg):  
    duration_list = [20,40]
    restart = True  
    while restart:
        if param in duration_list:
            print(msg)
            restart = False
            os.system('start eyeNap.exe ' + str(param))
            break
        else:
            print('[!] Enter valid minute interval between 20, 40.') 
            restart = False
            break

try:
    (options, args) = get_arguments()
    interval_time =  int(options.interval)
    message = '[+] Your system will be put in standby mode for every ' + str(interval_time) + ' minutes to rest your eyes.\n[+] You can now close this terminal window.' + '\n[+] If you want to stop this program, open Task Manager, choose eyeNap.exe and press delete.'
    if interval_time:
        print('[!] Run cmd as administrator and enter powercfg -hibernate off before running this program as your system might hibernate instead to standby! Ignore if already done.')
        input_validation(interval_time, message)
except:
    print('[!] Missing option values.')

