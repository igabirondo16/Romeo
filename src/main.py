from wit import Wit
from utils import get_last_message_info
from constants import ACCESS_TOKEN
from program_manager import run_action

client = Wit(ACCESS_TOKEN)

def print_menu():
    print("Choose type of message input:")
    print("0) Text message")
    print("1) Voice message")
    option = int(input("=============\n"))
    return option

def get_text_message():
    msg = str(input("Enter text command:"))
    resp = client.message(msg)
    return resp


def main():
    option = print_menu()

    if option == 0:
        resp = get_text_message()

    else:
        return -1

    info = get_last_message_info(resp)
    print(info)
    run_action(info)
    

if __name__ == "__main__":
    main()