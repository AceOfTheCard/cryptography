#encrypt 

# Vigenere cipher , implementation
LETTERS ="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #the letter of the alphabet 

def encryptMessage(key, message):
    return translateMessage(key, message, "encrypt")

def decryptMessage(key, message):
    return translateMessage(key, message, "decrypt")

def translateMessage(key, message, mode):
    translated =[]
    keyIndex=0
    key = key.upper()
    
    for symbol in message: #Loop through each symbol in message 
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS 
            if mode=="encrypt":
                num += LETTERS.find(key[keyIndex]) #add if encrypted 
            elif mode == "decrypt":
                num -= LETTERS.find(key[keyIndex]) #subtract if decrypting 
            # starting from the beginning if 
            num %= len(LETTERS) #handle any wrapp around 
            
            #Add the encrypted/ decrypted symbol to the end of translated 
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
                
            keyIndex+=1 # move to the next letter in the key 
            if keyIndex == len(key):
                keyIndex = 0
        else :
            #Append the symbol without encrypting/ decrypting 
            translated.append(symbol)
            
    return "".join(translated)
     


def main():
    message="Pwzevznvmfxz nyi mgfuflu :)!"
    key = "ASIMOV" #specify any key you want here 
    mode = "decrypt" #put the mode encrypt or decrypt
    
    if  mode=="encrypt":
        translated= encryptMessage(key,message)
    elif mode== "decrypt":
        translated= decryptMessage(key,message)
    else:
        print("The mode is not suitable") # specified an invalid mode 
        
    print(mode.title()) #the mode choosen either encrypt or decrypt
    print(translated)# the "translated based on the mode"
  
  
#deshmitar qe punon
main()      

