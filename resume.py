import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from datetime import datetime
import plotly.graph_objects as go
import altair as alt
import pandas as pd
from fpdf import FPDF
import base64
import timeline
import preprocess
#from color import custom_progress_bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_box(text,color):
    st.markdown(
    f"""
     <br></br>
    <div style='
        display: flex; 
        justify-content: center; 
        align-items: center; 
        width: 300px; 
        height: 60px; 
        background-color: {color}; 
        color: white; 
        font-size: 24px; 
        text-align: center; 
        border-radius: 10px; 
        box-shadow: 5px 5px 10px grey;'>
        {text}
       
    </div>
    <br></br>
    """,
    unsafe_allow_html=True,)


def display_header(name, social_urls, photo_path):
    # Load the photo using PIL
    photo = Image.open(photo_path)

    # Display the photo and name
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.sidebar.image(photo, use_column_width=False)
    with col2:
        st.sidebar.write(f"# {name}")

    # Display the social URLs
    st.write("")
    for url in social_urls:
        st.sidebar.write(f"[{url}]({url})")



def display_timeline():
    generate_box("Work History","darkblue")
    #with open('timeline.html', 'r') as f:
    #    html_code = f.read()
    html(timeline.html,width=1000,height=1000)




def display_activities():
    generate_box("Daily Activities","darkblue")
    # Define the daily activities
    activities = preprocess.activities

    # Define the time spent on each activity in minutes
    timespent = preprocess.time_spent

    # Create a bar chart using Plotly
    #fig = go.Figure(data=[go.Bar(x=activities, y=timespent)])
    fig = go.Figure(data=[go.Pie(labels=activities, values=timespent)])
    # Update the layout of the chart
    fig.update_layout(
        title={
            'text': 'My Daily Activities',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title="Activity",
        yaxis_title="Time Spent (minutes)",
        font=dict(
            family="Arial, monospace",
            size=14,
            color="#7f7f7f"
        )
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig)




def tools_and_frameworks():
    generate_box("Tools and Frameworks", "darkblue")
    text = " ".join(preprocess.tools)

    # Define the width and height of each bar
    width = 500
    height = 20

    # Loop through each skill and display its rating as a progress bar
    wordcloud = WordCloud(width=800, height=400, colormap='Blues', background_color='white').generate(text)

# Display the word cloud in Streamlit
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)


    
def certifcations():
    generate_box("Certifications","darkblue")

    #st.datatable()

def display_skills():
    # Define the skills and their ratings
    generate_box("Technical and Soft Skills","darkblue")
    skills = preprocess.skills

    # Define the width and height of each bar
    width = 500
    height = 20

    # Loop through each skill and display its rating as a progress bar
    for skill, rating in skills.items():
        # Set the text to display next to the progress bar
        text = f"{skill} ({rating}/10)"
        # Use st.text() to display the text
        st.text(text)
        # Use st.progress() to display the progress bar
        st.progress(rating / 10)

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

def rendered_page():
    st.empty()
    p_name = preprocess.profile_info["name"]
    social_urls = [preprocess.profile_info["linkedin"],preprocess.profile_info["github"]]
    photo_path = "IdCard.jpg"
    display_header(p_name, social_urls, photo_path)

    checkbox_names = [ "Work Experience", "Skills", "Tools and Frameworks","Daily Activities"]
    #download=st.sidebar.button("Download")

    # Loop through each checkbox name and create the checkbox
    count=0
    for name in checkbox_names:
        # Use st.sidebar.checkbox() to create the checkbox
        checked = st.sidebar.checkbox(name)
        # Use the value of the checkbox (True or False) to determine what to display
        if checked:
            if name==checkbox_names[0]:
                display_timeline()
            elif name==checkbox_names[1]:
                display_skills()
            elif name==checkbox_names[2]:
                tools_and_frameworks()
            elif name==checkbox_names[3]:
                display_activities()
        else:
            #st.write(f"{name} is not checked.")
            pass
    


rendered_page()