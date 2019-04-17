import turtle
running = True
while running:
	print('enter triangle, square, pentagon, hexagon, circle, or exit:')
	entered = input()
	if entered == 'triangle':
		for i in range(3):
			turtle.forward(100)
			turtle.right(120)

	elif entered == 'square':
		for i in range(4):
			turtle.forward(100)
			turtle.right(90)

	elif entered == 'pentagon':
		for i in range(5):
			turtle.forward(100)
			turtle.right(72)

	elif entered == 'hexagon':
		for i in range(6):
			turtle.forward(100)
			turtle.right(60)

	elif entered == 'circle':
		turtle.circle(50)

	elif entered == 'exit':
		running = False
		print('exiting...')
		print('bye')

	else:
		print('not a command')


