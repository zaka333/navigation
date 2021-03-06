# !/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains all the required routines to make an A* search algorithm.
__authors__ = """   
                    Zakaria El Haddad - 1462424
                    Alejandro Aznar - 1393102
                    Daniel Amaya - 1456942
                    Adrià Amorós - 1460597
              """
__group__ = 'DM17'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2017- 2018
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

        self.station = station  # STATION information of the Station of this Node
        self.g = 0  # REAL cost - depending on the type of preference -
        # to get from the origin to this Node
        self.h = 0  # REAL heuristic value to get from the origin to this Node
        self.f = 0  # REAL evaluate function
        if father is None:
            self.parentsID = []
        else:
            self.parentsID = [father.station.id]
            self.parentsID.extend(father.parentsID)  # TUPLE OF NODES (from the origin to its father)
        self.father = father  # NODE pointer to his father
        self.time = 0  # REAL time required to get from the origin to this Node
        # [optional] only useful for GUI
        self.num_stopStation = 0  # INTEGER number of stops stations made from the origin to this Node
        # [optional] Only useful for GUI
        self.walk = 0  # REAL distance made from the origin to this Node
        # [optional] Only useful for GUI
        self.transfers = 0  # INTEGER number of transfers made from the origin to this Node
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

            if node_destination.station.name == self.station.name:
                time = 0
            else:
                time = distance / city.max_velocity

            if node_destination.station.name != self.station.name and \
                    node_destination.station.line != self.station.line:
                self.h = time + city.min_transfer
            else:
                self.h = time

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
            # no adjacent, different line, 1 stop (stations id are for combination of ID+Line),
            # so it can be "adjacent" meaning 1 stop if the destination is on a different line (+1 transfer)
            else:
                self.h = 1

        elif typePreference == 0:
            # Null Heuristic
            self.h = 0

        else:
            # Do the default
            pass

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
    return math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)


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

    listWithoutCycles = []

    for child in childrenList:
        if child.father is not None:
            current = child.father
            while (current.father is not None) and (current.station.id != child.station.id):
                current = current.father
            if current.station.id is not child.station.id:
                listWithoutCycles.append(child)
        else:
            listWithoutCycles.append(child)

    return listWithoutCycles


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

    newChildrenList = []

    for child in childrenList:
        if child.station.id in partialCostTable.keys():
            if child.g < partialCostTable[child.station.id]:
                # update partial cost table
                partialCostTable[child.station.id] = child.g
                # remove redundant paths
                nodeList = [node for node in nodeList if node.station.id != child.station.id]
                newChildrenList.append(child)

        else:
            # add new entry
            partialCostTable[child.station.id] = child.g
            newChildrenList.append(child)

    return newChildrenList, nodeList, partialCostTable


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

    for child in childrenList:
        if nodeList:
            current = child.f
            i = 0
            while i < len(nodeList) and nodeList[i].f < current:
                i += 1

            nodeList.insert(i, child)
        else:
            nodeList = [child]

    return nodeList


def getPosibleDestinations(stationList):
    """
    
    :param stationList: LIST of the stations of a city. (- id, destinationDic, name, line, x, y -)
    :return: 
    """
    pass


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
                if station.x == stationList[destination - 1].x and \
                        station.y == stationList[destination - 1].y:
                    costTable[station.id][destination] = 0
                else:
                    costTable[station.id][destination] = time * vel  # distance = time*velocity

    elif typePreference == 3:
        for station in stationList:
            costTable[station.id] = {}
            for destination in station.destinationDic.keys():
                if station.x == stationList[destination - 1].x and \
                        station.y == stationList[destination - 1].y:
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
    else:
        # Do the default
        pass

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

    visitedNodes = []
    idsOptimalPath = [coord2station(coord_destination, stationList)[0]]
    min_distance_origin = 0.0
    min_distance_destination = 0.0

    # '1' = time, '2' = distance, '3' = transfers, '4' = stops
    optimalPath = {'1': 0.0, '2': 0.0, '3': 0, '4': 0}

    if coord_origin == coord_destination:
        pass

    else:
        costTable = {}
        costTable = setCostTable(int(typePreference), stationList, city)

        # creates a Node object with the coordinates of the nearest station
        originNode = Node(stationList[coord2station(coord_origin, stationList)[0]], None)
        destinationNode = Node(stationList[coord2station(coord_destination, stationList)[0]], None)

        partialCostTable = {}
        current = []
        current_children = []

        paths = [originNode]
        while paths and paths[0].station.id != destinationNode.station.id:
            current = paths.pop(0)
            current_children = Expand(current, stationList, int(typePreference), destinationNode, costTable, city)
            current_children = RemoveCycles(current_children)
            if flag_redundants:
                current_children, paths, partialCostTable = RemoveRedundantPaths(current_children, paths, partialCostTable)
            paths = sorted_insertion(paths, current_children)

            visitedNodes.append(current.station.id)

        if paths:
            min_distance_origin = paths[0].g
            min_distance_destination = paths[-1].g

            optimalPath[typePreference] = paths[0].f

            idsOptimalPath = []
            idsOptimalPath.extend(reversed(paths[0].parentsID))
            idsOptimalPath.append(destinationNode.station.id)

    return optimalPath['1'], optimalPath['2'], optimalPath['3'], optimalPath['4'], len(visitedNodes), \
           len(idsOptimalPath) - 1, visitedNodes, idsOptimalPath, min_distance_origin, min_distance_destination