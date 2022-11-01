import main
import uniform_cost_search

test = city.uniform_cost_search('S', 'G')
print('Start point:', test[0][1])
print('Goal:', path_km(test)[1])
print('The shortest route is:', test)
print('Kilometers quantity:', path_km(test)[0], 'km')