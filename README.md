# RSA-python
Simple Python implementation of RSA encryption library
  
Usage:
1. Generate E, D, N triple by generate_RSA_system(length), where length is your desired length of prime numbers. Greater length is more secure but much slower (it's very simple implementation and we do not generate prime numbers as OpenSSL does so it's rather slow process, length > 60 is noticeably slow)
2. {E, N} is a public key pair, share it with anyone. To encrypt message with public key use RSA.encrypt(message, E, N). Message must be a list of numbers (byte array maybe, or ord(letters) or smth similar)
3. {D, N} is a private key pair, use it to decrypt messages encrypted with {E, N} pair. Similar: RSA.decrypt(coded_message, D, N), where coded_message is a list of numbers
