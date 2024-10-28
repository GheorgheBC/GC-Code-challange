from collections import deque

# Could not make Networkx in xn and Path to.graphml work so I defined everything manually
# this is the solution for Rate Card 2
# Define connections and pots
Pot = ['B', 'C', 'D', 'E']
Cha = ['F', 'G', 'I', 'H']
Cab = ['A']

cost_per_material = {
    'Cabinet': 1200,
    'Pot': {},  # Initialize Pot costs as a dictionary # It will be calculated as a 20x trench length from Cabinet to the pot
    'Chamber': 200,
    'verge': 40,  # Cost per unit length for verge
    'road': 80  # Cost per unit length for road
}

connections = [
    {'from': 'A', 'to': 'F', 'length': 50, 'material': 'verge'},
    {'from': 'B', 'to': 'F', 'length': 20, 'material': 'verge'},
    {'from': 'C', 'to': 'G', 'length': 50, 'material': 'road'},
    {'from': 'D', 'to': 'H', 'length': 100, 'material': 'road'},
    {'from': 'E', 'to': 'H', 'length': 50, 'material': 'verge'},
    {'from': 'F', 'to': 'G', 'length': 100, 'material': 'verge'},
    {'from': 'G', 'to': 'I', 'length': 40, 'material': 'road'},
    {'from': 'H', 'to': 'G', 'length': 100, 'material': 'road'}
]

# Build adjacency list
graph = {}
for connection in connections:
    frm = connection['from']
    to = connection['to']
    length = connection['length']

    if frm not in graph:
        graph[frm] = []
    if to not in graph:
        graph[to] = []

    graph[frm].append((to, length))
    graph[to].append((frm, length))

# Calculate costs for each pot / track down and register the route to each pot / assign to each pot the new value as = to the length of trench fount from the allocated route
# Find the shortest route from 'A' (Cab) to each Pot and set costs using a Graph/matrix approach, BFS , the most similar with the function If in If While from C++
# Other 2 approaches could be as neighbours or tree

def find_route(start, end):
    queue = deque([(start, [start])])  # Queue stores (current_node, path_so_far)
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == end:
            return path  # Found the route

        if current not in visited:
            visited.add(current)
            for neighbor, _ in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # If no route found


# Calculate total cost of the route / Pot received value
def calculate_route_cost(route):
    total_length = 0
    for i in range(len(route) - 1):
        for connection in connections:
            if (connection['from'] == route[i] and connection['to'] == route[i + 1]) or \
                    (connection['to'] == route[i] and connection['from'] == route[i + 1]):
                total_length += connection['length']
                break
    return total_length




for pot in Pot:
    route = find_route('A', pot)
    if route:
        cost = 20 * calculate_route_cost(route)
        # Add the new variable to cost_per_material
        cost_per_material["Pot"][pot] = cost
        print(f'Route from A to {pot}: {route}, Cost: {cost}')
    else:
        print(f'No route found from A to {pot}.')

# Display the updated costs
print('Updated costs for each pot:', cost_per_material['Pot'])

# Calculate fixed costs using the new set of variable / pots were allocater an int nr
fixed_cost = len(Cab) * cost_per_material['Cabinet'] + sum(cost_per_material['Pot'].values()) + len(Cha) * cost_per_material['Chamber']

# Calculate variable costs based on connections
variable_cost = sum(conn['length'] * cost_per_material[conn['material']] for conn in connections)

# Total cost
total_cost = fixed_cost + variable_cost

# Display result
print(f'Fixed costs: {fixed_cost}')
print(f'Trench costs: {variable_cost}')
print(f'Total cost Netwotk: £{total_cost}')