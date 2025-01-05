#Perdorim python pasi perdor build-in functionalities 

import string
#Menyra I
import codecs 
plaintext="ECSC{the_winner_is_albania_2025}" #me mire ta besosh 
#to encode it 
cipher=codecs.encode(plaintext,"rot13") #the result ":)"
print(cipher)
#to decode we follow the
text= codecs.encode(cipher,"rot13")
print(text)
