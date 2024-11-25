#!/usr/bin/python3 -u

'''
INFO:
- the meds [key] are orignally randomly generated
- you can run as many notes [inputs] -> responses [ouput]
- you give Joe his meds to change the key
- If get Joe to read "Come on man." as "Donald Trump", you have the flag.
'''

import random

def raw(x):
  return bytes(map(lambda y:y if isinstance(y,int) else ord(y),x))

INTRO = '''
You have access to Joe Biden's medications. You have been tasked by the KGB so that in his upcoming speech he replaces "Come on man." with "Donald Trump".
Change his medications so that he will slip up.
'''

OPTIONS = '''
1.) Change Joe's meds
2.) Give Joe a note to read
'''

# Globals
FLAG = raw(open("./flag.txt").read())
DONALDTRUMP = "Donald Trump"
COMEONMAN = "Come on man."

#generate key
MEDS = []
def generate_key():
    for i in range(0,12):
        MEDS.append(random.randint(0,128))
generate_key()

def setKey(input):
    if len(input) != 24:
        print("Your medication was not 12 bytes long. Keeping original.")
        return
    byte_list = [int(input[i:i+2], 16) for i in range(0, len(input), 2)]
    global MEDS
    MEDS = byte_list

#encryption method
def encrypt(input_str):
    input_chars = list(input_str)
    key_values = MEDS
    output_chars = []
    
    for i in range(len(input_chars)):
        output_char = chr(ord(input_chars[i]) ^ key_values[i % len(key_values)])
        output_chars.append(output_char)
    return ''.join(output_chars)
    

def joeSpeaks(msg):
    response = encrypt(msg)
    print(f'Input: "{msg}" -> Medicated Output: "{response}"')
    if (msg == COMEONMAN) & (response == DONALDTRUMP):
        print("Flag: "+str(FLAG))
        return True

def choose():
  return input("> ")

print(INTRO)
while (True):
    print(OPTIONS)
    choice = choose()
    if choice == "1":
        print("What meds do you want to give Joe? (12 bytes in hex)")
        meds = choose()
        setKey(meds)

    elif choice == "2":
        print("What should the message say?")
        note = choose()
        # do sanity checks
        if joeSpeaks(note):
            break

    else:
        print("That's not one of the options. Are you more confused than Joe?")
