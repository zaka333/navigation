# TO TEST setHeuristic FUNCTION
#
__authors__='TO_BE_FILLED'
__group__='DL01'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

import os
import sys

from SearchAlgorithm import *

from SubwayMap import *

def main():
    #------------------------------------------------------------------#
    city_string="Lyon_smallCity"
    #read file
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Stations.txt")
    stationList=readStationInformation(filename)
    #read adjacency matrix
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Connections.txt")
    adjacency=readCostTable(filename)

    #Real TIME cost table
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Time.txt")
    timeStations = readCostTable(filename)
    setNextStations(stationList, timeStations)

    # CITY information
    # velocity
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"InfoVelocity.txt")
    infoVelocity = readInformation(filename)
    # Transfers times
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"InfoTransfers.txt")
    infoTransfers = readInformation(filename)
    multipleLines=search_multiple_lines(stationList)
    city=CityInfo(len(infoVelocity),infoVelocity,infoTransfers,adjacency, multipleLines)

    #------------------------------------------------------------------#
    print " \n\n\n___________ test EX 3 : SET COST TABLE_______________________\n"
	
	
	#test for time
    print "       TIME: \n"
    num_connections=0
    num_correct=0
    currentCostTable=setCostTable( 1, stationList,city)
    correct_dictionary={}
	
    correct_dictionary[1]={}
    correct_dictionary[1][2]=9.05375724726
    num_connections=num_connections+1
    correct_dictionary[2]={}
    correct_dictionary[2][1]=9.05375724726
    num_connections=num_connections+1
    correct_dictionary[2][10]=15
    num_connections=num_connections+1
    correct_dictionary[2][3]=4.21602556807
    num_connections=num_connections+1
    correct_dictionary[2][5]=20
    num_connections=num_connections+1
    correct_dictionary[3]={}
    correct_dictionary[3][2]=4.21602556807
    num_connections=num_connections+1
    correct_dictionary[4]={}
    correct_dictionary[4][5]=5.42857142857
    num_connections=num_connections+1
    correct_dictionary[5]={}
    correct_dictionary[5][2]=20
    num_connections=num_connections+1
    correct_dictionary[5][4]=5.42857142857
    num_connections=num_connections+1
    correct_dictionary[5][10]=8
    num_connections=num_connections+1
    correct_dictionary[5][6]=7.14285714286
    num_connections=num_connections+1
    correct_dictionary[6]={}
    correct_dictionary[6][5]=7.14285714286
    num_connections=num_connections+1
    correct_dictionary[6][7]=4.21428571429
    num_connections=num_connections+1
    correct_dictionary[7]={}
    correct_dictionary[7][8]=6.03739282526
    num_connections=num_connections+1
    correct_dictionary[7][6]=4.21428571429
    num_connections=num_connections+1
    correct_dictionary[8]={}
    correct_dictionary[8][9]=2.51651345907
    num_connections=num_connections+1
    correct_dictionary[8][12]=12
    num_connections=num_connections+1
    correct_dictionary[8][13]=6
    num_connections=num_connections+1
    correct_dictionary[8][7]=6.03739282526
    num_connections=num_connections+1
    correct_dictionary[9]={}
    correct_dictionary[9][8]=2.51651345907
    num_connections=num_connections+1
    correct_dictionary[10]={}
    correct_dictionary[10][2]=15
    num_connections=num_connections+1
    correct_dictionary[10][11]=2.1624212363
    num_connections=num_connections+1
    correct_dictionary[10][5]=8
    num_connections=num_connections+1
    correct_dictionary[11]={}
    correct_dictionary[11][10]=2.1624212363
    num_connections=num_connections+1
    correct_dictionary[11][12]=2.62222222222
    num_connections=num_connections+1
    correct_dictionary[12]={}
    correct_dictionary[12][8]=12
    num_connections=num_connections+1
    correct_dictionary[12][11]=2.62222222222
    num_connections=num_connections+1
    correct_dictionary[12][13]=15
    num_connections=num_connections+1
    correct_dictionary[13]={}
    correct_dictionary[13][8]=6
    num_connections=num_connections+1
    correct_dictionary[13][12]=15
    num_connections=num_connections+1
    correct_dictionary[13][14]=21.3732854482
    num_connections=num_connections+1
    correct_dictionary[14]={}
    correct_dictionary[14][13]=21.3732854482
    num_connections=num_connections+1
	
    same_keys_time= (sorted(currentCostTable.keys())== sorted(correct_dictionary.keys()))
	
    for i in correct_dictionary.keys():
        if currentCostTable.has_key(int(i)) == False:
			print "  FAIL. Your table does not have the primary key " + str(i)
        else:
			for j in correct_dictionary[i].keys():
				if currentCostTable[i].has_key(int(j)) == False:
					print "  FAIL. Your table does not have the secundary key " + str(j) + " for the primary key " + str(i)
				else:
					if abs (currentCostTable[i][j]  - correct_dictionary[i][j])> 0.01:
						print " FAIL. Incorrect value in the table at (" + str(i)+","+str(j)+")"
					else:
						num_correct=num_correct+1
	
   
    print "  \n                Test passed: " + str(num_correct) + " / "+ str(num_connections) + "\n\n"

	
	#.....................................................................................................
	#test for distance
    print "       DISTANCE: \n"
    num_connections=0
    num_correct=0
    currentCostTable=setCostTable( 2, stationList,city)
    correct_dictionary={}
	
    correct_dictionary[1]={}
    correct_dictionary[1][2]=90.5375724726
    num_connections=num_connections+1
    correct_dictionary[2]={}
    correct_dictionary[2][1]=90.5375724726
    num_connections=num_connections+1
    correct_dictionary[2][10]=0
    num_connections=num_connections+1
    correct_dictionary[2][3]=42.1602556807
    num_connections=num_connections+1
    correct_dictionary[2][5]=0
    num_connections=num_connections+1
    correct_dictionary[3]={}
    correct_dictionary[3][2]=42.1602556807
    num_connections=num_connections+1
    correct_dictionary[4]={}
    correct_dictionary[4][5]=76
    num_connections=num_connections+1
    correct_dictionary[5]={}
    correct_dictionary[5][2]=0
    num_connections=num_connections+1
    correct_dictionary[5][4]=76
    num_connections=num_connections+1
    correct_dictionary[5][10]=0
    num_connections=num_connections+1
    correct_dictionary[5][6]=100
    num_connections=num_connections+1
    correct_dictionary[6]={}
    correct_dictionary[6][5]=100
    num_connections=num_connections+1
    correct_dictionary[6][7]=59.0000000001
    num_connections=num_connections+1
    correct_dictionary[7]={}
    correct_dictionary[7][8]=84.5234995536
    num_connections=num_connections+1
    correct_dictionary[7][6]=59.0000000001
    num_connections=num_connections+1
    correct_dictionary[8]={}
    correct_dictionary[8][9]=35.231188427
    num_connections=num_connections+1
    correct_dictionary[8][12]=0
    num_connections=num_connections+1
    correct_dictionary[8][13]=0
    num_connections=num_connections+1
    correct_dictionary[8][7]=84.5234995536
    num_connections=num_connections+1
    correct_dictionary[9]={}
    correct_dictionary[9][8]=35.231188427
    num_connections=num_connections+1
    correct_dictionary[10]={}
    correct_dictionary[10][2]=0
    num_connections=num_connections+1
    correct_dictionary[10][11]=97.3089556335
    num_connections=num_connections+1
    correct_dictionary[10][5]=0
    num_connections=num_connections+1
    correct_dictionary[11]={}
    correct_dictionary[11][10]=97.3089556335
    num_connections=num_connections+1
    correct_dictionary[11][12]=118
    num_connections=num_connections+1
    correct_dictionary[12]={}
    correct_dictionary[12][8]=0
    num_connections=num_connections+1
    correct_dictionary[12][11]=118
    num_connections=num_connections+1
    correct_dictionary[12][13]=0
    num_connections=num_connections+1
    correct_dictionary[13]={}
    correct_dictionary[13][8]=0
    num_connections=num_connections+1
    correct_dictionary[13][12]=0
    num_connections=num_connections+1
    correct_dictionary[13][14]=64.1198563446
    num_connections=num_connections+1
    correct_dictionary[14]={}
    correct_dictionary[14][13]=64.1198563446
    num_connections=num_connections+1
	
    same_keys_time= (sorted(currentCostTable.keys())== sorted(correct_dictionary.keys()))
	
    for i in correct_dictionary.keys():
        if currentCostTable.has_key(int(i)) == False:
			print "  FAIL. Your table does not have the primary key " + str(i)
        else:
			for j in correct_dictionary[i].keys():
				if currentCostTable[i].has_key(int(j)) == False:
					print "  FAIL. Your table does not have the secundary key " + str(j) + " for the primary key " + str(i)
				else:
					if abs (currentCostTable[i][j]  - correct_dictionary[i][j])> 0.01:
						print " FAIL. Incorrect value in the table at (" + str(i)+","+str(j)+")"
					else:
						num_correct=num_correct+1
	
   
    print "  \n                Test passed: " + str(num_correct) + " / "+ str(num_connections) + "\n\n"
	
	
	#.....................................................................................................
	#test for TRANSFERS
    print "       TRANSFERS: \n"
    num_connections=0
    num_correct=0
    currentCostTable=setCostTable( 3, stationList,city)
    correct_dictionary={}
	
    correct_dictionary[1]={}
    correct_dictionary[1][2]=0
    num_connections=num_connections+1
    correct_dictionary[2]={}
    correct_dictionary[2][1]=0
    num_connections=num_connections+1
    correct_dictionary[2][10]=1
    num_connections=num_connections+1
    correct_dictionary[2][3]=0
    num_connections=num_connections+1
    correct_dictionary[2][5]=1
    num_connections=num_connections+1
    correct_dictionary[3]={}
    correct_dictionary[3][2]=0
    num_connections=num_connections+1
    correct_dictionary[4]={}
    correct_dictionary[4][5]=0
    num_connections=num_connections+1
    correct_dictionary[5]={}
    correct_dictionary[5][2]=1
    num_connections=num_connections+1
    correct_dictionary[5][4]=0
    num_connections=num_connections+1
    correct_dictionary[5][10]=1
    num_connections=num_connections+1
    correct_dictionary[5][6]=0
    num_connections=num_connections+1
    correct_dictionary[6]={}
    correct_dictionary[6][5]=0
    num_connections=num_connections+1
    correct_dictionary[6][7]=0
    num_connections=num_connections+1
    correct_dictionary[7]={}
    correct_dictionary[7][8]=0
    num_connections=num_connections+1
    correct_dictionary[7][6]=0
    num_connections=num_connections+1
    correct_dictionary[8]={}
    correct_dictionary[8][9]=0
    num_connections=num_connections+1
    correct_dictionary[8][12]=1
    num_connections=num_connections+1
    correct_dictionary[8][13]=1
    num_connections=num_connections+1
    correct_dictionary[8][7]=0
    num_connections=num_connections+1
    correct_dictionary[9]={}
    correct_dictionary[9][8]=0
    num_connections=num_connections+1
    correct_dictionary[10]={}
    correct_dictionary[10][2]=1
    num_connections=num_connections+1
    correct_dictionary[10][11]=0
    num_connections=num_connections+1
    correct_dictionary[10][5]=1
    num_connections=num_connections+1
    correct_dictionary[11]={}
    correct_dictionary[11][10]=0
    num_connections=num_connections+1
    correct_dictionary[11][12]=0
    num_connections=num_connections+1
    correct_dictionary[12]={}
    correct_dictionary[12][8]=1
    num_connections=num_connections+1
    correct_dictionary[12][11]=0
    num_connections=num_connections+1
    correct_dictionary[12][13]=1
    num_connections=num_connections+1
    correct_dictionary[13]={}
    correct_dictionary[13][8]=1
    num_connections=num_connections+1
    correct_dictionary[13][12]=1
    num_connections=num_connections+1
    correct_dictionary[13][14]=0
    num_connections=num_connections+1
    correct_dictionary[14]={}
    correct_dictionary[14][13]=0
    num_connections=num_connections+1
	
    same_keys_time= (sorted(currentCostTable.keys())== sorted(correct_dictionary.keys()))
	
    for i in correct_dictionary.keys():
        if currentCostTable.has_key(int(i)) == False:
			print "  FAIL. Your table does not have the primary key " + str(i)
        else:
			for j in correct_dictionary[i].keys():
				if currentCostTable[i].has_key(int(j)) == False:
					print "  FAIL. Your table does not have the secundary key " + str(j) + " for the primary key " + str(i)
				else:
					if abs (currentCostTable[i][j]  - correct_dictionary[i][j])> 0.01:
						print " FAIL. Incorrect value in the table at (" + str(i)+","+str(j)+")"
					else:
						num_correct=num_correct+1
	
   
    print "  \n                Test passed: " + str(num_correct) + " / "+ str(num_connections) + "\n\n"
	
	#.....................................................................................................
		#test for stop Stations
    print "       Stop Stations: \n"
    num_connections=0
    num_correct=0
    currentCostTable=setCostTable( 4, stationList,city)
    correct_dictionary={}
	
    correct_dictionary[1]={}
    correct_dictionary[1][2]=1
    num_connections=num_connections+1
    correct_dictionary[2]={}
    correct_dictionary[2][1]=1
    num_connections=num_connections+1
    correct_dictionary[2][10]=0
    num_connections=num_connections+1
    correct_dictionary[2][3]=1
    num_connections=num_connections+1
    correct_dictionary[2][5]=0
    num_connections=num_connections+1
    correct_dictionary[3]={}
    correct_dictionary[3][2]=1
    num_connections=num_connections+1
    correct_dictionary[4]={}
    correct_dictionary[4][5]=1
    num_connections=num_connections+1
    correct_dictionary[5]={}
    correct_dictionary[5][2]=0
    num_connections=num_connections+1
    correct_dictionary[5][4]=1
    num_connections=num_connections+1
    correct_dictionary[5][10]=0
    num_connections=num_connections+1
    correct_dictionary[5][6]=1
    num_connections=num_connections+1
    correct_dictionary[6]={}
    correct_dictionary[6][5]=1
    num_connections=num_connections+1
    correct_dictionary[6][7]=1
    num_connections=num_connections+1
    correct_dictionary[7]={}
    correct_dictionary[7][8]=1
    num_connections=num_connections+1
    correct_dictionary[7][6]=1
    num_connections=num_connections+1
    correct_dictionary[8]={}
    correct_dictionary[8][9]=1
    num_connections=num_connections+1
    correct_dictionary[8][12]=0
    num_connections=num_connections+1
    correct_dictionary[8][13]=0
    num_connections=num_connections+1
    correct_dictionary[8][7]=1
    num_connections=num_connections+1
    correct_dictionary[9]={}
    correct_dictionary[9][8]=1
    num_connections=num_connections+1
    correct_dictionary[10]={}
    correct_dictionary[10][2]=0
    num_connections=num_connections+1
    correct_dictionary[10][11]=1
    num_connections=num_connections+1
    correct_dictionary[10][5]=0
    num_connections=num_connections+1
    correct_dictionary[11]={}
    correct_dictionary[11][10]=1
    num_connections=num_connections+1
    correct_dictionary[11][12]=1
    num_connections=num_connections+1
    correct_dictionary[12]={}
    correct_dictionary[12][8]=0
    num_connections=num_connections+1
    correct_dictionary[12][11]=1
    num_connections=num_connections+1
    correct_dictionary[12][13]=0
    num_connections=num_connections+1
    correct_dictionary[13]={}
    correct_dictionary[13][8]=0
    num_connections=num_connections+1
    correct_dictionary[13][12]=0
    num_connections=num_connections+1
    correct_dictionary[13][14]=1
    num_connections=num_connections+1
    correct_dictionary[14]={}
    correct_dictionary[14][13]=1
    num_connections=num_connections+1
	
    same_keys_time= (sorted(currentCostTable.keys())== sorted(correct_dictionary.keys()))
	
    for i in correct_dictionary.keys():
        if currentCostTable.has_key(int(i)) == False:
			print "  FAIL. Your table does not have the primary key " + str(i)
        else:
			for j in correct_dictionary[i].keys():
				if currentCostTable[i].has_key(int(j)) == False:
					print "  FAIL. Your table does not have the secundary key " + str(j) + " for the primary key " + str(i)
				else:
					if abs (currentCostTable[i][j]  - correct_dictionary[i][j])> 0.01:
						print " FAIL. Incorrect value in the table at (" + str(i)+","+str(j)+")"
					else:
						num_correct=num_correct+1
	
   
    print "  \n                Test passed: " + str(num_correct) + " / "+ str(num_connections) + "\n\n"
	
if __name__ == '__main__':
    main()