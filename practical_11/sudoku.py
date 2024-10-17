import random
import math
def initialize():
	print(" * WELCOME TO SUDOKU * ")
	size = int(input("Enter the size you want : "))
	grid = [list(" "*size) for i in range(size)]
	#game_state = [[" " for i in range(size)] for j in range(size)]
	grid = create_puzzle(size)
	#print(display_grid(grid,size))
	levels = {1:("Very Easy" , 20) , 2:("Easy", 35) , 3:("Medium",50),4:("Hard" ,60) , 5:("Very Hard" , 75)}
	for key,value in levels.items():
		print(f"Level {key} : {value[0]}")
	level = int(input("Select a level :  "))
	hidden_feilds_counter = int(((levels[level][1]*(size*size))/100))
	hidden_feilds =[]
	all_possibility = list(range(size*size))
	for _ in range(hidden_feilds_counter):
		n = all_possibility.pop(random.randint(0,len(all_possibility)-1))
		row,col = n//size,n%size	
		hidden_feilds.append((math.ceil(row),math.ceil(col)))
	
	#put "X" in place of empty feilds that are hidden
	for r,c in hidden_feilds:
		grid[r][c] = "X"
		
	return grid,size,hidden_feilds


def start_game(grid ,size,hidden_feilds):
	display_grid(grid,size)
	for r,c in hidden_feilds:
		grid[r][c] = int(input(f"Enter value for row {r+1} and column {c+1} : "))
		display_grid(grid,size)
	return grid


def create_puzzle(size):
	grid = [list(" "*size) for i in range(size)]
	possible_set = set(range(1,size+1))
	for row in range(size):
		for col in range(size):
			available_set = set(grid[row]+[row[col] for row in grid])
			final = list(possible_set - available_set)
			if final:
				grid[row][col] = final[random.randint(0,len(final)-1)]
			else:
				return create_puzzle(size)	#create new puzzle forgetting the previous one
	return grid

def display_grid(game_state, size):
	print("----"*size)
	for row in range(size):
		for col in range(size):
            		print(f" {game_state[row][col]} ", end="|")
		print()
		print("----"*size)

def is_winner(grid,size):
	for i in range(size):
		row_values,col_values = set(),set()
		for j in range(size):
			if grid[i][j] in row_values or grid[j][i] in col_values:
				return False
			if grid[i][j] != " ":
				row_values.add(grid[i][j])
			if grid[j][i] != " ":
				col_values.add(grid[j][i])
	return True

def sudoku():
	grid , size,hidden_fields = initialize()
	grid = start_game(grid,size,hidden_fields)
	display_grid(grid,size)
	if is_winner(grid,size):
		print(" Congrats , You Won! ")
	else:
		print(" You lose Please try again! ")
sudoku()
