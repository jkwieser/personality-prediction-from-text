#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re
# a class for our Essays. Could be required for further development.
# to be extended in further versions

class Essay:
    def __init__(self, text, cEXT, cNEU, cAGR, cCON, cOPN):
        self.text = text
        self.cEXT = cEXT
        self.cNEU = cNEU
        self.cAGR = cAGR
        self.cCON = cCON
        self.cOPN = cOPN
        self.clean_text = self.remove_unwanted_chars(text)
        self.words = self.get_all_words(text)
        self.scentences = self.create_scentences(text)
        self.filtered_text = ""
        self.w2v_words = []
        self.glove = {}

    # a method to documents into scentences
    # possible further improvements. If "." or "!" or "?" is missing
    # split long junks of words into scentences. (see paper: )
    
    def create_scentences(self, text):
        scentences = re.split("(?<=[.!?]) +", text)
        return scentences
    
    # as defined in the paper, all text is changed to lowercase 
    # and all caracters other than ASCII-letters, digits exclamation marks
    # and single and double quotation marks are removed  # I also added "?"
    
    def remove_unwanted_chars(self, text):
        allowed_chars = """ 0123456789abcdefghijklmnopqrstuvwxyz!"".?"""
        clean_text = text.lower()
        for c in clean_text:
            if allowed_chars.find(c) == -1:
                clean_text = clean_text.replace(c, "")
            else:
                pass
        return clean_text


    def get_all_words(self, text):
        
        regex = re.compile("""[^A-Za-z ]""")
        text = regex.sub('', text)
        text = text.split()
        
        return text



