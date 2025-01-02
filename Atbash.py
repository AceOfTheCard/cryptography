def atbash_cipher(message):
    result=""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                result+= chr(90-ord(letter)+65)
            else:
                result+= chr(122-ord(letter)+97)
        else:
            result+= letter
    return result
