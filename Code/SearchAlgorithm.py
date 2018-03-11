# This file contains all the required routines to make an A* search algorithm.
#
__authors__ = 'TO_BE_FILLED'
__group__ = 'DL01'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

from SubwayMap import *
import math


class Node:
    # __init__ Constructor of Node Class.
    def __init__(self, station, father):
        """
        __init__: 	Constructor of the Node class
        :param
                - station: STATION information of the Station of this Node
                - father: NODE (see Node definition) of his father
        """

        self.station = station      # STATION information of the Station of this Node
        self.g = 0                  # REAL cost - depending on the type of preference -
                                    # to get from the origin to this Node
        self.h = 0                  # REAL heuristic value to get from the origin to this Node
        self.f = 0                  # REAL evaluate function
        if father == None:
            self.parentsID = []
        else:
            self.parentsID = [father.station.id]
            self.parentsID.extend(father.parentsID)  # TUPLE OF NODES (from the origin to its father)
        self.father = father        # NODE pointer to his father
        self.time = 0               # REAL time required to get from the origin to this Node
                                    # [optional] only useful for GUI
        self.num_stopStation = 0    # INTEGER number of stops stations made from the origin to this Node
                                    # [optional] Only useful for GUI
        self.walk = 0               # REAL distance made from the origin to this Node
                                    # [optional] Only useful for GUI
        self.transfers = 0          # INTEGER number of transfers made from the origin to this Node
                                    # [optional] Only useful for GUI

    def setEvaluation(self):
        """
        setEvaluation: 	Calculates the Evaluation Function. Actualizes .f value
       
        """

        self.f = self.g + self.h

    def setHeuristic(self, typePreference, node_destination, city):
        """
        setHeuristic: 	Calculates the heuristic depending on the preference selected
        :params
                - typePreference: INTEGER Value to indicate the preference selected: 
                                0 - Null Heuristic
                                1 - minimum Time
                                2 - minimum Distance 
                                3 - minimum Transfers
                                4 - minimum Stops
                - node_destination: PATH of the destination station
                - city: CITYINFO with the information of the city (see CityInfo class definition)
        """

        if typePreference == 1:
            distance = euclideanDistance(x1=self.station.x,
                                         x2=node_destination.station.x,
                                         y1=self.station.y,
                                         y2=node_destination.station.y)

            # avg_lines_velocity = (origin line velocity + destination line velocity) / 2.0
            avg_lines_velocity = (city.velocity_lines[self.station.line - 1] +
                                  city.velocity_lines[node_destination.station.line - 1]) / 2.0

            self.h = distance / avg_lines_velocity  # time = distance / velocity

        if typePreference == 2:
            self.h = euclideanDistance(x1=self.station.x,
                                       x2=node_destination.station.x,
                                       y1=self.station.y,
                                       y2=node_destination.station.y)

        elif typePreference == 3:
            if self.station.line != node_destination.station.line:
                self.h = 1
            else:
                self.h = 0

        elif typePreference == 4:
            # Same station, no stops
            if node_destination.station.name == self.station.name:
                self.h = 0
            # adjacent station, 1 stop
            elif node_destination.station.id in self.station.destinationDic.keys():
                self.h = 1
            # no "adjacent", same line, 2 stops (2 stations away at least, 2 stops at least) !!WRONG!! EDIT ME
            elif node_destination.station.line == self.station.line:
                self.h = 2
            # no adjacent, different line, 1 stop (stations id are for combination of ID+Line, so it can be "adjacent"
            #  meaning 1 stop if the destination is on a different line (+1 transfer)
            else:
                self.h = 1

        elif typePreference == 0:
            # Null Heuristic
            self.h = 0
        else:
            # Do the default
            print "Set correct type preference"

    def setRealCost(self, costTable):
        """
        setRealCost: 	Calculates the real cost depending on the preference selected
        :params
                 - costTable: DICTIONARY. Relates each station with their adjacency an their real cost. NOTE that this
                             cost can be in terms of any preference.
        """

        if self.father:
            self.g = self.father.g + costTable[self.father.station.id][self.station.id]


