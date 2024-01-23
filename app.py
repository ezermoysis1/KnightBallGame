import streamlit as st
from TheEndoftheTrackGame import TheEndoftheTrackGame

def display_interactive_board(game, board_id):
    pawn_symbols = {0: '', 1: '□', 2: '■', 3: '○', 4: '●'}
    ball_symbols = {3, 4}  # Set of ball identifiers

    if 'selected_cell' not in st.session_state:
        st.session_state.selected_cell = None
        st.session_state.move_start = None
        st.session_state.move_end = None
        st.session_state.invalid_move = False
        st.session_state.game_over = False

    for row in range(8):
        cols = st.columns(7)
        for col, each_col in enumerate(cols):
            button_key = f'{board_id}-{row}-{col}'
            pawn_symbol = pawn_symbols[game.board[row, col]]
            if st.session_state.game_over:
                each_col.button(pawn_symbol, key=button_key, disabled=True)
            elif each_col.button(pawn_symbol, key=button_key):
                current_cell = (row, col)
                cell_content = game.board[row, col]
                is_current_players_pawn = cell_content == game.players[game.player_turn]
                is_ball = cell_content in ball_symbols
                start_cell_content = game.board[st.session_state.move_start[0], st.session_state.move_start[1]] if st.session_state.move_start else None

                if st.session_state.selected_cell is None and (is_current_players_pawn or is_ball):
                    st.session_state.selected_cell = 'start'
                    st.session_state.move_start = current_cell
                elif st.session_state.selected_cell == 'start':
                    if start_cell_content in ball_symbols:
                        if is_current_players_pawn and not is_ball:
                            st.session_state.selected_cell = 'end'
                            st.session_state.move_end = current_cell
                        else:
                            st.session_state.selected_cell = None
                            st.session_state.move_start = None
                            st.session_state.invalid_move = True
                    else:
                        if is_current_players_pawn or is_ball:
                            st.session_state.move_start = current_cell
                        else:
                            st.session_state.selected_cell = 'end'
                            st.session_state.move_end = current_cell

    if st.session_state.selected_cell == 'end':
        move_valid = game.make_move(st.session_state.move_start, st.session_state.move_end)

        if move_valid:
            if game.check_win():
                winner = 'Black' if game.player_turn == 'W' else 'White'
                st.markdown(f"**{winner} wins!**")
                st.session_state.game_over = True
            else:
                # If the game is not over, rerun to update the board
                st.experimental_rerun()
        else:
            st.session_state.selected_cell = None
            st.session_state.move_start = None
            st.session_state.move_end = None
            st.session_state.invalid_move = True
            # st.error("Invalid move")  # Display "Invalid Move" here

    
        if move_valid:
            st.session_state.selected_cell = None
            st.session_state.invalid_move = False
            if game.check_win():
                winner = 'Black' if game.player_turn == 'W' else 'White'
                st.markdown(f"**{winner} wins!**")
                st.session_state.game_over = True
        else:
            st.session_state.selected_cell = None
            st.session_state.move_start = None
            st.session_state.move_end = None
            st.session_state.invalid_move = True

    if st.session_state.invalid_move:
        # st.error("Invalid move")
        st.session_state.invalid_move = False

    if st.session_state.game_over:
        if st.button("Restart Game", key=f"restart_button_{board_id}"):
            st.session_state.game = TheEndoftheTrackGame()
            st.session_state.selected_cell = None
            st.session_state.move_start = None
            st.session_state.move_end = None
            st.session_state.invalid_move = False
            st.session_state.game_over = False
            st.session_state.game_started = False

    return st.session_state.game_over



# Initialize game
if 'game' not in st.session_state:
    st.session_state.game = TheEndoftheTrackGame()
    st.session_state.board_id = 0
    st.session_state.game_started = False  # Add a flag to track if the game has started
    st.session_state.instructions_visible = False

game = st.session_state.game

st.title("The End of the Track - Online")
st.markdown("[View the game on Gaya Game](https://www.gaya-game.com/collections/strategy-game/products/the-end-of-the-track)")

# Initialize close_instructions
close_instructions = False

# Initialize show_instructions
show_instructions = False

# Add a button to show/hide instructions
if not st.session_state.instructions_visible:
    show_instructions = st.button("Show Instructions")
else:
    close_instructions = st.button("Show Instructions")

if show_instructions:
    st.image("images/game_instructions.png", caption="Instructions", use_column_width=True)
    st.session_state.instructions_visible = True

if close_instructions:
    st.session_state.instructions_visible = False


game_over = display_interactive_board(game, st.session_state.board_id)


if not game_over and st.session_state.game_started:
    st.markdown(f"**{'White' if game.player_turn == 'W' else 'Black'}'s turn:**")
    if st.session_state.move_start:
        st.write(f"Selected Start Position: {st.session_state.move_start}")
    if st.session_state.move_end:
        st.write(f"Selected End Position: {st.session_state.move_end}")

# Update the game_started flag once a move has been made
if st.session_state.move_start or st.session_state.move_end:
    st.session_state.game_started = True

# Reset the game_started flag when the game is restarted
if st.session_state.game_over and st.button("Restart Game"):
    st.session_state.game = TheEndoftheTrackGame()
    st.session_state.selected_cell = None
    st.session_state.move_start = None
    st.session_state.move_end = None
    st.session_state.invalid_move = False
    st.session_state.game_over = False
    st.session_state.game_started = False  # Reset the flag