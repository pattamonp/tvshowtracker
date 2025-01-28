import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

#TV show schedule
data = [
    {"Show": "Hell's Kitchen 🔪", "Platform": "Hulu", "Release Day": "Friday"},
    {"Show": "Singles' Inferno 🔥", "Platform": "Netflix", "Release Day": "Tuesday"},
    {"Show": "Kitchen Nightmares‍🍳", "Platform": "Hulu", "Release Day": "Thursday"},
    {"Show": "Severance 💼", "Platform": "Apple", "Release Day": "Saturday"},
    {"Show": "Abbott Elementary 🎒", "Platform": "Hulu", "Release Day": "Thursday"},
]

df = pd.DataFrame(data)

today = datetime.now().strftime("%A")

#UI
st.title("TV Show Tracker")
st.write("What's on TV today?")
available_shows = df[df["Release Day"] == today]

if not available_shows.empty:
    for _, row in available_shows.iterrows():
        st.write(f"🎥 {row['Show']} on {row['Platform']}")
else:
    st.write("No shows coming out today!")

# Calendar View
st.header("Full Release Schedule")
st.table(df)