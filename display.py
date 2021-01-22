'''
module name: display
date created: 27.12.2020

This module contains the display elements used in the interactive part of the program.

'''
import subsets, sounds, data

# whenever input = PAGE NAME, display page_top_info

### pages info
pns = "HOME INFO SELECT SYLLABLES SOUNDS COMPILE SAVE EXIT"
pagenames = pns.split(" ")

### error message
error_message1 = "Invalid input! Try again. \n"
error_message2 = "Invalid input! For more information, go to USAGE. Otherwise, select one of the options below to continue selection process (don't worry, your current selections are saved!): HOME    SELECT    SOUNDS    SYLLABLES"

### HOME page
home_top_info = "***   Welcome to the BENGALI PHONETIC WORD FINDER!   *** \n\nUse the options below to go to a page. If you are new to the program, go to INFO for usage instructions (note: input commands are case-sensitive). Have fun!\n"

home_options = "INFO    SELECT    EXIT \n"

home_input = "Select page name here : "

### INFO page

info_top_info = " \nHere, you can find information about the program. \n"
info_1 = "The sequence of pages available are given below:\nHOME--INFO (get information)    SELECT (select words)    EXIT (quit the program)\nSELECT--SOUNDS    SYLLABLES   COMPILE (view results of current selection) \nSOUNDS--beginning middle  end (to specify constraints on each position) \nCOMPILE--SAVE (save current selection to output file)   SELECT (modify current selection)\n \n"
info_2 = "The list of possible sounds and groups are given below. Note that these are case-sensitive: \n Consonants: [k kh g gh ch chh j jh ^n Y sh T Th D Dh rr R tt tth dd ddh n l s p ph b bh m h]\nVowels: [i ^i ~i ee ^ee E ^E A ^A a oh ^oh u ^u oi ou ^ou aa ^aa] \n \nSound groups: \nvoiced, voiceless, aspirated [kh gh chh jh Th Dh tth ddh ph bh], nasal [^i ^ee ^E ^A ^oh ^u ^ou ^aa ^n n m], fricative [s sh h], stop [k kh g gh T Th D Dh tt tth dd ddh p ph b bh], semi-vowel [Y r l], labial [p ph b bh m], dentialveolar [tt tth dd ddh n l s], retroflex [T Th D Dh], postalveolar [ch chh j jh Y sh T Th D Dh], velar [k kh g gh ^n]\n \n"
info_3 = "(i) SYLLABLE S and SOUNDS can be modified any number of times. Each modification overwrites previous selections. To specify multiple conditions (words matching any of the specified conditiona are allowed), separate them by commas. \n(ii) If you do not want to specify any constraints on a given parameter, type NONE \nThe COMPILE page allows you to see the list generated by the current selection. If not satisfied, you can go back and select certain parameters again, without affecting others (selecting SOUNDS preserves earlier SYLLABLES selection). SAVE creates an output .txt file. "

### SELECT page

select_input = "Options: SOUNDS    SYLLABLES    COMPILE :  "

select_top_info = "On this page, you can specify phonetic properties (sounds, no. of syllables) of your word-list. For more information, go to HOME --> INFO. To see the results of present selection, type COMPILE. For other options, go to HOME. To continue, select phonetic property to specify. \n"



## syllable selection

syllables_top_info = "On this page, you can select the word length(number of syllables). Words containing any of the specified number of syllables wil be included. By default, there are no constraints on syllable number. For more information, go to HOME --> INFO. \n To continue, type OK. To go back to previous page, type SELECT \n :"

syllables_options = "(Options: numbers from 1 to 9, separated by commas. Example: 1,3,4)"

syllables_input = "Enter number of syllables \n"+syllables_options+"\n :"

syllables_post_info = "Your syllable selection has been saved! To view current selection, change selection, or select sounds, go to SELECT \n"



## sound selection

sounds_top_info = "On this page, you can specify conditions on the beginning, middle, and end of the word. For more information, go to INFO. To go back to the previous page, type SELECT. To continue, type OK.\n"

sounds_options = "Options can be found in INFO. If you do not want to impose any restrictions for a particular position, type NONE \n"

sounds_post_info = "Your selections have been saved! To view current selection, change selection, or select syllabes, go to SELECT \n"


###COMPILE
compile_top_info = "This is your curent word-list. To save this as a text file, type SAVE. To modify, go to SELECT --> SOUNDS or SYLLABLES. For other options, go to HOME \n"


###SAVE
save_top_info = "On this page, you can save your current word-list, along with transcriptions, as a text file. The output has the name output.txt and can be found in the same directory as the program. \n ** Note that doing this will overwrite the existing output file. If you want to save that, rename it first! To continue, type OK. \n "

save_input = "(Options: OK   SELECT   HOME) : "

save_post_info = "Your file has been saved! To create another list, go to SELECT. To exit program, type EXIT. For other options, go to HOME.\n"

###EXIT

exit_top_info = "Are you sure you want to exit the program? If you exit, your current selections will be cleared. Your most recent saved list will be available in the program folder as output.txt \n"

exit_input = "To confirm, type YES. Press any other key to go back to the HOME page:\n"