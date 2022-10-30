from enigma import Enigma
from enigma.constants import CONFIG_FILE_PATH


RESET_CMD = "/rr"
EXIT_CMD = "/exit"
# ToDo
# implements commands:
# SHOW_CMD = "/show" 
# HELP_CMD = "/help" 


def main():
    encryptor = Enigma.from_config(CONFIG_FILE_PATH)

    while True:
        text = input("Type message to process\n")
        if text.lower() == EXIT_CMD:
            print("exit")
            exit()
        elif text.lower() == RESET_CMD:
            encryptor.set_rotor_config()
            print("Config reset \n")
        else:
            text_enc = encryptor.process_message(text)
            print(f'\nProccesed message:\n{text_enc}\n')


if __name__ == "__main__":
    main()
