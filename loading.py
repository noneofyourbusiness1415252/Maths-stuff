from time import sleep
from sys.stdout import flush
from random import uniform


def typewriter(t):
	for x in t:
		print(x, end="")
		flush()
		sleep(uniform(0, 0.05))


while True:
	typewriter("Loading...")
