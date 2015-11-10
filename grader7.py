# automaton imports
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


# other imports
import json

# Global Setup
while True:
	ideUN = raw_input('Please enter your CS50 IDE username: ')
	print "ENTERED:", ideUN
	c = raw_input('Confirm? (Y/N) ')
	if c.lower() == "y":
		break

URL = "http://ide50-" + ideUN + ".cs50.io"

# URL = "http://finance.cs50.net"
brows = wd.Firefox()
UN = 'SaMgReEn'
PW = 'Cs50RaWks!'


print "WELCOME TO THE pset7 GRADING MACHINE"
print "PLEASE KEEP THIS CONSOLE VISIBLE WHILE GRADING (if possible)"
print "WHEN PROMPTED BY FIREFOX, PLEASE LOG IN TO THE CS50 IDE"
print "WHEN LOGGED IN, START KARL'S runner7.sh SCRIPT w/ proper setup and chmods"
print "N.B. IF AT ANY POINT YOU ARE NOT SURE ABOUT THE SCRIPT'S OUTPUT,\
 YOU *CAN* AND *SHOULD* MANUALLY CONTROL FIREFOX TO KICK AROUND YOURSELF!"
print "<3 Sam"

# process user input for grades
def get_grade(axis):
	while True:
		grade = raw_input('Enter grade for {%s} (0/1): ' % axis)
		if not (grade.lower() == '0' or grade.lower() == '1'):
			print "Retry: {%s}" % axis
			continue
		else:
			return int(grade)

# Direct Automaton to register.php
def visit_register():
	brows.get(URL + "/register.php")

def login():
	print "LOGGING IN"
	brows.get(URL + "/login.php")

	un = brows.find_element_by_xpath('(//input)[1]')
	un.send_keys(UN)

	pw = brows.find_element_by_xpath('(//input)[2]')
	pw.send_keys(PW)

	btn = brows.find_element_by_xpath('//button')
	btn.click() 

def logout():
	brows.get(URL + "/logout.php")

