def initialize(size):
	game_state = [[" " for _ in range(size)] for _ in range(size)]
	return game_state

def display_grid(game_state, size):
	print("----"*size)
	for row in range(size):
		for col in range(size):
            		print(f" {game_state[row][col]} ", end="|")
		print()
		print("----"*size)

def is_valid_move(game_state, position, size):
    # Check if the position is within the grid
    row, col = position
    if row < 0 or row >= size or col < 0 or col >= size:
        return False
    # Check if the cell is already occupied
    if game_state[row][col] != " ":
        return False
    return True
        
def check_winner(game_state, size, player):
    # Check rows
    for row in range(size):
    		  if all(game_state[row][col] == player for col in range(size)):
            		return True

    # Check columns
    for col in range(size):
        if all(game_state[row][col] == player for row in range(size)):
            return True

    # Check main diagonal (top-left to bottom-right)
    if all(game_state[i][i] == player for i in range(size)):
        return True

    # Check anti-diagonal (top-right to bottom-left)
    if all(game_state[i][size - i - 1] == player for i in range(size)):
        return True

    return False

        
def start_the_game():
	print("Welcome to TIC-TAC-TOE")
	print("Enter player 1 name who will be having inital as X: ")
	player1 = input().strip()
	print("Enter player 2 name who will be having inital as O: ")
	player2 = input().strip()
	players = {player1 : "X" , player2 : "O"}	#initialize the initials to the particular players
	print("Enter the size of matrix you want to play :  ")
	size = int(input())
	game_state =initialize(size)
	display_grid(game_state,size)		#display an empty grid 
                                                                                                 
	for turn in range(size*size):
		if turn%2==0:
			current_player = player1 
		else:
			current_player = player2
		print(f"Its {current_player}'s turn - Enter the position : ")
		while True:
			row,col = map(int,input().split())
			position = (row,col)
			
			if is_valid_move(game_state, position, size):
				break
			else:
				print("Invalid move. Please enter a valid position (row, col): ")
		game_state[row][col] = players[current_player]
		#position = (row, col)
		
        # Display the updated grid
		display_grid(game_state, size)
		if check_winner(game_state,size, players[current_player]):
			print(f"Congratulations! {current_player} wins!")
		return

    # If no winner after all turns, it's a dra
	print("It's a draw!")
		
start_the_game()
