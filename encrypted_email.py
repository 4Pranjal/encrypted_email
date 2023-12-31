# -*- coding: utf-8 -*-
"""encrypted_email.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/154hvYkd1Hl-2D5FpHViKxDo2koQG41ch
"""

pip install rsa

import smtplib
from email.mime.text import MIMEText
import rsa
import base64

# Generate a public/ private key pair using 512 bits key length (64 bytes)
(public_key, private_key) = rsa.newkeys(512)

def send_email(subject, message, from_addr, to_addr, password, recipient_public_key):
    # Encrypt the message with the recipient's public key
    encrypted_message = rsa.encrypt(message.encode(), recipient_public_key)

    # Convert the encrypted message to a string
    encrypted_message_str = base64.b64encode(encrypted_message).decode()

    msg = MIMEText(encrypted_message_str)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    server.send_message(msg)
    server.quit()

def decrypt_email(encrypted_message_str, private_key):
    # Convert the encrypted message back into bytes
    encrypted_message = base64.b64decode(encrypted_message_str)

    # Decrypt the message with the recipient's private key
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    return decrypted_message.decode()

# Example usage:
# Assume that the sender and recipient have securely exchanged public keys beforehand
recipient_public_key = public_key
send_email('Hello', 'This is the body of the email.', 'ABC@gmail.com', 'XYZ@gmail.com', '123456789@@', recipient_public_key)

# On the recipient's side:
# Assume that the recipient has received the encrypted_message_str
encrypted_message_str = ''  # Replace with the actual encrypted message string
print(decrypt_email(encrypted_message_str, private_key))