'''
Created on Oct 20, 2021

@author: NSokol25
'''
def main():
    cof = input("Do you already know fahrenheit or celsius? ") #asking is celcius wants to be converted or farenheit wants to be converted
    if cof == ("celsius"):
        celsius = int(input("Enter celsius: "))    
        fahrenheit = (celsius * 1.8 + 32)       #conversion 
        fahrenheit = str(fahrenheit)            #turning back into str so it can be printed 
        print (fahrenheit + " degrees fahrenheit")
    elif cof == ("fahrenheit"):
            fahrenheit = int(input("Enter fahrenheit: "))   #same as celsius
            celsius = ((fahrenheit - 32) * .5556)
            celsius = str(celsius)
            print (celsius + " degrees celsius")
    else:
        print ("check spelling")
    
if __name__ == '__main__':
    main() 
