# With this exercise we will work on finding a station of the path given certain coordinates
#
__authors__='TO_BE_FILLED'
__group__='DL01'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

from SearchAlgorithm import *
from SubwayMap import *
import os

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

    coord=[67,79]
    coord1=[140,20]
    coord2=[100,199]
    #------------------------------------------------------------------#


    node=coord2station(coord,stationList)
    node1=coord2station(coord1,stationList)
    node2=coord2station(coord2,stationList)

    print "\nFrom coord: " + str(coord) + " possible nodes: "
    for i in node:
        print stationList[i].name + " L"+ str(stationList[i].line) + " with ID: " + str([stationList[i].id])




    print "\nFrom coord: " + str(coord1) + " possible nodes:  "
    for i in node1:
        print stationList[i].name + " L"+ str(stationList[i].line) + " with ID: " + str([stationList[i].id])


    print "\nFrom coord: " + str(coord2) + " possible nodes: "
    for i in node2:
        print stationList[i].name + " L"+ str(stationList[i].line) + " with ID: " + str([stationList[i].id])



if __name__ == '__main__':
    main()