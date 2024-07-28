import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Profile", page_icon=":smiley:", layout="wide")

# CSS for the profile page
css = """
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    color: #fff;
    line-height: 1.6;
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background: rgba(0, 0, 0, 1.10);
    border-radius: 1px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
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
    width: 200px;
    height: 200px;
    border-radius: 50%;
    margin: 20px auto;
    display: block;
    border: 5px solid #ffd700;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
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
.navbar {
    background-color: #2a2a2a;
    overflow: hidden;
    border-radius: 8px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-around;
}
.navbar a {
    display: block;
    color: #fff;
    text-align: center;
    padding: 15px 20px;
    text-decoration: none;
    transition: background-color 0.3s, transform 0.3s;
}
.navbar a:hover {
    background-color: #444;
    transform: scale(1.05);
}
.section {
    padding: 20px;
    margin-bottom: 40px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}
.section h2 {
    color: #ffd700;
    margin-bottom: 20px;
}
.section p {
    color: #ddd;
    line-height: 1.8;
}
.resume {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 40px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    text-align: center;
}
.resume h2 {
    color: #ffd700;
    margin-bottom: 20px;
}
.resume p {
    color: #ddd;
    margin-bottom: 20px;
    font-size: 1.2rem;
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
    background-color: #1e3c72;
    transform: scale(1.05);
}
.project-list {
    list-style-type: none;
    padding: 0;
}
.project-list li {
    margin-bottom: 40px;
    text-align: center;
}
.project-image {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 10px;
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
#live-clock-section {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 40px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    text-align: center;
}
#live-clock-section h2 {
    color: #ffd700;
    margin-bottom: 20px;
}
.btn {
    display: inline-block;
    padding: 12px 25px;
    background-color: #ffd700;
    color: #000;
    text-decoration: none;
    text-align: center;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
}
.btn:hover {
    background-color: #ffcc00;
    transform: scale(1.05);
}
.project-list {
    list-style-type: none;
    padding: 0;
}
.project-list li {
    margin-bottom: 25px;
}
.project-description {
    margin-bottom: 10px;
}
.contact-info {
    text-align: center;
    margin-top: 20px;
}
.contact-info a {
    color: #ffd700;
    text-decoration: none;
}
.contact-info a:hover {
    text-decoration: underline;
}
.achievements {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 40px;
}
.achievements h2 {
    color: #ffd700;
}
.achievement-item {
    margin-bottom: 15px;
}
.achievement-item h3 {
    margin-bottom: 5px;
}
.achievement-item p {
    margin: 0;
    color: #ddd;
}
.video-gallery {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 40px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}
.video-gallery h2 {
    color: #ffd700;
    margin-bottom: 20px;
    text-align: center;
}
.scroll-notice {
    color: #ffd700;
    text-align: center;
    margin-bottom: 20px;
    font-size: 1.2rem;
}
.video-gallery-container {
    display: flex;
    overflow-x: auto;
    gap: 20px;
    padding: 10px;
    scroll-snap-type: x mandatory;
}
.video-item {
    flex: 0 0 auto;
    width: 300px;
    background: rgba(0, 0, 0, 0.6);
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    scroll-snap-align: start;
}
.video-item iframe {
    width: 100%;
    height: 200px;
    border: none;
}
.video-description {
    padding: 10px;
    color: #ddd;
}
footer {
    background-color: #2a2a2a;
    color: #fff;
    padding: 20px 0;
    text-align: center;
    position: fixed;
    bottom: 0;
    width: 100%;
}
footer p {
    margin: 0;
}
footer a {
    color: #ffd700;
    text-decoration: none;
}
footer a:hover {
    text-decoration: underline;
}
.btn {
    display: inline-block;
    padding: 12px 25px;
    background-color: #ffd700;
    color: #000;
    text-decoration: none;
    text-align: center;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.3s;
}
.btn:hover {
    background-color: #ffcc00;
    transform: scale(1.05);
}
.centered {
    text-align: center;
}
"""

# HTML for the profile page
html_content = """
<div class="header">
    <h1>John Doe</h1>
    <img src="https://via.placeholder.com/200" alt="Profile Picture" class="profile-picture">
</div>
<div class="navbar">
    <a href="#about">About Me</a>
    <a href="#portfolio">Portfolio</a>
    <a href="#contact">Contact</a>
</div>
<div class="section" id="about">
    <h2>About Me</h2>
    <p>Hello! I'm John Doe, a passionate web developer with a knack for creating visually appealing and user-friendly websites. I have a strong background in HTML, CSS, and JavaScript, and I'm constantly learning new technologies to enhance my skills.</p>
</div>
<div class="section" id="portfolio">
    <h2>Portfolio</h2>
    <ul class="project-list">
        <li>
            <img src="https://via.placeholder.com/150" alt="Project Image" class="project-image">
            <div class="project-description">
                <h3>Project Title 1</h3>
                <p>Short description of the project.</p>
                <a href="#" class="btn">View Project</a>
            </div>
        </li>
        <li>
            <img src="https://via.placeholder.com/150" alt="Project Image" class="project-image">
            <div class="project-description">
                <h3>Project Title 2</h3>
                <p>Short description of the project.</p>
                <a href="#" class="btn">View Project</a>
            </div>
        </li>
    </ul>
</div>
<div class="resume" id="contact">
    <h2>Contact Me</h2>
    <p>If you'd like to get in touch, please send me an email at <a href="mailto:example@example.com">example@example.com</a>.</p>
</div>
<footer>
    <p>© 2024 John Doe. All rights reserved.</p>
</footer>
"""

# Render the HTML and CSS in Streamlit
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
html(html_content, height=800)
