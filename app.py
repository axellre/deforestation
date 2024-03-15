import streamlit as st
import random

from PIL import Image

def classify_image(image) -> bool:
    """ Classify if an image has palm trees or not
    
    Parameters:
    - image(bytes): image to be classified
    
    Returns:
    - bool: True if omage contains palm trees
    
    """
    
    return random.choice([True, False])

def analyse_image(image):
    """Analyse parts of image that most contribute to classification
    
    Parameters : 
    - image(bytes: image to analyse
    
    Returns: 
    - bytes: image showing most contributve part of the image
    """
    
    return Image.open(image).convert('L')


st.write("## Palm Tree Detector 🌴")

with st.sidebar:
    image_file = st.file_uploader("Choose an image",
                             type=['png', 'jpg'],
                             help='Select image to be classified',
                                 )

if image_file is not None:
        bytes_image = image_file.getvalue()
        st.image(bytes_image, width=350)
    
if st.button('Detect palm trees', disabled=(image_file is None)):
    result = classify_image(bytes_image)
    if result:
        st.write('Palm trees detected')
    else:
        st.write('Palm trees not detected')

    with st.expander('Sentivity Analysis', expanded=False):
        analysis_image = analyse_image(image_file)
        st.image(analysis_image, width=256)
        
        
