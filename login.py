import streamlit as st

# Page configuration
st.set_page_config(page_title="Login | B-Route Global", page_icon="🔒")

st.title("🔒 Admin Login Portal")
st.write("Please enter your credentials to access the dashboard.")


# Login Form
with st.form("login_box"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

    if submit:
        if username == "admin" and password == "broute123":
            st.success(f"Welcome back, {username}!")
            st.balloons()
    else:
         st.error("Invalid Username or Password. Please try again.")

# Back to Home button
if st.button("⬅️ Back to Home"):
    st.switch_page("app.web.py")