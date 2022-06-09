'''
Created on May 25, 2022

@author: NSokol25
Created on Apr 20, 2022
Log: 4/20 - open file, input look for, add traits counter 4/25 - fixed zip code by stripping \n, for line in file loop 5/1 - split into 3 functions, fully functional with 1 piece of data 
5/6 - compare current data and new data, 5/11 - no results where found, compare data fully functional 5/16 - append fully functional, 5/21 - 6/7 working on delete and making bulletproof
bonus: able to repeat
Description - able to sort, delete and append to GCDS database
@author: NSokol25
'''

from csv import writer


#arg 1 - file_in is just the file
#arg 2 - look_for - what the user wants to look for
#arg 3 - datarow - which row of data the user wants to look for
#arg 4 - traitscounter - used to count the amount of traits
#arg 5 - curret data - whoch data you already have(used for sorting throught multiple factors
#arg 6 - counter - just a counter to see if it has ran look for more than once
#returns: - new data - the data just found, counter - so you know how many times look for has been ran
#desc - used to sort through the data to find your current data

def LookFor(file_in, look_for, datarow, traitscounter, currentdata, counter):
    newdata = ""
    if counter != 0:
        traitscounter = 0
    for line in file_in:
        list_of_words = line.strip("\n").split(",")
        try: 
            if look_for in list_of_words[datarow-1]:
                if counter >= 1:
                    if line in currentdata:
                        newdata = newdata + line
                        traitscounter +=1
                else:
                    currentdata = currentdata + line
                    traitscounter +=1

        except: continue
    counter += 1
    if traitscounter > 0:    
        print(str(traitscounter) + ' results where found')
        while True:
            printlines = input("would you like to print your results ")
            if printlines == "yes": 
                if counter <= 1:
                    print(currentdata)
                elif counter > 1:
                    print(newdata)
                break
            elif printlines =='no':
                break
            else:
                print("please enter yes or no")
    elif traitscounter <= 0: 
        print("No results where found")
    if counter <= 1: return currentdata, counter
    else: return newdata, counter
    
#arg 1 - file_in - the file being used
#arg 2  -surrent data - the data user already has
#arg 3 - counter - to see how many times function has been run
#returns - current data - the data the user already has
#desc - used to find and return the data
    

def datafind(file_in, currentdata, counter):
    again = 'yes'
    traitscounter = 0
    while True:
        while True:
            try:
                datarow = int(input("1 for First Name, 2 for Middle Name, 3 for Last Name, 4 for grade, 5 for sex\n6 for Advisor last name, 7 advisor first name, 8 for city, 9 For state, 10 zipcode: "))
                break
            except: print('please enter 1, 2, 3, 4, 5, 6, 7, 8, 9 or 10')
        if datarow == 9: look_for = input("What would you like to look for? ").upper()
        elif datarow == 1 or datarow == 2 or datarow == 3 or datarow == 4 or datarow == 5 or datarow == 6 or datarow == 7 or datarow == 8 or datarow == 10: look_for = input("what would you like to look for? ").lower().capitalize()
        currentdata, counter = LookFor(file_in, look_for, datarow, traitscounter, currentdata, counter)
        file_in.seek(0) 
        if currentdata != '':
            again = input("would you like to compare to another piece of data: ").lower()
            if again != 'yes':
                break
        else: break
    return currentdata


#arg 1 - file_in - the file being used
#no returns
#desc - finds the data user wants to delete using datafind function, then if that data is in bad data, delete it    
    
def delete(file_in):
    file = open("GCDS_Directory.csv","r")
    list_csv = []
    currentdata = ''
    counter = int(0)
    badata = datafind(file_in, currentdata, counter)
    deleted_data = open('document.csv','a')
    for line in file:
        if line not in badata:
            list_csv.append(line)
        else: deleted_data.write(line)
    file_out = open("GCDS_Directory.csv","w")
    for record in list_csv:
        file_out.write(record)
    file.close()

#no args
#returns row - row created for new line(append function)
#used in append function to see which line the user wants to add


def AskForNewLine():
    first = input("Enter your first name: ").lower().capitalize()
    middle = input("Enter your middle name: ").lower().capitalize()
    last = input("Enter your last name: ").lower().capitalize()
    grade = input("Enter your grade: ").lower().capitalize()
    sex = input("Enter your sex: ").lower().capitalize()
    advisorlast = input("Enter your advisor's last name: ").lower().capitalize()
    advisorfirst = input("Enter your advisor's first name: ").lower().capitalize()
    city = input("Enter your city: ").lower().capitalize()
    state = input("Enter your state: ").upper()
    zipcode = input("Enter your zipcode: ")
    row = [first,middle,last,grade,sex,advisorlast,advisorfirst,city,state,zipcode]
    return row

#arg1 - file_in - just the file
#no returns
#desc - can be used to change the file


        
def FileChange(file_in):
    while True:
        action = input ("enter 1 to add a new line, enter 2 to delete a line, and enter 0 to not change the file: ")
        if action == '1':
            row = AskForNewLine()
            with open('GCDS_Directory.csv','a', newline = "") as appendirectory:
                enter = writer(appendirectory)
                enter.writerow(row)
                appendirectory.close()
            break
        elif action == '2':
            delete(file_in)
            break
        if action == '0':
            break
        
        else: print('Please enter 1 to add a line or 0 to not change the file')
            
            
#no args
#returns - file_in - file
#desc - used to open production file (gcds directory)
        
def Openfile():
    
    while True:
        yourself = input('would you like to enter the filename yourself')
        if yourself == 'yes':
            print ("GCDS_Directory.csv")
            file_in = input('Enter the file name: ')
            try:
                file_in = open(file_in)
            except:
                print('File cannot be opened', file_in)
            break
        elif yourself == 'no':
            file_in = open('GCDS_Directory.csv')
            break    
        else: print('please enter either yes or no')
    return file_in
    
               
#main
#desc - able to sort through GCDS database, able to sort, delete and append to a file           


def main():
    full = 'unbroke'
    while full == 'unbroke':
        file_in = Openfile()
        x = 'yes'
        while x == 'yes':
            counter = int('0')
            currentdata = ""
            datafind(file_in, currentdata, counter)
            while True:
                restart = input('Would you like to restart')
                if restart != 'yes' and restart != 'no':
                    print("Please enter yes or no")
                    
                elif restart == 'no':
                    x = 'no'
                    break
                elif restart =='yes':
                    break
        while True:
            filechange = input("would you like to change to file?")   
            if filechange == 'yes':
                FileChange(file_in)
                newfiledatafind = input("Would you like to use the updated file")
                if newfiledatafind == 'no':
                    break
                elif newfiledatafind == 'yes':
                    continue
                else: 
                    print("please enter yes or no")
                    continue
            elif filechange == 'no':     break
            else: print('print input either yes or no')
            '''
            just a concept
        while True:
            seedeleted = input('Would you like to see what you have deleted: ')
            if seedeleted == 'yes':
                deletedlines = open('document.csv')
                lines = deletedlines.readlines()
                for things in lines:
                    print(things)
                print(deletedlines)
                break
            elif seedeleted == 'no':
                print ('ok')
                break
            else:
                print ('please enter either yes or no')
            '''
        fullbreak = input('would you like to end the code: ')
        if fullbreak == 'yes':
            print('goodbye')
            full = 'broke'
        else: print ('ok')
                
        

    file_in.close()
    
            

    
    
main()
