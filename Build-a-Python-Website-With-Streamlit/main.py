import streamlit as st 
from PIL import Image


st.set_page_config(page_title="My Portfolio", page_icon="📄", layout="centered")

st.markdown(
    """
    <style>
        .stApp {
            background-color: #000080 ;
            color: #ffffff;
            font-family: timesnewroman, serif;
            font-size: 1.2em;
            border-radius: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            margin-top: 50px;
            margin-bottom: 50px;
            
            height: 100vh;

        }
    </style>
    """,
    unsafe_allow_html=True
)

profile_image = Image.open("sarfraz.jpg").rotate(-90)   




st.image(profile_image, width=150)
st.title("Sarfraz Aziz")
st.subheader("Front-End Developer")

st.write("Welcome to my portfolio! I am passionate about web development and coding. I specialize in front-end technologies and am currently learning Agentic AI.")


st.header("💡 Skills")
st.write("- Front-End Development (Next.js, TypeScript, Tailwind CSS)")
st.write("- Web Design & UX/UI")
st.write("- Python (Streamlit, Pandas, AI Tools)")




st.subheader("Data Sweeper Web App")
st.write("Submitted a Data Sweeper Web App project using Streamlit for class assignments.")
st.link_button("view project","https://class-1-assignment-growthmindset.streamlit.app/")

# Contact Section
st.header("📬 Contact")
st.write("📧 sarfraz.aziz786@hotmail.com")
st.write(f"💼 [LinkedIn]( https://www.linkedin.com/in/sarfraz-aziz-memon-2a267726a)")
st.write(f"📁 [GitHub](https://github.com/SarfrazAziz786)")

st.write("Feel free to reach out for collaboration opportunities!")
