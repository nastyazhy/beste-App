import streamlit as st
import random
import json
import os

# Function to read tasks from file
def read_tasks(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        tasks = file.readlines()
    return tasks

# Function to get a random task
def get_random_task(tasks):
    return random.choice(tasks)

# Define registration page layout
def registration_page():
    st.title("Welcome to Bingo-Health App")
    st.write("Please register or sign in to get started")

    # Add input fields for registration or login
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    if st.button("Sign In"):
        # Check if email exists in user_data and password matches
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as file:
                user_data = json.load(file)
                if email in user_data and user_data[email]["password"] == password:
                    st.session_state.name = user_data[email]["name"]
                    st.session_state.email = user_data[email]["email"]
                    st.session_state.avatar = user_data[email]["avatar"]
                    st.session_state.is_registered = True
                    st.experimental_rerun()
                else:
                    st.error("Incorrect email or password. Please try again.")
        else:
            st.error("Account not found. Please register.")
    else:
        name = st.text_input("Enter your name")
        avatars = {
            "Avatar 1": "images/Avatar 1.jpg",
            "Avatar 2": "images/Avatar 2.jpg",
            "Avatar 3": "images/Avatar 3.jpg",
            # Add more avatars as needed
        }

        # Display avatars in a row
        selected_avatar = None
        st.sidebar.title("Select your avatar")

        for i, (avatar_name, avatar_path) in enumerate(avatars.items()):
            col1, col2 = st.columns([3, 1])
            col1.image(avatar_path, caption=avatar_name, width=100)
            if col2.button("Select", key=f"avatar_button_{i}"):
                selected_avatar = avatar_path

        if st.button("Register"):
            # Save registration information to session state
            st.session_state.name = name
            st.session_state.email = email
            if selected_avatar:
                st.session_state.avatar = selected_avatar
            st.session_state.is_registered = True

            # Save user data to a file
            user_data = {}
            if os.path.exists("user_data.json"):
                with open("user_data.json", "r") as file:
                    user_data = json.load(file)
            user_data[email] = {
                "name": name,
                "email": email,
                "password": password,
                "avatar": selected_avatar
            }
            with open("user_data.json", "w") as file:
                json.dump(user_data, file)

            st.experimental_rerun()


# Define main page layout
def main():
    if "is_registered" not in st.session_state or not st.session_state.is_registered:
        registration_page()
    else:
        st.sidebar.title("Navigation")
        page = st.sidebar.radio("Go to", ["Profile", "Today's Task", "Bingo Check", "Learn More About"])

        if page == "Profile":
            profile_page()
        elif page == "Today's Task":
            todays_task_page()
        elif page == "Bingo Check":
            bingo_check_page()
        elif page == "Learn More About":
            learn_more_page()

# Define function for profile page
def profile_page():
    st.title("Profile")
    # Display registration information
    st.write(f"Name: {st.session_state.name}")
    st.write(f"Email: {st.session_state.email}")
    if hasattr(st.session_state, "avatar") and st.session_state.avatar:
        st.write(f"Avatar: {st.session_state.avatar}")
        st.image(f"images/{st.session_state.avatar}.jpg", width=200)
    else:
        st.write("Avatar: Not selected")

# Define function for today's task page
def todays_task_page():
    st.title("Today's Task")
    # Display a random task
    if st.button("Get a random task for today"):
        tasks = read_tasks("tasks.txt")
        random_task = get_random_task(tasks)
        st.write(random_task)

# Define function for Bingo check page
def bingo_check_page():
    st.title("Bingo Check")
    
    # Create a 3x3 grid of gray squares with rounded corners and more spacing
    for i in range(3):
        row = ""
        for j in range(3):
            row += '<div style="background-color: #CCCCCC; width: 150px; height: 150px; display: inline-block; margin: 10px; border-radius: 15px;"></div>'
        st.markdown(row, unsafe_allow_html=True)

# Define function for Learn More About page
def learn_more_page():
    st.title("Learn More About")
    st.sidebar.subheader("Choose a topic:")
    topic = st.sidebar.selectbox("", ["Mental Health", "Nutrition", "Physical Activities", "Sleep Hygiene"])
    if topic == "Mental Health":
        st.write("Articles on Mental Health:")
        st.write("Article 1")
        st.write("Article 2")
        st.write("Article 3")
    elif topic == "Nutrition":
        st.write("Articles on Nutrition:")
        st.write("Article 4")
        st.write("Article 5")
        st.write("Article 6")
    elif topic == "Physical Activities":
        st.write("Articles on Physical Activities:")
        st.write("Article 7")
        st.write("Article 8")
        st.write("Article 9")
    elif topic == "Sleep Hygiene":
        st.write("Articles on Sleep Hygiene:")
        st.write("Article 10")
        st.write("Article 11")
        st.write("Article 12")
# Function to display Bingo grid
def bingo_grid():
    # Add logic to display Bingo grid with checkboxes
    pass

# Run the main function to start the app
if __name__ == "__main__":
    main()

