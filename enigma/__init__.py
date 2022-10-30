__version__ = '0.1.0'
from typing import Optional, Dict, List
from pydantic import BaseModel
from enigma.constants import ALPHABET, LETTER_IDXS
from enigma.utils import load_config_from_file


class RotorConfig(BaseModel):
    name: str
    map: str
    pos: int
    notch: int


class Rotor():
    def __init__(self, config):
        self.name = config.name
        self._map = config.map
        self._map_len = len(self._map)
        self._pos = config.pos
        self._notch = config.notch
        self._char_idxs = {l: i for i, l in enumerate(self._map)}
    
    @property
    def position(self):
        return self._pos

    @property
    def notch(self):
        return self._notch

    def rotate_pos(self):
        self._pos += 1
        if self._pos % self._map_len == 0:
            self._pos = 0

    def step_forward(self, char):
        new_char_idx = (LETTER_IDXS[char] + self._pos) % self._map_len
        return self._map[new_char_idx]

    def step_backward(self, char):
        char_idx = self._char_idxs[char] - self._pos
        if char_idx < 0:
            alphabet_char_idx = self._map_len + char_idx
        elif char_idx > 0:
            alphabet_char_idx = char_idx % self._map_len
        else: 
            alphabet_char_idx = 0
        return ALPHABET[alphabet_char_idx]


class EnigmaConfig(BaseModel):
    plug_board: Optional[Dict] = None
    reflector_setting: str
    rotors_setting: List[RotorConfig]


class Enigma:
    def __init__(self, config):
        self._config = config
        self._alphabet = ALPHABET
        self._alphabet_len = len(self._alphabet)
        self._plug_board = config.plug_board
        self._plug_board.update({v: k for k, v in self._plug_board.items()})
        self._reflector = self._build_reflector(config.reflector_setting)
        self.set_rotor_config()

    @property
    def position_list(self):
        return self._rotor_pos_list

    @classmethod
    def from_config(cls, config):
        assert type(config) in {str, dict, EnigmaConfig}, f"Inappropriate config type {type(config)}"
        
        if isinstance(config, str):
            config = load_config_from_file(config)
        if isinstance(config, dict):
            config = EnigmaConfig(**config)
        return cls(config)

    def set_rotor_config(self):
        self._rotor_panel = [Rotor(cfg) for cfg in self._config.rotors_setting]
        self._rotor_pos_list = [rotor.position for rotor in self._rotor_panel]

    def _build_reflector(self, char_str):
        char_tuple = tuple(char_str.lower())
        return {k: v for k, v in zip(self._alphabet, char_tuple)}

    def _rotate_panel(self):
        rotate_next = False
        for idx, rot in enumerate(self._rotor_panel): 
            if idx == 0 or rotate_next:
                rot.rotate_pos()
                self._rotor_pos_list[idx] = rot.position
                notch_condition = (self._rotor_pos_list[idx] == (rot.notch + 1) % self._alphabet_len)
                rotate_next = True if notch_condition else False
    
    def process_message(self, msg):
        encrypted_msg  = []
        msg = list(msg.lower())

        for l in msg:
            letter = self._plug_board.get(l) or l
            self._rotate_panel()
            
            for rotor in self._rotor_panel:
                letter = rotor.step_forward(letter)
            letter = self._reflector[letter]
            for rotor in reversed(self._rotor_panel):
                letter = rotor.step_backward(letter)
            
            letter = self._plug_board.get(letter) or letter
            encrypted_msg.append(letter)
        return ''.join(encrypted_msg)
