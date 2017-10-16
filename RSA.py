"""
Our own implementation of RSA algo
"""

import random

def prime(num: int) -> int:
	"""
	Generator of next simple number

	:param num: seed for prime search
	:return: first prime number after seed
	"""

	while True:
		for i in range(2, int(num ** 0.5) + 1):
			if num % i == 0:
				break
		else:
			return num
		num += 1


def get_prime_number_pair(length: int) -> (int, int):
	"""
	Return pair of random prime numbers of given length (in bits)

	:param length: desired bit length of prime number
	:return: pair of prime numbers of desired length
	"""

	start = 1 << (length - 1)

	while True:
		first_prime = prime(start + int(random.random() * start))
		if first_prime.bit_length() == length:
			break

	while True:
		second_prime = prime(start + int(random.random() * start))
		if second_prime.bit_length() == length:
			break

	return first_prime, second_prime


def generate_RSA_system(length: int) -> (int, int, int):
	"""
	Generates E, D, N values of RSA system. E and N - public part, D and N - private part

	:param length: desired length of numbers in bits (greater -> more secure and more slow)
	:return: E, D, N values
	"""

	# Get pair of prime numbers
	p_prime, q_prime = get_prime_number_pair(length)
	N = p_prime * q_prime

	# Calculate Eiler function of our primes
	eiler_f = (p_prime - 1) * (q_prime - 1)

	# Choose E (coprime with eiler_f, usually Ferma's simple numbers)
	if eiler_f % 65537 != 0:
		E = 65537
	elif eiler_f % 257 != 0:
		E = 257
	elif eiler_f % 17 != 0:
		E = 17
	else:
		# If it's not coprime with Ferma's prime numbers then just use usual
		num = prime(101)
		while eiler_f % num == 0:
			num = prime(num + 1)
		E = num

	# Calculate D value
	D = calculate_D(E, eiler_f)
	return E, D, N


def calculate_D(E, eiler_f) -> int:
	"""
	gets E and eiler_f and returns such D wich D*E mod eiler_f = 1
	nod(D*E, eiler_f*some_unuserful_num) = 1 because d,e and eiler_f - mutually prime
	with upper clause helps wide Evklid algorithm

	:param E: E-key of RSA pair
	:param eiler_f: Eiler function value of N value
	:return: D part of RSA system
	"""

	def wide_euclid_help(e, n, x, y) -> (int, int, int):
		"""
		Internal function of wide Evklid algorithm
		"""
		if e == 0:
			return n, 0, 1
		d, x1, y1 = wide_euclid_help(n % e, e, x, y)
		y1 = y1 - n // e * x1
		return d, y1, x1

	res, first_mul, second_mul = wide_euclid_help(E, eiler_f, 0, 1)
	if first_mul < 0:
		first_mul += eiler_f
	return first_mul

def encrypt(message: list, E: int, N: int) -> list:
	"""
	Encrypt your message with given public key

	:param message: List of numbers representing a message
	:param E: First part of public key
	:param N: Second part of public key
	:return: List of encrypted numbers
	"""

	code = []

	# Calculate m ^ E mod N for each element
	for element in message:
		code.append(pow(element, E, N))

	return code


def decrypt(code: list, D: int, N: int) -> list:
	"""
	Decrypt message with given private key

	:param code: List of encoded numbers received from sender
	:param D: First part of private key
	:param N: Second part of private key
	:return: List of decrypted numbers
	"""

	# Just similar algo with one another var
	message = encrypt(code, D, N)

	return message



