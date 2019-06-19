"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will give "some_words" a series of intergers by calling the equal function.
some_words = ['what', 'does', 'this', 'line', 'do', '?'] # it give a list of words that could be printed out for "some_words"

# 'word' may be one of the item for 'some_words'?  (p.s. i dun rlly k how to use "for n in" function)
for word in some_words:
    print(word) 

for x in some_words:
    print(x) # It may hv th same result as the one above

print(some_words) #print out the list of 'some_words'

# This is gonna be an if n else founctions which could make out how many words for 'some_word' are n print out diif sentences
if len(some_words) > 3:
    print('some_words contains more than 3 words')

elif len(some_words) == 3:
    print('some_words conatains 3 words')

else :
    print('some_words contains less than 3 words') # I made a if, elif, else fucntion to let the computer distinguish the 'length' of 'some_words'

# I think this could define 'usefulFunction' with a 'print' function.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
# I think the uname platform is a func. for findout out the information of the computer
    print(platform.uname()) 
# Renter to make a sentence.
usefulFunction()
