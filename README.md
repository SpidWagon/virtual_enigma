# Virtual Enigma

## Overview
This project is an implementation of the Enigma cypher machine. Just like as
 the real Enigma, this one can encrypt and decrypt messages. It can also be
 configured in a similar way: you can change settings for plugboard, reflector
 and rotors. As for rotors, you can change their number, their letter mapping,
 start positions and turnover notch positions.

## Installation proccess
To try this project you'll need python and poetry package manager.

After `git clone`  
```
cd <directory to which you cloned the project>
poetry install
poetry shell
cd enigma
```
And you will be able to encrypt and decrypt your messages.

## Usage
To encrypt or decrypt messages you can run the same command `process`.  
Example of encryption and decryption of one phrase:

```
python3 -m run_app process "weather is good today"

Proccesed message:
,xupe kokxhwwzt, wvgr
```
```
python3 -m run_app process ",xupe kokxhwwzt, wvgr"

Proccesed message:
weather is good today
```
If you want to see what's in config of enigma you can use `show-cfg` command
```
python3 -m run_app show-cfg
Rotors config:
Rotor_I 	 position: 2 	 notch: 10 	 map: `. :,jgdqoxuscamifrvtpnewkblzyh`
Rotor_II 	 position: 1 	 notch: 3 	 map: `ntzpsfbokmwrcjdivlaeyuxhgq. :,`
Rotor_III 	 position: 3 	 notch: 25 	 map: `jviubhtcdyakeqzposgxnrmwfl. :,`


Plugboard config:
e <-> m
h <-> l
p <-> z
r <-> j
s <-> v
u <-> q

Reflector config:
abcdefghijklmnopqrstuvwxyz .,:
||||||||||||||||||||||||||||||
ejmzalyxvbwfcrquontspikhgd. :,
```

## Configuration
When you want to change the enigma setting you need to change the
`enigma/general_config.yml` file.  
Note several moments:   

- In reflector and rotors settings the letters are listed as connected to
  alphabet order. For example, if the first letter of a rotor is E, this means
  that the A is mapped to the E.
- Although the plugboard setting in general_config.yml file is just a python
  dictionary, plugboard maps letters in both directions.
- The notch position of the last rotor doesn't matter since it's not used.
- The real version of enigma did not have punctuation marks (as far as I know),
  but I decided to add them.

Example of config file:
```
plug_board: 
  e : m
  h : l
  p : z
  r : j
  s : v
  u : q
reflector_setting: "ejmzalyxvbwfcrquontspikhgd. :,"
rotors_setting:
  - name: Rotor_I
    map: ". :,jgdqoxuscamifrvtpnewkblzyh"
    pos: 2
    notch: 10
  - name: Rotor_II
    map: "ntzpsfbokmwrcjdivlaeyuxhgq. :,"
    pos: 1
    notch: 3
  - name: Rotor_III
    map: "jviubhtcdyakeqzposgxnrmwfl. :,"
    pos: 3
    notch: 25
```

