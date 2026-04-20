import streamlit as st

LANG = {
    "de": {
        "home": "Startseite",
        "title": "Blackjack Zähler",
        "continue": "Weiter",

        "m_info_text": "Eine Blackjack-App, die Chips/Währung ersetzt - gespielt wird aber trotzdem mit echten Karten. Entstanden ist sie, weil ich nicht immer meinen Pokerkoffer mitschleppen, aber auch nicht auf das Gefühl physischer Karten verzichten will. Quasi eine Hybridlösung",
        "m_go_button_label": "Los!",

        "ps_title": "Spielerauswahl",
        "ps_player_input_label": "Wer spielt mit?",
        "ps_player_input_placeholder": "Namen der Spieler*innen",
        "ps_dealer_input_label": "Wer ist Dealer?",
        "ps_dealer_input_placeholder": "Name des Dealers",
        "ps_budget_input_label": "Budget",
        "ps_dialog_label": "Passt alles?",
        "ps_dialog_players": "Spieler*innen:",
        "ps_dialog_dealer": "Dealer:",
        "ps_dialog_budget": "Budget:",
        "ps_dialog_page_link_label": "Spiel starten!",
        "ps_input_error_msg": "Mindestens ein Spieler und ein Budget größer als 0 sind erforderlich.",

        "g_bet_text": "bitte mach deinen Einsatz. Du hast noch",
        "g_bet_text_left": "",
        "g_bet_input_label": "Einsatz",
        "g_win_check_text": "hast du Gewonnen?",
        "g_win_check_yes": "Ja",
        "g_win_check_no": "Nein",
        "g_win_check_tie": "Unentschieden",
        "g_win_check_kick_text": "du bist leider raus.",

    },
    "en": {
        "home": "Home",
        "title": "Blackjack Counter",
        "continue": "Continue",

        "m_info_text": "A blackjack app that replaces chips and currency—but you still play with real cards. I created it because I don’t always want to lug my poker case around, but I also don’t want to give up the feel of physical cards. It’s basically a hybrid solution.",
        "m_go_button_label": "Go!",

        "ps_title": "Player selector",
        "ps_player_input_label": "Who's in?",
        "ps_player_input_placeholder": "Player names",
        "ps_dealer_input_label": "Who's the dealer?",
        "ps_dealer_input_placeholder": "Dealer name",
        "ps_budget_input_label": "Budget",
        "ps_dialog_label": "Everything ok?",
        "ps_dialog_players": "Players:",
        "ps_dialog_dealer": "Dealer:",
        "ps_dialog_budget": "Budget:",
        "ps_dialog_page_link_label": "Start game!",
        "ps_input_error_msg": "At least one player and a budget higher than 0 are required.",

        "g_bet_text": "please place your bet. You have",
        "g_bet_text_left": " left.",
        "g_bet_input_label": "Bet",
        "g_win_check_text": "did you win?",
        "g_win_check_yes": "Yes",
        "g_win_check_tie": "Tie",
        "g_win_check_no": "No",
        "g_win_check_kick_text": "sadly, you're out.",

    },
}

lang = st.segmented_control("🌐", options=list(LANG.keys()), default=list(LANG.keys())[0], label_visibility="hidden")
t = LANG[lang]

st.set_page_config(page_title=t["home"])
st.title(t["title"])

st.write(t["m_info_text"])
if st.page_link("pages/player_selector.py", label=t["m_go_button_label"]):
    st.session_state.lang = t