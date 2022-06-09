'''
Created on Nov 18, 2021
bugs: none
bonus: detects how many names are entered(if fn mn and ln was entered), can work without mn and ln, sorted array of characters,
menu, you can do multiple names in one run, as many middle names as you want
Description: Name detector that can detect many different things in name.
@author: NSokol25
'''
import random as ran

#arg - the word you are using, Type: str
#returns the first name capitalized
#my own function to covert a word's first letter to capitalized

def capitalized(word):              
    letter = word[0]                
    letter = ord(letter[0])         
    if letter > 90:
        letter = letter - 32
        letter = chr(letter)
        word = list(word)
        word[0] = letter
        word = ''.join(word)
    return word

#arg - the word you are using, type: str
#returns full word in lowercase
#my own function to covert a full word to lowercase

def lowercase(word):                
    length = len(word)              
    pos = 0                         
    output = ''
    while pos < length:
        letter = ord(word[pos])
        if letter >= 65 and letter < 90:
            letter = letter + 32
        letter = chr(letter)
        output = output + letter
        pos += 1
    return output

#arg1: - the word you are using, type: str
#returns: full word uppercase
#description: my own function to covert a full word to uppercase

def uppercase(word):                
    length = len(word)              
    pos = 0                         
    output = ''
    while pos < length:
        letter = ord(word[pos])
        if letter >= 65 and letter > 90:
            letter = letter - 32
        letter = chr(letter)
        output = output + letter
        pos += 1
    return output

#arg1: name
#arg2: ammounts of names entered
#arg3-5: first name, middle name, last name
#returns: the ammount of vowels and consenents, and if there are no vowels
def consenentfinder(name, names_entered, fn, mn, ln):
    vowelcounter = 0                         #defining empty variables at start
    consenentcounter = 0
    pos = 0
    while pos < len(name):                   #loops through every letter
        letter = name[pos]
        if letter == 'a' or letter == 'o' or letter == 'u' or letter == 'e' or letter == 'i':   #if letter is a vowel
            vowelcounter = vowelcounter + 1 #add one to vowelcounter
        pos = pos + 1
    if names_entered == 3:                     #if the user entered an fn mn and ln
        consenentcounter = len(fn) + len(mn) + len(ln) - vowelcounter   #finds how man consentents there are
    if names_entered == 2:                     #if user entered just fn and ln
        consenentcounter = len(fn) + len(ln) - vowelcounter
    if names_entered == 1:                     #if user just entered fn
        consenentcounter = len(fn) - vowelcounter
    vowelcounter = str(vowelcounter)        #coverting vowel and cosentcounter to str to be printed
    consenentcounter = str(consenentcounter)
    return vowelcounter, consenentcounter
    
#arg1: how many names where entered(as in fn,mn,ln)
#arg2: name
#returns: true if there is a hyphen

def hyphen(name):
    if '-' in (name):                         
        h = True
    else:
        h = False
    h = str(h)
    return h
    
#arg1: name
#returns: name with letters in random order
#description: makes random name out of letters in name


def randomname(name):
    namelist = list(name)
    randomname = ('')
    for letter in name:                     #for each letter in name
        randomletter = ran.choice(namelist) #pick a random letter out of all the letters in name
        randomname = randomname + randomletter
        name = namelist.remove(randomletter)
    return randomname
    
#arg1: name
#arg2: first name
#returns: name backwards and is palendrome is true
#description: gets the name backwards and checks for a palendrome 
    
def backwards(name, fn):
    backwards = ''
    pos = len(name) -1                      #so you start one less than the length of name  because starts at 0
    while pos >= 0:                         #when position is = to or > than 0
        letter = name[pos]                  #for each letter
        pos = pos - 1                       #going 1 letter back
        backwards = backwards + letter      #adding the letter to backwards
    backwardslist = backwards.split()       #same thing done as finding fn mn and ln
    backwardslength = len(backwardslist) - 1#backwardslength is the ammount of items in backwards list - 1 for the 0th place
    backwardsfn = backwardslist[(backwardslength)]#backwardsfn is the last item in backwardslist
    if backwardsfn == fn:                   #if backwardsfn = fn
        palindrome = True                   #palindrome is true
    else: palindrome = False                #if else palindrome is false
    palindrome = str(palindrome)            #boolean can't be printed
    return backwards, palindrome
    
#Arg1: name
#returns: name sorted alphabeticaly
#description: uses my lowercase function and a sorted function to sort name a-z
    
def sortedname(name):
    sortname = lowercase(name)
    sortedname = sorted(sortname)               #sorts name
    sortedname = ''.join(sortedname)        #so it doesn't \n every letter
    return sortedname
    
#Arg1: the ammount of names they entered
#Arg2-4: fn, mn and ln
#returns: the initials of the name entered
    
def initials(names_entered, fn, mn, ln):
    if names_entered == 3:                  #if user entered fn mn and ln
        initials = fn[0] + mn[0] + ln[0] #first letter of each fn mn and ln are initials
    if names_entered == 2:                  #if user only entered fn and ln
        initials = fn[0] + ln[0]
    if names_entered == 1:                  #if user only entered fn
        initials = fn[0]
    initials = uppercase(initials)
    return initials
    
#arg1: name
#returns: name uppercase
#description: converts name they entered to uppercase
    
