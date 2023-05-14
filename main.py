import re
import keyword

def isInt(userInput):
	regex_pattern = r'^[-+]?\d+$'
    #ya to + ayega ya - aur dono main se koi bhi nahi hoga to koi masla nahi.
    # aur us k bd ek ya us se ziyada digits asaktay hain.
	if re.match(regex_pattern, str(userInput)):
		return True
	else: 
		return False

def isFloat(userInput):
	regex_pattern = r'^[-+]?\d+\.\d+$'
    #ya to + ayega ya - aur dono main se koi bhi nahi hoga to koi masla nahi.
    # aur us k bd ek ya us se ziyada digits asaktay hain.
    #us ke bad ek dot(.) compulsory ayega.
    #us k bd phir se ek ya us se ziyada digits asaktay hain.
	if re.match(regex_pattern, str(userInput)):
		return True
	else:
		return False

def isString(userInput):
	regex_pattern = r'[A-z0-9!@#$%^&*()_+=-]+'
    #capital ya small alphabets, numbers aur special character asaktay hain.
    # kam se kam ek hona lazmi hai. 
	if re.match(regex_pattern, userInput):
		return True
	else:
		return False

def isIdentifier(userInput):
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    #capital ya small letter ya phir underscore se start ho.
    #us k bd 0 ya us se ziyada capital ya small letters asaktay hain.
    if re.match(regex_pattern, userInput):
        if userInput in keyword.kwlist:
            #keyword ko import kara hai ta ke reserved keywords pr loop laga kr unhe valid identifier banne se rok saken.
            print(f"{userInput} is an invalid identifier (reserved keyword).")
            return False
        else:
            print(f"{userInput} is a valid identifier.")
            return True
    else:
        print(f"{userInput} is an invalid identifier.")
        return False

        
def isCharacter(userInput):
    if len(userInput) == 1:
        return True
    else:
        return False

userInput = input("Enter something to check data type: ")
isValidIdentifier = input("Enter to check if identifier is valid or not: ")

if isInt(userInput):
    print(f"{userInput} is an integer")
elif isFloat(userInput):
    print(f"{userInput} is a float")
elif isString(userInput):
    print(f"{userInput} is a string")
elif isChar(userInput):
    print(f"{userInput} is a character")
    
isIdentifier(isValidIdentifier)
