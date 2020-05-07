if __name__ == '__main__':
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False
    s = input()
    for i in range(len(s)):
        if(s[i].isalnum() == True):alphanumeric = True
        if(s[i].isalpha() == True):alphabetical = True
        if(s[i].isdigit() == True):digits = True
        if(s[i].islower() == True):lowercase = True
        if(s[i].isupper() == True):uppercase = True 
    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)
