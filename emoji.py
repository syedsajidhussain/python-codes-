# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:33:25 2024

@author: syed.hussain
"""

message = input("enter")
words = message.split(' ') #converts input message into list of words
#create an emoji dictionery use windows logo key + dot(.) to add emojis
emojis = {
        ":)" : "😄" ,
        "(:" : " 😥"
        }

output =''
for word in words:
    output+=emojis.get(word)
print(output)