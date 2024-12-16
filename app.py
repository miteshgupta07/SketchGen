import streamlit as st

app_page=st.Page(page="views/main.py",
                 title="Generate",
                 icon="✨",
                 default=True)

home=st.Page(page="views/home.py",
                 title="Home",
                 icon=":material/info:")

documentation=st.Page(page="views/documentation.py",
                 title="Documentation",
                 icon=":material/description:")

about_me=st.Page(page="views/about_developer.py",
                 title="About Developer",
                 icon=":material/person:")


pg=st.navigation(pages=[home,app_page,documentation,about_me])

pg.run()
