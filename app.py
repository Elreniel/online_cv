import os
import base64
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


def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace(".", "")
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f"""
    <div style="text-align: center; padding-bottom:15px;">
        <a href="{target_url}">
        <img src="data:image/{img_format};base64,{bin_str}" style="width:64px; height:64px" />
        </a>
    </div>"""

    return html_code


with st.columns(3)[1]:
    st.markdown("<h1 style='color:black; font-size:50px; text-align:center;'>Barış Coşkun</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        mail_logo_html = get_img_with_href(os.path.join("logos", "mail.png"), 'mailto:bcoskun1993@gmail.com')
        st.markdown(mail_logo_html, unsafe_allow_html=True)

    with col2:
        linkedin_logo_html = get_img_with_href(os.path.join("logos", "linkedin.png"), 'https://www.linkedin.com/in/bar%C4%B1%C5%9F-co%C5%9Fkun-386b97141')
        st.markdown(linkedin_logo_html, unsafe_allow_html=True)

    with col3:
        github_logo_html = get_img_with_href(os.path.join("logos", "github.png"), 'https://github.com/Elreniel')
        st.markdown(github_logo_html, unsafe_allow_html=True)

selected_page = option_menu(
    menu_title=None,
    options=["About Me", "Education", "Experience"],
    icons=["person", "pc-display-horizontal", "buildings"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0px!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "center",
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
