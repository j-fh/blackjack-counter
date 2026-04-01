import streamlit as st


if "lang" not in st.session_state:
    st.switch_page("main.py")
else:
    t = st.session_state.lang
    
player_bets = []

t = st.session_state.lang 

st.set_page_config(page_title=t["ps_title"])


st.page_link("main.py", label=t["home"])
st.title(t["title"])
st.header(t["ps_title"])
players = st.multiselect(
    t["ps_player_input_label"],
    options=[],
    placeholder=t["ps_player_input_placeholder"],
    accept_new_options=True
)

dealer = st.selectbox(
    t["ps_dealer_input_label"],
    [],
    index=None,
    placeholder=t["ps_dealer_input_placeholder"],
    accept_new_options=True
)

budget = st.number_input(t["ps_budget_input_label"], value=500)

if st.button(t["continue"]):
    @st.dialog(t["ps_dialog_label"])
    def show_submit_dialog():
        
        st.write(f"## {t["ps_dialog_players"]}")
        st.markdown("\n".join(f"- {player}" for player in players))
        if dealer:
            st.write(f"## {t["ps_dialog_dealer"]} {dealer}")
        st.write(f"## {t["ps_dialog_budget"]} {budget}")
        if st.page_link("pages/game.py", label=t["ps_dialog_page_link_label"], query_params={"utm_source": "player_selector"}):
            st.session_state.players = players
            st.session_state.dealer = dealer
            st.session_state.budget = budget
            for player in players:
                player_bets.append(budget)
            st.session_state.player_bets = player_bets
    if players and budget > 0:
        show_submit_dialog()
    else:
        st.error(t["ps_input_error_msg"], icon="❌")