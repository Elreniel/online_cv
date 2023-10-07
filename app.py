import streamlit as st
from streamlit_option_menu import option_menu
from pages.about_me import about_me
from pages.education import education
from pages.work_experience import work_experience

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title="Barış Coşkun")

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

with st.columns(3)[1]:
    st.markdown("<h1 style='text-align: center; color: black;'>Barış Coşkun</h1>", unsafe_allow_html=True)

selected_page = option_menu(
    menu_title=None,
    options=["About Me", "Education", "Experience"],
    icons=["person", "pc-display-horizontal", "buildings"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "red"},
    },
)

if selected_page == "About Me":
    about_me()
elif selected_page == "Education":
    education()
elif selected_page == "Experience":
    work_experience()
