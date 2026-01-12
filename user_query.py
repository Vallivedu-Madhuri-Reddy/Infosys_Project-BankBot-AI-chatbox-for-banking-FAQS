import streamlit as st
import subprocess
import sys
from pathlib import Path

def user_query_ui():
    st.title("🧠 User Query – NLU Engine")

    if st.button("Open NLU Trainer & Visualizer"):
        subprocess.Popen([
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(Path("main_app.py"))
        ])
        st.success("NLU module launched in new tab.")
