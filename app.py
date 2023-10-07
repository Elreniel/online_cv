import streamlit as st
from streamlit_option_menu import option_menu
from pages.about_me import about_me
from pages.education import education
from pages.work_experience import work_experience

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

hide_streamlit_style =  """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        </style>
                        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

selected_page = option_menu(
    menu_title=None,
    options=["About Me", "Education", "Experience"],
    icons=["person-circle", "backpack", "buildings"],
    orientation="horizontal")

if selected_page == "About Me":
    about_me()
elif selected_page == "Education":
    education()
elif selected_page == "Experience":
    work_experience()
