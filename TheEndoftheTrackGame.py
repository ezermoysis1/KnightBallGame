import numpy as np

class TheEndoftheTrackGame:
    def __init__(self):
        self.board = np.zeros((8, 7), dtype=int)
        self.players = {'W': 1, 'B': 2}
        self.player_turn = 'W'  # White starts first
        self.ball_pawn_combo = {'W': 3, 'B': 4}  # Use integers to represent the ball and pawn combo on the board
        self.initialize_board()

    def initialize_board(self):
        # Place ball and pawn combos on the initial positions
        self.board[0, 1:6] = self.players['B']
        self.board[7, 1:6] = self.players['W']
        self.board[0, 3] = self.ball_pawn_combo['B']
        self.board[7, 3] = self.ball_pawn_combo['W']

    def display_board(self):
        pawn_symbols = {0: '·', 1: '○', 2: '●', 3: '◇', 4: '◆'}
        
        # Print column indices with a space in front
        print("   ", end="")
        for col in range(7):
            print(f" {col}", end="")
        print("\n" + "  +" + "--" * 7 + "+")

        # Print board with row indices and elements
        for row in range(8):
            print(f"{row} |", end=" ")
            for col in range(7):
                pawn_symbol = pawn_symbols[self.board[row, col]]
                print(pawn_symbol, end=" ")
            print("|")

        # Print bottom border
        print("  +" + "--" * 7 + "+")
        print()


    def is_valid_pawn_move(self, start, end):
        # Check if the move is within the board and follows the knight's move pattern
        if not (0 <= start[0] < 8 and 0 <= start[1] < 7 and 0 <= end[0] < 8 and 0 <= end[1] < 7):
            return False

        # Check if there is another pawn (current player's or opponent's) at the destination
        current_player = self.player_turn
        destination_pawn = self.board[end[0], end[1]]

        if destination_pawn != 0:
            return False

        return (abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1) or \
            (abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2)

    def is_valid_ball_move(self, start, end):
        # Check if the move is within the board
        if not (0 <= start[0] < 8 and 0 <= start[1] < 7 and 0 <= end[0] < 8 and 0 <= end[1] < 7):
            return False

        # Check if the end point is on a pawn of the same player
        current_player = self.player_turn
        if self.board[end[0], end[1]] != self.players[current_player]:
            return False

        # Check if the ball is being moved and not just a pawn
        if self.board[start[0], start[1]] != self.ball_pawn_combo[current_player]:
            return False

        # Find all pawns in line with the ball and check if the end position is reachable
        reachable_pawns = self.find_reachable_pawns(start, set())
        return end in reachable_pawns

    def find_reachable_pawns(self, position, visited):
        # Check vertical, horizontal, and diagonal lines for pawns of the current player
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        current_player_pawn = self.players[self.player_turn]
        opponent_player_pawn = self.players['B'] if self.player_turn == 'W' else self.players['W']

        for direction in directions:
            next_pos = (position[0] + direction[0], position[1] + direction[1])

            while 0 <= next_pos[0] < 8 and 0 <= next_pos[1] < 7:
                # Check if the next position has an opponent's pawn
                if self.board[next_pos[0], next_pos[1]] == opponent_player_pawn:
                    break  # Stop this direction if blocked by opponent's pawn

                # Check if the next position has a current player's pawn
                if self.board[next_pos[0], next_pos[1]] == current_player_pawn:
                    if next_pos not in visited:
                        visited.add(next_pos)
                        self.find_reachable_pawns(next_pos, visited)

                next_pos = (next_pos[0] + direction[0], next_pos[1] + direction[1])

        return visited

    def make_move(self, start, end):
        # Perform the move if it's valid
        if self.is_valid_pawn_move(start, end) and self.board[start] == self.players[self.player_turn]:
            self.board[end] = self.board[start]
            self.board[start] = 0
            self.switch_turn()
        elif self.is_valid_ball_move(start, end) and self.board[start] == self.ball_pawn_combo[self.player_turn]:
            self.board[end] = self.ball_pawn_combo[self.player_turn]

            # Leave only the pawn in the position where the ball left

            if self.player_turn == 'W':
                self.board[start] = 1
            elif self.player_turn == 'B':
                self.board[start] = 2
                        
            self.switch_turn()
        else:
            print('This move is not valid')

    def switch_turn(self):
        # Switch the turn between players
        self.player_turn = 'B' if self.player_turn == 'W' else 'W'

    def play(self):
        while True:
            self.display_board()
            print(f"{self.player_turn}'s turn:")
            
            # Get input for move
            start = tuple(map(int, input("Enter starting position (row col): ").split()))
            end = tuple(map(int, input("Enter ending position (row col): ").split()))

            # Make the move
            self.make_move(start, end)

            # Check for win condition
            if self.check_win():
                self.display_board()
                print(f"{self.player_turn} wins!")
                break

    def check_win(self):
        # Check if a ball and pawn combo is on the opponent's side
        for col in range(1, 6):
            if self.board[0, col] == self.ball_pawn_combo['W']:
                return True
            if self.board[7, col] == self.ball_pawn_combo['B']:
                return True
        return False

if __name__ == "__main__":
    game = TheEndoftheTrackGame()
    game.play()
