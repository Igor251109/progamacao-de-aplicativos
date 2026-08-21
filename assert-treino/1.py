def dobrar(numero):
 	return numero * 2

assert dobrar(3) == 6  # passa
assert dobrar(-2) == -4  # passa
assert dobrar(0) == 1  # não passa. 0 * 2 não é 1, é zero.
