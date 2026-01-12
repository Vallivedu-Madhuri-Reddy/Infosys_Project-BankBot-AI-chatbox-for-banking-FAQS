
# ui/login.py
import streamlit as st
from database.bank_crud import authenticate_user, create_account

def login_ui():
    """
    Handles:
    - User login
    - Admin login
    - New user registration
    - Session & role management
    """

    st.markdown("## 🔐 BankBot AI Authentication")
    st.caption("Secure login with role-based access")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user" not in st.session_state:
        st.session_state.user = None
    if "role" not in st.session_state:
        st.session_state.role = "user"

    # Show current login status
    if st.session_state.logged_in:
        st.success(f"✅ Logged in as: **{st.session_state.user}** (Role: {st.session_state.role})")
        st.info("Navigate using the sidebar menu")
        
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.role = "user"
            st.success("Logged out successfully")
            st.rerun()
        return

    tab1, tab2 = st.tabs(["🔑 Login", "🆕 Register"])

    # ---------------- LOGIN ----------------
    with tab1:
        st.markdown("### Login to Your Account")
        
        username = st.text_input("Username", key="login_user", placeholder="Enter your username")
        password = st.text_input("Password", type="password", key="login_pass", placeholder="Enter your password")

        remember = st.checkbox("Remember me")
        
        # Admin hint
        st.info("💡 **Admin Access**: Use username 'admin' to access admin panel")

        if st.button("🚀 Login", use_container_width=True, type="primary"):
            if not username or not password:
                st.error("❌ Please enter both username and password")
                return
                
            user = authenticate_user(username, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.user = username

                # ADMIN DETECTION - Multiple methods
                if username.lower() == "admin" or username.lower() == "administrator":
                    st.session_state.role = "admin"
                    st.balloons()
                    st.success(f"🎉 Welcome Admin {username}! You have full access.")
                    st.info("✨ Admin Panel is now available in the sidebar!")
                else:
                    st.session_state.role = "user"
                    st.success(f"Welcome {username} 👋")
                
                # Debug info (can be removed later)
                st.write("**Debug Info:**")
                st.write(f"- Username: {st.session_state.user}")
                st.write(f"- Role: {st.session_state.role}")
                st.write(f"- Logged in: {st.session_state.logged_in}")
                
                st.rerun()
            else:
                st.error("❌ Invalid username or password")
                st.warning("💡 **Tip**: If you haven't registered yet, use the Register tab")

    # ---------------- REGISTER ----------------
    with tab2:
        st.markdown("### Create New Account")
        
        new_user = st.text_input("Username", key="reg_user", placeholder="Choose a username")
        
        # Highlight admin username
        if new_user.lower() == "admin":
            st.success("✨ This will create an ADMIN account!")
        
        new_pass = st.text_input("Password", type="password", key="reg_pass", placeholder="Choose a strong password")
        new_pass_confirm = st.text_input("Confirm Password", type="password", key="reg_pass_confirm")
        
        acc_type = st.selectbox("Account Type", ["savings", "current"])
        balance = st.number_input("Initial Balance (₹)", min_value=0.0, step=500.0, value=5000.0)

        if st.button("🧾 Create Account", use_container_width=True, type="primary"):
            if not new_user or not new_pass:
                st.warning("⚠️ Username & password required")
            elif new_pass != new_pass_confirm:
                st.error("❌ Passwords don't match!")
            elif len(new_pass) < 4:
                st.warning("⚠️ Password should be at least 4 characters")
            else:
                success = create_account(new_user, new_pass, acc_type, balance)
                if success:
                    st.success("✅ Account created successfully!")
                    if new_user.lower() == "admin":
                        st.balloons()
                        st.success("🎉 Admin account created! You can now login with full privileges.")
                    st.info("👉 Switch to the Login tab to sign in")
                else:
                    st.error("⚠️ Username already exists. Please choose a different username.")

    # Quick Login Buttons (for testing)
    st.markdown("---")
    st.markdown("### 🚀 Quick Access (Development)")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("👤 Demo User Login", use_container_width=True):
            st.info("Create a regular account first using the Register tab")
    
    with col2:
        if st.button("👨‍💼 Demo Admin Login", use_container_width=True):
            st.info("Create an account with username 'admin' using the Register tab")