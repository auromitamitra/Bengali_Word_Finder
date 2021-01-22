'''
module name: main
date created: 27.12.2020

This module contains the interactive program.

'''

import sounds,data,subsets,display,sys
from display import*

d = data.dictionary
full_list = list(d.keys())

### page navigation

def page_func(x):
    '''function to redirect user to appropriate page, if input is a page name'''
    a = x.lower()
    b = a+"_func()"
    c = eval(b)
    return c

### error message
def error_func():
    a = input(error_message)
    return page_func(a)

### HOME 
def home_func():
    '''function for interacting with the HOME page'''
    print(home_top_info)
    print(home_options)
    a = input(home_input)
    return page_func(a)

### INFO

def info_func():
     print(info_top_info)
     print("*****************************")
     print(info_1)
     print("*****************************")
     print(info_2)
     a = input("Type HOME to go back to previous page, type SELECT to start selecting words : ")
     return page_func(a)

### SELECT 

def select_func():
    '''x = string argument; displays options available on the page SELECT '''
    print(select_top_info)
    a = input(select_input)
    if a in pagenames:
        b = page_func(a)
        return b
    else:
        return print(error_message1),select_func()


## SYLLABLE selection

#default = full wordlist(no restrictions on syllable number)    
final_syll_selection = full_list.copy()


def syllables_func(x = final_syll_selection):
    '''function for interacting with the SYLLABLES page'''
    #display top info
    a = input(syllables_top_info)
    
    #if input is a pagename, redirect to corresponding page
    if a in pagenames:
        b = page_func(a)
        return b
    
     #if input is "ok", allow user to select no. of syllables
    if a.lower() == "ok":
        #clear previous selection
        x.clear()
        b = input(syllables_input)
        #if user types "NONE", return default list
        if b.lower() == "none":
            postinput = input(syllables_post_info)
            for i in full_list:
                x.append(i)
            return x
        else:
            #otherwise, using the syllfeeder function, create a list of words matching the syllable conditions
            c = subsets.syllfeeder(b)
            postinput = input(syllables_post_info)
            for word in c:
                x.append(word)
            return x,page_func(postinput)
        
    #if input is neither a page name nor "ok", display error message to allow user to start again
    else:
        return print(error_message1), syllables_func(x = final_syll_selection)

    

## SOUND selection


#condition on beginning sound

#default = full wordlist(no restrictions on first sound) 
final_sound_selectionb = full_list.copy()

def sounds_funcb(x = final_sound_selectionb):
    '''function for matching conditions in the beginning sound'''
    #clear previous selection
    x.clear()
    a = input("Enter conditions for word beginning: ")
    #if user types "none", return default list
    if a.lower()== "none":
        for i in full_list:
            x.append(i)
        return x
    #otherwise, using the soundfeeder function, create a list of words matching the sound conditions
    else:
        b = subsets.soundfeederb(a)
        for word in b:
            x.append(word)
        return x


#condition on middle sound

#default = full wordlist(no restrictions on middle sound) 
final_sound_selectionm = full_list.copy()


def sounds_funcm(x = final_sound_selectionm):
    '''function for matching conditions in the middle sound'''
    #clear previous selection
    x.clear()
    a = input("Enter conditions for word middle: ")
    #if user types "none", return default list
    if a.lower()== "none":
        for i in full_list:
            x.append(i)
        return x
    #otherwise, using the soundfeeder function, create a list of words matching the sound conditions
    else:
        b = subsets.soundfeederm(a)
        for word in b:
            x.append(word)
        return x


#condition on end sound

#default = full wordlist(no restrictions on middle sound) 
final_sound_selectione = full_list.copy()


def sounds_funce(x = final_sound_selectione):
    '''function for matching conditions in the end sound'''
    #clear previous selection
    x.clear()
    a = input("Enter conditions for word end: ")
    #if user types "none", return default list
    if a.lower()== "none":
        for i in full_list:
            x.append(i)
        return x
    #otherwise, using the soundfeeder function, create a list of words matching the sound conditions
    else:
        b = subsets.soundfeedere(a)
        for word in b:
            x.append(word)
        return x



#main sound selection function
    
def sounds_func():
    '''function for interacting with the sound selection page'''
    #display top info
    a = input(sounds_top_info)
    #if input is a pagename, redirect to corresponding page
    if a in pagenames:
        b = page_func(a)
        return b
    #if input is "ok", allow user to select sounds   
    if a.lower() == "ok":
        print(sounds_options)
        beginning = sounds_funcb()
        middle = sounds_funcm()
        end = sounds_funce()
        postinput = input(sounds_post_info)
        return beginning, middle, end, page_func(postinput)
    #if input is neither a page name nor "ok", display error message to allow user to start again
    else:
        return print(error_message1), sounds_func()


##COMPILE function

#final list of transcriptions
compiled_list_sound = []
#final list of words
compiled_list_word = []

def compile_func(x = compiled_list_sound,y = compiled_list_word):
    '''arg = s/w -- whether to print phonetic transcriptions(s) or words (w). Function to compile final list of words satisfying all selected conditions. '''
    #clear current selection
    x.clear()
    y.clear()
    #take the lists from each condition
    a = final_syll_selection
    b = final_sound_selectionb
    c = final_sound_selectionm
    d = final_sound_selectione
    #get their intersection
    temp = subsets.andlist(a,b,c,d)
    #transcription list
    for i in temp:
        x.append(i)
    #word list
    for i in temp:
        if i in d:
            word = data.dictionary[i]
            y.append(word)
    #ask user whether to display word-list, or transcription-list, print the corresponding list
    printinfo = input("Do you want to see the words (w) or phonetic transcriptions (s)?\n Options: s \t w : ")
    if printinfo.lower()== "s" :
        print(compile_top_info+"\n CURRENT LIST (words = ",len(x),"):\n",x,"\n")
    if printinfo.lower()== "w" :
        print(compile_top_info+"\n CURRENT LIST (words = ",len(y),"):\n",y,"\n")
        
    postinput = input("Select option (SAVE \t SELECT \t HOME): ")
    return x,y,page_func(postinput)


##SAVE function

def save_func():
    output = open("output.txt","w")
    print(save_top_info)
    a = input(save_input)
    if a.lower() == "ok":
        slist = compiled_list_sound
        output.write("Bengali Word-list *** Words: "+ str(len(slist))+"   \n   \n")
        for i in slist:
            w = d[i]
            s = i
            #write words and their transcriptions in the output file
            output.writelines('%s \t\t %s \n'% (w,s))
        output.close()
        postinput = input(save_post_info)
        return page_func(postinput)
    else:
        return page_func(a)
        

##EXIT function

def exit_func():
    print(exit_top_info)
    confirm = input(exit_input)
    if confirm.lower() == "yes":
        sys.exit("Thank you!")
    else:
        page_func("HOME")
    return
    
#program starter command
page_func("HOME")
