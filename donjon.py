# -*- coding: utf-8 -*-

# Donjon 1.0
# *Simple adventure game written as my first application while learning programming with Python.
#  It is a classic adventure game (think Colossal Cave Adventure or Zork) where you explore the
#  rooms of a dungeon and solve riddles along the way.
# *It features the following:
#	- random selection of riddles from a list at the beginning of a new game.
#	- save/resume feature (save the parameters of your progress in a text file, which allows you to resume the same game later on).
#       - inventory management, that allows you to pick up, carry and use items.

import os
import os.path
from random import randint
from random import choice

# create (riddle, solution) couples
red_riddle0 = """
What has rivers but no water,
forests but no trees,
and cities but no buildings?
"""
red_solution0 = "map"
red0 = [red_riddle0, red_solution0]

red_riddle1 = """
Who makes it, has no need of it.
Who buys it, has no use for it. 
Who uses it can neither see nor feel it. 
What is it?
"""
red_solution1 = "coffin"
red1 = [red_riddle1, red_solution1]

red_riddle2 = """
What always runs but never walks,
often murmurs but never talks,
has a bed but never sleeps,
has a mouth but never eats?
"""
red_solution2 = "river"
red2 = [red_riddle2, red_solution2]

green_riddle0 = """
A   C              JK
   B   DEFGHI     LMNOPQRSTUVWXYZ
"""
green_solution0 = "hijack"
green0 = [green_riddle0, green_solution0]

green_riddle1 ="""
    N
  U
S
"""
green_solution1 = "sunrise"
green1 = [green_riddle1, green_solution1]

green_riddle2 = "\nI<-->I"
green_solution2 = "eye to eye"
green2 = [green_riddle2, green_solution2]

blue_riddle0 = """
What would the eighth rung of the following ladder be?

1
11
21
1211
111221
312211
13112221
"""
blue_solution0 = "1113213211"
blue0 = [blue_riddle0, blue_solution0]

blue_riddle1 = """
5+3+2 = 151022
9+2+4 = 183652
8+6+3 = 482466
5+4+5 = 202541
7+2+5 = ?
"""
blue_solution1 = "143547"
blue1 = [blue_riddle1, blue_solution1]

blue_riddle2 ="""
1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
1 + 1 x 0 + 1 = ?
"""
blue_solution2 = "30" 
blue2 = [blue_riddle2, blue_solution2]


# group couples in lists
reds = [red0, red1, red2]
greens = [green0, green1, green2]
blues = [blue0, blue1, blue2]


# reset the parameters of the game, select riddles at random
def initialize():
	global red_riddle, red_solution, green_riddle, green_solution, blue_riddle, \
	blue_solution, reds, greens, blues, red_choice, green_choice, blue_choice, \
	red_passed, green_passed, blue_passed, bear_passed, music_passed, bridge_down, \
	door_unlocked, light, inventory 
	
	# choices picked as integers to be able to save them easily in a text file later on (as opposed
	# to using the choice function directly on the lists)
	red_choice = randint(0, len(reds)-1)	
	green_choice = randint(0, len(greens)-1) 
	blue_choice = randint(0, len(blues)-1)
	
	# unpacking the chosen (riddle, solution) couples
	red_riddle, red_solution = reds[red_choice]
	green_riddle, green_solution = greens[green_choice]
	blue_riddle, blue_solution = blues[blue_choice]
	
	# parameters of riddles completion status
	red_passed = False
	green_passed = False
	blue_passed = False
	bear_passed = False
	music_passed = False
	bridge_down = False
	door_unlocked = False
	light = False
	
	inventory = ['lamp', 'food']

	
