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
	
	
    typePreference=int(1)
    nodeList=[]
    currentCostTable=setCostTable( typePreference, stationList,city)
    origin1=Node(stationList[13],None)                 				# Dauphhine Lacassagne L4
    destination=Node(stationList[2],None)							# Republique L1
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    current_ids=[]
    test_ok=0
    print "\n sorted insertion for TIME"	
	
	
    #for i in nodeList:
	#	current_ids.append(i.station.id)
    #if current_ids==[13]:
	#	print "     1:  sorted insertion  --> OK!"
	#	test_ok=test_ok+1
    #else:
	#	print "     1:  sorted insertion  --> FAIL!"
		
	
    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        
    #if current_ids==[13]:
    #    print "     1:  sorted insertion  --> OK!"
    #    test_ok=test_ok+1
    #else:
    #    print "     1:  sorted insertion  --> FAIL!"

    if tmp_total_ok==len(nodeList)-1:
       print "     1:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     1:  sorted insertion  --> FAIL! ->"  + str(list_valors)      
    
	#----------------------------------------------------------------------

    origin1=Node(stationList[12],None)                 				
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)


    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     2:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     2:  sorted insertion  --> FAIL! ->"  + str(list_valors)  
		
	#----------------------------------------------------------------------	

    origin1=Node(stationList[3],None)                 	

    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     3:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     3:  sorted insertion  --> FAIL! ->"  + str(list_valors)  
	
	#----------------------------------------------------------------------

    origin1=Node(stationList[0],None)                 		
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)


    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     4:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     4:  sorted insertion  --> FAIL! ->"  + str(list_valors)  
	
	#----------------------------------------------------------------------

    
    
    
    print "\n sorted insertion for DISTANCE"
	
	
	
	
	
    typePreference=int(2)
    nodeList=[]
    currentCostTable=setCostTable( typePreference, stationList,city)
    origin1=Node(stationList[13],None)                 				# Dauphhine Lacassagne L4
    destination=Node(stationList[2],None)							# Republique L1
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     5:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     5:  sorted insertion  --> FAIL! ->"  + str(list_valors)  
	#----------------------------------------------------------------------

    origin1=Node(stationList[12],None)                 				
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     6:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     6:  sorted insertion  --> FAIL! ->"  + str(list_valors)  
		
	#----------------------------------------------------------------------	

    origin1=Node(stationList[3],None)                 	

    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     7:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     7:  sorted insertion  --> FAIL! ->"  + str(list_valors)
       
	#----------------------------------------------------------------------

    origin1=Node(stationList[0],None)                 		
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
        

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     8:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     8:  sorted insertion  --> FAIL! ->"  + str(list_valors)
	
	#----------------------------------------------------------------------

	
	
    print "\n sorted insertion for TRANSFERS"	
	
	
	
	
    typePreference=int(3)
    nodeList=[]
    currentCostTable=setCostTable( typePreference, stationList,city)
    origin1=Node(stationList[13],None)                 				# Dauphhine Lacassagne L4
    destination=Node(stationList[2],None)							# Republique L1
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
        

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     9:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     9:  sorted insertion  --> FAIL! ->"  + str(list_valors)
	#----------------------------------------------------------------------

    origin1=Node(stationList[12],None)                 				
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
        

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     10:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     10:  sorted insertion  --> FAIL! ->"  + str(list_valors)
		
	#----------------------------------------------------------------------	

    origin1=Node(stationList[3],None)                 	

    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
       

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     11:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     11:  sorted insertion  --> FAIL! ->"  + str(list_valors)
	
	#----------------------------------------------------------------------

    origin1=Node(stationList[0],None)                 		
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
        

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     12:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     12:  sorted insertion  --> FAIL! ->"  + str(list_valors)
	
	#----------------------------------------------------------------------
  
	
	
	
    print "\n sorted insertion for STOP STATIONS"
	
	
    typePreference=int(4)
    nodeList=[]
    currentCostTable=setCostTable( typePreference, stationList,city)
    origin1=Node(stationList[13],None)                 				# Dauphhine Lacassagne L4
    destination=Node(stationList[2],None)							# Republique L1
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
       

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     13:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     13:  sorted insertion  --> FAIL! ->"  + str(list_valors)
	#----------------------------------------------------------------------

    origin1=Node(stationList[12],None)                 				
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
         

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     14:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     14:  sorted insertion  --> FAIL! ->"  + str(list_valors)
		
	#----------------------------------------------------------------------	

    origin1=Node(stationList[3],None)                 	

    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
       

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     15:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     15:  sorted insertion  --> FAIL! ->"  + str(list_valors)
	
	#----------------------------------------------------------------------

    origin1=Node(stationList[0],None)                 		
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
          

    anterior=nodeList[0]
    tmp_total_ok=0
    list_valors=[anterior.f]
    for i in range(1,len(nodeList)):
        current_node=nodeList[i]
        list_valors.append(current_node.f)
        if anterior.f <= current_node.f:
            tmp_total_ok=tmp_total_ok+1
        anterior=current_node
        


    if tmp_total_ok==len(nodeList)-1:
       print "     16:  sorted insertion  --> OK!"
       test_ok=test_ok+1
    else:
       print "     16:  sorted insertion  --> FAIL! ->"  + str(list_valors)
	
	#----------------------------------------------------------------------
    print "\n                   Test Passed : " + str(test_ok) + " / 16 \n"
	
	
		
if __name__ == '__main__':
    main()