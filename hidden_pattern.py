from random_word import get_word
import streamlit as st

def initialize_game(state):
    if "word" not in state:
        state.word, state.hint = get_word()
    if "clue" not in state:
        state.clue = ["-"] * len(state.word)
    if "letters_tried" not in state:
        state.letters_tried = []
    if "letters_wrong" not in state:
        state.letters_wrong = 0 
    if "game_over" not in state:
        state.game_over = False
    if "hint_offered" not in state:
        state.hint_offered = False

def display_game_info(state):
    st.write(f"The word has {len(state.word)} letters.")
    st.markdown(f"### Word: ```{' '.join(state.clue)}```")

def display_remaining_lives(state):
    remaining_lives = 6 - st.session_state.letters_wrong
    st.write(f"Remaining Lives: {remaining_lives}")

def offer_hint(state):
    if state.letters_wrong >= 2 and not state.hint_offered:
        if st.button("Do you want a hint?"):
            state.hint_offered = True
            st.info(f"Hint: {state.hint}")