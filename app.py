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
    st.title("Barış Coşkun")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<a href='mailto:bcoskun1993@gmail.com' style='color:black;font-size:35px;'>✉</a> ", unsafe_allow_html=True)
    with col2:
        st.markdown("[![Title](https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-48.png)](https://www.linkedin.com/in/bar%C4%B1%C5%9F-co%C5%9Fkun-386b97141)", unsafe_allow_html=True)
    with col3:
        st.markdown("[![Title](https://img.icons8.com/material-outlined/48/000000/github.png)](https://github.com/Elreniel)", unsafe_allow_html=True)

selected_page = option_menu(
    menu_title=None,
    options=["About Me", "Education", "Experience"],
    icons=["person", "pc-display-horizontal", "buildings"],
    orientation="horizontal",
    styles={
        "container": {"padding": "10px 5px!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "blue"},
    },
)

if selected_page == "About Me":
    about_me()
elif selected_page == "Education":
    education()
elif selected_page == "Experience":
    work_experience()
