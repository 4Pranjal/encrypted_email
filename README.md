# Encrypted Email Sender and Receiver

This repository contains a Python script that demonstrates how to send and receive encrypted emails using the RSA encryption algorithm. The script utilizes the `rsa` library for encryption and the `smtplib` library for sending emails via SMTP (Simple Mail Transfer Protocol).

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Results](#results)
- [Additional Comments](#additional-comments)
- [Advice](#advice)

## Introduction

In today's digital world, ensuring the confidentiality of email communication is crucial. This script showcases a basic implementation of encrypting and decrypting emails using the RSA encryption algorithm. RSA is a widely-used asymmetric encryption algorithm that relies on the use of public and private key pairs.

The script includes functions for sending and receiving encrypted emails:
- `send_email`: Encrypts and sends an email using the recipient's public key.
- `decrypt_email`: Decrypts an encrypted email using the recipient's private key.

## Usage

1. Install the required libraries:
   ```bash
   pip install rsa
   ```

2. Run the script using a Python interpreter:
   ```bash
   python encrypted_email.py
   ```

3. Observe the example usage of sending and receiving encrypted emails.
You have to add your id and password of gmail, then try to execute it.
There maybe extra setting which you have adjust from your gmail account like enabling 3rd party to access your account.

## Results

The script demonstrates an example of sending and receiving encrypted emails. The provided example uses randomly generated public and private key pairs for demonstration purposes. In real-world scenarios, it's important to securely exchange public keys with the recipients.

Upon execution, the script showcases:
- Encryption of an email message using the recipient's public key.
- Sending the encrypted email via Gmail's SMTP server.
- Decryption of the received email using the recipient's private key.

## Additional Comments

- The script focuses on the fundamental concepts of email encryption using RSA. In practice, public keys must be securely exchanged before sending encrypted emails.
- The example usage showcases encryption and decryption within the same script. In actual usage, the sender and recipient would be separate entities.

## Advice

1. **Secure Key Exchange**: Public keys should be exchanged securely between communication parties to ensure the confidentiality of encrypted emails. Manually exchanging keys through secure channels or using established protocols like PGP (Pretty Good Privacy) can enhance security.

2. **Key Management**: Proper management of public and private keys is essential. Private keys should be kept secure and protected, while public keys can be shared openly.

3. **Use Established Libraries**: While this script provides a basic understanding of email encryption, using established libraries like OpenPGP (GnuPG) for email encryption is recommended for real-world scenarios.

4. **Testing and Validation**: Before deploying any encryption system, rigorous testing and validation are required to ensure its correctness and security.

---
## Author

This repository is maintained by 4Pranjal. Feel free to use and modify the code for educational and research purposes.

For any questions or suggestions, you can contact me through my GitHub profile: [@4Pranjal](https://github.com/4Pranjal).

Made with ❤️ by [Pranjal Jain](https://github.com/4Pranjal)

Happy coding!
