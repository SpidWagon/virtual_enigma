import yaml

from enigma import Enigma, EnigmaConfig
from enigma.constants import CONFIG_FILE_PATH
from enigma.utils import load_config_from_file


def test_rotor_panel():
    enigma_cfg = load_config_from_file(CONFIG_FILE_PATH)
    enigma_cfg = EnigmaConfig(**enigma_cfg)
    
    rotor_num = len(enigma_cfg.rotors_setting)
    rotor_len = len(enigma_cfg.rotors_setting[0].map)
    
    for r in enigma_cfg.rotors_setting:
        r.pos = 0
        r.notch = rotor_len - 1

    encryptor = Enigma.from_config(enigma_cfg)

    if rotor_num > 1:
        rotation_num = rotor_len**(rotor_num - 1)
        res_list = [0 for i in range(rotor_num)]
        res_list[-1] = 1
    else:
        rotation_num, res_list = rotor_len, [1]
    
    msg = 'a' * rotation_num
    encryptor.process_message(msg)

    assert encryptor.position_list == res_list

def test_custom_notch_rotor_panel():
    res_list = [5,3,2]
    rotor_positions = [1,1,1]
    notch_positions = [4,2,0]
    
    enigma_cfg = load_config_from_file(CONFIG_FILE_PATH)
    enigma_cfg = EnigmaConfig(**enigma_cfg)
    enigma_cfg.rotors_setting = enigma_cfg.rotors_setting[:3]
    for idx, r in enumerate(enigma_cfg.rotors_setting):
        r.pos = rotor_positions[idx]
        r.notch = notch_positions[idx]

    encryptor = Enigma.from_config(enigma_cfg)

    rotor_len = len(enigma_cfg.rotors_setting[0].map)
    rotation_num = res_list[0] - rotor_positions[0] + rotor_len
    msg = 'a' * rotation_num
    encryptor.process_message(msg)

    assert encryptor.position_list == res_list


    
    

