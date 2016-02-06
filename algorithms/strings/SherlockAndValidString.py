#!/bin/python3

import sys

str = input().strip();
alphabet = {};
for c in str:
    if c in alphabet:
        alphabet[c] = alphabet[c] + 1
    else:
        alphabet[c] = 1;

freq = {}
max = 0;
for key, value in alphabet.items():
    if value in freq:
        freq[value] = freq[value] + 1
    else:
        freq[value] = 1;
    if freq[value] > max:
        max = value;
oneOff = False;
no = False;
for key, value in freq.items():
    if key != max:
        if value > 1:
            no = True
            break;
        elif oneOff:
            no = True
            break;
        else:
            oneOff = True
if no:
    print("NO")
else:
    print("YES")
