import streamlit as st
from TheEndoftheTrackGame import TheEndoftheTrackGame

def display_interactive_board(game, board_id):
    pawn_symbols = {0: '', 1: '○', 2: '●', 3: '◇', 4: '◆'}

    if 'selected_cell' not in st.session_state:
        st.session_state.selected_cell = None
        st.session_state.move_start = None
        st.session_state.move_end = None

    for row in range(8):
        cols = st.columns(7)
        for col, each_col in enumerate(cols):
            # Create a unique key for each button using row, column, and board_id
            button_key = f'{board_id}-{row}-{col}'
            pawn_symbol = pawn_symbols[game.board[row, col]]
            if each_col.button(pawn_symbol, key=button_key):
                if st.session_state.selected_cell is None:
                    st.session_state.selected_cell = 'start'
                    st.session_state.move_start = (row, col)
                elif st.session_state.selected_cell == 'start':
                    st.session_state.selected_cell = 'end'
                    st.session_state.move_end = (row, col)

    if st.session_state.selected_cell == 'end':
        game.make_move(st.session_state.move_start, st.session_state.move_end)
        st.session_state.selected_cell = None
        # display_interactive_board(game, board_id + 1)  # Increment board_id to ensure unique keys

        if game.check_win():
            winner = 'Black' if game.player_turn == 'W' else 'White'
            st.markdown(f"**{winner} wins!**")
            st.session_state.game = TheEndoftheTrackGame()  # Reset the game

# Initialize game
if 'game' not in st.session_state:
    st.session_state.game = TheEndoftheTrackGame()
    st.session_state.board_id = 0  # Initialize a board identifier

game = st.session_state.game

st.title("The End of the Track - Online")
st.markdown("[View the game on Gaya Game](https://www.gaya-game.com/collections/strategy-game/products/the-end-of-the-track)")
display_interactive_board(game, st.session_state.board_id)

st.markdown(f"**{'White' if game.player_turn == 'W' else 'Black'}'s turn:**")

# Display the selected start and end position
if st.session_state.move_start:
    st.write(f"Selected Start Position: {st.session_state.move_start}")
if st.session_state.move_end:
    st.write(f"Selected End Position: {st.session_state.move_end}")
