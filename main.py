import streamlit as st
from hidden_pattern import initialize_game, display_game_info, offer_hint, display_remaining_lives
from user_input import handle_guess, display_guessed_letters
from check_input import check_game_over, reset_game
from graphics import display_hangman

def main():
    st.set_page_config(page_title="Hangman Game", layout="wide")
    st.title("Hangman Game")
    
    # Initialize game
    initialize_game(st.session_state)

    
    # Layout with two columns
    col1, col2 = st.columns(2)
    
    with col1:
        display_game_info(st.session_state)
        display_remaining_lives(st.session_state)
        offer_hint(st.session_state)
        
        if not st.session_state.game_over:
            if "letter" not in st.session_state:
                st.session_state.letter = ""

            def clear():
                st.session_state.letter = st.session_state.widget
                st.session_state.widget = ""
                return st.session_state.letter

            # Text input for letter guessing
            st.text_input(label="Guess a letter:", max_chars=1, key="widget", placeholder="Write a letter.....", on_change=clear)
            letter = st.session_state.letter

            display_guessed_letters(st.session_state)
            handle_guess(st.session_state, letter)
        
        else:
            st.session_state.letter = ""
    
    with col2:
        display_hangman(st.session_state)
        
    if st.session_state.letter:
        check_game_over(st.session_state)
    
    if st.session_state.game_over:
        if st.button("Play Again"):
            reset_game(st.session_state)

if __name__ == "__main__":
    main()
