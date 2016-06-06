#!/usr/bin/env python2.7
import random , string

count = 0

word_length = input("Word length : ")

string.lowecase = 'abcdefghijklnmopqrstuvwhyz'

def randomword(word_length):
    return ''.join(random.choice(string.lowecase) for i in range(word_length))

while count < 10:
    word = randomword(word_length)
    print word
    usr_input = raw_input("")
    
    if word == usr_input:
       count += 1
