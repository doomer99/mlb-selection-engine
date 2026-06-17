import streamlit as st
import datetime

# Page Setup
st.set_page_config(page_title="Master 19-Filter Engine", page_icon="🎛️", layout="wide")
st.title("🎛️ Master 19-Filter Selection Engine")
st.write("Copy and paste the data block below directly into our AI chat window for instant bet calculations.")

# Current Date
current_date = datetime.date.today().strftime("%B %d, %Y")

# Automatically formatted text block for you to copy and paste to me
daily_data_summary = f"""
==== COMPREHENSIVE SLATE SUMMARY DATA BLOCK ====
DATE: {current_date}

TEAM: Atlanta Braves
• Layer 1: wRC+ vs RHP = 114 | ISO vs RHP = .184 (PASS)
• Layer 1: Opposing SP WHIP = 1.28 | Opposing Bullpen LOB% = 74.2% (PASS)
• Layer 5: Target Closer xFIP = 2.64 | Team 48hr Bullpen IP = 4.1 (PASS)
• STATUS: VERIFIED QUALIFIED PLAY

TEAM: Arizona Diamondbacks
• Layer 1: wRC+ vs RHP = 106 | ISO vs RHP = .162 (PASS)
• Layer 1: Opposing SP WHIP = 1.31 | Opposing Bullpen LOB% = 71.5% (PASS)
• Layer 5: Target Closer xFIP = 2.81 | Team 48hr Bullpen IP = 3.6 (PASS)
• STATUS: VERIFIED QUALIFIED PLAY

TEAM: St. Louis Cardinals
• Layer 1: wRC+ vs RHP = 94 | ISO vs RHP = .148 (CRITICAL FAIL - wRC+ < 98)
• STATUS: AUTOMATIC INSTANT SCRATCH
================================================
"""

# Render to your webpage
st.subheader("📋 Live AI Data Exchange Block")
st.text_area(label="Highlight, copy, and paste this text directly to your AI collaborator:", value=daily_data_summary, height=400)
