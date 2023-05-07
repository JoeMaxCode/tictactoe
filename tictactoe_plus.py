from data import * 
import numpy as np

# Initialize pygame
pygame.font.init()

# Sound and music
# Bg music
pygame.mixer.music.load('music/bg_music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
#Click sound
click_sound = pygame.mixer.Sound('music/pop_sound.wav')
# Winner sound
win_sound = pygame.mixer.Sound('music/winner_sound.wav')

pygame.display.set_caption("TicTacToe")

class Board:
	# Screen Title
	def __init__(self):
		self.center_space()
		self.saved_marks = np.zeros((rows,cols))
	
	# Getting the center coordinates for each space
	# In order to place the X or O in the exact middle of each space
	def center_space(self):
		self.middle_x = SQUARESPACE//2
		self.middle_y = SQUARESPACE//2

		for i in range(3):
			if i == 0:
				centerX.append(self.middle_x)
				centerY.append(self.middle_y)
			elif i == 1:
				centerX.append(self.middle_x+SQUARESPACE)
				centerY.append(self.middle_x+SQUARESPACE)
			elif i == 2:
				centerX.append(self.middle_x+SQUARESPACE*2)
				centerY.append(self.middle_x+SQUARESPACE*2)

	# Saves the inputs made by the user on the board
	def marks(self, rows, cols, player):
		self.saved_marks[rows][cols] = player

	# Checks if the square the user chose is empty, if empty, returns true
	def check_empty(self, rows, cols):
		if self.saved_marks[rows][cols] == 0:
			return True
		else: 
			return False

	# Check if there is a tie
	def check_tie(self, row, col):
		for lst in self.saved_marks:
			for value in lst:
				if value == 0:
					return False
		return True


	# Check who won
	def get_winner(self, row, col, player):
		# Check if its a horizontal win
		if col == 0:
			if (self.saved_marks[row][col+1] == player and
		 	self.saved_marks[row][col+2] == player):
				return True
		elif col == 1:
			if (self.saved_marks[row][col-1] == player and
		 	self.saved_marks[row][col+1] == player):
		 	 	return True
		elif col == 2:
			if (self.saved_marks[row][col-1] == player and
		 	self.saved_marks[row][col-2] == player):
		 		return True
		# Check if its a vertical win
		if row == 0:
			if (self.saved_marks[row+1][col] == player and
		 	self.saved_marks[row+2][col] == player):
		 		return True
		elif row == 1:
			if (self.saved_marks[row-1][col] == player and
		 	self.saved_marks[row+1][col] == player):
		 		return True
		elif row == 2:
		 	if (self.saved_marks[row-1][col] == player and
		 	self.saved_marks[row-2][col] == player):
		 		return True

		 # Check if its a diagonal win
		if row == 0 and col == 0:
			if (self.saved_marks[row+1][col+1] == player and
		 	self.saved_marks[row+2][col+2] == player):
		 		return True
		elif row == 1 and col == 1: # Two possibilities here
			if (self.saved_marks[row-1][col-1] == player and
		 	self.saved_marks[row+1][col+1] == player):
		 		return True
			elif (self.saved_marks[row-1][col+1] == player and
		 	self.saved_marks[row+1][col-1] == player):
		 		return True
		elif row == 2 and col == 2:
			if (self.saved_marks[row-1][col-1] == player and
		 	self.saved_marks[row-2][col-2] == player):
		 		return True
		elif row == 0 and col == 2:
			if (self.saved_marks[row+1][col-1] == player and
		 	self.saved_marks[row+2][col-2] == player):
		 		return True
		elif row == 2 and col == 0:
			if (self.saved_marks[row-1][col+1] == player and
		 	self.saved_marks[row-2][col+2] == player):
		 		return True

	def change_player(self, player):
		if player == 1:
			player = 2
		else:
			player = 1
		return player


		



class Game:

	def __init__(self):
		WIN.fill( BG_COLOR )
		self.menu_screen()
		self.player = 1

	def menu_screen(self):
		self.menu = Menu()
		self.start_game()

	def start_game(self):	
		WIN.fill(BG_COLOR)
		self.board = Board()
		self.lines()
	# Setting up lines on board
	def lines(self):
		self.show_score(x_score, o_score)
		self.line_pos = SQUARESPACE
		for l in range(v_lines):
			pygame.draw.line(WIN, BLACK, (self.line_pos, 0), (self.line_pos, HEIGHT), line_width)
			self.line_pos += SQUARESPACE

		self.line_pos = SQUARESPACE
		for l in range(h_lines):
			pygame.draw.line(WIN, BLACK, (0, self.line_pos), (WIDTH, self.line_pos), line_width)
			self.line_pos +=SQUARESPACE

	# Getting the center x and y coordinates of where the player clicked
	def closest_click(self, pos):
		self.coor_x = centerX[min(range(len(centerX)), key=lambda i: abs(centerX[i]-pos[0]))]
		self.coor_y = centerY[min(range(len(centerY)), key=lambda i: abs(centerY[i]-pos[1]))]

	# Shows on the screen the move made by player X or O
	def show_mark(self, pos, player, row, col):
		click_sound.play()
		self.closest_click(pos)
		# If player is X 
		if player == 1:	
			self.cross_rect = cross.get_rect(center = (self.coor_x, self.coor_y))
			WIN.blit(cross, (self.cross_rect))
		# If player is O
		if player == 2:
			self.circle_rect = circle.get_rect(center = (self.coor_x, self.coor_y))
			WIN.blit(circle, (self.circle_rect))
				
		self.board.marks(row, col, player)
		player = self.board.change_player(player)
		print(self.board.saved_marks)

	def show_winner(self, player, game_state):
		# Shows the winner in the middle of the screen 
		# And adds a point to the scoreboard. If game is tied, no point is added.
		# If game_state == 0 there is a winner, otherwise is a tie.
		self.winner_panel()
		global x_score, o_score
		# If there is a winner
		if game_state == 0:
			if player == 1:
				self.winner = winner_font.render('X PLAYER WINS!!', True, (0, 0, 0))
				self.winner_rect = self.winner.get_rect(center=(WIDTH//2, HEIGHT//2-55))
				x_score += 1
			else:
				self.winner = winner_font.render('O PLAYER WINS!!', True, (0, 0, 0))
				self.winner_rect = self.winner.get_rect(center=(WIDTH//2, HEIGHT//2-55))
				o_score += 1
		# If there isn't a winner
		else:
			self.winner = winner_font.render("IT IS A TIE!!", True, (0, 0, 0))
			self.winner_rect = self.winner.get_rect(center=(WIDTH//2, HEIGHT//2-55))

		WIN.blit(self.winner, self.winner_rect)
		win_sound.play()	

	def winner_panel(self):
		# Sets the panel where the winner will be shown
		second_surface = pygame.Surface([WIDTH//2, HEIGHT//2])
		surface_border = pygame.Surface([WIDTH//2+20, HEIGHT//2+20])

		second_rect = second_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
		border_rect = surface_border.get_rect(center=(WIDTH//2, HEIGHT//2))


		second_surface.fill(BG_COLOR)
		surface_border.fill((200, 150, 0))

		WIN.blit(surface_border, border_rect)
		WIN.blit(second_surface, second_rect)

	def show_score(self, x_score, o_score):
		# Shows the scores of both player at the top right of the screen
		# Scores will get reset when user returns to the menu
		self.scores = score_font.render(f"X Wins: {str(x_score)}  |  O Wins: {str(o_score)}",
		 True, RED)
		WIN.blit(self.scores, (WIDTH-SQUARESPACE+13, 2))

	def update_screen(self, pos, row, col):
		# Saves the spot that the player chose
		# Shows the mark on the screen
		# Checks if there is a winner

		self.show_mark(pos, self.player, row, col)
		global run
		if self.board.get_winner(row, col, self.player): 
			self.show_winner(self.player, 0)
			self.replay_display()
			run = self.replay()
			if run:
				self.restart()
		elif self.board.check_tie(row, col):
			self.show_winner(self.player, 1)
			self.replay_display()
			run = self.replay()
			if run:
				self.board.change_player(self.player)
				self.restart()
		
		self.player = self.board.change_player(self.player)
		
	def replay_display(self):
		# After a game, this method will display an option to play again or quit the game
		# It will be in the winner panel under the announcement of the winner
		# Replay button
		self.replay_button = pygame.Rect(WIDTH//2, HEIGHT//2, 100, 25)
		self.replay_button.centerx = 255
		self.replay_button.centery = 280
		pygame.draw.rect(WIN, (0, 0, 0), self.replay_button, border_radius=2) 

		self.play_again = replay_font.render('Play Again', True, (255, 255, 255))
		self.play_rect = self.play_again.get_rect(center=(255, 280))
		WIN.blit(self.play_again, self.play_rect)

		# Quit button
		self.quit_button = pygame.Rect(WIDTH//2, HEIGHT//2, 100, 25)
		self.quit_button.centerx = 255
		self.quit_button.centery = 320
		pygame.draw.rect(WIN, (0, 0, 0), self.quit_button, border_radius=2) 

		self.quit = replay_font.render('Quit', True, (255, 255, 255))
		self.quit_rect = self.quit.get_rect(center=(255, 320))
		WIN.blit(self.quit, self.quit_rect)

	def replay(self):
		# After a game, player can choose play again or quit the game
		pygame.display.update()
		loop = True
		global run
		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					loop = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.pos = pygame.mouse.get_pos()
					if self.quit_button.collidepoint(self.pos):
						run = False
						loop = False
						return run
					if self.play_rect.collidepoint(self.pos):
						click_sound.play()
						run = True
						loop = False
						return run

	def restart(self):
		self.board.saved_marks = np.zeros((rows, cols))
		self.start_game() 
		
class Menu:
	def __init__(self):
		WIN.fill(BG_COLOR)
		self.choose_option()

	def title(self):
		self.game_title = title_font.render('TicTacToe', True, (0, 0, 0))
		self.title_rect = self.game_title.get_rect(center=(WIDTH//2, HEIGHT//2-40))
		WIN.blit(self.game_title, self.title_rect)

	def menu_display(self):
		# Creating buttons on the screen
		# Buttons
		self.pvp_button = pygame.Rect((WIDTH//2, HEIGHT//2+50, 210, 50))
		self.exit_button = pygame.Rect((WIDTH//2, HEIGHT//2+50, 210, 50))

		# Buttons' rect
		self.pvp_button.centerx = WIDTH//2
		self.pvp_button.centery = HEIGHT//2+100

		self.exit_button.centerx = WIDTH//2
		self.exit_button.centery = HEIGHT//2+180

		# Buttons text
		self.pvp_mode = modes_font.render("Start Game", True, BLACK)
		self.exit = modes_font.render("Exit",True, BLACK)

		# Text rect
		self.pvp_txt_rect = self.pvp_mode.get_rect(center=(250, 250+100))
		self.exit_txt_rect = self.exit.get_rect(center=(250, 250+180))

		# Blit to the screen the rects, which will serve as buttons
		# And the text for each corresponding rect
		# Draw Rects/buttons
		pygame.draw.rect(WIN, (RED), self.pvp_button, border_radius=30)
		pygame.draw.rect(WIN, (RED), self.exit_button, border_radius=30)

		# Blit text
		WIN.blit(self.pvp_mode, self.pvp_txt_rect)
		WIN.blit(self.exit, self.exit_txt_rect)

	def choose_option(self):
		# User will pick which gamemode to play or exit the game
		loop = True
		global run
		self.title()
		self.menu_display()
		pygame.display.update()
		while loop:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
					loop = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.pos = pygame.mouse.get_pos()
					# Player vs player mode
					if self.pvp_button.collidepoint(self.pos):
						loop = False
					# Exit game
					if self.exit_button.collidepoint(self.pos):
						run = False
						loop = False
		
		click_sound.play()



						












	
# Main loop
run = True
def main():
	global run
	game = Game()
	menu = game.menu
	board = game.board 
	player = game.player

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos
				row = pos[1] // SQUARESPACE
				col = pos[0] // SQUARESPACE

				# Check if space chosen is empty
				if not board.check_empty(row, col) == False:
					game.update_screen(pos, row, col)
				else:
					print('hi')
					



		pygame.display.update()
		clock.tick(60)
				

	

	pygame.quit()

		

if __name__ == '__main__':
	main()