def uppercasefn(name):
    uppername = uppercase(name)
    return (uppername)

#Arg 1: name
#returns: name lowercase
#description: converts name they entered to lowercase

def lowercasefn(name):
    lowername = lowercase(name)
    return (lowername)

#return: name
#description: just gets name

def getname():
    name = input('Please enter your name: ')
    return name
    
#arg 1: just name
#returns: true or false
#description: checks if name is vaild for code 
#if true continue through the code, if false ask for name again

def namechecker(name):
    while True:
        namecheck = name.replace(' ','')
        namecheck = namecheck.replace('-','')
        namecheck = namecheck.isalpha()         #isalpha returns true if all numbers and false if not
        if namecheck == True:
            return True
        elif namecheck == False:
            print('Invalid character detected\nPlease try again')
            return False

#arg 1: just name entered in getname function
#returns: fn, mn, ln and ammount of names entered
#description: used for fullnamecheck function to get and sort the name

def namesorter(name):
    newname = name.split()                  #splits name in list at spaces 
    namelength = len(newname)               #detects length of name
    namelength -= 1                         #because of 0th place
    fn = newname[0]                         #0th item is fn
    capfn = fn.replace ('-','')            #in case of -
    printfn = capitalized(capfn)            #capitalized function
    mn = ''
    ln = ''
    if namelength >= 1:                     #if user only entered fn
        ln = newname[namelength]            #last item is ln
        capln = ln.replace('-',' ')         #in case of -
        println = capitalized(capln)
        if namelength >= 2:                 #if user only entered fn and ln
            newname.remove(fn)              #removing fn from list
            newname.remove(ln)              #removing ln from list
            mn = ', '.join(newname)         #joining the list to make mn and seperating each middle name by ", "
            mn = mn.replace("-",", ")       #if someone has a hyphen to show multiple middle names
            capmn = mn.replace('-',' ')     #in case of -
            printmn = capitalized(capmn)
            print ('First: ' + printfn + '\nMiddle: ' + printmn + '\nLast: ' + println)#printing
            names_entered = 3
            printname = fn + ' ' + mn + ' '+ ln#for upper lower functions
        else: 
            print ("First: " + printfn + "\nLast: " + println)#if user didn't enter middle name
            names_entered = 2
            printname = fn + ' ' + ln       #for upper lower functions
    else: 
        print ("First: " + printfn)         #if user didn't enter last name and middle name
        names_entered = 1
        printname = fn                      #for upper lower functions
        
    if names_entered == 1:
        print ('you entered only your first name')
    elif names_entered == 2:
        print('You entered your first and last names')
    elif names_entered == 3:
        print ('You entered your first middle and last names')
    return fn, mn, ln, names_entered, printname

#returns: Full name, first mame, middle name, last name and how many names were entered
#Uses my functions get name and name checker to sort the name into fn, mn and ln and make sure its usable

def fullnamecheck():
    while True:
        name = getname()
        hi = namechecker(name)
        if hi == True:
            break
    fn, mn, ln, names_entered, printname = namesorter(name)
    return name, fn, mn, ln, names_entered, printname

def main ():   
    print('Hello User\nWelcome to My Name Detector')
    newname = 'yes'   
    while newname == 'yes':
        name, fn, mn, ln, names_entered, printname = fullnamecheck()
        while True:
            menu = input('Enter m For Possible Options\nWhat Would You Like To Do?: ')
            menu = lowercase(menu)              #converting to lowercase with own function
            if menu == 'm':                     #menu
                print ('Enter c for vowel and consenent counter\nEnter h to check for a hyphen, enter r to scramble the letters in your name\nEnter b to check your name backwords/check for a palindrome\nenter s to sort your name alphabeticaly, enter i for initial(s)\nenter u for uppercase, enter l for lowercase\nenter end to stop checking your name')
            elif menu == 'c':                     #calling all functions
                vowelcounter, consenentcounter, = consenentfinder(name, names_entered, fn, mn, ln)
                print ('You have ' + vowelcounter + ' vowels')  #print statements
                print ('You have ' + consenentcounter + ' consenents')
            elif menu == 'h':
                h = hyphen(name)
                h = str(h)
                print ('Hyphen: '+ h)
            elif menu == 'secret':
                print ('hi creator')
            elif menu == 'r':
                random = randomname(name)
                print ('your name scrambled is ' + random)
            elif menu == 'b':
                backward, palendrome = backwards(name, fn)
                print ('your name backwards is ' + backward)
                print ('palendrome: ' + palendrome)
            elif menu == 's':
                namesorted = sortedname(name)
                print('your name sorted alphabetically is: ' + namesorted)
            elif menu == 'i':
                initial = initials(names_entered, fn, mn, ln)   
                print('your initials are: ' + initial)
            elif menu == 'u':
                uppername = uppercase(printname)
                print (uppername)
            elif menu == 'l':
                lowername = lowercase(printname)
                print (lowername)
            elif menu == 'end':
                newname = input('Enter yes if you would like to enter another name: ') #for the while loop 
                newname = lowercase(newname)
                if newname != 'yes':
                    print ('Goodbye!')
                    break
                    break
                else:
                    break
            else: print ("please enter either m, c, h, r, b, s, i, u, l or end") # if something other than in menu is printed
            



if __name__ == '__main__':
    main()