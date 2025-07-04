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
from game import Directions
from typing import List

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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    "*** YOUR CODE HERE ***"
        
    stack = [problem.getStartState()]
    visited = set()
    path = []
    previous = {}
    while len(stack)>0:
        currState = stack.pop()
        visited.add(currState)
        if problem.isGoalState(currState):
            while currState!=problem.getStartState():
                (currState, direction) = previous[currState]
                path.append(direction)
            path.reverse()
            return path
        for successor in problem.getSuccessors(currState):
            if successor[0] not in visited:
                stack.append(successor[0])
                previous[successor[0]] = (currState, successor[1])
                
def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    queue = [problem.getStartState()]
    visited = set()
    visited.add(problem.getStartState())
    path = []
    previous = {}
    while len(queue)>0:
        currState = queue.pop(0)
        if problem.isGoalState(currState):
            while currState!=problem.getStartState():
                (currState, direction) = previous[currState]
                path.append(direction)
            path.reverse()
            return path
        for successor in problem.getSuccessors(currState):
            if successor[0] not in visited:
                queue.append(successor[0])
                visited.add(successor[0])
                previous[successor[0]] = (currState, successor[1])

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    pq = util.PriorityQueue()
    pq.push(problem.getStartState(), 0)
    distances = {problem.getStartState(): 0}
    visited = set()
    path = []
    previous = {}
    while not pq.isEmpty():
        currState = pq.pop()
        
        if problem.isGoalState(currState):
            while currState!=problem.getStartState():
                (currState, direction) = previous[currState]
                path.append(direction)
            path.reverse()
            return path
        
        for successor in problem.getSuccessors(currState):
            if successor[0] not in visited:
                dist = distances.get(currState, 0) + successor[2]
                if successor[0] not in distances or dist < distances[successor[0]]:
                    pq.push(successor[0], dist)
                    distances[successor[0]] = dist
                    previous[successor[0]] = (currState, successor[1])

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    pq = util.PriorityQueue()
    pq.push(problem.getStartState(), heuristic(problem.getStartState(), problem))
    distances = {problem.getStartState(): 0}
    path = []
    previous = {}
    while not pq.isEmpty():
        currState = pq.pop()
        
        if problem.isGoalState(currState):
            while currState!=problem.getStartState():
                (currState, direction) = previous[currState]
                path.append(direction)
            path.reverse()
            return path
        
        for successor in problem.getSuccessors(currState):
            dist = distances.get(currState, 0) + successor[2]
            if successor[0] not in distances or dist < distances[successor[0]]:
                pq.push(successor[0], dist + heuristic(successor[0], problem))
                distances[successor[0]] = dist
                previous[successor[0]] = (currState, successor[1])

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
