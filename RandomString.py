import string    
import random # define the random module 


def User_ID_Gen():
    S = 7  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    ran2 = "".join(random.choices(string.digits, k = 3))
    ran_final = ran+ran2
    return ran_final

def Order_ID_Gen():
    S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    ran2 = "".join(random.choices(string.digits, k = 5))
    ran_final = ran+ran2
    return ran_final

def Payment_ID_Gen():
    S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    ran2 = "".join(random.choices(string.digits, k = 5))
    ran_final = ran+ran2
    return ran_final

def City_ID_Gen():
    #S = 10  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    #ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    ran2 = "".join(random.choices(string.digits, k = 5))
    ran_final = ran2
    return ran_final


def Resturant_ID_Gen():
    S = 5  # number of characters in the string.  
    # call random.choices() string module to find the string in Uppercase + numeric data.  
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    ran2 = "".join(random.choices(string.digits, k = 3))
    ran_final = ran+ran2
    return ran_final
print("The randomly generated string is : " + str(Resturant_ID_Gen())) # print the random data  