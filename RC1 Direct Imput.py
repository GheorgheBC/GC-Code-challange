# Unsuccessful in reading the doc so I imputed the data manually to sort the rest of the exercise
# Solution for Rate Card 1
# Define variables
Pot = ['B', 'C' , 'D' , 'E']
Cha = [ 'F', 'G' , 'I' , 'H' ]
Cab = [ 'A' ]
connections = [
    {"from": 'A', 'to': 'F', 'length': 50, 'material': 'verge'},
    {'from': 'B', 'to': 'F', 'length': 20, 'material': 'verge'},
    {'from': 'C', 'to': 'G', 'length': 50, 'material': 'road'},
    {'from': 'D', 'to': 'H', 'length': 100, 'material': 'road'},
    {'from': 'E', 'to': 'H', 'length': 50, 'material': 'verge'},
    {'from': 'F', 'to': 'G', 'length': 100, 'material': 'verge'},
    {'from': 'G', 'to': 'I', 'length': 40, 'material': 'road'},
    {'from': 'H', 'to': 'G', 'length': 100, 'material': 'road'}
]

# Cost per material and item type
cost_per_material = {
    "Cabinet": 1000,
    "Pot": 100,
    "Chamber": 200,
    "verge": 50,  # Cost per unit length for verge
    "road": 100   # Cost per unit length for road
}

# Calculate fixed costs
fixed_cost = len(Cab) * cost_per_material['Cabinet'] + len(Pot) * cost_per_material['Pot'] + len(Cha) * cost_per_material['Chamber']

# Calculate variable costs based on connections
variable_cost = sum(conn['length'] * cost_per_material[conn['material']] for conn in connections)

# Total cost
total_cost = fixed_cost + variable_cost

# Display result
print(f'Fixed costs: {fixed_cost}')
print(f'Trench costs: {variable_cost}')
print(f'Total cost Netwotk: £{total_cost}')