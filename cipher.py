import random
import time

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_list = [letter for letter in alphabet]


def format_message(msg):
    # convert message to list of strings and remove spaces
    msg_list = [char for char in msg.lower()]
    remove_spaces = [x for x in msg_list if x.strip()]
    return remove_spaces


def encode(m, l):
    # shift letters according to lag
    cipher = alphabet_list[l:] + alphabet_list[:l]

    indices = []
    encoded = []

    # get position of letters in message in the alphabet
    for char in format_message(m):
        indices.append(alphabet_list.index(char))

    # create new word based on cipher
    for index in indices:
        encoded.append(cipher[index])

    return ''.join(encoded)


def decode(enc_msg, lag_guess):
    # break up encoded message back into list of strings
    enc_msg_lst = [char for char in enc_msg]
    dec_indices_lst = []
    decoded = []

    # take indices of positions in alphabet, subtract constant offset (lag) and take modulo of alphabet length
    for char in enc_msg_lst:
        dec_indices_lst.append(alphabet_list.index(char) - lag_guess % 26)

    # convert indices back to characters
    for index in dec_indices_lst:
        decoded.append(alphabet_list[index])

    return ''.join(decoded)


def brute_force():
    english_words = load_words()
    guesses = []

    # try possible configurations of lag
    for lag in range(26):
        guesses.append(decode(encoded_message, lag))

    # test whether guess is in english dictionary
    for guess in guesses:
        if guess in english_words:
            return f"Your word probably was: {guess}, with a lag of {guesses.index(guess)}"
    return f"The message probably was not an English word, but there are the possibilities: {guesses}"


def load_words():
    # read file with english words
    with open('english_words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


# get input for word
msg = input("Choose word to encode: ")

# check if message is string with with single word
while msg.isnumeric() or " " in msg and msg[-1] != " ":
    print("Please type a single word.")
    msg = input("Choose word to encode: ")

# get input for lag
lag = input("Choose your rotor lag (0-25): ")

# check if lag is int
while not lag.isnumeric() or isinstance(lag, int):
    print("Please type an integer value")
    lag = input("Choose your rotor lag: ")

# encode message based on lag
encoded_message = encode(msg, int(lag))
print(f"Encoding {msg} with rotor lag {lag}")
print(f"This is your encoded message: {encoded_message}")
print()

# -----------------------------------------------------------
# Encode message
if input("Would you like the program to attempt to crack the code: (yes/no) ") == "no": exit()

# print faux loading message
print("Decoding message...")
for i in range(3):
    time.sleep(random.randint(1, 3))
    print(".")

# decode message based on encoded message
print(brute_force())
