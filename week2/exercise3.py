# -*- coding: UTF-8 -*-
"""Modify each function until the tests pass."""


def is_odd(a_number):
    """Return True if a_number is odd, and False if a_number is even.

    Look into modulo division using the '%' operator as one way of doing this.
    """
    answer = None
    if a_number % 2 == 0: 
        # it's even
        answer = False
    else:
        # it's odd
        answer = True
    return answer 


def fix_it(moves=True, should_move=True):
    """Decide what to do.

    Using the engineering flowchart (in week2 folder of the CODE1161-2019
    repo engineeringFlowchart.png) for the rules, return the apropriate
    response to the input parameters.
    Use conditional statements: if, else, elif etc.
    This function should return either:
    "WD-40"
    "Duct Tape"
    "No Problem"

    Most people write this function with 4 return statements. 
    As an extra challenge, see if you can get that down to three.
    """
  
    if moves == True and should_move == False: 
        return "Duct Tape"
    
    elif moves == False and should_move == True: 
        return "WD-40"

    else: 
        return  "No Problem"

  
    

def loops_1a():
    """Make 10 stars.

    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
    a = []
    for i in range (10):
        a.append("*")
    return a

def loops_1c(number_of_items=5, symbol="#"):
    """Respond to variables.

    Using any method, return a list of number_of_items items, each one a
    string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']
    """
    xdd = []
    for i in range (number_of_items):
        xdd.append(symbol)
    return xdd


def loops_2():
    """Make a big square starfield.

    return a list of 10 items, each one a list of 10 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
          ]
    """
    list1 = []
    for a in range (10):
        list2 = []
        for i in range (10):
            list2.append("*")
        list1.append(list2)
    return list1

def loops_3():
    """Make a rising block of numbers.

    Return this:
    [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
        ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
        ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
        ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
        ['6', '6', '6', '6', '6', '6', '6', '6', '6', '6'],
        ['7', '7', '7', '7', '7', '7', '7', '7', '7', '7'],
        ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
        ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
    ]
    remember that range(10) produces a list of numbers from 0...9
    So for every step produced by `for i in range(10):` i is a different number
    TIP: notice that this needs to to return strings of numbers,
         so call str(number) to cast.
    """
    list1 = []
    for i in range (10):
        list2 = []
        for a in range (10):
            list2.append(str(i))
        list1.append(list2)
    return list1      
   

def loops_4():
    """Make a block of numbers that rises left to right.

    Return this:
    [
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    """
    list1 = []
    for a in range (10):
        list2 = []
        for b in range (10):
            list2.append(str(b))
        list1.append(list2)
    return list1


def loops_5():
    """Make the coordinates of the block.

    Return this:
    [
      ['(i0, j0)', '(i0, j1)', '(i0, j2)', '(i0, j3)', '(i0, j4)'],
      ['(i1, j0)', '(i1, j1)', '(i1, j2)', '(i1, j3)', '(i1, j4)'],
      ['(i2, j0)', '(i2, j1)', '(i2, j2)', '(i2, j3)', '(i2, j4)'],
      ['(i3, j0)', '(i3, j1)', '(i3, j2)', '(i3, j3)', '(i3, j4)'],
      ['(i4, j0)', '(i4, j1)', '(i4, j2)', '(i4, j3)', '(i4, j4)'],
      ['(i5, j0)', '(i5, j1)', '(i5, j2)', '(i5, j3)', '(i5, j4)'],
      ['(i6, j0)', '(i6, j1)', '(i6, j2)', '(i6, j3)', '(i6, j4)'],
      ['(i7, j0)', '(i7, j1)', '(i7, j2)', '(i7, j3)', '(i7, j4)'],
      ['(i8, j0)', '(i8, j1)', '(i8, j2)', '(i8, j3)', '(i8, j4)'],
      ['(i9, j0)', '(i9, j1)', '(i9, j2)', '(i9, j3)', '(i9, j4)']
    ]

    TIP:
    You can construct strings either by concatinating them:
        "There are " + str(8) + " green bottles"
    or by using format:
        "There are {} green bottles".format(8)
    you'll come to see the pros and cons of each over time.
    """
    list1 = []
    for i in range (10):
        list2 = []
        for a in range(5):
            list2.append("(" + "i" + str(i) + "," + " " + "j" + str(a) + ")")
        list1.append(list2)
    return list1
       
   
   


def loops_6():
    """Make a wedge of numbers.

    Return this:
    [
      ['0'],
      ['0', '1'],
      ['0', '1', '2'],
      ['0', '1', '2', '3'],
      ['0', '1', '2', '3', '4'],
      ['0', '1', '2', '3', '4', '5'],
      ['0', '1', '2', '3', '4', '5', '6'],
      ['0', '1', '2', '3', '4', '5', '6', '7'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    You don't have to use a literal number in the range function.
    You can use a variable.
    TIP: look out for the starting condition.
    """
    list1 = []
    for a in range (10):
        list2 = []
        for b in range(a+1):
            list2.append(str(a))
        list1.append(list2)
    return list1


def loops_7():
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    or in more simple terms:
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    (this is what will print when you test from inside this file)
    This is a hard problem. Use lots of experimentation and draw
    lots of diagrams!
    """
    
    list1 = []
    for a in range (1,6):
        list2 = []
        for b in range (1,10):
            x = 0 
            y = 5
            if b > y - a and b < y + a:
                list2.append("*")
            else:
                list2.append(" ")
            x = x + 1
        list1.append(list2)
    return list1


def lp(some_kind_of_list, exercise_name):
    """Help to see what's going on.

    This is a helper function that prints your
    results to check that they are tidy.
    Note: You don't have to do anything with it.
    """
    if some_kind_of_list is not None:
        print("\n" + exercise_name)
        if type(some_kind_of_list[0]) is list:
            for row in some_kind_of_list:
                for column in row:
                    print(column, end="")
                print()
        else:
            for column in some_kind_of_list:
                print(column, end="")
            print()
    else:
        print(exercise_name, "maybe you haven't got to this one yet?")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    print(is_odd(1), "is_odd odd")
    print(is_odd(4), "is_odd even")
    print(fix_it(True, True), "fix_it")
    print(fix_it(True, False), "fix_it")
    print(fix_it(False, True), "fix_it")
    print(fix_it(False, False), "fix_it")
    lp(loops_1a(), "loops_1a")
    lp(loops_1c(4, "×°×"), "loops_1c")
    lp(loops_2(), "loops_2")
    lp(loops_3(), "loops_3")
    lp(loops_4(), "loops_4")
    lp(loops_5(), "loops_5")
    lp(loops_6(), "loops_6")
    lp(loops_7(), "loops_7")
