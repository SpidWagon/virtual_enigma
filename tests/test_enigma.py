import yaml

from enigma import Enigma
from enigma.constants import CONFIG_FILE_PATH

def test_word():
    text = "wetterbericht"
    
    encryptor = Enigma.from_config(CONFIG_FILE_PATH)

    text_enc = encryptor.process_message(text)
    encryptor.set_rotor_config()
    assert encryptor.process_message(text_enc) == text

def test_sentence():
    text_sentence = "sechs uhr wetterbericht klares wetter am morgen bewolktes wetter am abend"
    text_list = text_sentence.split()
    
    encryptor = Enigma.from_config(CONFIG_FILE_PATH) 

    encrypted_list = [encryptor.process_message(w) for w in text_list]
    encryptor.set_rotor_config()
    decrypted_list = [encryptor.process_message(w) for w in encrypted_list]

    assert text_list == decrypted_list

def test_many_key_press():
    text = "wetterbericht"
    
    encryptor = Enigma.from_config(CONFIG_FILE_PATH) 

    iter_num = 100
    text_enc = encryptor.process_message(text)
    for _ in range(iter_num):
        text_enc = encryptor.process_message(text_enc)
    
    assert True

