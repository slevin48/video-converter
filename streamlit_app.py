import streamlit as st
from moviepy.editor import VideoFileClip
import os
import tempfile

def convert_and_save_video(uploaded_file):
    # Create a temporary file to hold the uploaded video
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())
    
    # Load video file using MoviePy
    clip = VideoFileClip(tfile.name)
    
    # Define the name for the converted file
    webm_file = os.path.splitext(tfile.name)[0] + ".webm"
    
    # Convert and Save the video to webm format
    clip.write_videofile(webm_file, codec='libvpx')
    
    # Return the name of the converted file
    return webm_file

# Streamlit app
st.title("MP4 to WebM Converter")

uploaded_file = st.file_uploader("Choose a video file", type=['mp4'])

if uploaded_file is not None:
    st.video(uploaded_file)
    with st.spinner('Converting...'):
        webm_file = convert_and_save_video(uploaded_file)
    st.success('Conversion complete!')
    st.video(webm_file)
