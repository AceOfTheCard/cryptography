# implementation of the ceasar cipher 
import string  # working with strings 

def ceaesar(text, shift, alphabet):
    
    #specify the shifting function
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    
    shifted_alphabets = tuple(map(shift_alphabet, alphabet))
    final_alphabet = "".join(alphabet)
    final_shifted_alphabet= "".join(shifted_alphabets)
    
    #making a translation table
    #we can have different types if alphabets in here  
    table = str.maketrans(final_alphabet,final_shifted_alphabet)
    
    return text.translate(table)


message = " This is the last warning "
# how to break it, very simple can you find it?
print(ceaesar(text=message, shift=21,alphabet=[string.ascii_lowercase,string.ascii_uppercase, string.punctuation]))