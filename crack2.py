#!/usr/bin/python

# Resources:
#     Code adapted from Science Buddies

# --------------- import libraries -----------
import sys, time, hashlib
from array import *


# --------------- global variables -----------

which_password = 0

# the user names and password we're trying to crack. These will get written
password1 = ""
password2 = ""
password3 = ""
password4 = ""
password5 = ""
password6 = ""
password7 = ""
password8 = ""
password9 = ""
password10 = ""

# total number of guesses we had to make to find it
totalguesses = 0


# --------------- extra helper functions -------------------

# Convert a string into MD5 hash
def MD5me(s):
    result = s.encode("utf-8")
    result = hashlib.md5(result).hexdigest()
    return result

# Takes a number from 0 on up and the number of digits we want it to have.
# It uses that number of digits to make a string like "0000" if we wanted 4 or
# "00000" if we wanted 5, converts our input number to a character string,
# sticks them together and then returns the number we started with,
# with extra zeroes stuck on the beginning.
def leading_zeroes(n, zeroes):
    t = ("0"*zeroes)+str(n)
    t = t[-zeroes:]
    return t

# This function takes in numbers, rounds them to the nearest integer and puts
# commas in to make it more easily read by humans

def make_human_readable(n):
    if n >= 1:
        result = ""
        temp = str(int(n+0.5))
        while temp != "":
            result = temp[-3:] + result
            temp = temp[:-3]
            if temp != "":
                result = "," + result
    else:
        temp = int(n*100)
        temp = temp / 100
        result = str(temp)
    return result

# check_userpass
def check_userpass(which_password, password):
    global password1, password2, password3, password4, password5
    global password6, password7, password8, password9, password10

    result = False
    
    if (1 == which_password):
        if MD5me(password) == password1:
            result = True
	
    if (2 == which_password):
		if (MD5me(password) == password2):
			result = True
	
    if (3 == which_password):
		if (MD5me(password) == password3):
			result = True
	
    if (4 == which_password):
		if (MD5me(password) == password4):
			result = True
	
    if (5 == which_password):
		if (MD5me(password) == password5):
			result = True
	
    if (6 == which_password):
		if (MD5me(password) == password6):
			result = True
	
    if (7 == which_password):
		if (MD5me(password) == password7):
			result = True
	
    if (8 == which_password):
		if (MD5me(password) == password8):
			result = True
	
    if (9 == which_password):
		if (MD5me(password) == password9):
			result = True
	
    if (10 == which_password):
		if (MD5me(password) == password10):
			result = True
    return result
# This displays the result of a search including tests per second when possible
def report_search_time(tests, seconds):
    if (seconds > 0.000001):
        print ("The search took %s"%(seconds)+" seconds for "
                +make_human_readable(tests)+
        		" tests or "+make_human_readable(tests/seconds)
                +" tests per second.")
    else:
        print ("The search took %s"%(seconds)+" seconds for "
                +make_human_readable(tests)+" tests.")
    return


#--------------- search method 1 -------------------

def search_method_1(num_digits):
    global totalguesses
    result = False
    a=0
    starttime = time.time()
    tests = 0
    still_searching = True
    print("Using method 1 and searching for "+str(num_digits)+" digit numbers.")
    while still_searching and a<(10**num_digits):
        ourguess = leading_zeroes(a,num_digits)
        tests = tests + 1
        totalguesses = totalguesses + 1
        if (check_userpass(which_password, ourguess)):
            print ("Success! Password "+str(which_password)+" is " + ourguess)
            still_searching = False   # we can stop now - we found it!
            result = True
        a=a+1

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

#--------------- run program(main) -------------------

def main(argv=None):
    global password1, password2, password3, password4, password5
    global password6, password7, password8, password9, password10
    global which_password, totalguesses

    # Set up the passwords we want to crack. These must be MD5 hash
    password1=MD5me("7")
    password2=MD5me("59")
    password3=MD5me("285")
    password4=MD5me("1803")
    password5=MD5me("48526")
    password6=MD5me("829531")
    password7=MD5me("6405701")
    password8=MD5me("34930967")
    password9=MD5me("807392238")
    password10=MD5me("4168030411")
	
    # start searching
    which_password = int(input("Which password (1-10)? "))
    overallstart = time.time()
    foundit = False
    print("Trying to guess password "+str(which_password))

    # See if it's a single digit
    if not foundit:
        foundit = search_method_1(1)
    # Still looking? See if it's a 2 digit number
    if not foundit:
        foundit = search_method_1(2)
    # Still looking? See if it's a 3 digit number
    if not foundit:
        foundit = search_method_1(3)
    # Still looking? See if it's a 4 digit number
    if not foundit:
        foundit = search_method_1(4)
	# Still looking? See if it's a 5 digit number
    if not foundit:
        foundit = search_method_1(5)
    # Still looking? See if it's a 6 digit number
    if not foundit:
        foundit = search_method_1(6)
    # Still looking? Try 7 digit numbers
    if not foundit:
        foundit = search_method_1(7)
    # Still looking? Try 8 digit numbers
    if not foundit:
        foundit = search_method_1(8)
    # Still looking? Try 9 digit numbers
    if not foundit:
        foundit = search_method_1(9)
    # Still looking? Try 10 digit numbers
    if not foundit:
        foundit = search_method_1(10)
    seconds = time.time()-overallstart
    
    # Print results. Else block to prevent crashing when python divides by 0.
    if (seconds < 0.00001):
        print ("The total search took %s"%(seconds)+" seconds and "
        		+make_human_readable(totalguesses)+" guesses.")
        print ("(on some machines, Python doesn't know how long things" 
                +"actually took)")
    else:
        print ("The total search took %s"%(seconds)+" seconds and "
        		+make_human_readable(totalguesses)+" guesses.("
        		+make_human_readable(totalguesses/seconds)
                +" guesses per second)")

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
