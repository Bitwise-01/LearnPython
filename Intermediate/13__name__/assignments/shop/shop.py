# Date: 08/20/2018
# Author: Pure-L0G1C
# Description: Shopping app

from lib import cart
from lib.db import db 

codes = { 
 'view_cart': { 'code': -1, 'func': cart.view },
 'check_out': { 'code': -2, 'func': cart.check_out } 
}

def user_input(txt):
 ''' used to prompting the user '''
 return int(input(txt))
 
def display_cart_outline():
 ''' display outline info '''
 size, price = cart.outline()
 check_out_code = codes['check_out']['code']
 view_cart_code = codes['view_cart']['code']
 msg = 'Check-out: {}\nView cart: {}'.format(check_out_code, view_cart_code)
 print('\nItems: {}\nTotal: ${}\n{}'.format(size, price, msg))

def display_items(cat_id):
 ''' display a list of item in the given category '''
 cart.clear_scrn()
 print('\n\t# ----- {} ----- #\n'.format(db[cat_id]['name'].title()))
 print('\n ID \t\t\t\t Product($)\n')
 items = db[cat_id]['items']
 
 # display items
 for item_id in items:
  item = items[item_id]
  item_name = item['name']
  item_price = item['price']
  print(' {} \t\t\t\t {}(${})'.format(item_id, item_name.title(), item_price))

def select_item(cat_id):
 ''' display a list of item in the given category & prompt user '''
 while True:
  display_items(cat_id)
  display_cart_outline()
  print('Main menu: 99')
  if _user_input(db[cat_id]) == -1:break   

def display_categories():
 ''' display main menu '''
 cart.clear_scrn()
 print('\n\t# ----- Categories ----- #')
 print('\n ID \t\t\t\t Category\n')

 # display categories
 for cat_id in db:
  category = db[cat_id]['name'].title()
  print(' {} \t\t\t\t {}'.format(cat_id, category))
  
def select_category():
 ''' display main menu & prompt user '''
 while True:
  display_categories()
  display_cart_outline()
  if _user_input() == -1:
   break

def _user_input(category=False):
 try:
  if category:
   txt = '[-] Select an item: '
  else:
   txt = '[+] Select a category: '
  chosen_id = user_input(txt)
 except KeyboardInterrupt:
  cart.check_out()
  return -1
 except:
  pass
 
 if category:
  if chosen_id == 99:
   select_category()
   pass
  else:
   items = category['items']
   if chosen_id in items:
    cart.add(items[chosen_id])
 else:
  if chosen_id in db:
   if select_item(chosen_id) == -1:
    cart.check_out()

 if chosen_id in [codes[_]['code'] for _ in codes]:
  for item in codes:
   if codes[item]['code'] == chosen_id:
    func = codes[item]['func']
    break
  func()

if __name__ == '__main__':
 select_category()