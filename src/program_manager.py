import subprocess
from constants import PROGRAM_PATHS, PROGRAM_CODES, PROGRAM_NAMES
import psutil
import os, signal

def get_process_pid(program_code):
    program_name = PROGRAM_NAMES[program_code]
    print(program_name)

    pid = []

    for proc in psutil.process_iter():
        try:
            if program_name.lower() in proc.name().lower():
                pid.append(proc.pid)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return pid


def stop_program(program_code):
    program_pid_list = get_process_pid(program_code)
    print("Killing program with pid: " + str(program_pid_list))

    for pid in program_pid_list: 
        os.kill(pid, signal.SIGKILL)

def run_program(program_code):
    program_path = PROGRAM_PATHS[program_code]
    print(program_path)
    proc = subprocess.Popen(program_path)
    print("Started program with pid: " + str(proc.pid))

def get_program_code(entity):
    program_code = PROGRAM_CODES[entity]
    return program_code


def run_action(info):
    intent = info['intent']
    program_code = get_program_code(info['entity'])

    if intent == 'run_program':
        run_program(program_code)

    elif intent =='close_program':
        stop_program(program_code)
    
    else:
        return -1