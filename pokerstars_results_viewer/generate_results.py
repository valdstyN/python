#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi
import os
from itertools import islice
import re

def pause():
    programPause = input("Press the <ENTER> key to continue...")

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
    	fullPath = os.path.join(dirName, entry)
    	allFiles.append(fullPath)
    return allFiles

def main():
	dirName = 'C:\\Users\\valdstyN\\AppData\\Local\\PokerStars.BE\\TournSummary\\valdstyNz';
  # replace with your windows user and local PokerStarts folder
	listOfFiles = getListOfFiles(dirName)

	var_loss = 0.0
	var_win = 0.0
	var_nbTourney = 0

	with open('results.html', 'w') as the_file:
   		the_file.write('<!doctype html>\n')
   		the_file.write('<html>\n')
   		the_file.write('<head></head>\n')
   		the_file.write('<style>tr,td{border:1px solid #BBB} *{font-size:12px; font-family:verdana;}</style><body>\n')
   		the_file.write('<table><tr><td>Tournament</td><td>Date</td><td>Prize Pool</td>\n')
   		the_file.write('<td>Buy-In</td><td>Placement</td><td>Win/Loss</td><td>Profit</td></tr>\n')

	for elem in listOfFiles:
		e = ""
		# print(elem)
		with open(elem, encoding="utf8") as f:
			# print(elem)
			for x in f:
				e = e + x

			with open('results.html', 'a') as the_file:
				the_file.write('<tr>')

			var_nbTourney = var_nbTourney + 1
			var_buyin = re.findall("Buy-In: \$(\d{1,2}\.\d{2})\/\$(\d{1,2}\.\d{2}) (...)",e)
			var_players = re.findall("(\d{1,5}) players",e)
			var_placement = re.findall("You finished in (\d{1,5}).. place",e)
			var_gains = re.findall("valdstyNz \(Belgium\)\, \$(\d{1,5}\.\d{2})",e)
			var_ticket = 0
			var_date = re.findall("started (.+) CET",e)
			var_tournament = re.findall("T\d{1,10}(.+)\.txt",elem)
			var_prize = re.findall("Pool: \$(\d{1,5}\.?\d{0,2})",e)

			with open('results.html', 'a') as the_file:
				the_file.write('<td>'+str(var_tournament[0])+'</td>')

			with open('results.html', 'a') as the_file:
				the_file.write('<td>'+str(var_date[0])+'</td>')

			with open('results.html', 'a') as the_file:
				the_file.write('<td>'+str(var_prize[0])+' USD</td>')

			if len(var_gains) == 0:
				var_gains = "0"
			try:
				with open('results.html', 'a') as the_file:
					the_file.write('<td>'+str(float(var_buyin[0][0])+float(var_buyin[0][1]))+ " " + var_buyin[0][2]+'</td>')
			except:
				with open('results.html', 'a') as the_file:
					the_file.write('<td>Ticket</td>')
				var_ticket = 1

			try:
				with open('results.html', 'a') as the_file:
					the_file.write('<td>'+var_placement[0] + "/" + var_players[0]+'</td>')
			except:
				with open('results.html', 'a') as the_file:
					the_file.write('<td>Early exit</td>')

			if var_gains == "0":
				if var_ticket == 0:
					with open('results.html', 'a') as the_file:
						the_file.write("<td>-" + str(float(var_buyin[0][0])+float(var_buyin[0][1])) +' USD</td>')
						the_file.write("<td></td>")
					var_loss =  var_loss + float(var_buyin[0][0]) + float(var_buyin[0][1])

			else:
				with open('results.html', 'a') as the_file:
					the_file.write("<td>+" + str(var_gains[0])+' USD</td>')

				if var_ticket == 0:
					with open('results.html', 'a') as the_file:
						the_file.write("<td>" + str(float(var_gains[0])-float(var_buyin[0][0])-float(var_buyin[0][1]))+' USD</td>')
				else:
					with open('results.html', 'a') as the_file:
						the_file.write("<td>" + str(var_gains[0])+' USD</td>')
				var_win = var_win + float(var_gains[0])

			with open('results.html', 'a') as the_file:
				the_file.write('</tr>')

	with open('results.html', 'a') as the_file:
		the_file.write('</table><br><br>')
		the_file.write('Number of tournaments played: ' + str(var_nbTourney) + '<br>')
		the_file.write("Total gains: +" + str(round(var_win,2)) + " USD" + '<br>')
		the_file.write("Total losses: -" + str(round(var_loss,2)) + " USD" + '<br>')
		the_file.write("Total profit: " + str(round(var_win,2)-round(var_loss,2)) + " USD" + '<br>')
		the_file.write('</body>\n')
		the_file.write('</html>\n')


if __name__ == '__main__':
    main()

# pause()
