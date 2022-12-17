
import typer
from enigma import Enigma
from enigma.constants import CONFIG_FILE_PATH


app = typer.Typer()

@app.command()
def process(text: str):
    encryptor = Enigma.from_config(CONFIG_FILE_PATH)
    text_enc = encryptor.process_message(text)
    print(f"\nProccesed message:\n{text_enc}\n")

@app.command()
def show_cfg():
    encryptor = Enigma.from_config(CONFIG_FILE_PATH)
    encryptor.show_config()

@app.command()
def help():
    print(
        "This is a placeholder of help command, but I swear here will be normal help command soon"
    )

def main():
    app()

if __name__ == "__main__":
    main()
