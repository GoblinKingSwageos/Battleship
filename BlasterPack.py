import random
import string
import time
from threading import Timer

# Function to create a substitution cipher
def create_cipher():
    alphabet = string.ascii_lowercase
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    cipher = dict(zip(alphabet, shuffled))
    return cipher

# Function to encrypt a message using the cipher
def encrypt_message(message, cipher):
    encrypted_message = ''.join(cipher.get(char, char) for char in message.lower())
    return encrypted_message

# Function to decrypt a message using the cipher
def decrypt_message(encrypted_message, cipher):
    reversed_cipher = {v: k for k, v in cipher.items()}
    decrypted_message = ''.join(reversed_cipher.get(char, char) for char in encrypted_message.lower())
    return decrypted_message

# Function to handle the cipher battle game
def cipher_battle(player1_message, player2_message):
    player1_cipher = create_cipher()
    player2_cipher = create_cipher()

    encrypted_message1 = encrypt_message(player1_message, player1_cipher)
    encrypted_message2 = encrypt_message(player2_message, player2_cipher)

    print(f"Player 1's encrypted message: {encrypted_message1}")
    print(f"Player 2's encrypted message: {encrypted_message2}")

    def timeout():
        print("\nTime's up! Let's see the results.")

    timer = Timer(60.0, timeout)
    timer.start()

    player1_guess = input("Player 1, guess Player 2's original message: ")
    player2_guess = input("Player 2, guess Player 1's original message: ")

    timer.cancel()

    player1_decrypted_message = decrypt_message(encrypted_message2, player2_cipher)
    player2_decrypted_message = decrypt_message(encrypted_message1, player1_cipher)

    player1_correct = player1_guess.lower() == player1_decrypted_message
    player2_correct = player2_guess.lower() == player2_decrypted_message

    if player1_correct and player2_correct:
        print("It's a tie! Both players guessed correctly.")
    elif player1_correct:
        print("Player 1 wins! Guessed Player 2's message correctly.")
    elif player2_correct:
        print("Player 2 wins! Guessed Player 1's message correctly.")
    else:
        print("No correct guesses. It's a draw!")

# Example usage
player1_message = input("Player 1, enter your message: ")
player2_message = input("Player 2, enter your message: ")

cipher_battle(player1_message, player2_message)