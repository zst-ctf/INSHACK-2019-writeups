#!/usr/bin/env python
from dashlame import decrypt_stream
import dashlame

with open('wordlist.txt', 'rb') as (fi):
    passwords = fi.read().strip().split('\n')

with open('admin.dla', 'rb') as (dla_fd):
    dla_fd_content = dla_fd.read()

def decrypt_archive_no_delete(passphraseA, passphraseB):
    dec1 = decrypt_stream(dla_fd_content, passphraseB)
    dec2 = decrypt_stream(dec1, passphraseA)
    return dec2

for p1 in passwords:
    print("Attempt: " + p1)
    for p2 in passwords:
        try:
            decrypt_archive_no_delete(p1, p2)
            if 'INSA{' in dec2:
                print(dec2)
            print("Success p1: " + p1)
            print("Success p2: " + p2)
            quit()
        except:
            pass