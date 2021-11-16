# Bengali Word-Finder  

Psycholinguistic experiments often require sets of words that begin with, end with, or contain certain sounds, have a certain number of syllables etc. Finding these by introspection takes time and is not the most efficient or reliable.

The word-finder uses an underlying corpus to generate lists of words matching specified phonological descriptions. These can be the presence or absence of certain sounds at given positions, or number of syllables. Apart from single sounds, it also pre-defines linguistically relevant sound groups, so that it is possible to find, for example, words that begin with a nasal, or contain a voiced retroflex. You can use boolean operators (`AND` and `OR`) to combine multiple conditions.

It is also possible to preview, edit, and filter a current selection before generating an output file with the list of words.

--------
To use:

1. Clone this repository
2. Open a terminal window and direct it to the base directory (`cd path/to/directory/Bengali_Word_Finder/`)
3. Run `bengali_word_finder.py` on python 3 (`python3 bengali_word_finder.py`)
- Note that the other scripts are called as modules by the main program, so make sure the directory structure remains the same
- Detailed documentation and example output in the `Documentation` folder. Usage instructions can also be found from the `HELP` command when you run the main program

-------


This tool currently works with data and transcription system from the Bengali [SHRUTI corpus](http://cse.iitkgp.ac.in/~pabitra/shruti_corpus.html). Words are transliterated using the [ITRANS](https://www.aczoom.com/itrans/html/tblall/tblall.html) format (Indian languages TRANSliteration). To use with any related language that has a corpus with a similar transcription scheme (reference on pg. 52 [here](http://cse.iitkgp.ac.in/~pabitra/paper/ococosda11.pdf)), replace the file `shruti.dic` with the pronunciation dictionary from your corpus of choice.

Using the word-finder with a different transcription scheme/phonologically unrelated language will need some changes to the code. I'm working to separate the language-specific part of the program from core part, so that customizing for new languages is simpler. If you want to use it for another language, are interested in contributing to the code, or have any suggestions, please get in touch! 
 
