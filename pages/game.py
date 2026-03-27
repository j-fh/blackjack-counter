import streamlit as st
import time

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

if "result_player_id_helper" not in st.session_state:
    st.session_state.result_player_id_helper = 0

result_player_id_helper = st.session_state.result_player_id_helper

if "player_bet_dict" not in st.session_state:
    st.session_state.player_bet_dict = {}

player_bet_dict = st.session_state.player_bet_dict


def create_md_table():
    global md_list
    md_helper = 0
    md_list = {}
    for player in players:
        md_name = players[md_helper]
        md_list[md_name] = player_bets[md_helper]
        md_helper = md_helper + 1

create_md_table()


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="stSidebarCollapseButton"] {display: none;}
    </style>
""", unsafe_allow_html=True)

st.page_link("main.py", label="Startseite")

st.title("Blackjack Zähler")

if progress < 95:
    st.progress(progress)
    progress = int(progress + progress_chunk)

if player_id_helper < len(players):
    st.sidebar.table(md_list)
    st.write(f":rainbow[**{players[player_id_helper]}**], bitte mach deinen Einsatz. Du hast noch **{player_bets[player_id_helper]}฿**")
    player_bet_input = st.number_input("Einsatz", value=None, step=10, min_value=1, max_value=player_bets[player_id_helper], icon="💵")
    if st.button("Weiter"):
        player_bets[player_id_helper] = player_bets[player_id_helper] - player_bet_input
        player_bet_dict[player_id_helper] = player_bet_input
        st.session_state.player_id_helper = st.session_state.player_id_helper + 1
        st.session_state.player_bets = player_bets
        st.session_state.progress = progress
        st.session_state.player_bet_dict = player_bet_dict
        st.rerun()
elif result_player_id_helper < len(players):
# ––––– continue –––––––––––––––––––––––––––––––––––––––––––––
    st.write(f":rainbow[**{players[result_player_id_helper]}**], hast du Gewonnen?")
    st.sidebar.table(md_list)
    if st.button("Ja"):
        player_bets[result_player_id_helper] = player_bets[result_player_id_helper] + player_bet_dict[result_player_id_helper] * 2
        st.session_state.result_player_id_helper = st.session_state.result_player_id_helper + 1
        st.rerun()
    if st.button("Nein"):
        st.session_state.result_player_id_helper = st.session_state.result_player_id_helper + 1
        st.rerun()
else:
    del st.session_state.player_id_helper
    del st.session_state.result_player_id_helper
    del st.session_state.progress
    del st.session_state.player_bet_dict
    st.rerun()