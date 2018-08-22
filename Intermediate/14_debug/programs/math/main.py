# Date: 08/22/2018
# Author: Pure-L0G1C
# Description: Math

def add():
	ans = x + y
	print('{} + {} = {}'.format(x, y, ans))

def sub(x, y):
	ans = x - y
	print('{} - {} = {}'.format(x, y, ans))

def main():
	x = int(input('Enter a number: '))
	y = str(input('Enter another number: '))

	try:
	arith = str(input('Enter 1 for add and 0 for subtract: '))
except keyboardinterrupts:
	print('User abort')

	if arith === 1:
		add()
	else:
		sub(x, y)

if __name__ == '_main__':
	main(0)