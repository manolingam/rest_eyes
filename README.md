# rest_eyes
A python program to automate standby mode in time intervals for windows users to break the continued system work.

# Usage
* Clone this repository to your machine.
* Run Command Prompt as Administrator and enter `powercfg -hibernate off` to turn off hiberante mode as your PC may enter into hibernation instead of standby.
* Navigate to the repository directory using `cd rest_eyes`.
* Enter `python restEyes.py -h` for help.
* Enter `python restEyes.py -i 20` to put your system in standby mode for every 20 minutes. You can either enter 20 or 40 as interval.
* You can then close your terminal window. If everything was successful, you should see a program named eyeNap.exe under running process in your Task Manager Window.

# How to stop this program
Open Task Manager and select eyeNap.exe and press delete.

## LICENSE
MIT @ [Manolingam](./LICENSE)

### CONTRIBUTORS
* [Manolingam](https://github.com/manolingam)


