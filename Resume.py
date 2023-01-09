import streamlit as st
from pathlib import Path
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "pages" / "styles" / "resumeMain.css"
resume_file = current_dir / "pages" / "assets" / "UDIT_GAGNANI.pdf"
# profile_pic = current_dir / "assets" / "profile-pic.png"
profile_pic = current_dir / "pages" / "assets" / "UDIT_GAGNANI.jpg"

# GENERAL SETTINGS

PAGE_TITLE = "RESUME | UDIT GAGNANI"
PAGE_ICON = ":wave:"
NAME = "UDIT GAGNANI"
DESCRIPTION = "Python Developer passionate about Reinforcement Learning," \
              " my main interest lies in Image Processing, Computer Vision"
EMAIL = "kpumgagnani@gmail.com"

SOCIAL_MEDIA = {
    "Youtube": "https://www.youtube.com/@uditkishoregagnani8294",
    "LinkedIn": "https://linkedin.com/in/udit-kishore-gagnani",
    "Github": "https://github.com/UditKGagnani"
}

INTRODUCTION = "I am a python developer interested in data science and reinforcement learning. My strength is to " \
               "\nanalyze my mistakes and perform strategical decision making for my future choices (just like " \
               "\nreinforcement learning).  The only 3 words to describe myself are decisive, affable, meticulous. My " \
               "\ninterested in machine learning developed when I read an article which mentioned that Harvard " \
               "\nUniversity's professors used computer vision and image processing to generate a clear image of the " \
               "\n1st interstellar object to enter our solar system. "

EDUCATION1 = """
    - #### SSC (2017)
    - Delhi Public School, Surat
    - 8.4 CGPA (on the scale of 10)
"""
EDUCATION2 = """
    - #### HSC (2019)
    - Delhi Public School, Surat
    - 78.8%
"""
EDUCATION3 = """
    - #### Bachelor of Science, Information Technology (2019-22)
    - Auro University, Surat
    - 8.79 CGPA (on the scale of 10)
"""

WORKEXPERIENCE = """
    - #### NJ Technologies
    - Position: Java Full Stack Developer
    - Duration: 10 months
    - Project: Loan Management System
    - - It was an in-house project to keep track of all the activities between investment company and client. 
    - - It automatically calculates amortization table on the basis of loan details.
    - Explored: Spring MVC Framework, Java, JavaScript, Linux OS, HTML, CSS, Tomcat Server
"""

CERTIFICATIONS = """
    - 🏆 [HarvardX Using Python for Research](https://courses.edx.org/certificates/6eaf2878a6c7405d98aa139db5137d59)
    - 🏆 [Coursera Google Machine Learning for Business Professionals](https://www.coursera.org/account/accomplishments/certificate/AYPFMWH3DD9A)
    - 🏆 [Coursera AWS Getting Started with AWS Machine Learning](https://www.coursera.org/account/accomplishments/certificate/77RPPY55UHJZ)
    - 🏆 [Coursera MathWorks Exploratory Data Analysis with MATLAB](https://www.coursera.org/account/accomplishments/certificate/PQBLAVHYQUKM)
    - 🏆 [Coursera IBM Python for Data Science and AI](https://www.coursera.org/account/accomplishments/certificate/49J3FHJ8JE3P)
    - 🏆 [British Airways Data Science Virtual Internship program](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/British%20Airways/NjynCWzGSaWXQCxSX_British%20Airways_FHk5d9BtAE5JZBc4k_1670881201335_completion_certificate.pdf)
"""



# PYTHON CODE

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# ---- HERO SECTION
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=220)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📬", EMAIL)

# ---- SOCIAL LINKS
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))

for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# ---- INTRODUCTION
# st.write("#")
st.write(" ## ABOUT ME")
st.write(INTRODUCTION)
st.write("---")

# --- EDUCATION
# st.write("#")
st.write(" ## EDUCATION")
st.write(EDUCATION1)
st.write(EDUCATION2)
st.write(EDUCATION3)
st.write("---")

# --- WORK EXPERIENCE
# st.write("#")
st.write(" ## WORK EXPERIENCE")
st.write(WORKEXPERIENCE)
st.write("---")

# --- CERTIFICATIONS
# st.write("#")
st.write(" ## CERTIFICATIONS")
st.write(CERTIFICATIONS)
st.write("---")
