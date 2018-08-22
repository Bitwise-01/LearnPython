# Date: 08/20/2018
# Author: Pure-L0G1C
# Description: Cart

from sys import exit
from os import system # os.system allows us to run command-line commands
from platform import system as platform # platform.system is used for getting current platform

cart = []
DISCOUNT = 0.20 # 20%

# for clearing screen
if platform().lower() == 'windows':
 clear_screen_cmd = 'cls'
else:
 clear_screen_cmd = 'clear'

def clear_scrn():
 system(clear_screen_cmd)

def view():
 if not cart:return
 clear_scrn()
 print('\n\t# ----- Cart ----- #')
 print('\n#\t\tProduct($)\n')

 num = 0
 for item in cart:
  num += 1
  print('{}\t\t{}(${})'.format(num, item['name'].title(), item['price']))

 try:
  input('\nTotal items: {}\nTotal price: ${}\nPress Enter to Continue'.format(len(cart), calc_price()))
 except KeyboardInterrupt:
  check_out()
 except:pass

def add(item):
 name = item['name']
 price = item['price']
 cart.append({ 'name': name, 'price': price }) 

def calc_price():
 total_price = 0.00
 for item in cart:
  price = item['price']
  total_price += price
 return total_price

def outline():
 total_items = len(cart)
 total_price = calc_price()
 return total_items, total_price

def check_out():
 clear_scrn()
 price = calc_price()
 _price = price - (price * DISCOUNT)
 print('Original price: ${}\nDiscount price: ${}'.format(price, _price))
 exit()