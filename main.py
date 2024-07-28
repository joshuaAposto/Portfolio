import streamlit as st
from PIL import Image
import time

# Custom CSS
st.markdown("""
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            font-family: 'Arial', sans-serif;
        }
        .sidebar .sidebar-content {
            background: #1e3c72;
            padding: 20px;
            color: #fff;
        }
        .sidebar .sidebar-content h1, .sidebar .sidebar-content p {
            color: #ffd700;
        }
        .main-content {
            margin-left: 220px;
            padding: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .header h1 {
            font-size: 3rem;
            color: #ffd700;
            margin-bottom: 10px;
        }
        .profile-picture {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 20px auto;
            display: block;
            border: 5px solid #ffd700;
        }
        .stats {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 10px;
        }
        .stats div {
            text-align: center;
        }
        .stats h3 {
            margin: 0;
            color: #ffd700;
        }
        .stats p {
            font-size: 1.2rem;
        }
        .section {
            padding: 20px;
            margin-bottom: 40px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            color: #ddd;
        }
        .section h2 {
            color: #ffd700;
            margin-bottom: 20px;
        }
        .resume-btn {
            background-color: #1e3c72;
            color: #fff;
            border-radius: 5px;
            padding: 15px 30px;
            font-size: 1.1rem;
            transition: background-color 0.3s, transform 0.3s;
            text-decoration: none;
        }
        .resume-btn:hover {
            background-color: #2a5298;
            transform: scale(1.05);
        }
        .btn {
            display: inline-block;
            padding: 12px 25px;
            background-color: #007bff;
            color: #fff;
            text-decoration: none;
            text-align: center;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            margin-top: 10px;
        }
        .btn:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        #portfolio {
            text-align: center;
            padding: 40px 20px;
        }
        #portfolio h2 {
            font-size: 2.5em;
            font-weight: bold;
            color: #007bff;
            margin-bottom: 30px;
            position: relative;
            display: inline-block;
        }
        #portfolio h2::after {
            content: '';
            display: block;
            width: 80px;
            height: 4px;
            background-color: #007bff;
            margin: 10px auto 0;
            border-radius: 2px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("")
st.sidebar.markdown("""
    <div class="sidebar-content">
        <h1>Joshua Apostol</h1>
        <p>Web Developer | Designer</p>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#about-me">About Me</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#portfolio">Portfolio</a></li>
            <li><a href="#resume">Resume</a></li>
            <li><a href="#achievements">Achievements</a></li>
            <li><a href="#adsense">AdSense</a></li>
            <li><a href="#coming-soon">Coming Soon</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Header section
st.markdown("""
    <div class="header">
        <img class="profile-picture" src="https://i.imgur.com/mmBfKMo.jpeg" alt="Profile Picture">
        <h1>Joshua Apostol</h1>
        <p>Web Developer | Designer</p>
    </div>
""", unsafe_allow_html=True)

# Stats section
st.markdown("""
    <div class="stats">
        <div>
            <h3>Followers</h3>
            <p>50,000</p>
        </div>
        <div>
            <h3>Likes</h3>
            <p>70,000</p>
        </div>
        <div>
            <h3>Projects</h3>
            <p>6</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Live clock for Home page only
st.markdown("""
    <section id="home" class="section">
        <h2>Welcome to my Portfolio</h2>
        <p>Explore the sections using the sidebar to learn more about me and my work.</p>
        <div id="live-clock-section" class="section">
            <div id="liveClock" style="font-size: 2rem; font-family: 'Courier New', Courier, monospace; color: #ffd700;"></div>
        </div>
    </section>
""", unsafe_allow_html=True)

# Live clock script
live_clock_script = """
    <script>
        function updateClock() {
            const clockElement = document.getElementById('liveClock');
            const now = new Date();
            const timeString = now.toLocaleTimeString();
            clockElement.textContent = timeString;
        }
        setInterval(updateClock, 1000);
        updateClock();
    </script>
"""
st.markdown(live_clock_script, unsafe_allow_html=True)

# Page content
page_content = {
    "About Me": """
        <section id="about-me" class="section">
            <h2>About Me</h2>
            <p>I’m passionate about learning new technologies and creating innovative projects. As a beginner in HTML, CSS, JS, and Node.js, I continually work on enhancing my skills and developing projects that inspire me.</p>
        </section>
    """,
    "Skills": """
        <section id="skills" class="section">
            <h2>Skills</h2>
            <div class="skills-container">
                <div class="skill">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" alt="HTML" class="skill-icon">
                    <p class="skill-name">HTML</p>
                </div>
                <div class="skill">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png" alt="JavaScript" class="skill-icon">
                    <p class="skill-name">JavaScript</p>
                </div>
                <div class="skill">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" class="skill-icon">
                    <p class="skill-name">Python</p>
                </div>
                <div class="skill">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Node.js_logo.svg" alt="Node.js" class="skill-icon">
                    <p class="skill-name">Node.js</p>
                </div>
            </div>
        </section>
    """,
    "Portfolio": """
        <div id="portfolio" class="section">
            <h2>Portfolio</h2>
            <ul class="project-list">
                <li>
                    <img src="https://via.placeholder.com/150" alt="Project Image" class="project-image">
                    <p class="project-description">Project 1</p>
                    <a href="#" class="btn">View Project</a>
                </li>
                <li>
                    <img src="https://via.placeholder.com/150" alt="Project Image" class="project-image">
                    <p class="project-description">Project 2</p>
                    <a href="#" class="btn">View Project</a>
                </li>
            </ul>
        </div>
    """,
    "Resume": """
        <div id="resume-section" class="section">
            <h2>Resume</h2>
            <a href="#" class="resume-btn">Download Resume</a>
        </div>
    """,
    "Achievements": """
        <div id="achievements-section" class="section">
            <h2>Achievements</h2>
            <p>Certificate in Web Development from XYZ Academy</p>
            <p>Completed 100 Days of Code Challenge</p>
        </div>
    """,
    "AdSense": """
        <div id="adsense-section" class="section">
            <h2>AdSense</h2>
            <p>AdSense ads will be displayed here.</p>
        </div>
    """,
    "Coming Soon": """
        <div id="coming-soon-section" class="section">
            <h2>Coming Soon</h2>
            <p>Stay tuned for upcoming updates!</p>
        </div>
    """
}

for section, content in page_content.items():
    st.markdown(content, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
