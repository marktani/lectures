#!/usr/bin/python
# -*- coding: utf-8 -*-

# let User specify cipher file
# path = raw_input("Input path to cipher file: ");
path = "./test1.txt"
print path

# read file
cipherFile = open(path, "r")

cipher = ""
for line in cipherFile:
    cipher = cipher + line.strip()

# m = raw_input("Input Vigenere variable m: ")
m = 7

k_list = []
for i in xrange(0, m):
    k_list.append(int(raw_input("Input k_" + str(i) + ": ")))


message = ""
k_index = 0
for char in cipher:
    ascii_index = (ord(char) + k_list[k_index % len(k_list)])
    if (ascii_index > 90):
        ascii_index = (ascii_index % 90) + 64
    char = chr(ascii_index)
    k_index = k_index + 1
    message = message + char

print " Cipher: " + cipher
print "Message: " + message

# TODO: bruteforce aller möglichkeiten, in Datei schreiben
# test

cipherFile.close()
