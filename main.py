import streamlit as st

def main():
    st.set_page_config(page_title="My Portfolio", layout="wide")

    st.sidebar.title('Projects')
    st.title('My Portfolio')

    projects = [
        {
            "name": "NASHBOT FB BOT",
            "image": "https://i.imgur.com/bNtTDI5.jpeg",
            "description": "This is the best messenger chatbot because it can help you create an essay or anything you need for education. Currently, it has 39 commands.",
            "link": "https://nash-bot-v2.onrender.com"
        },
        {
            "name": "AUTOBOT FB BOT",
            "image": "https://i.imgur.com/vdBytT7.jpeg",
            "description": "This is the best messenger chatbot because it can help you create an essay or anything you need for education. Currently, it has 24 commands.",
            "link": "https://nashbot.onrender.com"
        },
        {
            "name": "NASH API ENDPOINT",
            "image": "https://i.imgur.com/6IavJPv.jpeg",
            "description": "I want to introduce my REST API. You can use it to create your bot commands or website.",
            "link": "https://nash-api-end.onrender.com/"
        },
        {
            "name": "NashBot AI Chatbot",
            "image": "https://i.imgur.com/Kw0Y0uR.jpeg",
            "description": "Introducing NashBot, an AI chatbot designed to provide seamless and interactive conversations. Features include persistent chat history, customizable chat names, and real-time responses. Experience the power of NashBot and engage in dynamic conversations without losing any context!",
            "link": "nash/index.html"
        },
        {
            "name": "AUTO FB POST REACTION",
            "image": "https://i.imgur.com/9J9U7y0.jpeg",
            "description": "I want to introduce my web-to-app. Please download it and enjoy.",
            "link": "other-html/maintenance.html"
        },
        {
            "name": "NGL SPAMMER",
            "image": "https://i.imgur.com/KBy7H6u.jpeg",
            "description": "I just want to introduce my ngl spammer website you can use it and make it fun.",
            "link": "other-html/nglspam.html"
        },
        {
            "name": "SPAM SHARE FB POST",
            "image": "https://i.imgur.com/WMVaY2O.jpeg",
            "description": "This is a spam share facebook posts you use it and enjoy.",
            "link": "other-html/spamshare.html"
        }
    ]

    selected_project = st.sidebar.selectbox(
        'Select a project',
        [project['name'] for project in projects]
    )

    project = next((p for p in projects if p['name'] == selected_project), None)

    if project:
        st.image(project['image'], use_column_width=True)
        st.header(project['name'])
        st.write(project['description'])
        st.markdown(f"[Learn more]({project['link']})", unsafe_allow_html=True)

    st.sidebar.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-image: linear-gradient(#2e7bcf,#2e7bcf);
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .reportview-container {
            background: #f0f2f6;
        }
        .sidebar .sidebar-content {
            background: #2e7bcf;
            color: white;
        }
        .sidebar .sidebar-content a {
            color: white;
        }
        .sidebar .sidebar-content a:hover {
            color: #d3d3d3;
        }
        .stButton>button {
            background-color: #2e7bcf;
            color: white;
        }
        .stButton>button:hover {
            background-color: #1e5bbf;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