def start():
	print "\n\n"
	print "                                 \316\316\316\316\316\316\316\316\316\316"
	print "                                 \316 \321\235Nj\235N \316"
	print "                                 \316\316\316\316\316\316\316\316\316\316\n\n\n"
	print "Welcome to \321\235Nj\235N!"
	
	
	print "Do you wish to read the playing instructions?"
	
	while True:
		answer = checked_input()
		
		if answer == "no":
			break
		elif answer == "yes":
			print "\n\316\316\316 INSTRUCTIONS \316\316\316"
			print "\nYour goal is to explore a dungeon and find the hidden treasure, while dodging traps"
			print "and solving riddles along the way.\n"
			print "\316 HOW TO PLAY? \316"
			print 'When prompted by ">", type in a ONE-word command and press ENTER.'
			print "Otherwise, just press ENTER without typing anything to continue."
			raw_input("")
			print "***IMPORTANT*** ALL COMMANDS MUST BE TYPED IN lower-case letters ***IMPORTANT***" 
			raw_input("")
			print "\316 DEFAULT COMMANDS \316\nIn each room of the dungeon, you have access to the following basic commands:"
			raw_input("")
			commands_list()
			raw_input("")
			print "\316 CONTEXT-BASED COMMANDS \316\nIn some specific contexts, you will have access to additional actions that may also be called"
			print "with ONE-word commands only. If the command is relevant in the room's context, it will be executed."
			print "For instance, you can type the name of an object or a character in order to interact with them."
			raw_input("")
			print "\316 ANSWERING QUESTIONS/RIDDLES \316\nYou may also be asked to answer specific questions or solve riddles from time to time." 
			print "In such situations, the one-word-command rule does not apply."
			print "Just type your answer in the most straightforward way you can think of.\n"
			raw_input("")
			print "Alright, you are ready to go. Good luck!"
			raw_input("")
			break
		else:
			print "Please answer the question."
		
	print "\n                       \316\316\316\316\316\316\316\316\316\316\316\316\316\316\316\316\
\316\316\316\316\316\316\316\316\316\316\316\316\316\n\n"
	print "YOU ARE stepping inside the dungeon through a heavy wooden gate. The gate shuts behind you."
	print "There is no more going back."
	
	initialize()
	entrance_hall()

	
def commands_list():
	print "**List of default commands**"
	print 'n -> go North.'
	print 's -> go South.'
	print 'e -> go East.'
	print 'w -> go West.'
	print 'inventory -> check your inventory.'
	print 'save -> save your progression.'
	print 'resume -> resume a game that has previously been saved.'
	print 'quit -> exit the game. Make sure you save your progression beforehand.'
	print 'help -> show the list of basic commands.'
		
	
def dead(why):
	print why
	print "Game Over!"
	raw_input("")
	exit(0)

 # make sure the player's input is one-word long
def checked_input():
	while True:
		input = raw_input("> ").strip(" ")
		if input == "" or len(input.split(" ")) > 1:
			print "Please type a one-word command."
		else:
			break
	return input
	
	
# save all the parameters of the current game in a file whose name is asked to the user, under dir "../donjon_saved_games"
def save():
	global red_choice, green_choice, blue_choice, red_passed, green_passed, blue_passed, bear_passed, \
			music_passed, bridge_down, door_unlocked, light, inventory, location
		
	parameters = [red_choice, green_choice, blue_choice, red_passed, 
					green_passed, blue_passed, bear_passed, music_passed, bridge_down, \
					door_unlocked, light, inventory, location]
	
	print "Choose a name under which you want to save this game:"
	game_name = raw_input("> ")
	
	path = './donjon_saved_games'
	
	# create the directory if it does not exists, creates the file and save the parameters
	if not os.path.exists(path):
		os.makedirs(path)
		
		game_file = open("%s/%s.txt" % (path, game_name), 'w')
	
		for p in parameters:
			if p == inventory: # because inventory is a list, it has to be "joined" in a single string
				game_file.write("%s\n" % "_".join(p))		
			else:
				game_file.write("%s\n" % p)
				
		game_file.close()
		print "Game saved"
	# if the game name already exists, ask whether the user wants to replace it
	elif "%s.txt" % game_name in [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]:
		print "A game is already saved under this name. Do you want to replace it?"
		
		while True:
			yesno = raw_input("> ")
			
			if yesno == "yes":			
				game_file = open("%s/%s.txt" % (path, game_name), 'w')
		
				for p in parameters:
					if p == inventory: # because inventory is a list, it has to be "joined" in a single string
						game_file.write("%s\n" % "_".join(p))		
					else:
						game_file.write("%s\n" % p)
				
				game_file.close()
				print "Game saved"
				break
			elif yesno == "no":
				print "Game not saved."
				break
			else:
				print "Please answer the question."
	else:
		game_file = open("%s/%s.txt" % (path, game_name), 'w')
		
		for p in parameters:
			if p == inventory: # because inventory is a list, it has to be "joined" in a single string
				game_file.write("%s\n" % "_".join(p))		
			else:
				game_file.write("%s\n" % p)
		
		game_file.close()
		print "Game saved"
		
