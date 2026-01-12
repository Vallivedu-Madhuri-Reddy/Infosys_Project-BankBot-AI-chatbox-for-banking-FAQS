import streamlit as st
from database.bank_crud import get_all_users, create_account, get_balance

def database_ui():
    st.title("🗄️ Database Management")

    # SHOW USERS
    st.subheader("👥 Existing Users")
    users = get_all_users()

    if users:
        for u in users:
            st.write(f"👤 {u['username']} | {u['account_type']} | ₹{u['balance']}")
    else:
        st.info("No users available")

    st.divider()

    # CREATE USER
    st.subheader("➕ Create New User")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    account_type = st.selectbox("Account Type", ["Savings", "Current"])
    balance = st.number_input("Initial Balance", min_value=0.0)

    if st.button("Create Account"):
        if create_account(username, password, account_type, balance):
            st.success("✅ User Created Successfully")
            st.rerun()
        else:
            st.error("❌ Username already exists")
