# With this exercise we will work on understanding the representation of the knowledge.
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
from SubwayMap import *
#from SearchAlgorithm import *


def main():
    # Which information we need of a station?

    city_string="Lyon_smallCity"
	
    # read file o f
    print "CITY INFORMATION   *******************************************"
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Stations.txt")
    stationList = readStationInformation(filename)
    # Print information of the stations
    print_stationList(stationList)

    #Load and print the ADJACENCY matrix
    print "ADJACENY MATRIX    *******************************************"
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Connections.txt")
    adjacency = readCostTable(filename)
    #Print information of the adjaceny
    print_connections(adjacency)

    #print dictionary:
    # See MapaMetro.py
    # Pay attention in the structure where the data is saved

    #Station Time Cost Table (without connections)
    print "STATION TIME COST TABLE *******************************************"
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Time.txt")
    timeStations = readCostTable(filename)
    # Now timeStations corresponds to the time cost table, where the real time info between two different stations is
    # saved
    print " Real time between two different stations:"
    print_connections(timeStations)

    #Now we have to set the values of the dictionary for each station (destinationDic) with the values in timeStations
    setNextStations(stationList, timeStations)
    print_dictionary(stationList)
    # with previous lines, real cost of the route between two stations is saved in the dictionary 'destinationDic'.
    # Analyze how is the information structured. Each station has its own dictionary. Its dictionary has only the keys
    # of the ID's of the stations where a real connection exists. The value of this dictionary is just the real time
    # that takes the route between the current station and the station identified by the ID.

    #PLAYING WITH THE INFORMATION
    # REAL time to go from BROTTEAUX L3 to PART-DIEU  L3
    print " from " + stationList[10].name + " L" + str(stationList[10].line) + " to " + stationList[11].name + " L" + str(stationList[11].line) + " : " + str(stationList[10].destinationDic[12]) + " minutes"
    # REAL time to go from PART-DIEU SERVIENT L3 to PART-DIEU L3
    print  " from " + stationList[11].name + " L" + str(stationList[11].line) + " to " + stationList[10].name + " L" + str(stationList[10].line) + " : " +  str(stationList[11].destinationDic[11]) + " minutes"
    print"\n"
    """"   PAY ATTENTION WITH THE INDEXES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            - stationList is a list and indexes start at '0'
            - destinationDic contains as keys the set ID's of the stations, and they start at '1' [see STATION FILE]
          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """


    # Now we want to analyze extra information from the files.
    # Velocity of the lines
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"InfoVelocity.txt")
    infoVelocity = readInformation(filename)
    print " Metro Lines run at velocity: "
    print infoVelocity
    print " max. velocity = "+ str(max(infoVelocity))
    print " min. velocity = "+ str(min(infoVelocity))
    print "\n"

    # Transfers times
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"InfoTransfers.txt")
    infoTransfers = readInformation(filename)
    print " Times of the transfers: "
    print infoTransfers
    print " max. transfer = "+ str(max(infoTransfers))
    print " min. transfer = "+ str(min(infoTransfers))
    print "\n"

    #we save the global information of the city in 'city' variable.
    #Analyze which information contains an element of the class CityInfo.
    multipleLines=search_multiple_lines(stationList)
    city=CityInfo(len(infoVelocity),infoVelocity,infoTransfers,adjacency, multipleLines)
    #check if max_velocity is saved appropiatley
    print "The faster subway runs at : " + str(city.max_velocity)





if __name__ == '__main__':
    main()