def euclideanDistance(x1, x2, y1, y2):

    return math.sqrt(abs(x1-x2)**2+abs(y1-y2)**2)


def Expand(fatherNode, stationList, typePreference, node_destination, costTable, city):
    """
        Expand: It expands a node and returns the list of connected stations (childrenList)
        :params
                - fatherNode: NODE of the current node that should be expanded
                - stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)
                - typePreference: INTEGER Value to indicate the preference selected:
                                0 - Null Heuristic
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
                                4 - minimum Stops
                - node_destination: NODE (see Node definition) of the destination
                - costTable: DICTIONARY. Relates each station with their adjacency an their real cost. NOTE that this
                             cost can be in terms of any preference.
                - city: CITYINFO with the information of the city (see CityInfo class definition)
        :returns
                - childrenList:  LIST of the set of child Nodes for this current node (fatherNode)

    """

    childrenList = []
    for destination in city.adjacency[fatherNode.station.id].keys():
        child = Node(stationList[destination - 1], fatherNode)
        childrenList.append(child)

        # TODO: Add extra part

        child.setHeuristic(typePreference, node_destination, city)
        child.setRealCost(costTable)
        child.setEvaluation()

    return childrenList


def RemoveCycles(childrenList):
    """
        RemoveCycles: It removes from childrenList the set of childrens that include some cycles in their path.
        :params
                - childrenList: LIST of the set of child Nodes for a certain Node
        :returns
                - listWithoutCycles:  LIST of the set of child Nodes for a certain Node which not includes cycles
    """

    # Work In Progress EDIT ME
    listWithoutCycles = []
    print "==LIST=="
    for child in childrenList:

        childPath = []
        if child.father is not None:
            current = child.father
            cycle = False
            if child.station.id != current.station.id:
                childPath.append(child.station.id)
            print "LIST"
            print child.station.id
            while (current.father is not None) and (cycle is False):
                if current.station.id != current.father.station.id:
                    childPath.append(current.station.id)
                print (current.station.id)
                current = current.father
                cycle = FindDuplicates(childPath)

            if cycle is False:
                listWithoutCycles.append(child)
        else:
            listWithoutCycles.append(child)

    return listWithoutCycles

def FindDuplicates(in_list):
    unique = set(in_list)
    for each in unique:
        count = in_list.count(each)
        if count > 1:
            return True
    return False

def RemoveRedundantPaths(childrenList, nodeList, partialCostTable):
    """
        RemoveRedundantPaths:   It removes the Redundant Paths. They are not optimal solution!
                                If a node is visited and have a lower g in this moment, TCP is updated.
                                In case of having a higher value, we should remove this child.
                                If a node is not yet visited, we should include to the TCP.
        :params
                - childrenList: LIST of NODES, set of childs that should be studied if they contain rendundant path
                                or not.
                - nodeList : LIST of NODES to be visited
                - partialCostTable: DICTIONARY of the minimum g to get each key (Node) from the origin Node
        :returns
                - childrenList: LIST of NODES, set of childs without rendundant path.
                - nodeList: LIST of NODES to be visited updated (without redundant paths)
                - partialCostTable: DICTIONARY of the minimum g to get each key (Node) from the origin Node (updated)
    """


def sorted_insertion(nodeList, childrenList):
    """ Sorted_insertion:   It inserts each of the elements of childrenList into the nodeList.
							The insertion must be sorted depending on the evaluation function value.
							
		: params:
			- nodeList : LIST of NODES to be visited
			- childrenList: LIST of NODES, set of childs that should be studied if they contain rendundant path
                                or not.
		:returns
            - nodeList: sorted LIST of NODES to be visited updated with the childrenList included
	"""

def getPosibleDestinations(stationList):
    """
    
    :param stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)
    :return: 
    """

