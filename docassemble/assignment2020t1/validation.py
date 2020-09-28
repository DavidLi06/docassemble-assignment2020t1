import re
from docassemble.base.util import *

def check_nric(nric):
#test for correct NRIC format

    if not re.match("^[STFG]\d{7}[A-Z]$", nric):
       validation_error("Incorrect NRIC format.")

#test for valid NRIC
    weights = "2765432"

    total_sum = 0
    counter = 0
    for matcher in nric[1:8]:
        matcher_int = int(matcher)
        weights_int = int(weights[counter])
        total_sum += matcher_int * weights_int
        counter += 1

    last_number = total_sum % 11

    alphabets = "JZIHGFEDCBA"
    last_alpha = alphabets[last_number]

    if nric[8] != last_alpha:
        validation_error("Please enter a valid NRIC.")
        
    else:
       return True
