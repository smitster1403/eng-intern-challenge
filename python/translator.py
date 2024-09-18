import sys
import re
from collections import Counter

capital_follows = ".....O"
decimal_follows = ".O...O"
num_follows = ".O.OOO"
special = {
" " : "......",
"." : "..OO.O",
"," : "..O...",
"?" : "..O.OO",
"!" : "..OOO.",
":" : "..OO..",
";" : "..O.O.",
"-" : "....OO",
"/" : ".O..O.",
"<" : ".OO..O",
">" : "O..OO.",
"(" : "O.O..O",
")" : ".O.OO."
}
braille_int = {
    "1":"O.....",
    "2":"O.O...",
    "3":"OO....",
    "4":"OO.O..",
    "5":"O..O..",
    "6":"OOO...",
    "7":"OOOO..",
    "8":"O.OO..",
    "9":".OO...",
    "0":".OOO.."
                }
braille_char = {
    'A':"O.....",
    'B':"O.O...",
    'C':"OO....",
    'D':"OO.O..",
    'E':"O..O..",
    'F':"OOO...",
    'G':"OOOO..",
    'H':"O.OO..",
    'I':".OO...",
    'J':".OOO..",
    'K':"O...O.",
    'L':"O.O.O.",
    'M':"OO..O.",
    'N':"OO.OO.",
    'O':"O..OO.",
    'P':"OOO.O.",
    'Q':"OOOOO.",
    'R':"O.OOO.",
    'S':".OO.O.",
    'T':".OOOO.",
    'U':"O...OO",
    'V':"O.O.OO",
    'W':".OOO.O",
    'X':"OO..OO",
    'Y':"OO.OOO",
    'Z':"O..OOO"
                }

retVal = []

# FUNCTION TO GET STRING FROM BRAILLE
def string_to_braille(str_val:str):
    addNum = False
    addCapital = False
    converted = []
    # print(f"String to braile: {str_val}")
    for i in range(len(str_val)):
        if not str_val[i] in braille_char.keys():
            try:
                if str_val[i].capitalize() in braille_char.keys():
                    converted.append(braille_char[str_val[i].capitalize()])
            except:
                pass
        if str_val[i] in braille_char.keys():
            converted.append(capital_follows)
            converted.append(braille_char[str_val[i].capitalize()])
        if str_val[i] in braille_int.keys() and addNum == False:
            converted.append(num_follows)
            converted.append(braille_int[str_val[i]])
            addNum = True
        elif str_val[i] in braille_int.keys() and addNum == True:
            # converted.append(num_follows)
            converted.append(braille_int[str_val[i]])
        if str_val[i] in special.keys():
            if str_val[i] == ".":
                converted.append(decimal_follows)
                converted.append(special["."])
            else: converted.append(special[str_val[i]])
        # print(converted)
    retVal = "".join(converted)
    print(retVal)
            

# FUNCTION TO GET BRAILLE FROM STRING
# done
def get_key(d, target):
    return [k for k,v in d.items() if v == target]

def braille_to_string(str_val:str):
    print(f"Braile to string: {str_val}")
    vals = [str_val[i:i+6] for i in range(0,len(str_val), 6)]
    print(f"The braille content: {vals}") 
    converted = []
    currentNum = False
    outputVal = " "
    for i in range(len(vals)-1):
        if vals[0] == capital_follows:
            currentNum = False
            i += 1
            key = get_key(braille_char, vals[i])
            print(key) 
            converted += (key)
            continue
        elif vals[i] == num_follows:
            currentNum = True
            key = get_key(braille_int,vals[i])
            print(key) 
            converted += (key)
        elif vals[i] == decimal_follows:
            converted += (".")
        if vals[i] in braille_char.values() and currentNum == False:
            key = get_key(braille_char, vals[i])
            print(key) 
            converted += (key.lower())
        elif vals[i] in braille_int.values() and currentNum == True:
            key = get_key(braille_int, vals[i])
            print(key) 
            converted += (key)
        if vals[i] in special.values():
            key = get_key(special, vals[i])
            print(key)
            converted += (key)
            
    outputVal = outputVal.join(converted)
    print(outputVal)
            
            
            
            
            
            
            
        
    
args = sys.argv[1:]
if len(args) == 0:
    print(special[" "])
    exit()

str_val = " ".join(args)
# print(str_val)
valCount = Counter(str_val)
# print(valCount)
# any(char.capitalize() in braille_char.keys() or char in braille_int.keys() for char in str_val)
if all(c in {"O", "."} for c in str_val):
    check_letters_int = False
else:
    check_letters_int = True
        
# print(check_letters_int)

if check_letters_int:
    string_to_braille(str_val)
else:
    braille_to_string(str_val)
    
    
    
