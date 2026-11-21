total_area = float(input("Enter total area: "))
total_cost = float(input("Enter total cost: "))
tile_area = float(input("Enter tile area: "))

num_tiles = total_area / tile_area
cost_per_tile = total_cost / num_tiles
print("Cost per tile: ", cost_per_tile)