def setCostTable(typePreference, stationList, city):
    """
    setCostTable :      Real cost of a travel.
    :param
            - typePreference: INTEGER Value to indicate the preference selected:
                                0 - Adjacency
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
                                4 - minimum Stops
            - stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)
            - city: CITYINFO with the information of the city (see CityInfo class definition)
    :return:
            - costTable: DICTIONARY. Relates each station with their adjacency an their g, depending on the
                                 type of Preference Selected.
    """

    costTable = {}
    if typePreference == 1:
        for station in stationList:
            costTable.update({station.id: station.destinationDic})

    elif typePreference == 2:
        for station in stationList:
            costTable[station.id] = {}
            vel = city.velocity_lines[station.line - 1]
            for destination, time in station.destinationDic.items():
                if station.x == stationList[destination-1].x and \
                   station.y == stationList[destination-1].y:
                    costTable[station.id][destination] = 0
                else:
                    costTable[station.id][destination] = time*vel  # distance = time*velocity

    elif typePreference == 3:
        for station in stationList:
            costTable[station.id] = {}
            for destination in station.destinationDic.keys():
                if station.x == stationList[destination-1].x and \
                   station.y == stationList[destination-1].y:
                    costTable[station.id][destination] = 1
                else:
                    costTable[station.id][destination] = 0

    elif typePreference == 4:
        for station in stationList:
            costTable[station.id] = {}
            for destination in station.destinationDic:
                if station.x == stationList[destination - 1].x and \
                   station.y == stationList[destination - 1].y:
                    costTable[station.id][destination] = 0
                else:
                    costTable[station.id][destination] = 1

    return costTable


def coord2station(coord, stationList):
    """
    coord2station :      From coordinates, it searches the closest station.
    :param
            - coord:  LIST of two REAL values, which refer to the coordinates of a point in the city.
            - stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)

    :return:
            - possible_origins: List of the Indexes of the stationList structure, which corresponds to the closest
            station
    """

    possible_origins = []

    x = coord[0]
    y = coord[1]

    minDistance = -1

    for index, station in enumerate(stationList):
        sx = station.x
        sy = station.y
        dx = abs(sx - x)
        dy = abs(sy - y)
        # Euclidean distance
        distance = ((dx * dx + dy * dy) ** 0.5)

        if distance == minDistance:
            possible_origins.append(index)

        elif distance < minDistance or minDistance == -1:
            minDistance = distance
            possible_origins = [index]

    return possible_origins


def AstarAlgorithm(stationList, coord_origin, coord_destination, typePreference, city, flag_redundants):
    """
     AstarAlgorithm: main function. It is the connection between the GUI and the AStar search code.
     INPUTS:
            - stationList: LIST of the stations of a city. (- id, name, destinationDic, line, x, y -)
            - coord_origin: TUPLE of two values referring to the origin coordinates
            - coord_destination: TUPLE of two values referring to the destination coordinates
            - typePreference: INTEGER Value to indicate the preference selected:
                                0 - Adjacency
                                1 - minimum Time
                                2 - minimum Distance
                                3 - minimum Transfers
                                4 - minimum Stops
            - city: CITYINFO with the information of the city (see CityInfo class definition)
			- flag_redundants: [0/1]. Flag to indicate if the algorithm has to remove the redundant paths (1) or not (0)
			
    OUTPUTS:
            - time: REAL total required time to make the route
            - distance: REAL total distance made in the route
            - transfers: INTEGER total transfers made in the route
            - stopStations: INTEGER total stops made in the route
            - num_expanded_nodes: INTEGER total expanded nodes to get the optimal path
            - depth: INTEGER depth of the solution
            - visitedNodes: LIST of INTEGERS, IDs of the stations corresponding to the visited nodes
            - idsOptimalPath: LIST of INTEGERS, IDs of the stations corresponding to the optimal path
            (from origin to destination)
            - min_distance_origin: REAL the distance of the origin_coordinates to the closest station
            - min_distance_destination: REAL the distance of the destination_coordinates to the closest station
            


            EXAMPLE:
            return optimalPath.time, optimalPath.walk, optimalPath.transfers,optimalPath.num_stopStation,
            len(expandedList), len(idsOptimalPath), visitedNodes, idsOptimalPath, min_distance_origin,
            min_distance_destination
    """
