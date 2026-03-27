import streamlit as st

# Check if everything is in its place, otherwise redirect back
if st.query_params.get("utm_source") != "player_selector":
    st.switch_page("pages/player_selector.py")

players = st.session_state.get("players")
budget = st.session_state.get("budget")

if "player_bets" not in st.session_state:
    st.switch_page("pages/player_selector.py")
else:
    player_bets = st.session_state.player_bets

if "progress" not in st.session_state:
    st.session_state.progress = 0

progress = st.session_state.progress
progress_chunk = 100 / len(players)

if "player_id_helper" not in st.session_state:
    st.session_state.player_id_helper = 0
    
player_id_helper = st.session_state.player_id_helper

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––

st.page_link("main.py", label="Startseite")

st.title("Blackjack Zähler")

if progress < 100:
    st.progress(progress)
    progress = int(progress + progress_chunk)

if player_id_helper < len(players):
    st.write(f":rainbow[**{players[player_id_helper]}**], bitte mach deinen Einsatz. Du hast noch **{player_bets[player_id_helper]}฿**")
    player_bet_input = st.number_input("Einsatz", value=None, step=10, min_value=1, max_value=player_bets[player_id_helper], icon="💵")
else:
    st.success("Alle Einsätze wurden eingegeben.")
    st.write(player_bets)

if player_id_helper < len(players):
    if st.button("Weiter"):
        player_bets[player_id_helper] = player_bets[player_id_helper] - player_bet_input
        st.session_state.player_id_helper = st.session_state.player_id_helper + 1
        st.session_state.player_bets = player_bets
        st.session_state.progress = progress
        st.rerun()