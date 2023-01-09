import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(
    page_title="Udit Gagnani",
    layout="wide"
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "resumeMain.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title("Projects")
st.write("### (Even this Website is a Python Project as it is Developed using Streamlit and Deployed using Render)")

with st.container():
    st.write("##")
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.write("##")
        project1img = Image.open(current_dir / "assets" / "projects" / "project_1_stanford.jpg")
        st.image(project1img)
    with text_col:
        st.subheader("STANFORD'S CODEINPLACE'S PASSWORD MANAGER PROJECT")
        st.write("""
                 - Official Stanford Website Link:
                 - [https://codeinplace.stanford.edu/2021/showcase/890](https://codeinplace.stanford.edu/2021/showcase/890)
                 - Selected out of 6,00,000+ applicants for this program. One of
                 - 1,500 students to successfully complete the final project.
                 - Python Libraries: Kivy, Sqlite3
                 - [Watch Video](https://www.youtube.com/watch?v=wZ-FaCV4LFY&ab_channel=UditKishoreGagnani)""")
    st.write("---")

    st.write("##")
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.write("##")
        project1img = Image.open(current_dir / "assets" / "projects" / "project_2_dataset_generation.jpg")
        st.image(project1img)
    with text_col:
        st.subheader("MEANINGFUL RANDOM DATASET GENERATION USING REGRESSION")
        st.write("""
                     - Generated meaningful random student's dataset using various regression algorithms in python:
                     - - ✅ Linear Regression
                     - - ✅ Ridge Regression
                     - - ✅ Lasso Regression
                     - - ✅ K Neighbors Regressor
                     - - ✅ Decision Tree Regressor
                     - - ✅ Random Forest Regressor
                     - - ✅ Gradient Boosting Regressor
                     - - ✅ Adaboost Regressor
                     - Cross Validation used to find the best(most accurate) Model 
                     - - ✅ [Ridge Regression with 78% Accuracy without parameter tuning]
                     - Created efficient dataset by reducing the base dataset's size by manifolds.
                     - Also used statistical, mathematical concepts in python to generate the dataset
                     - Statistical concepts such as defining probabilities was used to generate random students of each category
                     - Inspired and based on Kaggle Dataset 
                     - Python Libraries: Sklearn, Numpy, Pandas, Matplotlib, Random
                     - [Source Code](https://github.com/UditKGagnani/StudentRandomDatasetGeneration/blob/main/CreateDataset.ipynb)""")
    st.write("---")

    st.write("##")
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.write("##")
        project1img = Image.open(current_dir / "assets" / "projects" / "project_3_students_admission_eda.jpg")
        st.image(project1img)
    with text_col:
        st.subheader("STUDENTS UNIVERSITY ADMISSION EXPLORATORY DATA ANALYSIS")
        st.write("""
                     - Presented meaningful conclusions based on the dataset in form of various charts and graphs:
                     - - ✅ PieChart (GRE, TOEFL Score Category) 
                     - - ✅ Bargraph (SOP Rank Category)
                     - - ✅ Unconnected Line Graph (CGPA Score Category)
                     - - ✅ Tables (Too ambitious students, Students who are underestimating themselves)
                     - Python Libraries: Plotly, Seaborn, Numpy, Pandas, Matplotlib
                     - [Source Code](https://github.com/UditKGagnani/StudentUniversityAdmissionEDA/blob/main/Shop_EDA.ipynb)""")
    st.write("---")

    st.write("##")
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.write("##")
        project1img = Image.open(current_dir / "assets" / "projects" / "project_4_grocery_sales_eda.jpg")
        st.image(project1img)
    with text_col:
        st.subheader("GROCERY STORE SALES EXPLORATORY DATA ANALYSIS")
        st.write("""
                             - Analysed dataset on the basis of various categories:
                             - - ✅ On the basis of Region
                             - - ✅ On the basis of Category, SubCategory
                             - - ✅ On the basis of Date
                             - In-depth Analysis of dataset:
                             - - ✅ Relation between various Parameters
                             - - ✅ Most Faithful Customers
                             - - ✅ Most Profitable Customers
                             - - ✅ Least Profitable Customers
                             - Inspired and based on Kaggle Dataset 
                             - Python Libraries: Plotly, Seaborn, Numpy, Pandas, Matplotlib, Random
                             - [Source Code](https://github.com/UditKGagnani/GroceryShopSalesEDA/blob/main/StudentAdmitEDA.ipynb)""")
    st.write("---")