def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False
    else:
         raise ValueError	
		
		
def resume(): # check that there are saved games in the directory, ask the player to choose one of them,
              # open the pertaining file and read it to restore the paramaters of the chosen game
	global red_riddle, red_solution, green_riddle, green_solution, blue_riddle, \
			blue_solution, reds, greens, blues, red_passed, green_passed, blue_passed, \
			bear_passed, music_passed, bridge_down, door_unlocked, light, inventory, location
	
	path = './donjon_saved_games'
	
	# check that the directory exists and list all the files within
	file_list = []
	
	if os.path.exists(path):
		file_list = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
	else:
		pass
	
	# list text files only, by their names without the ".txt" extension
	text_list = []
	for file in file_list:
		if file.split('.')[1] == "txt":
			text_list.append(file.split('.')[0])
	
	# check that the list is not empty and restore the game chosen by the player from a list
	if text_list == []:
		print "There is currently no game saved."
	else:
		print "Choose the game you wish to resume:"
	
		for name in text_list:
			print "\t* %s" % name
			
		game = raw_input("> ")
		
		if game in text_list:
			game_file = open("%s/%s.txt" % (path, game))
			
			# restore all the parameters
			red_riddle, red_solution = reds[int(game_file.readline().strip('\n'))]
			green_riddle, green_solution = greens[int(game_file.readline().strip('\n'))]
			blue_riddle, blue_solution = blues[int(game_file.readline().strip('\n'))]
			red_passed = str_to_bool(game_file.readline().strip('\n'))   # convert string to Boolean value
			green_passed = str_to_bool(game_file.readline().strip('\n'))
			blue_passed = str_to_bool(game_file.readline().strip('\n'))  
			bear_passed = str_to_bool(game_file.readline().strip('\n'))
			music_passed = str_to_bool(game_file.readline().strip('\n'))
			bridge_down = str_to_bool(game_file.readline().strip('\n'))
			door_unlocked = str_to_bool(game_file.readline().strip('\n'))
			light = str_to_bool(game_file.readline().strip('\n'))
			inventory = (game_file.readline().strip('\n')).split('_')    # rebuild the list from the string
			location = game_file.readline().strip('\n')
			
			game_file.close()
			
			# send the player back to the last room visited	
			if location == "entrance":
				entrance_hall()
			elif location == "red":
				red_room()
			elif location == "green":
				green_room()
			elif location == "blue":
				blue_room()
			elif location == "key":
				key_room()
			elif location == "flute":
				flute_room()
			elif location == "tunnel":
				tunnel()
			elif location == "bear":
				bear_room()
			elif location == "window":
				window_room()
			elif location == "music":
				music_room()
			elif location == "corridor":
				corridor()
			elif location == "pit":
				pit_room()
			elif location == "lever":
				lever_room()
			elif location == "dark":
				dark_room()
			elif location == "treasure":
				treasure_room()
			else:
				pass				
		else:
			print "There is no game saved under this name."

			
def quit_game():
	while True:	
		print "Are you sure you want to quit?"
		
		choice = raw_input("> ")
		
		if choice == "yes":
			exit(0)
		elif choice == "no":		
			break
		else:
			print "Please answer the question."
			
			
def show_inventory():
	global inventory
	
	print "You are carrying the following items:\n"
	
	for item in inventory:
		print "\t* %s" % item
		
	

	
def entrance_hall():
	global location
	location = "entrance"
	
	print "\nYou are standing in the entrance hall."
	print "There is a door to the North, a door to the East and a door to the West."
	
	while True:
		action = checked_input()
		
		if action == "n":
			red_room()			
		elif action == "s":
			print "The entrance gate is shut, you cannot exit the dungeon."
		elif action == "e":
			green_room()	
		elif action =="w":
			blue_room()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()
		else:
			print "Nothing happens."

			
