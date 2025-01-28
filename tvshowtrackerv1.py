import pandas as pd
import streamlit as st
import datetime

# Initialize the DataFrame in session state
if "tv_data" not in st.session_state:
    st.session_state.tv_data = pd.DataFrame(
        {"Show": [], "Platform": [], "Release Day": []}
    )

# Get today's day of the week
today = datetime.datetime.now().strftime('%A')  # Returns the full name of the current day (e.g., 'Monday')

st.title("📺 Noo and Tom's TV Show Tracker")

# Show the list of shows available today
st.subheader(f"📅 Shows Available Today")
available_today = st.session_state.tv_data[st.session_state.tv_data["Release Day"] == today]

if not available_today.empty:
    st.table(available_today)
else:
    st.write("No shows available today. Sadness.")

# Show current schedule
st.subheader("Current TV Show Schedule")
st.table(st.session_state.tv_data)

# Add a new show form
st.subheader("➕ Add a New Show")
with st.form("add_show_form", clear_on_submit=True):
    show_name = st.text_input("Show Name")
    platform = st.selectbox("Platform", ["Hulu", "Netflix", "HBO", "Apple TV", "Disney"])
    release_day = st.selectbox("Release Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    submitted = st.form_submit_button("Add Show")

    if submitted:
        # Update session state
        new_entry = pd.DataFrame({"Show": [show_name], "Platform": [platform], "Release Day": [release_day]})
        st.session_state.tv_data = pd.concat([st.session_state.tv_data, new_entry], ignore_index=True)
        st.success(f"Added {show_name}!")
        # Immediately re-render the updated table
        st.rerun()

# Delete a show section
st.subheader("🗑️ Delete a Show")
if not st.session_state.tv_data.empty:
    show_to_delete = st.selectbox("Select a show to delete", st.session_state.tv_data["Show"].unique())
    if st.button("Delete Show"):
        st.session_state.tv_data = st.session_state.tv_data[st.session_state.tv_data["Show"] != show_to_delete]
        st.success(f"Deleted {show_to_delete}!")
        st.rerun()
else:
    st.write("No shows available for deletion.")
