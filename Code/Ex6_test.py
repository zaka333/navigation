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
	
    coord1=[140,56]
    eval1=coord2station(coord1,stationList)
    eval1.sort()
	
    coord2=[100,127]
    eval2=coord2station(coord2,stationList)
    eval2.sort()
	
    coord3=[102,200]
    eval3=coord2station(coord3,stationList)
    eval3.sort()
	
    coord4=[65,78]
    eval4=coord2station(coord4,stationList)
    eval4.sort()
	
    coord5=[150,220]
    eval5=coord2station(coord5,stationList)
    eval5.sort()
	
    coord6=[3,8]
    eval6=coord2station(coord6,stationList)
    eval6.sort()
	
    coord7=[135,50]
    eval7=coord2station(coord7,stationList)
    eval7.sort()
	
    coord8=[80,200]
    eval8=coord2station(coord8,stationList)
    eval8.sort()
	
    coord9=[108,206]
    eval9=coord2station(coord9,stationList)
    eval9.sort()
	
    coord10=[166,60]
    eval10=coord2station(coord10,stationList)
    eval10.sort()
	
    print " \n\n\n___________ test EX 6 : COOD2STATION _______________________\n"
  
    test_ok=0
    if eval1 == [1,4,9]:
		print "             1  : " + str(eval1) +  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             1  : " + str(eval1) +  "    --> FAIL!"
	
    if eval2 == [10]:
		print "             2  : " + str(eval2)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             2  : " + str(eval2) +  "    --> FAIL!"	
		
    if eval3 == [7,11,12]:
		print "             3  : " + str(eval3)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             3  : " + str(eval3) +  "    --> FAIL!"	
	
    if eval4==[0]:
		print "             4  : " + str(eval4)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             4  : " + str(eval4) +  "    --> FAIL!"	
		
    if eval5 == [13]:
		print "             5  : " + str(eval5)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             5  : " + str(eval5) +  "    --> FAIL!"	
	
	
    if eval6 == [0]:
		print "             6  : " + str(eval6)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             6  : " + str(eval6) +  "    --> FAIL!"	
	
    if eval7 == [1,4,9]:
		print "             7  : " + str(eval7)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             7  : " + str(eval7) +  "    --> FAIL!"	

    if eval8 == [8]:
		print "             8  : " + str(eval8)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             8  : " + str(eval8) +  "    --> FAIL!"	
		
    if eval9 ==[7,11,12]:
		print "             9  : " + str(eval9)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             9  : " + str(eval9) +  "    --> FAIL!"	
	
    if eval10 ==[2]:
		print "             10 : " + str(eval10)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             10 : " + str(eval10) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(test_ok) + " / 10 \n"
	
if __name__ == '__main__':
    main()