import streamlit as st

# Check if everything is in its place, otherwise redirect back
if st.query_params.get("utm_source") != "player_selector":
    st.switch_page("main.py")
    
if "lang" not in st.session_state:
    st.switch_page("main.py")
else:
    t = st.session_state.lang

players = st.session_state.get("players")
budget = st.session_state.get("budget")

if players == []:
    st.switch_page("main.py")

if "player_bets" not in st.session_state:
    st.switch_page("main.py")
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

st.set_page_config(page_title=t["title"])

st.page_link("main.py", label=t["home"])

st.title(t["title"])

if progress < 95 and len(players) >= 2:
    st.progress(progress)
    progress = int(progress + progress_chunk)

if player_id_helper < len(players):
    st.sidebar.table(md_list)
    if player_bets[player_id_helper] >= 1:
        st.write(f":rainbow[**{players[player_id_helper]}**], {t["g_bet_text"]} **{player_bets[player_id_helper]}฿**{t["g_bet_text_left"]}")
        player_bet_input = st.number_input(t["g_bet_input_label"], value=None, step=10, min_value=1, max_value=player_bets[player_id_helper], icon="💵")
        if st.button(t["continue"]):
            player_bets[player_id_helper] = player_bets[player_id_helper] - player_bet_input
            player_bet_dict[player_id_helper] = player_bet_input
            st.session_state.player_id_helper = st.session_state.player_id_helper + 1
            st.session_state.player_bets = player_bets
            st.session_state.progress = progress
            st.session_state.player_bet_dict = player_bet_dict
            st.rerun()
# ––––– if someone has no money anymore, delete them ––––––––
    else:
            st.session_state.player_bets = player_bets
            st.session_state.progress = progress
            del st.session_state.players[player_id_helper]
            del st.session_state.player_bets[player_id_helper]
            st.rerun()
elif result_player_id_helper < len(players):
# ––––– continue –––––––––––––––––––––––––––––––––––––––––––––
    st.write(f":rainbow[**{players[result_player_id_helper]}**], {t["g_win_check_text"]}")
    st.sidebar.table(md_list)
    with st.container(horizontal=True):
        if st.button(t["g_win_check_yes"]):
            player_bets[result_player_id_helper] = player_bets[result_player_id_helper] + player_bet_dict[result_player_id_helper] * 2
            st.session_state.result_player_id_helper = st.session_state.result_player_id_helper + 1
            st.rerun()
        if st.button(t["g_win_check_tie"]):
            player_bets[result_player_id_helper] = player_bets[result_player_id_helper] + player_bet_dict[result_player_id_helper]
            st.session_state.result_player_id_helper = st.session_state.result_player_id_helper + 1
            st.rerun()
        if st.button(t["g_win_check_no"]):
            st.session_state.result_player_id_helper = st.session_state.result_player_id_helper + 1
            if player_bets[result_player_id_helper] < 1:
                st.write(f"{players[result_player_id_helper]}, {t["g_win_check_kick_text"]}")
            st.rerun()
else:
    del st.session_state.player_id_helper
    del st.session_state.result_player_id_helper
    del st.session_state.progress
    del st.session_state.player_bet_dict
    st.rerun()