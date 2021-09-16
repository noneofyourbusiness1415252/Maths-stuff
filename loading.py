def typewriter(t):
	for x in t:
		print(x, end='')
		sys.stdout.flush()
		sleep(random.uniform(0,0.5))
while True:
	typewriter('Loading...')