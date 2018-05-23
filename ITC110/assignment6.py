# 1. Create "Caesar" encoder() and decoder() functions.

def encoder(message, key):
    encoded_message = ''
    for character in message:
      encoded_message += chr(ord(character) + key)

    return encoded_message


def decoder(encoded_message, key):
    message = ''
    for character in encoded_message:
      message += chr(ord(character) - key)

    return message

# Test
print(encoder("Banana", 2))
print(decoder("Dcpcpc", 2))


# 2. Count the number of words in a string

def word_count(sentence):
    count = dict()
    words = sentence.split(' ')

    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    total = 0
    for key, value in count.items():
        total += value
    return total

# Test
print(word_count("Hello, Ricky Bobby, and that's a nice car"))
