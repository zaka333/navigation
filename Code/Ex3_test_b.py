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
	
	
    origin1=Node(stationList[0],None)                 				# Massena L1
    destination_tmp_1_1=Node(stationList[1],origin1)     			# Charpenes L1
    destination1=Node(stationList[2],destination_tmp_1_1)			# Republique L1
	
    origin2=Node(stationList[3], None)                				# Le Tonkin L2
    destination_tmp_2_1=Node(stationList[4],origin2)      			# Charpennes L2
    destination_tmp_2_2=Node(stationList[5],destination_tmp_2_1) 	# College Bellecombe L2
    destination_tmp_2_3=Node(stationList[6],destination_tmp_2_2) 	# Thiers Lafayette L2
    destination_tmp_2_4=Node(stationList[7],destination_tmp_2_3) 	# Part-Dieu L2
    destination2=Node(stationList[8],destination_tmp_2_4)    		# Part-Dieu Sirvent L2
	
    origin3=Node(stationList[9],None) 								# Charpennes L3
    destination_tmp_3_1=Node(stationList[10],origin3) 				# Brotteaux L3
    destination3=Node(stationList[11],destination_tmp_3_1)			# Part-Dieu L3
	
    origin4=Node(stationList[12],None) 								# Part-Dieu L4
    destination4=Node(stationList[13],origin4) 						# Dauphhine Lacassagne L4
	
    origin5=Node(stationList[3], None)                				# Le Tonkin L2
    destination_tmp_5_1=Node(stationList[4],origin5)      			# Charpennes L2
    destination_tmp_5_2=Node(stationList[9],destination_tmp_5_1) 	# Charpennes L3
    destination5=Node(stationList[10],destination_tmp_5_2) 			# Brotteaux L3
	
    origin6=Node(stationList[8],None)				    			# Part-Dieu Sirvent L2
    destination_tmp_6_1=Node(stationList[7],origin6) 				# Part-Dieu L2
    destination_tmp_6_2=Node(stationList[6],destination_tmp_6_1) 	# Thiers Lafayette L2
    destination_tmp_6_3=Node(stationList[5],destination_tmp_6_2) 	# College Bellecombe L2
    destination_tmp_6_4=Node(stationList[4],destination_tmp_6_3)	# Charpennes L2
    destination_tmp_6_5=Node(stationList[9],destination_tmp_6_4) 	# Charpennes L3
    destination6=Node(stationList[10],destination_tmp_6_5)			# Brotteaux L3
	
    origin7=Node(stationList[13],None)								# Dauphhine Lacassagne L4
    destination_tmp_7_1=Node(stationList[12],origin7) 				# Part-Dieu L4
    destination_tmp_7_2=Node(stationList[7],destination_tmp_7_1) 	# Part-Dieu L2
    destination7=Node(stationList[8],destination_tmp_7_2)	   		# Part-Dieu Sirvent L2
	
    origin8=Node(stationList[5],None) 								# College Bellecombe L2
    destination_tmp_8_1=Node(stationList[4],origin8)				# Charpennes L2
    destination_tmp_8_2=Node(stationList[1],destination_tmp_8_1) 	# Charpenes L1
    destination8=Node(stationList[2],destination_tmp_8_2)			# Republique L1
	
    origin9=Node(stationList[10],None) 								# Brotteaux L3
    destination_tmp_9_1=Node(stationList[9],origin9) 				# Charpennes L3
    destination_tmp_9_2=Node(stationList[1],destination_tmp_9_1) 	# Charpenes L1
    destination9=Node(stationList[0],destination_tmp_9_2)    		# Massena L1
	
    origin10=Node(stationList[3], None)                				# Le Tonkin L2
    destination_tmp_10_1=Node(stationList[4],origin10)      		# Charpennes L2
    destination_tmp_10_2=Node(stationList[9],destination_tmp_10_1) 	# Charpennes L3
    destination_tmp_10_3=Node(stationList[10],destination_tmp_10_2)	# Brotteaux L3
    destination_tmp_10_4=Node(stationList[11],destination_tmp_10_3)	# Part-Dieu L3
    destination_tmp_10_5=Node(stationList[7],destination_tmp_10_4) 	# Part-Dieu L2
    destination10=Node(stationList[6],destination_tmp_10_5) 		# Thiers Lafayette L2
	
	
	
	
    print " \n\n\n___________ test EX 3 : SET REAL COST_______________________\n"
	
	
	#test for time
    print "       TIME: \n"
    currentCostTable=setCostTable( 1, stationList,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination1.setRealCost(currentCostTable)
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_3.setRealCost(currentCostTable)
    destination_tmp_2_4.setRealCost(currentCostTable)
    destination2.setRealCost(currentCostTable)
	
    destination_tmp_3_1.setRealCost(currentCostTable)
    destination3.setRealCost(currentCostTable)
	
    destination4.setRealCost(currentCostTable)
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_2.setRealCost(currentCostTable)
    destination5.setRealCost(currentCostTable)
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_4.setRealCost(currentCostTable)
    destination_tmp_6_5.setRealCost(currentCostTable)
    destination6.setRealCost(currentCostTable)
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination7.setRealCost(currentCostTable)
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_2.setRealCost(currentCostTable)
    destination8.setRealCost(currentCostTable)
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination9.setRealCost(currentCostTable)
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)	
    destination10.setRealCost(currentCostTable)
	
    time_ok=0
    if abs(destination1.g - 13.269782153)<0.01:
		print "             1  : " + str(destination1.g) +  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             1  : " + str(destination1.g) +  "    --> FAIL!"	
	
    if abs(destination2.g - 25.33962057)<0.01:
		print "             2  : " + str(destination2.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             2  : " + str(destination2.g) +  "    --> FAIL!"	
		
    if abs(destination3.g - 4.78464345852)<0.01:
		print "             3  : " + str(destination3.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             3  : " + str(destination3.g) +  "    --> FAIL!"	
	
    if abs(destination4.g -21.3732854482)<0.01:
		print "             4  : " + str(destination4.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             4  : " + str(destination4.g) +  "    --> FAIL!"	
		
    if abs(destination5.g - 15.5909926649)<0.01:
		print "             5  : " + str(destination5.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             5  : " + str(destination5.g) +  "    --> FAIL!"	
	
	
    if abs(destination6.g - 30.0734703778)<0.01:
		print "             6  : " + str(destination6.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             6  : " + str(destination6.g) +  "    --> FAIL!"	
	
    if abs(destination7.g - 29.8897989073)<0.01:
		print "             7  : " + str(destination7.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             7  : " + str(destination7.g) +  "    --> FAIL!"	

    if abs(destination8.g - 31.358827109)<0.01:
		print "             8  : " + str(destination8.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             8  : " + str(destination8.g) +  "    --> FAIL!"	
		
    if abs(destination9.g - 26.2161784836)<0.01:
		print "             9  : " + str(destination9.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             9  : " + str(destination9.g) +  "    --> FAIL!"	
	
    if abs(destination10.g - 36.2506077124)<0.01:
		print "             10 : " + str(destination10.g)+  "    --> OK!"
		time_ok=time_ok+1
    else:
		print "             10 : " + str(destination10.g) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(time_ok) + " / 10 \n"
	
	
	
	
	#.....................................................................................................
	#test for distance
    print "       DISTANCE: \n"
    currentCostTable=setCostTable( 2, stationList,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination1.setRealCost(currentCostTable)
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_3.setRealCost(currentCostTable)
    destination_tmp_2_4.setRealCost(currentCostTable)
    destination2.setRealCost(currentCostTable)
	
    destination_tmp_3_1.setRealCost(currentCostTable)
    destination3.setRealCost(currentCostTable)
	
    destination4.setRealCost(currentCostTable)
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_2.setRealCost(currentCostTable)
    destination5.setRealCost(currentCostTable)
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_4.setRealCost(currentCostTable)
    destination_tmp_6_5.setRealCost(currentCostTable)
    destination6.setRealCost(currentCostTable)
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination7.setRealCost(currentCostTable)
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_2.setRealCost(currentCostTable)
    destination8.setRealCost(currentCostTable)
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination9.setRealCost(currentCostTable)
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)	
    destination10.setRealCost(currentCostTable)
	
    dist_ok=0
    if abs(destination1.g - 132.697828153)<0.01:
		print "             1  : " + str(destination1.g) +  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             1  : " + str(destination1.g) +  "    --> FAIL!"	
	
    if abs(destination2.g - 354.754687981)<0.01:
		print "             2  : " + str(destination2.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             2  : " + str(destination2.g) +  "    --> FAIL!"	
		
    if abs(destination3.g - 215.308955633)<0.01:
		print "             3  : " + str(destination3.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             3  : " + str(destination3.g) +  "    --> FAIL!"	
	
    if abs(destination4.g -64.1198563446)<0.01:
		print "             4  : " + str(destination4.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             4  : " + str(destination4.g) +  "    --> FAIL!"	
		
    if abs(destination5.g - 173.308955633)<0.01:
		print "             5  : " + str(destination5.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             5  : " + str(destination5.g) +  "    --> FAIL!"	
	
	
    if abs(destination6.g - 376.063643614)<0.01:
		print "             6  : " + str(destination6.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             6  : " + str(destination6.g) +  "    --> FAIL!"	
	
    if abs(destination7.g - 99.3510447716)<0.01:
		print "             7  : " + str(destination7.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             7  : " + str(destination7.g) +  "    --> FAIL!"	

    if abs(destination8.g - 142.160255681)<0.01:
		print "             8  : " + str(destination8.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             8  : " + str(destination8.g) +  "    --> FAIL!"	
		
    if abs(destination9.g - 187.846528106)<0.01:
		print "             9  : " + str(destination9.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             9  : " + str(destination9.g) +  "    --> FAIL!"	
	
    if abs(destination10.g - 375.832455187)<0.01:
		print "             10 : " + str(destination10.g)+  "    --> OK!"
		dist_ok=dist_ok+1
    else:
		print "             10 : " + str(destination10.g) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(dist_ok) + " / 10 \n"
	
	
	
	
	#.....................................................................................................
	#test for TRANSFERS
    print "       TRANSFERS: \n"
    currentCostTable=setCostTable( 3, stationList,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination1.setRealCost(currentCostTable)
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_3.setRealCost(currentCostTable)
    destination_tmp_2_4.setRealCost(currentCostTable)
    destination2.setRealCost(currentCostTable)
	
    destination_tmp_3_1.setRealCost(currentCostTable)
    destination3.setRealCost(currentCostTable)
	
    destination4.setRealCost(currentCostTable)
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_2.setRealCost(currentCostTable)
    destination5.setRealCost(currentCostTable)
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_4.setRealCost(currentCostTable)
    destination_tmp_6_5.setRealCost(currentCostTable)
    destination6.setRealCost(currentCostTable)
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination7.setRealCost(currentCostTable)
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_2.setRealCost(currentCostTable)
    destination8.setRealCost(currentCostTable)
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination9.setRealCost(currentCostTable)
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)	
    destination10.setRealCost(currentCostTable)
	
    transf_ok=0
    if abs(destination1.g - 0)<0.01:
		print "             1  : " + str(destination1.g) +  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             1  : " + str(destination1.g) +  "    --> FAIL!"	
	
    if abs(destination2.g - 0)<0.01:
		print "             2  : " + str(destination2.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             2  : " + str(destination2.g) +  "    --> FAIL!"	
		
    if abs(destination3.g - 0)<0.01:
		print "             3  : " + str(destination3.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             3  : " + str(destination3.g) +  "    --> FAIL!"	
	
    if abs(destination4.g -0)<0.01:
		print "             4  : " + str(destination4.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             4  : " + str(destination4.g) +  "    --> FAIL!"	
		
    if abs(destination5.g - 1)<0.01:
		print "             5  : " + str(destination5.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             5  : " + str(destination5.g) +  "    --> FAIL!"	
	
	
    if abs(destination6.g - 1)<0.01:
		print "             6  : " + str(destination6.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             6  : " + str(destination6.g) +  "    --> FAIL!"	
	
    if abs(destination7.g - 1)<0.01:
		print "             7  : " + str(destination7.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             7  : " + str(destination7.g) +  "    --> FAIL!"	

    if abs(destination8.g - 1)<0.01:
		print "             8  : " + str(destination8.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             8  : " + str(destination8.g) +  "    --> FAIL!"	
		
    if abs(destination9.g - 1)<0.01:
		print "             9  : " + str(destination9.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             9  : " + str(destination9.g) +  "    --> FAIL!"	
	
    if abs(destination10.g - 2)<0.01:
		print "             10 : " + str(destination10.g)+  "    --> OK!"
		transf_ok=transf_ok+1
    else:
		print "             10 : " + str(destination10.g) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(transf_ok) + " / 10 \n"
	
    
	
	#.....................................................................................................
		#test for stop Stations
    print "       STOP STATIONS: \n"
    currentCostTable=setCostTable( 4, stationList,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination1.setRealCost(currentCostTable)
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_3.setRealCost(currentCostTable)
    destination_tmp_2_4.setRealCost(currentCostTable)
    destination2.setRealCost(currentCostTable)
	
    destination_tmp_3_1.setRealCost(currentCostTable)
    destination3.setRealCost(currentCostTable)
	
    destination4.setRealCost(currentCostTable)
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_2.setRealCost(currentCostTable)
    destination5.setRealCost(currentCostTable)
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_4.setRealCost(currentCostTable)
    destination_tmp_6_5.setRealCost(currentCostTable)
    destination6.setRealCost(currentCostTable)
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination7.setRealCost(currentCostTable)
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_2.setRealCost(currentCostTable)
    destination8.setRealCost(currentCostTable)
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination9.setRealCost(currentCostTable)
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)	
    destination10.setRealCost(currentCostTable)
	
    stations_ok=0
    if abs(destination1.g - 2)<0.01:
		print "             1  : " + str(destination1.g) +  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             1  : " + str(destination1.g) +  "    --> FAIL!"	
	
    if abs(destination2.g - 5)<0.01:
		print "             2  : " + str(destination2.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             2  : " + str(destination2.g) +  "    --> FAIL!"	
		
    if abs(destination3.g - 2)<0.01:
		print "             3  : " + str(destination3.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             3  : " + str(destination3.g) +  "    --> FAIL!"	
	
    if abs(destination4.g -1)<0.01:
		print "             4  : " + str(destination4.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             4  : " + str(destination4.g) +  "    --> FAIL!"	
		
    if abs(destination5.g - 2)<0.01:
		print "             5  : " + str(destination5.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             5  : " + str(destination5.g) +  "    --> FAIL!"	
	
	
    if abs(destination6.g - 5)<0.01:
		print "             6  : " + str(destination6.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             6  : " + str(destination6.g) +  "    --> FAIL!"	
	
    if abs(destination7.g - 2)<0.01:
		print "             7  : " + str(destination7.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             7  : " + str(destination7.g) +  "    --> FAIL!"	

    if abs(destination8.g - 2)<0.01:
		print "             8  : " + str(destination8.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             8  : " + str(destination8.g) +  "    --> FAIL!"	
		
    if abs(destination9.g - 2)<0.01:
		print "             9  : " + str(destination9.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             9  : " + str(destination9.g) +  "    --> FAIL!"	
	
    if abs(destination10.g - 4)<0.01:
		print "             10 : " + str(destination10.g)+  "    --> OK!"
		stations_ok=stations_ok+1
    else:
		print "             10 : " + str(destination10.g) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(stations_ok) + " / 10 \n"
	
   
	
if __name__ == '__main__':
    main()