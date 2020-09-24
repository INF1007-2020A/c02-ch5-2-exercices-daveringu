#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
    num_letter=0
    for chr in text:
        if chr.isalnum:
            num.letter+=1
	return num_letter

def get_word_length_histogram(text):
    histogram=[0]
    for word in text.split():
        lenght = get_num_letters(word)
        if lenght>=len(histogram):
            
            histogram+=[0]*(lenght-len(histogram))
        histogram[lenght]+=int(lenght !=0)

	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
    print(get_num_letter("Hello"))
	print(get_num_letters)
    spam = "Stop right there criminal scum! shouted the guard confidently."
	
    eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
