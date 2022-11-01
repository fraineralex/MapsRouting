from sre_constants import FAILURE, SUCCESS
import heapq
import queue

def uniform_cost_search(initialState, goalTest):
  frontier = heapq.heapify(initialState)
  explored = []

  while frontier != []:
    state = frontier.deleteMin()
    explored.add(state)

    if goalTest(state):
        return SUCCESS(state)

    for neighbor in state.neighbor():
        if neighbor not in frontier or explored:
            frontier.insert(neighbor)
        elif neighbor in frontier:
            frontier.decreaseKey(neighbor)

  return FAILURE

 
#Graph example
graph = {
  'San Juan': [('Azua', 20), ('Barahona', 30), ('La Romana', 50)],
  'Azua': [('San Cristobal', 40)],
  'Barahona': [('La Romana', 40)],
  'San Cristobal': [('La Romana', 10), ('Santo Domingo', 20)],
  #'G': []
}

#Calculate the total const of a path
def path_km(path):
  total_km = 0
  for (neighbor, km) in path:
    total_km += km
  return total_km, path[-1] [0] # ==> The queue items will sort based on total_km, but if two items have the same total_km, then sort by node name (alphabetically)

#Uniform km Search function
def uniform_cost_search(initialState, goalState):
  explored = []
  frontier = [[(initialState, 0)]]

  while frontier:
    frontier.sort(key=path_km) # ==> sorting by km
    state = frontier.pop(0) # ==> choosing least km
    neighbor = state[-1][0]
     
    if neighbor in explored:
      continue
    explored.append(neighbor)
    if neighbor == goalState:
      return state
    else:
      for (neighbor, km) in graph.get(neighbor, []):
        new_state = state.copy()
        new_state.append((neighbor, km))
        frontier.append(new_state)


test = uniform_cost_search('San Juan', 'Santo Domingo')
print('Start point:', test[0][0])
print('Goal:', path_km(test)[1])
print('The shortest route is:', test)
print('Kilometers quantity:', path_km(test)[0], 'km')
