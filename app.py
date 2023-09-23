import streamlit as st
import cv2
import numpy as np
from keras.models import load_model
from PIL import Image
import tempfile
import time

st.set_page_config(layout='wide')

# Load the trained model
model = load_model('model.h5')

class_names = [
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]

def predict_disease(image_path):
    try:
        # Load and preprocess the image
        image = cv2.imread(image_path)
        if image is not None:
            image = cv2.resize(image, (256, 256))  # Resize the image to match the model's input size
            image = image.astype("float") / 255.0  # Normalize the pixel values

            # Make a prediction
            image = np.expand_dims(image, axis=0)  # Add a batch dimension
            prediction = model.predict(image)

            # Get the class label with the highest probability
            predicted_class_index = np.argmax(prediction)
            
            # Get the predicted class name
            predicted_class_name = class_names[predicted_class_index]

            return predicted_class_name
        else:
            return "Error: Failed to load the image."
    except Exception as e:
        return str(e)




title = st.container()
body = st.container()
temp1 = 0
predicted_class_name = ''
with title:
        st.markdown(
        """
            <style>
            .title{
                text-align: center;
                font-weight: bold;
            }
            .mainheading{
                text-align: center;
                font-family: monospace;
                font-size: 25px;
            }
            </style>
        """,
        unsafe_allow_html=True
        )
        st.markdown('<h2 class="title">Plant Doctor</h2>',unsafe_allow_html=True)
        st.markdown('<h3 class="mainheading">Detecting Plant Diseases with AI</h3>',unsafe_allow_html=True)


     

with body:
            task1 = ["Upload Image", "Camera Input"]
            uploaded_file = ''
            choice = st.selectbox("Select option",task1)
            if choice == 'Upload Image':
                uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png",'jpeg'])
            elif choice == 'Camera Input':
                uploaded_file = st.camera_input("Take a picture")
            
            

            c1, c2, c3 = st.columns([1,3,1])
            with c2:
                if uploaded_file is not None:  
                       with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                            temp_file.write(uploaded_file.read())
                            image_path = temp_file.name

                       image = Image.open(uploaded_file)
                       st.image(image, caption='Uploaded Image', use_column_width=True)
                        
                       c11,c22,c33,c44,c55 = st.columns([1,1.5,1.3,1,1])
                       with c33:
                           if st.button('Predict'):
                               temp1 = 1
                               predicted_class_name = predict_disease(image_path)
                               #print(predicted_class_name)
                               with st.spinner(text='Predicting...'):
                                    time.sleep(2)
                       if temp1 == 1:
                            html_code = f"""
                            <div style='
                                    background-color: #2A2937;
                                    border-radius: 5px;
                                    padding: 20px;
                                    text-align: center;
                                    font-family: Arial;
                                    font-size: 15px;
                            '>
                            <h4>{'Model Detected - '+predicted_class_name}</h4>
                            </div>
                            """
                            st.markdown(html_code,unsafe_allow_html=True)

     