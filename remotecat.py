#!/usr/bin/python3

"""
 Description: A simple wrapper for hashcat that loads rockyou.txt into memory
              from a remote source. The author claims no responsibility for
              any misuse of this wrapper, or hashcat itself. Usage of this
              script is identical to hashcat, minus the need to specify a
              wordlist.

 Author: skirmish

 Usage: ./remotecat.py -m <mode> hash.txt
"""

import requests
import sys
from subprocess import Popen, PIPE
from tqdm import tqdm


# Hashcat $PATH (change this if your hashcat binary is located elsewhere)
hashPATH = "/usr/bin/hashcat"

# Create command to run hashcat (with args)
cmd = sys.argv[1:]
cmd.insert(0, hashPATH)
wordlist = ""


def getlist():
    global wordlist
    response = requests.get(url)
    wordlist += response.text


# rockyou.txt filelist (each under 25 MB)
filelist = [
    "rockyou-1.txt",
    "rockyou-2.txt",
    "rockyou-3.txt",
    "rockyou-4.txt",
    "rockyou-5.txt",
    "rockyou-6.txt",
]

# Load rockyou.txt into memory
print("")
for file in tqdm(filelist, desc="Fetching rockyou.txt into memory..."):
    url = "https://raw.githubusercontent.com/skrmsh/rockyou-unzipped/main/" + file
    getlist()
print("")

# Start hashcat/pass wordlist via STDIN
proc = Popen(cmd, stdin=PIPE)
proc.communicate(wordlist.encode())
