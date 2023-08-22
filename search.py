# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import *

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def visite(deja_visite, dir):
    for e in deja_visite:
        if e[0][0] == dir[0]:
            return True
    return False

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    start=problem.getStartState()
    s = start
    L=Stack()
    deja_visite=[]
    L.push(((s,"base",0),0))
    deja_visite.append(((s,"base",0),0))
    chemin=[]
    etape=0
    while not L.isEmpty():
        etape=etape+1
        tmp = L.pop()
        dir, indice = tmp
        s=dir[0]
        while visite(deja_visite, dir) and not (dir == (start,"base",0)):
            
            tmp = L.pop()
            dir, indice = tmp
            s=dir[0]
        deja_visite.append(tmp)
        if problem.isGoalState(s):
            while indice != 0:
                chemin.append(dir[1])
                dir, indice = deja_visite[indice][0], deja_visite[indice][1]
            chemin.append(dir[1])
            longueur_chemin = len(chemin)
            chemin_2=[0] * (longueur_chemin-1)
            for i in range(1,longueur_chemin):
                chemin_2[i-1] = chemin[longueur_chemin-1-i]
            return(chemin_2)
        else :
            C = problem.getSuccessors(s)
            for element in C :
                L.push((element,etape))
                
    print("Pas de solution")
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    start=problem.getStartState()
    s = start
    L=Queue()
    deja_visite=[]
    L.push(((s,"base",0),0))
    deja_visite.append(((s,"base",0),0))
    chemin=[]
    etape=0
    while not L.isEmpty():
        etape=etape+1
        tmp = L.pop()
        dir, indice = tmp
        s=dir[0]
        while visite(deja_visite, dir) and not (dir == (start,"base",0)):
            
            tmp = L.pop()
            dir, indice = tmp
            s=dir[0]
        deja_visite.append(tmp)
        if problem.isGoalState(s):
            while indice != 0:
                chemin.append(dir[1])
                dir, indice = deja_visite[indice][0], deja_visite[indice][1]
            chemin.append(dir[1])
            longueur_chemin = len(chemin)
            chemin_2=[0] * (longueur_chemin-1)
            for i in range(1,longueur_chemin):
                chemin_2[i-1] = chemin[longueur_chemin-1-i]
            return(chemin_2)
        else :
            C = problem.getSuccessors(s)
            for element in C :
                L.push((element,etape))
                
    print("Pas de solution")

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    start=problem.getStartState()
    s = start
    priorite = 0
    L=PriorityQueue()
    deja_visite=[]
    L.push(((s,"base",0),0,0),0)
    deja_visite.append(((s,"base",0),0))
    chemin=[]
    etape=0
    while not L.isEmpty():
        etape=etape+1
        dir, indice, priorite = L.pop()
        s=dir[0]
        while visite(deja_visite, dir) and not (dir == (start,"base",0)):
            dir, indice, priorite = L.pop()
            s=dir[0]
        deja_visite.append((dir,indice))
        if problem.isGoalState(s):
            while indice != 0:
                chemin.append(dir[1])
                dir, indice = deja_visite[indice][0], deja_visite[indice][1]
            chemin.append(dir[1])
            longueur_chemin = len(chemin)
            chemin_2=[0] * (longueur_chemin-1)
            for i in range(1,longueur_chemin):
                chemin_2[i-1] = chemin[longueur_chemin-1-i]
            return(chemin_2)
        else :
            C = problem.getSuccessors(s)
            for element in C :
                L.push((element,etape, element[2] + priorite),element[2]+priorite)
                
    print("Pas de solution")
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    start=problem.getStartState()
    s = start
    priorite = 0
    L=PriorityQueue()
    deja_visite=[]
    L.push(((s,"base",0),0,0),0)
    deja_visite.append(((s,"base",0),0))
    chemin=[]
    etape=0
    while not L.isEmpty():
        etape=etape+1
        dir, indice, priorite = L.pop()
        s=dir[0]
        while visite(deja_visite, dir) and not (dir == (start,"base",0)):
            dir, indice, priorite = L.pop()
            s=dir[0]
        deja_visite.append((dir,indice))
        if problem.isGoalState(s):
            while indice != 0:
                chemin.append(dir[1])
                dir, indice = deja_visite[indice][0], deja_visite[indice][1]
            chemin.append(dir[1])
            longueur_chemin = len(chemin)
            chemin_2=[0] * (longueur_chemin-1)
            for i in range(1,longueur_chemin):
                chemin_2[i-1] = chemin[longueur_chemin-1-i]
            return(chemin_2)
        else :
            C = problem.getSuccessors(s)
            for element in C :
                L.push((element,etape, element[2] + priorite),element[2]+priorite+heuristic(element[0],problem))       
    print("Pas de solution")
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
