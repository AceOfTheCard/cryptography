#Perdorim python pasi perdor build-in functionalities 

import string
#Menyra I
import codecs 
plaintext="Hello World?__good_to_see_you"
#to encode it 
cipher=codecs.encode(plaintext,"rot13") #the result ":)"
print(cipher)
#to decode we follow the
text= codecs.encode(cipher,"rot13")

#Menyra 2 
#The function takes a message as parameters 
def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append((char)) #special characters here 
    return ''.join(result)


print(rot13(text=text))