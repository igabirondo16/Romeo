from wit import Wit
from utils import get_last_message_info
from constants import ACCESS_TOKEN
from program_manager import run_action


def main():
    client = Wit(ACCESS_TOKEN)
    resp = client.message('Stop browser')
    print(resp)
    info = get_last_message_info(resp)
    print(info)
    run_action(info)
    

if __name__ == "__main__":
    main()