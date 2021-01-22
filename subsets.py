'''
module name: subsets
date created: 27.12.2020

This module creates subsets of the phonetic dictionary (transcription column), based on:
1. No. of syllables (syllablelist function)
2. Sounds/sound groups present (soundlist function)
3. Complement list-- list of items which DO NOT fulfill a given condition (notlist function)
4. Intersection list-- list of items which are present in all the given lists (andlist function)
5. Union list-- list of items which are present in at least one of given lists (orlist function)

'''

import re,sounds,data


def syllablecount(x):
    '''x = input string; returns no. of syllables(counted as no. of vowel sounds)'''
    v = sounds.vowel
    string = str(x)
    #separate string into sounds
    s = string.split(" ")
    count = 0
    for i in s:
        if i in v:
            count += 1
    return count
            


def syllablelist(n):
    '''n = no. of syllables; returns list of items in dictionary having n syllables'''
    d = data.dictionary
    #get all transcriptions
    keys = list(d.keys())
    syllablelist = []
    #if transcription has the required no. of syllables, add it to the list
    for i in keys:
        if syllablecount(i) == n:
            word = i
            syllablelist.append(word)
    return syllablelist


def protect(x):
    '''x = a string; returns string in which regex special character(^) in the input is protected with a backslash. This prevents nasal sounds in the transcriptions from being misinterpreted.'''
    a = "^\^"
    #if 1st character of input is a regex special character
    res = re.search(a, x)
    if res:
        #add a backslash before the string
        y = "\\"+x
        return y
    return x



def matchsound(w,x,p):
    '''w = word, x = sound, p = position: b(beginning)/m(middle)/e(end); returns True if the word contains the given sound in the specified position'''
    sound = w.split(" ")
    if p == 'b':
        s = sound[0]
        if s == x:
            return True
        return False

    if p == 'm':
        if len(sound) < 3:
            return False
        else:
            count = 0
            midsounds = sound[1:-1]
            for i in midsounds:
                if i == x:
                    count += 1
            if count > 0:
                return True
            return False    
                
    if p == 'e':
        s = sound[-1]
        if s == x:
            return True
        return False


def matchgroup(w,g,p):
    '''w = word, g = sound group, p = position: b(beginning)/m(middle)/e(end); returns True if the word contains the given sound in the specified position'''
    sound = w.split(" ")
    #if position is "begining"
    if p == "b":
        #take the 1st sound
        s = sound[0]
        #define sound group according to the input
        group = eval("sounds."+g)
        #check if 1st sound belongs to the given group
        if s in group:
            return True
        return False

    #if position is "end"       
    if p =="e":
        s = sound[-1]
        group = eval("sounds."+g)
        if s in group:
            return True
        return False

    #if position is "middle"
    if p == "m":
        # false if there are less than 3 phonemes (no medial sound)
        if len(sound) < 3:
            return False
        else:
            #take the word-medial sounds
            midsounds = sound[1:-1]
            group = eval("sounds."+g)
            count = 0
            #for each sound, check if it belongs to the group
            for i in midsounds:
                if i in group:
                    count += 1
            #if any of the sounds are in the group, return True
            if count > 0:
                return True
            return False
    

    

def soundlist(x,y):
    '''x = sound or group, y = position: b(beginning)/m(middle)/e(end); returns a list of words containing the specified sound/group in the specified position'''
    soundlist = []
    d = data.dictionary
    #list of all the transcriptions
    keys = list(d.keys())
    
    #if a group is specified
    if x in sounds.groups:        
        for word in d:
        #iterate over all transcriptions in the dictionary, check if there is a group match
            a = matchgroup(word,x,y)
            if a:
                #add matched entries to new list
                soundlist.append(word)

    #if a sound is specified
    if x not in sounds.groups:
        #iterate over all transcriptions in the dictionary, check if there is a sound match
        for word in d:
            a = matchsound(word,x,y)
            if a:
                #add matched entries to new list
                soundlist.append(word)
            
    return soundlist





def notlist(x):
    '''x = a list; returns list of all items in the phonetic dictionary which are not in the input list (complement list)'''
    d = data.dictionary
    wholelist = list(d.keys())
    notlist = []
    for i in wholelist:
        if i not in x:
            notlist.append(i)
    return notlist




def andlist(*x):
    '''x = list names separated by commas; returns the list of items which are present in all the input lists'''
    #get all the lists
    lists = list(x)
    #convert each list into a set and get the intersection. Convert final set back into a list
    return list(set.intersection(*map(set, lists)))
    


def orlist(x):
    '''x = list of input lists; returns a list of items which are present in any of the input lists'''
    #get all the lists
    lists = x
    #convert each list into a set and get the union. Convert final set back into a list
    return list(set.union(*map(set, lists)))


#syllable selection feeder function
def syllfeeder(x):
    '''x = string of numbers separated by commas; returns a list containing words in which no. of syllables = the input numbers'''
    syll_selection = []
    #get the numbers in the input
    inputlist = x.split(",")
    #for each number, create a list of words having that no. of syllables
    for i in inputlist:
        a = syllablelist(eval(i))
        syll_selection.append(a)
    #return the union set
    final_syll_selection = orlist(syll_selection)
    return final_syll_selection

###sound selection feeder functions   
def soundfeederb(x):
    '''x = string of conditions separated by commas; returns a list containing words in which the first sound fulfills any of the the input conditions'''
    sound_selectionb = []
    #get conditions
    inputlistb = x.split(",")
    #iterate over conditions, create a list of words matching each one
    for i in inputlistb:
        a = soundlist(i,'b')
        sound_selectionb.append(a)
    #return the union set
    final_sound_selectionb = orlist(sound_selectionb)
    return final_sound_selectionb


def soundfeederm(x):
    '''x = string of conditions separated by commas; returns a list containing words in which the middle sounds fulfill any of the the input conditions'''
    sound_selectionm = []
    #get conditions
    inputlistm = x.split(",")
    #iterate over conditions, create a list of words matching each one
    for i in inputlistm:
        a = soundlist(i,'m')
        sound_selectionm.append(a)
    #return the union set
    final_sound_selectionm = orlist(sound_selectionm)
    return final_sound_selectionm

def soundfeedere(x):
    '''x = string of conditions separated by commas; returns a list containing words in which the first sound fulfills any of the the input conditions'''
    sound_selectione = []
    #get conditions
    inputliste = x.split(",")
    #iterate over conditions, create a list of words matching each one
    for i in inputliste:
        a = soundlist(i,'e')
        sound_selectione.append(a)
    #return the union set
    final_sound_selectione = orlist(sound_selectione)
    return final_sound_selectione

