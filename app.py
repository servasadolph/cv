from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Servas Adolph"
PAGE_ICON = ":wave:"
NAME = "Servas Adolph"
DESCRIPTION = """
Data Analyst, Software Developer, Web Developer.
"""
EMAIL = "servasadolph09@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCWPagdH-POziaM_8w4w1B8Q",
    "LinkedIn": "https://www.linkedin.com/in/servas-adolph-66494066/",
    "Instagram": "https://www.instagram.com/servasadolph/",
    "Twitter": "https://twitter.com/servasadolph/",
    "Facebook": "https://www.facebook.com/servasadolph/",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- About Me ---
st.write('\n')
st.write("---")
st.subheader("About & Me.")
st.write("---")
st.write(
    """
Greetings! I am a Research Assistant pursuing a Master's degree at SoonChunHyang University in South Korea. My primary areas of interest and study include Machine Learning,
Deep Learning, and Data Analysis, with a particular emphasis on applications in the Medical Data Analysis or Healthcare Data Analysis and Natural Language Processing.
"""
)

# --- AFFILIATIONS, BIOGRAPHY & RESEARCH AREA ---
st.write('\n')
st.write("---")
st.subheader("Affiliations, Biography & Research Area.")
st.write("---")
st.markdown("**Affiliations:**")
st.write(
  """
👩‍💻 BigData Engineering Department (ICT Department), SCH Media Lab, SoonChunHyang University, South Korea.
"""
)

st.markdown("**Biography:**")
st.write( 
  """
📚  Servas Adolph, originally from the United Republic of Tanzania, earned a BSc in Computer Engineering and Information Technology from the United African University of Tanzania in October 2020. He is now pursuing a Master's degree in Big Data Engineering at SoonChunHyang University, studying within the Department of ICT Convergence in South Korea.
"""
)

st.markdown("**Research Area:**")
st.write( 
  """
📊  Medical Data Analysis or Healthcare Data Analysis.

📚  Natural Language Processing(NLP).
"""
)



# --- PAPERS, AWARDS & OPEN DATA---
st.write('\n')
st.subheader("Papers, Awards & Open Data.")
st.write("---")
st.markdown("**Papers:**")
st.write(
    """
✔️ International Conference (In Proceedings..)
- ► Servas Adolph and Jiyoung Woo, "White Blood Cell Detection and Classification using YOLOv5 with Hybrid ResNet50-VGG16-SVM" ICT4sHealth & Home: The 6th International Conference on Information and Communication Technologies for Smart Health & Home, which held in Kota Kinabalu, Malaysia from December 18th to 22nd, 2022.
"""
)

st.markdown("**Awards:**")
st.write(
    """
✔️ In Progress....
"""
)

st.markdown("<span style=\"color: white;\">**Open Data:**</span>", unsafe_allow_html=True)
st.write(
    """
✔️ In Progress....
"""
)


# # --- SKILLS ---
# st.write('\n')
# st.subheader("Hard Skills")
# st.write(
#     """
# - 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Java, HTML, CSS, Python, C, C++, XML, PHP
# - 📊 Data Visulization: PowerBi, MS Excel, Plotly
# - 📚 Modeling: Logistic regression, linear regression, decition trees
# - 🗄️ Databases: MongoDB, MySQL
# """
# )


# --- EDUCATION ---
st.write('\n')
st.subheader("Education.")
st.write("---")

# --- EDU 1
st.write("📚", "**SoonChunHyang University | Republic of Korea**")
st.write("✔️ 08/2021 - Present")
st.write(
    """
- ►  Big Data Engineering 
- ►  Department of Big Data Engineering
"""
)

# --- EDU 2
st.write('\n')
st.write("📚", "**United African University of Tanzania | The United Republic of Tanzania**")
st.write("✔️ 10/2016 - 09/2020")
st.write(
    """
- ► Computer Engineering and Information Technology.
- ► Department of Computer Engineering & Information Technology(COET).
"""
)


# --- CONTACT ---
st.write('\n')
st.subheader("Contact.")
st.write("---")
st.write(
    """
- 📫 servasadolph09@gmail.com
"""
)



# # --- WORK HISTORY ---
# st.write('\n')
# st.subheader("Work History")
# st.write("---")

# # --- JOB 1
# st.write("🚧", "**Developer | TymTalk Cooperation**")
# st.write("02/2021 - Present")
# st.write(
#     """
# - ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
# - ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
# - ► Redesigned data model through iterations that improved predictions by 12%
# """
# )

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Intership us Developer | UAUT University**")
# st.write("01/2018 - 02/2021")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Intership us Network Experties | MBEYA HOSPITAL**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
