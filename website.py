import streamlit as st
import pymongo

client = pymongo.MongoClient("mongodb+srv://sherwinroger:tronster@cluster0.vvp2vpz.mongodb.net/?retryWrites=true&w=majority")
db = client["drestin"]
collection = db["users"]

def display_leaderboard():
    st.title("Leaderboard - Prompt ur way thru!!!!!")

    leaderboard_data = collection.find().sort("score", pymongo.DESCENDING)

    st.warning("Username | Score")
    for entry in leaderboard_data:
        st.success(f"{entry['username']} | {entry['score']}")

display_leaderboard()