def dwarf(riddle, solution, color_passed):
	print "\nYou approach the dwarf."
	print "He asks you the following enigma:"
	print riddle
				
	answer = raw_input("> ")
	
	if solution in answer:
		print "Correct, the dwarf moves out of the way."
		color_passed = True
	else:
		print "This is incorrect, the dwarf turns his attention off you."
		print "But he is still blocking the way."
		
	return color_passed
		
	
			
def red_room():
	global red_passed, red_riddle, red_solution, location
	location = "red"
	
	print "\nYou are now standing in a simple square room."
	print "There is a red dwarf in here."
	
	if red_passed == False:	
		print "You can see a door to the South and a door to the North."
		print "But the dwarf is blocking the way to the latter and will not let you pass."
	else:	
		print "He is now sitting aside."
		print "There is a door to the South and a door to the North."

	while True:	
		action = checked_input()
		
		if action in ["dwarf", "talk"]:
			red_passed = dwarf(red_riddle, red_solution, red_passed)
		elif action == "n" and red_passed == False:
			print "The dwarf is in the way."
		elif action == "n" and red_passed == True:	
			tunnel()
		elif action == "s":
			entrance_hall()
		elif action == "e":
			print "There is nothing in this direction."
		elif action =="w":
			print "There is nothing in this direction."
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()		
		else:
			print "Nothing happens."

			
def green_room():
	global green_passed, green_riddle, green_solution, location
	location = "green"
	
	print "\nYou are now standing in a simple square room."
	print "There is a green dwarf in here."

	if green_passed == False:	
		print "You can see a door to the West and a staircase that goes up to the North."
		print "But the dwarf is blocking the way to the latter and will not let you pass."
	else:	
		print "He is now sitting aside."
		print "There is a door to the West and a staircase that goes up to the North."

	while True:	
		action = checked_input()
		
		if action in ["dwarf", "talk"]:
			green_passed = dwarf(green_riddle, green_solution, green_passed)
		elif action == "n" and green_passed == False:
			print "The dwarf is in the way."
		elif action == "n" and green_passed == True:	
			flute_room()
		elif action == "s":
			print "There is nothing in this direction."
		elif action == "e":
			print "There is nothing in this direction."
		elif action =="w":
			entrance_hall()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()		
		else:
			print "Nothing happens."
				

def blue_room():
	global blue_passed, blue_riddle, blue_solution, location
	location = "blue"
	
	print "\nYou are now standing in a simple square room."
	print "There is a blue dwarf in here."

	if blue_passed == False:	
		print "You can see a door to the East and a door to the West."
		print "But the dwarf is blocking the way to the latter and will not let you pass."
	else:	
		print "He is now sitting aside."
		print "There is a door to the East and a door to the West."
	
	while True:
		action = checked_input()
		
		if action in ["dwarf", "talk"]:
			blue_passed = dwarf(blue_riddle, blue_solution, blue_passed)
		elif action == "n":
			print "There is nothing in this direction."
		elif action == "s":
			print "There is nothing in this direction."
		elif action == "e":
			entrance_hall()
		elif action == "w" and blue_passed == False:
			print "The dwarf is in the way."
		elif action == "w" and blue_passed == True:	
			key_room()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()		
		else:
			print "Nothing happens."
			
def key_room():
	global inventory, location
	location = "key"
	
	print "\nYou are in a tiny room, which looks more like a walk-in closet."
	print "A small chest is sitting on a two-foot-tall stone base at the back of the room."
	print "There is only one door, to the East."

	while True:	
		action = checked_input()
		
		if "open" in action or "chest" in action:
			print "You walk up to the chest and open it."
				
			if not("key" in inventory):
				print "Inside is a large key. You pick it up and put it in your pouch."
				inventory.append("key")
			else:
				print "The chest is empty."
					
		elif action == "n":
			print "You bump into a wall, you cannot go this way."				
		elif action == "s":
			print "You bump into a wall, you cannot go this way."	
		elif action == "w":
			print "You bump into a wall, you cannot go this way."
		elif action == "e":
			blue_room()		
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()			
		else:
			print "Nothing happens."
			

