#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 12:57:41 2023

@author: thomastesselaar
"""
# Might need to open Terminal/Command line and enter "pip install openai"
# for this code to work

# Please do not run this file too many times, after a certain point I will run 
# out of openai usage credits



# Imports functions from other .py files
from summarize_book import read_book, summarize_book, summarize_to_sentence
from generate_image import generate_image
from manage_user import view_reading_list, recommend_books


# Reads in book as a string
book = read_book("three_little_pigs.txt")


# Toggle 0/1 to get a summary and ai generated image
# All features tested and work well
if(1):
    
    # Prints a summary of the book
    summary = summarize_book(book, 0)
    print(summary)
    print("\n")
    
    
    # Summarizes the book to a single sentence
    short_summary = summarize_to_sentence(book)
    
    
    # Generates an image visual the book (or a portion of it) and returns a url
    # to view it
    image_name = "three_little_pigs"
    print(generate_image(short_summary, image_name))


# Toggle 0/1 to view the library of some user
# Leave as 0 since not all features work yet, still are bugs
if(0):
    print(view_reading_list(3))




