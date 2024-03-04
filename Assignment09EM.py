from os import system, path, get_terminal_size
window_width = get_terminal_size().columns

from datetime import date
today = date.today().strftime("%B %d, %Y")

words = []

star_border = "*"*135

states = []

candies = []

def header():
	system("cls||clear")
	print("\n\n"+"{0} {1}". format("Edin Mehanovic CIS125 Structure and Logic", today).center(window_width)+"\n\n")
	
def center(phrase):
	phrase = str(phrase)
	return ('%s'.center(get_terminal_size().columns-len(phrase))%phrase)
	
def formating_process(phrase):
	print(center("*  {0:<8}  {1:<27}  {2:<10}  {3:<27}  {4:<10}  {5:<27}  {6:<10}  *".format(phrase[0],phrase[1],phrase[2],phrase[3],phrase[4],phrase[5],phrase[6])))
	
def input_center (phrase):
	return input("".ljust((window_width - len(phrase))//2)+ phrase)	
	
def read_file(my_file):
	global titles, states, candies
	states = []
	candies = []
	first = True
	file = open(my_file)
	for line in file: 
		line=line.strip()
		words = line.split(",")
		if first:
			titles = words
			first = False
		else:
			states += [words[0].strip()]
			candies += [words]
	file.close()
	
def file_check(my_file):
	if path.isfile(my_file):
		read_file(my_file)
	else:
		print((my_file +" does not exist!!!").center(window_width))
	
def candy_input():
	global state_input, failed_input
	state_input = ""
	center_string = ""
	for i in range(len(states)):
		if i % 9 == 0:
			print(center(center_string))
			center_string = ""
		center_string +="{0:^4}".format(states[i])
	i += 1
	while i % 9 != 0:
		center_string +="{0:^4}".format("")
		i += 1
	print(center(center_string))
	center_string = ""
	print("\n\n")
	while not state_input in states:
		state_input = (input_center("Enter one of the sets of intials from above: "))
		state_input = state_input.upper()
		if not state_input in states:
			failed_input = (state_input + " is an invalid entry \n\n")
			print("\n\n")
			print(center(failed_input))
	print("\n\n")
	
def candy_process():
	global f_state, final_list, percent_list
	
	one_total = 0
	two_total = 0
	three_total = 0
	
	for y in candies:
		if state_input == y[0].strip():
			f_state = y
			break
	
	for y in candies:
		if f_state[1] == y[1]:
			one_total += int(y[2])
		if f_state[1] == y[3]:
			one_total +=int(y[4])
		if f_state[1] == y[5]:
			one_total +=int(y[6])
		if f_state[3] == y[1]: 
			two_total +=int(y[2])
		if f_state[3] == y[3]:
			two_total +=int(y[4])
		if f_state[3] == y[5]: 
			two_total +=int(y[6])
		if f_state[5] == y[1]: 
			three_total +=int(y[2])
		if f_state[5] == y[3]: 
			three_total +=int(y[4])
		if f_state[5] == y[5]:
			three_total +=int(y[6])
	
	final_list = ["Total", f_state[1],"{0:>10,}".format(one_total), f_state[3],"{0:>10,}".format(two_total),f_state[5],"{0:>10,}".format(three_total)]

	percentage_one = 0
	percentage_two = 0
	percentage_three = 0
	
	percentage_one = int(f_state[2])/one_total
	percentage_two = int(f_state[4])/two_total
	percentage_three = int(f_state[6])/three_total
	
	percent_list = ["Total",f_state[1],"{0:>10.2%}".format(percentage_one),f_state[3],"{0:>10.2%}".format(percentage_two),f_state[5],"{0:>10.2%}".format(percentage_three)]
	
	f_state = [f_state[0], f_state[1],"{0:>10,}".format(int(f_state[2])), f_state[3],"{0:>10,}".format(int(f_state[4])),f_state[5],"{0:>10,}".format(int(f_state[6]))]
	
def candy_output():
	equals_border = ["="*6,"="*27,"="*10,"="*27,"="*10,"="*27,"="*10]
	space_between_border = ["","","","","","",""]
	
	print(center("List of States as well as the District of Columbia Abbreviations: \n\n"))
	print(center(star_border))
	formating_process(space_between_border)
	formating_process(titles)
	formating_process(equals_border)
	formating_process(f_state)
	formating_process(final_list)
	formating_process(equals_border)
	formating_process(percent_list)
	formating_process(space_between_border)	
	print(center(star_border))
	print("\n")
	
def file_fun():
	file_check("Candies2021.csv")
	
def main(repeat = "y"):
	global states, titles
	if repeat == 'n' or repeat == 'N':
		print("\n\n\n")
		print(center('''"Have a nice day!"'''))
		input_center("Press <Enter> to continue... ")
		return
	elif repeat == "y" or repeat == "Y":
		header()
		file_fun()		
		candy_input()
		candy_process()
		candy_output()
		repeat = input_center("Would you like to run again (Y/N): ")
		main(repeat)
	else:
		print("\n\n")
		print(center(repeat+" is an invalid entry\n\n"))
		repeat = input_center("Would you like to run again (Y/N): ")
		main(repeat)
	
main()


# Edin Mehanovic
# What I found challenging was the whole setting up of the 'read_file' function. As well as the error-correcting in the input, the how to do the process for this assignment. 
# I now have a better understanding of how lists work and how to use them properly. I've learned how to use a dataset in excel, which I think will heavily help me down my future career pathway. 