def flute_room():
	global inventory, location
	location = "flute"
	
	print "\nYou are standing in a small room furnished with a single table."
	
	if not ("flute" in inventory):
		print "There is a flute on the table."
	else:
		pass
	print "You can only see one exit: a staircase that goes down to the South."	

	while True:
		action = checked_input()
		
		if action in ["flute", "take", "play"] and not ("flute" in inventory):
			print "You pick up the flute and play a few notes. You are not a bad player!"
			raw_input("")
			print "You put the flute in your pouch."
			inventory.append("flute")
		elif action == "n":
			print "There is nothing in this direction."	
		elif action == "s":
			green_room()	
		elif action == "w":
			print "There is nothing in this direction."
		elif action == "e":
			print "There is nothing in this direction."
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()			
		else:
			print "Nothing happens."
		
def tunnel():
	global location
	location = "tunnel"
	
	print "\nYou have entered some sort of tunnel."
	print "You can see a door to the West and a door to the South."
	
	while True:
		action = checked_input()
		
		if action == "n":
			print "There is nothing in this direction."	
		elif action == "s":
			red_room()	
		elif action == "w":
			bear_room()
		elif action == "e":
			print "There is nothing in this direction."
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()			
		else:
			print "Nothing happens."
			
def bear_room():
	global location, inventory, bear_passed
	location = "bear"
	
	print "\nYou have stepped in a medium-sized room with a staunch animal smell."
	print "It comes from a massive grizzly bear."
	print "You can see a door to the South, a door to the East and a door to the North."
	
	if bear_passed == False:
		print "The bear is lying asleep in front of the latter."
	else:
		print "The bear is sleeping quietly out of the way."
	
	while True:
		action = checked_input()
		
		if ("food" in action or "feed" in action) and "food" in inventory:
			print "You throw your food at the bear, away from the door."
			print "Enticed by the smell, the bear wakes up and moves towards your gift."
			print "After eating all of it, he falls asleep again, removed from the door."
			del inventory[1]
			bear_passed = True
		elif action in ["attack", "call", "shout", "scream", "pat", "stroke", "sing", "touch", "kick", "hit",
							"caress", "tackle","jump", "taunt", "punch", "whistle", "scream"] \
							or action == "flute" and "flute" in inventory:
			dead("Big mistake, the bear wakes up angry and eats your face off.")				
		elif "bear" in action:
			print "What do you want to do with the bear?"
			
			choice = checked_input()
			
			if ("food" in choice or "feed" in choice) and "food" in inventory:
				print "You throw your food at the bear, away from the door."
				print "Enticed by the smell, the bear wakes up and moves towards your gift."
				print "After eating all of it, he falls asleep again, removed from the door."
				del inventory[1]
				bear_passed = True
			
			elif choice in ["attack", "call", "shout", "scream", "pat", "stroke", "sing", "touch", "kick", "hit",
							"caress", "tackle","jump", "taunt", "punch", "whistle", "scream", "cuddle"] \
							or choice == "flute" and "flute" in inventory:
				dead("Big mistake, the bear wakes up angry and eats your face off.")
			else:
				print "Nothing happens, the bear is still sleeping deeply."
				
		elif action == "n":
			
			if bear_passed == True:
				music_room()
			else:
				print "The bear is in the way."
		elif action == "n":
			music_room()
		elif action == "s":
			window_room()	
		elif action == "w":
			print "There is nowhere to go in this direction."
		elif action == "e":
			tunnel()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()			
		else:
			print "Nothing happens."


def window_room():
	global location
	location = "window"
	
	print "\nYou are standing in an empty room wih a barred window to the West, onto the outside."
	print "It looks dark and gloomy out there."
	print "There is a door to the North."

	while True:
		action = checked_input()
		
		if "window" in action or action == "w":
			print "The bars look very strong, there is no way you can go through."
		elif action == "n":
			bear_room()
		elif action == "s":
			print "You cannot go this way."
		elif action == "e":
			print "You cannot go this way."
		elif action == "zyxx":
			print "\nSWWWIFFF!!"
			dark_room()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()			
		else:
			print "Nothing happens."

