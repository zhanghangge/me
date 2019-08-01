"""All about IO."""


import json
import os
import requests
import inspect
import sys

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()
    data = json.loads(json_data)
    last_name = ["results"]["0"]["name"]["last"]
    password = ["results"]["0"]["login"]["password"]
    postcode = ["results"]["0"]["location"]["postcode"]
    id_value = ["results"]["0"]["id"]["value"]
    id = int(id_value)
    postcode = int(postcode)
    postcodePlusID = id_value + postcode
    return {"lastName": last_name, "PassWord": password, "postcodePlusID": postcodePlusID}



def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    http://api.wordnik.com/v4/words.json/randomWords?api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5&minLength=10&maxLength=10&limit=1
    The arguments that the generator takes is the minLength and maxLength of the word
    as well as the limit, which is the the number of words. 
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &minLength=
    """
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={len}"
    min = 3
    max = 20
    list0 = []
    list1 = []
    list2 = []
    for a in range(min,max+1):
        fullurl=url.format(len=a)
        pull = requests.get(fullurl)   
        if pull.status_code is 200:         
            randomWord = pull.content  
            if randomWord is None: 
                pass
            else:
                randword = str(randword)
                if int(a) % 2 == 0:
                    list2.append(randword[2:len(randword)-1])
                else:
                    list1.append(randword[2:len(randword)-1])
    list2.reverse()
    list0.extend(list1)
    list0.extend(list2)
    return list0


def pokedex(low=1, high=5):
    """ Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.
    
    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    template = "https://pokeapi.co/api/v2/pokemon/{id}"

    index = -1
    tallest = -1

    for x in range (low, high):
        url = template.format(base=template,id=x)
        r = requests.get(url)
        if r.status_code is 200:
            data = json.loads(r.text)
            height = data["height"]
            if height > tallest:
                tallest = height
                index = x

    url = template.format(base=template,id=index)
    r = requests.get(url)
    if r.status_code is 200:
        data = json.loads(r.text)
        answer1 = data["name"]
        answer2 = data["weight"]
        answer3 = data["height"]
    return {"name": answer1, "weight": answer2, "height": answer3}



def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the week4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.
    """
    gcode_data = open(LOCAL + "/Trispokedovetiles(laser).gcode").readlines()
    number_of_times = 0
    for cactusLine in gcode_data:
        print (cactusLine)
        if "M10 P1" in cactusLine:
            number_of_times += 1
    f = open("lasers.pew", "w")
    f.write(str(number_of_times))
    f.close


if __name__ == "__main__":
    functions = [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj))
    ]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print("diarist did not create lasers.pew")