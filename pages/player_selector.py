import streamlit as st

player_bets = []

st.page_link("main.py", label="Startseite")
st.title("Blackjack Zähler")
st.header("Spielerauswahl")
players = st.multiselect(
    "Wer spielt mit?",
    options=[],
    placeholder="Namen der Spieler*innen",
    accept_new_options=True
)

dealer = st.selectbox(
    "Wer ist Dealer?",
    [],
    index=None,
    placeholder="Name des Dealers",
    accept_new_options=True
)

budget = st.number_input("Einsatz", value=500)

if st.button("Weiter"):
    @st.dialog("Passt alles?")
    def show_submit_dialog():
        
        st.write("## Spieler*innen:")
        st.markdown("\n".join(f"- {player}" for player in players))
        if dealer:
            st.write(f"## Dealer: {dealer}")
        st.write("## Budget:", budget)
        if st.page_link("pages/game.py", label="Spiel starten!", query_params={"utm_source": "player_selector"}):
            st.session_state.players = players
            st.session_state.dealer = dealer
            st.session_state.budget = budget
            for player in players:
                player_bets.append(budget)
            st.session_state.player_bets = player_bets
    if players and budget > 0:
        show_submit_dialog()
    else:
        st.error("Mindestens ein Spieler und ein Einsatz größer als 0 sind erforderlich.", icon="❌")