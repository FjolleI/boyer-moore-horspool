import sys
import string

class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def printprocess(shift):
    print(text)
    for i in range(0, shift):
        print(" ", end = "")
    print(pattern)

def preprocess(pattern):
    occ = dict.fromkeys(string.ascii_lowercase, -1)
   
    for i in range(0,len(pattern)-1):
        occ[pattern[i]] = i

    return occ

def search(text,pattern,occ):
    found = 0
    i = 0
    m = len(pattern)
    n = len(text)

    while i <= n - m:
        printprocess(i)
        
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j = j - 1

        if j < 0:
            found = found + 1
            print(f"{color.GREEN}Found!{color.ENDC}")

        i = i + m-1
        i = i - occ[text[i]]

    return found

text=""
pattern=""

while len(text) <= 0:
    text = input("Text: ")

while len(pattern) <= 0:
    pattern = input("Pattern: ")

occ = preprocess(pattern)

found = search(text,pattern,occ)

print(f"{color.RED}Found", found, f"match(es){color.ENDC}")