# test empty form behavior
def register_empty_fields():
	axis = "register_empty"
	print axis
	
	# test all empty
	logout()
	visit_register()
	btn = brows.find_element_by_xpath('//button')
	btn.click()
	raw_input('Test 1 of 4 finished. Press any key to continue.')

	# test confirm empty
	logout()
	visit_register()
	un = brows.find_element_by_xpath('(//input)[1]')
	un.send_keys(UN)

	pw = brows.find_element_by_xpath('(//input)[2]')
	pw.send_keys(PW)	

	btn = brows.find_element_by_xpath('//button')
	btn.click()
	raw_input('Test 2 of 4 finished. Press any key to continue.')


	# test pw empty
	logout()
	visit_register()
	un = brows.find_element_by_xpath('(//input)[1]')
	un.send_keys(UN)
	cnf = brows.find_element_by_xpath('(//input)[3]')
	cnf.send_keys(PW)
	btn = brows.find_element_by_xpath('//button')
	btn.click()
	raw_input('Test 3 of 4 finished. Press any key to continue.')

	# test un empty
	logout()
	visit_register()
	pw = brows.find_element_by_xpath('(//input)[2]')
	pw.send_keys(PW)
	cnf = brows.find_element_by_xpath('(//input)[3]')
	cnf.send_keys(PW)
	btn = brows.find_element_by_xpath('//button')
	btn.click()


	while True:
		input = raw_input('Test 4 of 4 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return register_empty_fields()

# test mismatch behavior
def register_mismatch():
	axis = 'register_mismatch'
	print axis
	
	logout()
	visit_register()

	un = brows.find_element_by_xpath('(//input)[1]')
	un.send_keys(UN)

	pw = brows.find_element_by_xpath('(//input)[2]')
	pw.send_keys(PW)

	cnf = brows.find_element_by_xpath('(//input)[3]')
	cnf.send_keys(PW + "WRENCH!!!!")

	btn = brows.find_element_by_xpath('//button')
	btn.click()

	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return register_mismatch()

# test duplicate user behavior
def register_duplicates():
	axis = 'register_duplicates'
	print axis

	# setup for repeat registration
	logout()
	visit_register()

	# repeat registration
	un = brows.find_element_by_xpath('(//input)[1]')
	un.send_keys(UN)

	pw = brows.find_element_by_xpath('(//input)[2]')
	pw.send_keys(PW)

	cnf = brows.find_element_by_xpath('(//input)[3]')
	cnf.send_keys(PW)

	btn = brows.find_element_by_xpath('//button')
	btn.click()

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return register_duplicates()
			break	

# test valid registration behavior
def register_valid():
	axis = 'register_valid'
	print axis

	logout()
	visit_register()

	# repeat registration
	un = brows.find_element_by_xpath('(//input)[1]')
	un.send_keys(UN)

	pw = brows.find_element_by_xpath('(//input)[2]')
	pw.send_keys(PW)

	cnf = brows.find_element_by_xpath('(//input)[3]')
	cnf.send_keys(PW)

	btn = brows.find_element_by_xpath('//button')
	btn.click()

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return register_valid()
			break	

# direct automaton to visit
def visit_quote():
	brows.get(URL + "/quote.php")

# test quote with a valid symbol
def quote_valid():
	axis = 'quote_valid'
	print axis

	# setup
	visit_quote()

	# send the request
	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('NFLX')

	btn = brows.find_element_by_xpath('//button')
	btn.click()	

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return quote_valid()
			break

# test quote with an invalid symbol
def quote_invalid():
	axis = 'quote_invalid'
	print axis

	# set up
	visit_quote()

	# send the bogus request
	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('CS50')

	btn = brows.find_element_by_xpath('//button')
	btn.click()	

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return quote_invalid()
			break

# direct automaton to the buy pag
def visit_buy():
	brows.get(URL + "/buy.php")

def buy_invalid_sym():
	axis = 'buy_invalid_sym'
	print axis

	# setup 
	visit_buy()

	# send the bogus request
	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('CS50')

	q = brows.find_element_by_xpath('(//input)[2]')
	q.send_keys('10')

	btn = brows.find_element_by_xpath('//button')
	btn.click()	

		# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return buy_invalid_sym()
			break

def buy_invalid_quant():
	axis = 'buy_invalid_quant'
	print axis

	# setup
	visit_buy()

	# send the bogus request
	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('NFLX')

	q = brows.find_element_by_xpath('(//input)[2]')
	q.send_keys('-1')
	btn = brows.find_element_by_xpath('//button')
	btn.click()	
	raw_input('Finished running test 1 of 3. Press enter to continue.')

	# reset
	visit_buy()

	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('NFLX')

	q = brows.find_element_by_xpath('(//input)[2]')
	q.send_keys('2.5')
	btn = brows.find_element_by_xpath('//button')
	btn.click()	
	raw_input('Finished running test 2 of 3. Press enter to continue.')

	# reset
	visit_buy()

	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('NFLX')

	q = brows.find_element_by_xpath('(//input)[2]')
	q.send_keys('poopyface')

	# click
	btn = brows.find_element_by_xpath('//button')
	btn.click()	

	# get input to grade
	while True:
		input = raw_input('Test 3 of 3 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return buy_invalid_quant()
			break

	return (axis, get_grade(axis))

def buy_too_expensive():
	axis = 'buy_too_expensive'
	print axis

	# reset
	visit_buy()

	# send ticker
	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('NFLX')

	# send insane number of shares
	q = brows.find_element_by_xpath('(//input)[2]')
	q.send_keys('1000000000')

	# click
	btn = brows.find_element_by_xpath('//button')
	btn.click()	

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return buy_invalid_quant()
			break

def buy_valid():
	axis = 'buy_valid'
	print axis
	
	# reset
	visit_buy()

	# send ticker
	sym = brows.find_element_by_xpath('(//input)[1]')
	sym.send_keys('NFLX')

	# send insane number of shares
	q = brows.find_element_by_xpath('(//input)[2]')
	q.send_keys('15')

	btn = brows.find_element_by_xpath('//button')
	btn.click()	

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return buy_valid()
			break

def visit_sell():
	brows.get(URL + "/sell.php")


def sell_invalid():
	axis = 'sell_invalid'
	print axis

	# reset
	visit_sell()

	try:
		# send ticker
		sym = brows.find_element_by_xpath('(//input)[1]')
		sym.send_keys('CS50')

		btn = brows.find_element_by_xpath('//button')
		btn.click()

	except:
		print "No text field found. Assuming dropdown."
		print "If student used dropdown, verify that options make sense"
		raw_input('Press enter to test dropdown')

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return sell_invalid()
			break
	

def sell_valid():
	axis = 'sell_valid'
	print axis

	visit_sell()

	# check for an input form
	try:
		# send ticker
		sym = brows.find_element_by_xpath('(//input)[1]')
		sym.send_keys('NFLX')

		# click
		btn = brows.find_element_by_xpath('//button')
		btn.click()	

	except: 
		print "No input form found. Verify dropdown exists. "
		raw_input('Press enter to test dropdown.')

	try:
		select = Select(brows.find_element_by_xpath('//select'))
		select.select_by_index(1)

		# click
		btn = brows.find_element_by_xpath('//button')
		btn.click()	
	except Exception as e:
		print "Unknown error occured."
		print "Please check SELL functionality manually in the open firefox window."
		pass

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return sell_valid()
			break

def visit_history():
	brows.get(URL + "/history.php")

def history():
	axis = "history"
	print axis

	visit_history()

	print "Please do a visual inspection of history.php \
			to see if the previous transactions were captured."

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return history()
			break


def extra_feature():
	axis = 'extra_feature'
	print axis

	print "Please visually inspect the extra feature."

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return history()
			break

def require_login():
	axis = 'require_login'
	print axis

	logout()

	print "Please make sure the following requests do not allow user access."
	print "If working properly, you should not leave index.php"
	
	visit_buy()
	raw_input("Press enter for next. (1 of 4 done)")
	visit_sell()
	raw_input("Press enter for next. (2 of 4 done")
	visit_history()
	raw_input("Press enter for next. (3 of 4 done")
	visit_quote()

	# get input to grade
	while True:
		input = raw_input('Test 4 of 4 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return history()
			break

def validate_index():
	axis = 'validate_index'
	print axis

	login()
	html_source = brows.page_source
	brows.get('https://validator.w3.org/#validate_by_input')

	form = brows.find_element_by_xpath('//textarea[@id=\'fragment\']')
	form.send_keys(html_source)

	print "PRESS ENTER"

	# get input to grade
	while True:
		input = raw_input('Test 1 of 1 finished. Press g to enter score. Press r to rerun.')

		if input.lower() == 'g':
			return (axis,get_grade(axis))
		elif input.lower() == 'r':
			return history()
			break

def grade():

	gdict = {}

	# run register tests
	ax, g = register_empty_fields()
	gdict[ax] = g

	ax, g = register_mismatch()
	gdict[ax] = g

	ax, g = register_valid()
	gdict[ax] = g

	if g == 1:
		ax, g = register_duplicates()
		gdict[ax] = g
	else:
		print "VALID REGISTRATION FAILED"
		print "CONSIDER FIXING STUDENT CODE BEFORE CONTINUING"
		
	logout()
	login()
		
	# run quote test
	ax,g = quote_valid()
	gdict[ax] = g

	ax,g = quote_invalid()
	gdict[ax] = g

	# run buy tests
	ax, g = buy_too_expensive()
	gdict[ax] = g
	ax, g = buy_invalid_sym()
	gdict[ax] = g
	ax, g = buy_invalid_quant()
	gdict[ax] = g
	ax, g = buy_valid()
	gdict[ax] = g

	# run sell tests
	ax, g = sell_invalid()
	gdict[ax] = g

	ax, g = sell_valid()
	gdict[ax] = g

	# run history test
	ax, g = history()
	gdict[ax] = g

	# extra feature
	ax, g = extra_feature()
	gdict[ax] = g

	# run require login tests
	ax, g = require_login()
	gdict[ax] = g

	# validate dat html
	ax, g = validate_index()
	gdict[ax] = g

	# all done yay
	return gdict


while(True):

	cmd = raw_input('Please enter a command (g to grade, q to quit): ')
	if cmd.lower() == 'q':
		break
	elif cmd.lower() == 'g':
		brows.get('https://cs50.io')
		print "Set up server using runner.sh!"
		print "Enter name of current student below:"
		student = ''
		while student is '':
			student = raw_input('Student name:')
		gdict = grade()
		with open(student + '.json', 'w') as outfile:
			json.dump(gdict, outfile ,indent=4, separators=(',', ': '))
		print 'finished grading {%s}, looping' % student
	else:
		print "Bad command. Enter g for grade or q for quit."

