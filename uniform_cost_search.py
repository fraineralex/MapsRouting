from collections import defaultdict
from queue import PriorityQueue
from sre_constants import FAILURE

class Scheme:
    def __init__(self, directed): 
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_frontier(self, neighbor, frontier, km):
        if self.directed:
            state = (km, frontier)
            self.graph[neighbor].append(state)
        else:
            state = (km, frontier)
            self.graph[neighbor].append(state)
            state = (km, neighbor)
            self.graph[frontier].append(state)

    def uniform_cost_search(self, initialState, goalState):
        explored = []  
        frontier = PriorityQueue()
        frontier.put((0, initialState))
        path = []
        
        while not frontier.empty():
            state =  frontier.get()
            
            if state[1] == goalState:
                path += [state]
                frontier.queue.clear()
            else:
                if state[1] in explored:
                    continue
                    
                path += [state]
                explored.append(state[1])

                for neighbor in self.graph[state[1]]:
                        frontier.put((neighbor[0], neighbor[1]))

        if(path):
          return path
        else:
          return FAILURE

city = Scheme(False)
city.graph =  defaultdict(list)
city.add_frontier('S', 'A', 1)
city.add_frontier('S', 'G', 12)
city.add_frontier('A', 'B', 3)
city.add_frontier('A', 'C', 1)
city.add_frontier('C', 'D', 1)
city.add_frontier('B', 'D', 3)
city.add_frontier('C', 'G', 2)
city.add_frontier('D', 'G', 3)
city.graph

defaultdict(list,
            {'S': [(1, 'A'), (12, 'G')],
             'A': [(1, 'S'), (3, 'B'), (1, 'C')],
             'G': [(12, 'S'), (2, 'C'), (3, 'D')],
             'B': [(3, 'A'), (3, 'D')],
             'C': [(1, 'A'), (1, 'D'), (2, 'G')],
             'D': [(1, 'C'), (3, 'B'), (3, 'G')]})
#defaultdict(list, graphs)

#Calculate the total km of a path
def path_km(path):
  total_km = 0
  for (km, neighbor) in path:
    total_km += km
  return total_km, path[-1] [1] 