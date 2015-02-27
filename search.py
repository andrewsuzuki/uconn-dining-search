import sys
import urllib.request
import pprint

print("""
                                        _ _       _                                           _     
  _   _  ___ ___  _ __  _ __         __| (_)_ __ (_)_ __   __ _       ___  ___  __ _ _ __ ___| |__  
 | | | |/ __/ _ \| '_ \| '_ \ _____ / _` | | '_ \| | '_ \ / _` |_____/ __|/ _ \/ _` | '__/ __| '_ \ 
 | |_| | (_| (_) | | | | | | |_____| (_| | | | | | | | | | (_| |_____\__ \  __/ (_| | | | (__| | | |
  \__,_|\___\___/|_| |_|_| |_|      \__,_|_|_| |_|_|_| |_|\__, |     |___/\___|\__,_|_|  \___|_| |_|
                                                          |___/                                     
    by: Andrew Suzuki

""")

args = sys.argv
args.pop(0) # get rid of script name

foods = []

for arg in args:
	if arg.endswith('.foods'):
		try:
			foodsfile = open(arg)
			foods += foodsfile.read().splitlines() # merge lines in file with foods list
		except Exception:
			print("File " + arg + " could not be opened.")
	else:
		foods.append(arg)

if not foods:
	print("You didn't enter any foods.")
	sys.exit(0)

foods = [food.lower() for food in foods]
foods = list(set(foods)) # remove duplicates
print("Searching for: " + ", ".join(foods))
print("")

diningHalls = {
	'03': ('Buckley', 'Buckley+Dining+Hall'),
	'42': ('Towers (Gelfenbein Commons)', 'Gelfenbien+Commons+%26+Halal'),
	'05': ('McMahon', 'McMahon+Dining+Hall'),
	'07': ('North', 'North+Campus+Dining+Hall'),
	'15': ('Northwest', 'Northwest+Marketplace'),
	'06': ('Putnam', 'Putnam+Dining+Hall'),
	'16': ('South', 'South+Campus+Marketplace'),
	'01': ('Whitney','Whitney+Dining+Hall'),
}

base = 'http://nutritionanalysis.dds.uconn.edu/shortmenu.asp?sName=UCONN+Dining+Services&locationNum={0}&locationName={1}&naFlag=1'

for num in diningHalls:
	print(diningHalls[num][0])
	
	url = base.format(num, diningHalls[num][1])
	
	try:
		response = urllib.request.urlopen(url)
	except Exception:
		print("URL couldn't be loaded.")
		continue

	data = response.read() 
	text = data.decode('ISO-8859-1').lower()

	for food in foods:
		if food in text:
			print("* " + food + " is being served today.")

	print("")
