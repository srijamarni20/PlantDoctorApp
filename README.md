# 🌱 PlantDoctorApp 🌿

PlantDoctorApp is an innovative application that utilizes the power of artificial intelligence to diagnose and detect diseases in plants. Designed to assist gardeners, farmers, and plant enthusiasts, this application can identify a wide range of plant diseases quickly and accurately, helping users take timely action to protect their crops and greenery.

## 🔑 Key Features

- **Image-Based Diagnosis**: Simply upload an image of a plant with symptoms, and PlantDoctorApp will analyze it to identify the specific disease or issue affecting the plant.

- **📷 Real-Time Camera Input**: Use your device's camera to capture photos of plants, making it convenient for on-the-spot diagnosis and monitoring.

- **🌿 Extensive Plant Database**: PlantDoctorApp is trained on a diverse dataset of plant diseases, ensuring it can recognize a wide variety of issues across different plant species.

- **⚡ Fast and Reliable**: Our AI-powered model delivers rapid and reliable results, allowing users to act promptly to address plant health concerns.

- **🖥️ User-Friendly Interface**: The app features an intuitive and user-friendly interface, making it accessible to individuals of all skill levels.

## 🚀 How It Works

1. **Upload or Capture**: Upload or capture an image of the plant you want to diagnose.

2. **AI Diagnosis**: PlantDoctorApp's AI model will analyze the image and provide a detailed diagnosis, including the name of the disease and recommended actions.

## 📦 Dataset

PlantDoctorApp is trained on a diverse dataset of plant images containing various plant species and their corresponding diseases. You can access the dataset used for training on Kaggle: [Plant Disease Detection Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease).

<div align="center">
    <img src="https://github.com/srijamarni20/PlantDoctorApp/assets/145783038/2f3cec97-73f4-4b3a-9c6a-fbdfcd791712" alt="Sample Plant Disease Dataset">
    <p>Sample Dataset</p>
</div>

## 🧠 Model Architecture

PlantDoctorApp's disease detection model is built using deep learning techniques. It consists of several convolutional layers followed by activation functions, batch normalization, and max-pooling layers. The model's architecture is designed for multi-class classification, where each class corresponds to a specific plant disease. The model is trained using the Adam optimizer and binary cross-entropy loss.

## 📈 Model Training and Evaluation

<div align="center">
    <img src="https://github.com/srijamarni20/PlantDoctorApp/assets/145783038/5a041251-9cfb-47e8-84ac-c9109ce66d5d" alt="Sample Dataset">
    <p>Training and Validation Accuracy</p>
</div>

## 🖼️ Output

Below is an example of the output you can expect when using PlantDoctorApp:

<div align="center">
  <img width="959" alt="image" src="https://github.com/srijamarni20/PlantDoctorApp/assets/145783038/fa0c9938-1333-4059-a69f-78dd90fe9a2d">
  <img width="960" alt="image" src="https://github.com/srijamarni20/PlantDoctorApp/assets/145783038/d20ee637-4a8f-4c1e-a390-4606f7436d1c">
  <img width="960" alt="image" src="https://github.com/srijamarni20/PlantDoctorApp/assets/145783038/71924182-a559-49c9-89c6-60c05a175a8d">
</div>

## Usage

1. Install the required Python packages listed in the `requirements.txt` file.
2. Make sure you have the trained model file `model.h5` available.
3. Run the Streamlit app by executing `streamlit run app.py` in your terminal.

## Dependencies

- Streamlit
- OpenCV
- NumPy
- Keras (with TensorFlow backend)
- PIL (Python Imaging Library)

## 👩‍💻 Author

Srija Marni 
- Department of Computer Science and Engineering  
- Kalasalingam Academy of Research and Education

## 🙏 Acknowledgments

The development of PlantDoctorApp was made possible through the valuable guidance and support of individuals who have contributed their expertise and knowledge. We extend our sincere gratitude to:

- **Mr. R. Raja Subramaniam**
  - Associate HOD of CSE
  - Department of Computer Science and Engineering
  - Kalasalingam Academy of Research and Education
  - GitHub: [R.Raja Subramaniam](https://github.com/RajaSubramanian10)

Mr. R. Raja Subramaniam has been a mentor and guide throughout the development of PlantDoctorApp, providing invaluable insights and direction. His expertise in the field of computer science and commitment to the project's success have been instrumental.

PlantDoctorApp is a testament to the collaborative spirit of our team and the support of our mentors and colleagues. We appreciate their contributions and commitment to the project's success.

## 🙌 Contributors

PlantDoctorApp is the result of collaborative efforts from dedicated contributors who have played a vital role in its development and improvement. We would like to express our gratitude to the following contributors:

1. **Gujula Rohini Reddy**
   - Department of Computer Science and Engineering
   - Kalasalingam Academy of Research and Education

2. **M. Sai Sree Krishna**
   - Department of Computer Science and Engineering
   - Kalasalingam Academy of Research and Education

3. **Bathula Lakshmi Prasanna**
   - Department of Computer Science and Engineering
   - Kalasalingam Academy of Research and Education

We deeply appreciate the dedication and hard work of our contributors, without whom this project would not have been possible. Thank you for being part of the PlantDoctorApp community!
