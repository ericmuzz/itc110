secret_message = input("Enter a secret message: ")
encoded_message = ''

for character in secret_message:
    encoded_message += str(ord(character)) + '-'
    # e.g 76-92-42-31

encoded_message = encoded_message[:-1]

print("Encoded message:", encoded_message)

decoded_message = ''
for encoded_char in encoded_message.split('-'):
    print(encoded_char)
    decoded_message += chr(int(encoded_char))

print("The decoded message:", decoded_message)
