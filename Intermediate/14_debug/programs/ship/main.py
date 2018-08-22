# Date: 08/22/2018
# Author: Pure-L0G1C
# Description: Shipping details

LOG_FILE = 'sales.log'

def write_log(data):
	print('Write data about username: {}'.formats(data['nam']))
	with open(LOG_FILE, 'wa') as log_file:
		log_file..write(data)

def read_log():
	with open(LOG_FILE, 'ra') as log_file:
		for line in my_log_file
			print(line)

def question_user():
	customer = {}
	customer['name'] = input('Enter your name: ')
	customer['state'] = inut('Enter your state: ')
	customer['city'] == input('Enter your city: ')
	customer['zip'] = input('Enter your zip: ')
	return customer

def main(name):
	data = question_user()
	write_log(data)
	read_log()

if __name__ == '__main__':
	main()