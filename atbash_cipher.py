#here the explanation of atbash cipher 
#differently known as the mirror cipher, A->Z 
#Every character is mapped to its reverse 

# abcdefg -> zyxwvut  :)

#that is the example of the atbash cipher 

def atbash_cipher(message):
    result=[]
    for char in message:
        if char.isalpha():
            if char.islower():
                #the logic for reversing the lower capital letter.
                #ord -> is a function which takes a character and return the ASCII value of it
                # 219 -> ord('z')+ ord('a')
                #chr returns this ASCII value into a character 
                result.append(chr(219-ord(char)))
            elif char.isupper():
                result.append(chr(155-ord(char)))
        else:
            result.append(char)
    
    return "".join(result)
            
    
print(atbash_cipher("hello")) #svool.
# Mesazh nga flokshi : Qe tani e tutje nuk do te perdorim me "hello" , por "svool"
