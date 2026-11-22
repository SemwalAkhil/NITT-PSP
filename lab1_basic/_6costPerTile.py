# 6. Write a program to calculate the cost per tile for a given area and total cost.
# Input: (1000 5000 10), (5000 2000 5)
# Output: Cost per tile:  50.0, Cost per tile:  20.0

total_area = float(input("Enter total area: "))
total_cost = float(input("Enter total cost: "))
tile_area = float(input("Enter tile area: "))

num_tiles = total_area / tile_area
cost_per_tile = total_cost / num_tiles
print("Cost per tile: ", cost_per_tile)