def music_room():
	global inventory, music_passed, location
	location = "music"
	
	print "\nYou are in a magnificent room with two rows of big white columns."
	print "There is an altar at the center."
	
	if music_passed == False:
		print "You can see a massive marble door to the East, which is closed, and a door to the South."
	else:
		print "You can see a massive marble door to the East, which is now open, and a door to the South."
		
	print "The following music notes are carved on the altar:\n\n\t\tdo-mi-re-sol-do-fa\n"
	
	while True:
		action = checked_input()
		
		if "flute" in action and "flute" in inventory:
			print "What do you want to play with the flute?"
		
			melody = raw_input("> ")
			
			print 'You take the flute out of your pouch and play "%s"' % melody
			
			if melody == "do-mi-re-sol-do-fa" and music_passed == False:
				print "The marble door starts moving on its own... It is now fully open."
				music_passed = True
			else:
				print "Nothing happens."

		elif action == "n":				
			print "There is nothing in this direction."		
		elif action == "s":
			bear_room()
		elif action == "e" and music_passed == True:
			corridor()
		elif action == "e":
			print "The marble door is too heavy, you cannot open it."		
		elif action =="w":
			print "There is nothing in this direction."
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()
		else:
			print "Nothing happens."
			

def corridor():
	global location
	location = "corridor"
	
	print "You have entered a long and narrow corridor."
	print "There is a door at each end: one to the West and on the East."

	while True:
		action = checked_input()
		
		if action == "n":				
			print "This does not lead anywhere."
		elif action == "s":
			print "This does not lead anywhere."
		elif action == "e":
			pit_room()
		elif action =="w":
			music_room()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()
		else:
			print "Nothing happens."
				
				
def pit_room():
	global location, bridge_down, door_unlocked, inventory
	location = "pit"
	
	print "\nYou are in a room split in two by a wide pit, with deadly spikes at the bottom."
	print "There is a door to the West, a door the East and a door to the North."
	print "The Northern door is on the opposite side of the pit from the two others."

	if bridge_down == False:
		print "There is a drawbridge linking both sides, but it is currently up."
	else:
		print "There is a drawbridge linking both sides, and it is currently down."
		print "The Eastern door is closed."

	while True:
		action = checked_input()
		
		if action == "n" and bridge_down == False:
			print "The drawbridge is up, you cannot cross the pit."
		elif action == "n" and bridge_down == True:
				print "You cross the drawbridge and stop in front of the door."
				
				if door_unlocked == False:
					print "It is locked and has a large keyhole."
					raw_input("")
					
					if "key" in inventory:
						print "You try to insert the key that you are carrying. It fits."
						print "The door is now unlocked."
						print "You pull it open and step through it."
						door_unlocked = True
						raw_input("")
						treasure_room()
					else:
						print "You will not get through without the key."
						
				else:
					print "It is open, you step through it."
					raw_input("")
					treasure_room()
				
		elif action == "s":
			print "There is nowhere to go in this direction."
		elif action == "e" and bridge_down == False:
			lever_room()
		elif action == "e" and bridge_down == True:
			print "The door is closed and you cannot lift it open."
		elif action =="w":
			corridor()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()
		else:
			print "Nothing happens."

			
def lever_room():
	global location, bridge_down
	location = "lever"
	
	print "\nYou are in chamber with a lever at the center."
	print "There is a room to the West and a room to the East."
		
	while True:
		action = checked_input()
		
		if action in ["lever", "pull"] and bridge_down == False:
			print "You pull the lever."
			print "You can hear a the drawbridge moving in the room next door."
			raw_input("")
			print "You turn around to go have a look, but the Western door drops closed suddenly."
			bridge_down = True
		elif action in ["lever", "pull"] and bridge_down == True:
			print "You pull the lever."
			print "You can hear the drawbridge moving in the room next door."
			raw_input("")
			print "The Western door is lifted open."
			bridge_down = False
		elif action == "n":
			print "There is nothing there."
		elif action == "s":
			print "There is nowhere to go in this direction."
		elif action == "e":
			dark_room()
		elif action =="w":
			
			if bridge_down == True:
				print "The door is way too heavy for you to lift it open."
			else:
				pit_room()
				
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()
		else:
			print "Nothing happens."
	

