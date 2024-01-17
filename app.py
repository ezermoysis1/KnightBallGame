import streamlit as st
from TheEndoftheTrackGame import TheEndoftheTrackGame

# Function to display the board
def display_board(game):
    pawn_symbols = {0: '', 1: '○', 2: '●', 3: '◇', 4: '◆'}
    board_html = "<table style='border-collapse: collapse;'>"

    # Add column headers for horizontal index (top)
    board_html += "<tr><td style='border: none;'></td>"
    for col in range(7):
        board_html += f"<td style='text-align: center; border: 1px solid black; background-color: lightblue;'>{col}</td>"
    board_html += "<td style='border: none;'></td></tr>"

    # Add rows with vertical index
    for row in range(8):
        board_html += "<tr>"

        # Add row header for vertical index
        board_html += f"<td style='text-align: center; border: 1px solid black; background-color: lightblue;'>{row}</td>"

        # Add cells for game board
        for col in range(7):
            pawn_symbol = pawn_symbols[game.board[row, col]]
            board_html += f"<td style='text-align: center; width: 30px; height: 30px; border: 1px solid black; background-color: yellow;'>{pawn_symbol}</td>"

        # Add row trailer for vertical index
        board_html += f"<td style='text-align: center; border: 1px solid black; background-color: lightblue;'>{row}</td>"

        board_html += "</tr>"

    # Add column headers for horizontal index (bottom)
    board_html += "<tr><td style='border: none;'></td>"
    for col in range(7):
        board_html += f"<td style='text-align: center; border: 1px solid black; background-color: lightblue;'>{col}</td>"
    board_html += "<td style='border: none;'></td></tr>"

    board_html += "</table>"
    st.markdown(board_html, unsafe_allow_html=True)



# Initialize game
if 'game' not in st.session_state:
    st.session_state.game = TheEndoftheTrackGame()

game = st.session_state.game

# Title with a link
st.title("The End of the Track - Online")
st.markdown("[View the game on Gaya Game](https://www.gaya-game.com/collections/strategy-game/products/the-end-of-the-track)")


# Display board
display_board(game)

st.write(" ")

st.markdown(f"**{'White' if game.player_turn == 'W' else 'Black'}'s turn:**")

# First row for starting row and column inputs
col1, col2 = st.columns(2)
with col1:
    start_row = st.number_input("Enter starting row:", 0, 7, 0, key="start_row")
with col2:
    start_col = st.number_input("Enter starting column:", 0, 6, 0, key="start_col")

# Second row for ending row and column inputs
col3, col4 = st.columns(2)
with col3:
    end_row = st.number_input("Enter ending row:", 0, 7, 0, key="end_row")
with col4:
    end_col = st.number_input("Enter ending column:", 0, 6, 0, key="end_col")



# Button to make move
if st.button('Make Move'):
    game.make_move((start_row, start_col), (end_row, end_col))
    display_board(game)

    # Check for win condition
    if game.check_win():
        # Identify the other player
        winner = 'Black' if game.player_turn == 'W' else 'White'
        
        st.markdown(f"**{winner} wins!**")
        st.session_state.game = TheEndoftheTrackGame()  # Reset the game
