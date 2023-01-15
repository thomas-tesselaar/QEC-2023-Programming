#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 14:11:41 2023

@author: thomastesselaar
"""

# Not all functions in this file are complete

import pandas as pd
from pandasql import sqldf


# A function to view a users library
def view_reading_list(user):
    user_df = pd.read_csv("Library.csv")
    book_df = pd.read_csv("Book.csv")
    
    # query the database for the IDs of the books being read
    q = f'SELECT bookID FROM user_df WHERE userID = {user}'
    book_ids = sqldf(q, locals())
    
    # Converts book_ids to a list
    book_ids = book_ids["bookID"].tolist()
    
    # Get the titles of those books
    q = f'SELECT title FROM book_df WHERE bookID IN {book_ids}'
    books = sqldf(q, locals())
    
    return books


# Recommends books a user may like based on books they have read
def recommend_books(user):
    
    # Get the books this user has read 
    books_read = view_reading_list(user)
    
    # Find the book most similar, a good model for this might be KNN
    '''
    import scikit_learn as sk
    from sk import knn
    
    # Set knn parameters
    
    recommendation = sk.predict(books_read)
    
    '''
    
    # Give them their most read genre
    print("Your most read genre is")
    
    # Provide book recommendations
    print("We recommend")
    
    # return recommendation
    
    pass


# Recommends clubs that may fit the users interests based on books they liked
def recommend_clubs(user):
    # This function would recommend clubs to a reader based on the similarity 
    # of genres read by the other members of the club
    
    pass