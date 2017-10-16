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


def generate_RSA_system(length) -> (int, int, int):
	"""
	:param length: Length (in bits) of prime numbers

	Returns E (public only part),
	D (private only part),
	N (public and private part)
	"""

	# Get pair of prime numbers
	p_prime, q_prime = get_prime_number_pair(length)
	N = p_prime * q_prime

	# Calculate Eiler function of our primes
	eiler_f = (p_prime - 1) * (q_prime - 1)

	# Choose E (coprime with eiler_f, usually Pherma's simple numbers, but what if it's not coprime with them all...?)
	if eiler_f % 65537 != 0:
		E = 65537
	elif eiler_f % 257 != 0:
		E = 257
	elif eiler_f % 17 != 0:
		E = 17
	else:
		# If it's not coprime with Ferm's prime numbers then just use usual
		num = prime(101)
		while eiler_f % num == 0:
			num = prime(num + 1)
		E = num

	# Calculate D value
	D = calculate_D(E, eiler_f)
	return (E, D, N)


def cypher(message: list, E, N) -> list:
	"""
	message - list of numbers,
	E and N - public key pair of RSA
	"""
	code = []

	# Calculate m ^ E mod N for each element
	for element in message:
		code.append(pow(element, E, N))

	return code


def decypher(code: list, D, N) -> list:
	"""
	code - list of numbers,
	D and N - private key pair of RSA
	"""
	message = []

	# Calculate c ** D mod N for each element
	for element in code:
		message.append(pow(element, D, N))

	return message


def calculate_D(E, eiler_f):
	raise NotImplementedError