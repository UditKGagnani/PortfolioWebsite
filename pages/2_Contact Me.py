from pathlib import Path
import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(
    page_title="Udit Gagnani",
    layout="wide"
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file1 = current_dir / "styles" / "resumeMain.css"

with open(css_file1) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

css_file2 = current_dir / "styles" / "contactPage.css"

with open(css_file2) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/kpumgagnani@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

SOCIAL_MEDIA = {
            "Youtube": "https://www.youtube.com/@uditkishoregagnani8294",
            "LinkedIn": "https://linkedin.com/in/udit-kishore-gagnani",
            "Github": "https://github.com/UditKGagnani"
        }

with st.container():
    image_col, break_col, form_col = st.columns((2, 1, 2))

    with image_col:
        lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
        st_lottie(lottie_hello,
                  speed=1,
                  reverse=False,
                  loop=True,
                  quality='low',
                  key=None)

    with break_col:
        st.write("##")

    with form_col:
        st.header(":mailbox: Get In Touch With Me!")
        st.markdown(contact_form, unsafe_allow_html=True)

        st.write("#")
        st.header("Connect With Me!")

        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            st.write(f"[{platform}]({link})")
