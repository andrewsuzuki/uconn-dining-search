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

foods = sys.argv
foods.pop(0) # get rid of script name
if not foods:
	print("You didn't enter any foods, or a .foods file.")
	sys.exit(0)

if foods[0].endswith('.foods'):
	foodsfile = open(foods[0])
	foods.pop(0) # get rid of .foods file name
	foods = foods + foodsfile.read().splitlines() # merge lines in file with foods list

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