def dark_room():
	global location, light
	location = "dark"
	
	print "\nYou are standing in a small alcove."
	
	if light == False:
		print "It is very dark and you cannot really make out the details of this room."
	else:
		print "Something is carved on one of the walls:"
		print "\n\t\tWord of Power:\n\n\t\t      zyxx\n"

	while True:
		action = checked_input()
		
		if "lamp" in action:
		
			if light == False:
				light = True
				print "You have lit the lamp up."
				raw_input("")
				print "Something is carved on one of the walls:"
				print "\n\t\tWord of Power:\n\n\t\t      zyxx\n"
			else:
				light = False
				print "You have switched off the lamp."
				
		elif action == "zyxx":
			print "\nSWWWIFFF!!"
			window_room()
		elif action == "n":
			print "You cannot go in this direction."
		elif action == "s":
			print "There is nowhere to go in this direction."
		elif action == "e":
			print "You bump into a wall."
			raw_injput("")
		elif action =="w":
			lever_room()
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()
		else:
			print "Nothing happens."
			

def treasure_room():
	global location
	location = "treasure"
	
	print "\nYou are in the treasure room."
	print "A large chest is set on a stone platform at the North."
	print "It is open and you can see the precious gems sparkling inside."
	print "But a fierce dragon is standing between you and the treasure."
		
	while True:
		action = checked_input()
		
		if action in ["dragon", "talk"]:
			print "You approach the dragon."
			print "He will only let you put your hands on the chest if you can\nbeat him at a battle of Rock-Paper-Scissors."
			raw_input("")
			
			if rps(3):
				print "The treasure is yours. Well done!"
				print "\nThanks for playing \321\235Nj\235N"
				raw_input("")
				exit(0)
			else:
				print "Come back when you are stronger!"
				
		elif action == "n":
			print "You cannot get to the treasure, the Dragon is in the way."
		elif action == "s":
			pit_room()
		elif action == "e":
			print "There is nowhere to go in this direction."
		elif action =="w":
			print "There is nowhere to go in this direction."
		elif action == "inventory":
			show_inventory()
		elif action == "save":
			save()
		elif action == "resume":
			resume()
		elif action == "quit":
			quit_game()
		elif action == "help":
			commands_list()
		else:
			print "Nothing happens."

			
def rps(number):
	win = False
	
	print "BATTLE RULES"
	print '* When asked for your choice, type:\n\n\t "r" for Rock, "p" for Paper or "s" for Scissors.'
	raw_input("")
	print "* The first opponent to win %s rounds wins the challenge." % number
	raw_input("")
	
	count = 1
	player = 0
	dragon = 0
	rpc = ('r', 'p', 's')
	rpc_names = ("Rock", "Paper" , "Scissors")
	
	while dragon < number and player < number:
		print "\n*** Round %s ***" % count
		count += 1
		
		while True:
			print "Your choice:"
			player_choice = checked_input()
			
			if player_choice in rpc:
				break
			else:
				print "Please choose r, p ou c."
		
		dragon_choice = choice(rpc)
		print "You have chosen:\n  %s\n" % rpc_names[rpc.index(player_choice)]
		print "The Dragon's choice is:\n  %s\n" % rpc_names[rpc.index(dragon_choice)]
		
		if player_choice == dragon_choice:
			print "It is a draw."
		elif (player_choice == "r" and dragon_choice == "s") or (player_choice == "p" and dragon_choice == "r") or (player_choice == "s" and dragon_choice == "p"):		
			print "You win this round."
			player += 1
			dragon += 0
		elif (player_choice == "s" and dragon_choice == "r")or (player_choice == "r" and dragon_choice == "p") 	or (player_choice == "p" and dragon_choice == "s"):
			print "The dragon wins this round."
			player += 0
			dragon += 1
			
			
		print "You: %s / Dragon: %s" % (player, dragon)
		raw_input("")
		
	if dragon == number:
		print "The dragon wins the challenge."
		raw_input("")
		
	else:
		print "You win the challenge."
		win = True
		raw_input("")
		
	return win
	
start()
