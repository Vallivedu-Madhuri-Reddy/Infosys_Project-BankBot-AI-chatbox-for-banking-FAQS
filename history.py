import streamlit as st
from database.bank_crud import get_transactions

def history_ui():
    st.title("📜 Transaction History")

    if not st.session_state.logged_in:
        st.warning("🔐 Please login to view history.")
        return

    transactions = get_transactions()

    if not transactions:
        st.info("No transactions found.")
        return

    for t in transactions:
        st.markdown(
            f"""
            🔁 **{t['sender']} → {t['receiver']}**  
            💰 Amount: ₹{t['amount']}  
            🕒 {t['timestamp']}
            ---
            """
        )
