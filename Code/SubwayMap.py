# This file has all the functions required to load the information of a city.
# - Definition of the class Station
# - Definition of the class CityInfo
# - Read functions from files
# - Structure of the information
#
__authors__='TO_BE_FILLED'
__group__='DL01'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _________________________________________________________________________________________


class Station:
    # __init__ Constructor of Station Class.
    def __init__(self, id, name, line, x, y):
        self.id = id                    # station id
        self.destinationDic = {}        # Dictionary where principal keys refers to the set of stations that it is connected.
                                        # The value of this dictionary refers to the time cost between two stations.
        self.name = name                # station Name
        self.line = int(line)           # line name string
        self.x = x                      # coordinate X of the station
        self.y = y                      # coordinate Y of the station

class CityInfo:
    # __init__ Constructor of CityInfo class
    def __init__(self, num_lines, vel_lines, trans_time, adjacency, multipleLines):
        self.num_lines=num_lines            # Number of different lines
        self.velocity_lines=vel_lines       # velocity of each line
        self.transfers_time=trans_time      # set of transfers
        self.max_velocity=max(vel_lines)    # maximum velocity of the subways (faster subway)
        self.min_velocity=min(vel_lines)    # minimum velocity of the subways  (slower subway)
        self.max_transfer=max(trans_time)   # slower transfer time
        self.min_transfer=min(trans_time)   # faster transfer time
        self.adjacency=adjacency
	self.multipleLines=multipleLines
	

#search_multiple_lines: Searches the set of stations that have different lines.

def search_multiple_lines(stationList):
  

    multipleLines = {}
    for i in stationList:
        for j in stationList:
            if i.id != j.id:
                if i.x == j.x & i.y == j.x:
                    if multipleLines.has_key(i.id):
                        if j.line not in multipleLines[i.id]:
                            multipleLines[i.id].append(j.line)
                        else:
                            multipleLines[i.id] = []
                            multipleLines[i.id].append(j.line)
                        if multipleLines.has_key(j.id):
                            if i.line not in multipleLines[j.id]:
                                multipleLines[j.id].append(i.line)
                            else:
                                multipleLines[j.id] = []
                                multipleLines[j.id].append(i.line)
                    
    return multipleLines

# readStationInformation: Given a filename, it reads the information of this file.
# The file should keep the format:
#	id <\t> name <\t> line <\t> x <\t> y <\n>
def readStationInformation(filename):
    fileMetro = open(filename, 'r')
    stationList = []
    for line in fileMetro:
        information = line.split('\t')
        station_read = Station(int(information[0]), information[1], information[2], int(information[3]),
                               int((information[4].replace('\n', '')).replace(' ', '')))
        stationList.append(station_read)
    fileMetro.close()
    return stationList

def readInformation(filename):
    vector=[]
    fp = open(filename,'r')
    line = fp.readline()
    while line:
       # tmp=fp.readline()
       try:
            value=line.split(" : ")
            value=value[1].split("\n")
            vector.append(int(value[0]))
            line = fp.readline()
       except :
            line = fp.readline()
    del vector[-1] #remove min value
    del vector[-1] #remove max value
    fp.close()
    return (vector)


# readCostTable: Given a filename, it reads the information of this file.
# The file should be an inferior matrix with the cost between two different stations.
def readCostTable(filename):
    fileCorrespondencia = open(filename, 'r')
    connections = {}
    origin = 1
    for i in fileCorrespondencia:
        informations = i.split('\t')
        destination = 1 # because ID of the stations started at '1' instead of '0'
        for j in informations:
            j = j.replace('\n', '')
            if j != '':
                if j != '0':
                    if connections.has_key(int(origin)) == False:
                        connections[int(origin)] = {}
                    if (connections[int(origin)].has_key(int(destination)) == 0):
                        connections[int(origin)][int(destination)] = float(j)
                    # as the matrix is an inferior matrix, we should duplicate the information to the superior missing part.
                    if connections.has_key(int(destination)) == False:
                        connections[int(destination)] = {}
                    if (connections[int(destination)].has_key(int(origin)) == 0):
                        connections[int(destination)][int(origin)] = float(j)

            destination = destination + 1
        origin = origin + 1
    return connections


# setNextStations: Given a stationList (- id, name, line, x, y - information), and the set of possible connections between stations,
# This function set the dictionary of the possible destinations for each station (including the cost )
def setNextStations(stationList, connections):
    for i in stationList:
        if connections.has_key(int(i.id)):
            i.destinationDic.update(connections[int(i.id)])

    return stationList


# print_stationList: Given a stationList (- id, name, line, x, y - information), it prints the information by terminal
def print_stationList(stationList):
    print "\n"
    print " ______________ STATION LIST________________"
    print "\n"
    for i in stationList:
        print " ID : " + str(i.id) + " - " + str(i.name) + " linea: " + str(i.line) + "   pos: (" + str(
            i.x) + "," + str(i.y) + ")"
    print "\n"
    print "\n"


# print_connections: Given a connections dictionary, it prints the information by terminal
def print_connections(connections):
    print "\n"
    print " ______________ CONNECTIONS ________________"
    print "\n"
    for i in connections.keys():
        print " ID : " + str(i) + "  "
        for j in connections[i].keys():
            print "           " + str(j) + " : " + str(connections[i][j])
    #print "\n"
    #print "\n"

def print_dictionary(stationList):
    print "\n"
    print " ______________ DICTIONARY ________________"
    print "\n"
    for i in stationList:
            print " ID : "+  str(i.id) + "  -->   " + str(i.destinationDic)
    print "\n"
    print "\n"