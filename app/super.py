import psutil
import subprocess
import os
import time
import schedule
import daemon
import args
import sys

process_name = args.process_name
max_restarts = args.max_restarts
restart_interval = args.restart_interval
command = args.command
check_interval =args.check_interval

CUNT = 0 
timer = 0

daemon.logger.info("######## arguments ######## \n \
    \trestart_interval = %s, \n \
    \tmax_restarts = %s , \n \
    \tprocess_name = %s , \n \
    \tcheck_interval = %s , \n \
    \tcommand = %s \n ",
    restart_interval, max_restarts, process_name, check_interval, command )

def checkIfProcessRunning(processName):
    '''
    Checking processes
    '''
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def startpc():
    global CUNT
    if checkIfProcessRunning(process_name) is False:
        daemon.logger.info("starting %s",process_name)
        os.system(command)
        CUNT = CUNT + 1    
        if CUNT >= int(max_restarts):
            daemon.logger.error("max number of restarts reached")
            exit()
        time.sleep(int(restart_interval))
    else:
        daemon.logger.debug("is running with pid: %s", process_name)
        CUNT = 0

schedule.every(int(restart_interval)).seconds.do(startpc)

while 1:
    schedule.run_pending()
    time.sleep(1)
