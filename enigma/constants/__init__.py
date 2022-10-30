import os
from string import ascii_lowercase


ALPHABET = tuple(ascii_lowercase) + (' ', '.', ',', ':')
LETTER_IDXS = {l: idx for idx, l in enumerate(ALPHABET)}

CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "configs", "general_config.yml")