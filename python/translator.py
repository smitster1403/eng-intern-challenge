import sys
import re

capital_follows = ".....0"
decimal_follows = ".0...0"
num_follows = ".0.000"
special = {
" " : "......",
"." : "..00.0",
"," : "..0...",
"?" : "..0.00",
"!" : "..000.",
":" : "..00..",
";" : "..0.0.",
"-" : "....00",
"/" : ".0..0.",
"<" : ".00..0",
">" : "0..00.",
"(" : "0.0..0",
")" : ".0.00."
}
braille_int = {
    1:"0.....",
    2:"0.0...",
    3:"00....",
    4:"00.0..",
    5:"0..0..",
    6:"000...",
    7:"0000..",
    8:"0.00..",
    9:".00...",
    0:".000.."
                }
braille_char = {
    'A':"0.....",
    'B':"0.0...",
    'C':"00....",
    'D':"00.0..",
    'E':"0..0..",
    'F':"000...",
    'G':"0000..",
    'H':"0.00..",
    'I':".00...",
    'J':".000..",
    'K':"0...0.",
    'L':"0.0.0.",
    'M':"00..0.",
    'N':"00.00.",
    'O':"0..00.",
    'P':"000.0.",
    'Q':"00000.",
    'R':"0.000.",
    'S':".00.0.",
    'T':".0000.",
    'U':"0...00",
    'V':"0.0.00",
    'W':".000.0",
    'X':"00..00",
    'Y':"00.000",
    'Z':"0..000"
                }

retVal = []

# FUNCTION TO GET STRING FROM BRAILLE
def string_to_braille(str_val:str):
    print(f"String to braile: {str_val}")
    vals = list(str_val)
    print(f"The string content: {vals}")
    

# FUNCTION TO GET BRAILLE FROM STRING
def braille_to_string(str_val:str):
    print(f"Braile to string: {str_val}")
    vals = [str_val[i:i+6] for i in range(0,len(str_val), 6)]
    print(f"The braille content: {vals}")
    

args = sys.argv[1:]
if len(args) == 0:
    print(special[" "])
    exit()

str_val = " ".join(args)
print(str_val)

try:
    check_letters_int = any(char in braille_char.keys() for char in str_val) or any(char.capitalize() in braille_char.keys() for char in str_val) or any(int(char) in braille_int.keys() for char in str_val) 
except:
    check_letters_int = False
        
print(check_letters_int)

if check_letters_int:
    string_to_braille(str_val)
else:
    braille_to_string(str_val)
    
    
    
