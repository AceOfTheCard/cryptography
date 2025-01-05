# implementation of the ceasar cipher 
import string  # working with strings 

def ceaesar(text, shift, encrypt=True):
    
    if not encrypt:
        shift=-shift #change the shift 
        
    #keep an empty array where we can store our results 
    result=[]
    for char in text:
        if char.isalpha(): #to process alphabetic characters only, omited the signs and numbers 
            base= ord('A') if char.isupper() else ord('a')
            #shift character and wrap around the alphabet
            shifted= (ord(char)-base +shift)%26 + base
            result.append(chr(shifted)) #the result of shifted is ASCII value that is why we turn it back again to a character 
        else:
            result.append(char) #non-alphabetic characters remain unchanged 
            
    return "".join(result) #returning the result in the form of a string. 


print(ceaesar("Hello, World", 3, encrypt=True)) 

    