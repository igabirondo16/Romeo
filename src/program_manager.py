import subprocess
from constants import GOOGLE_URL, WIKIPEDIA_URL, PROGRAM_PATHS, PROGRAM_CODES, PROGRAM_NAMES
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

def google_search(args):
    program_path = PROGRAM_PATHS[0]
    url = GOOGLE_URL + args
    args_list = [program_path, url]
    proc = subprocess.Popen(args_list)

def wikipedia_search(args):
    program_path = PROGRAM_PATHS[0]
    url = WIKIPEDIA_URL + args
    args_list = [program_path, url]
    proc = subprocess.Popen(args_list)

def get_program_code(entities):
    if not 'program' in entities.keys():
        return ''

    program_code = PROGRAM_CODES[entities['program']]
    return program_code

def get_query(entities):
    if not 'query' in entities.keys():
        return ''
        
    query = entities['query']
    return query

def run_action(info):
    intent = info['intent']

    if intent == 'run_program':
        program_code = get_program_code(info['entities'])
        run_program(program_code)

    elif intent =='close_program':
        program_code = get_program_code(info['entities'])
        stop_program(program_code)

    elif intent == 'run_browser_with_args':
        query = get_query(info['entities'])
        google_search(query)

    elif intent == 'wikipedia_search':
        query = get_query(info['entities'])
        wikipedia_search(query)
    
    else:
        return -1