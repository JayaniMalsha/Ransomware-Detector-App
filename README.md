# Ransomware-Detector-App
An innovative project to simplify complex workflows with intuitive code.

which includes instructions on setting up the environment, running Jupyter Notebook, and launching your Flask app:

markdown
Copy code
# Ransomware Detection Project

This repository contains a machine learning project aimed at detecting ransomware using a dataset available on Kaggle. The project involves preprocessing data, building a Random Forest Classifier, and creating a Flask web application to visualize the results of the ransomware detection.

## Dataset

You can find the dataset used in this project here:
[Ransomware Detection Dataset on Kaggle](https://www.kaggle.com/datasets/amdj3dax/ransomware-detection-data-set)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. Create and Activate a Virtual Environment
To avoid conflicts with your system's Python environment, it is recommended to use a virtual environment.

For Windows:
bash
Copy code
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv env

# Navigate to the Scripts directory
cd env/Scripts

# Activate the virtual environment
activate

# Navigate back to the project root
cd ../../
For macOS/Linux:
bash
Copy code
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv env

# Activate the virtual environment
source env/bin/activate
3. Install the Required Packages
Once the virtual environment is activated, install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Ensure that the requirements.txt file includes the following dependencies:

Copy code
pandas
matplotlib
scikit-learn
flask
4. Download the Dataset
Download the dataset from Kaggle: Ransomware Detection Dataset

After downloading, extract the dataset and move the CSV file into the project directory.

Running the Project
1. Running the Jupyter Notebook
You can explore the data and run the machine learning code using a Jupyter Notebook. Run the following commands:

bash
Copy code
jupyter notebook
This will launch the Jupyter Notebook interface in your web browser, where you can open and run the notebook files.

2. Running the Flask Web App
To run the Flask web app for ransomware detection, execute the following command:

bash
Copy code
python app.py
Once the app is running, open your web browser and go to http://127.0.0.1:5000/. This will allow you to interact with the web application and visualize the ransomware detection results based on user input.

Project Structure
bash
Copy code
|-- env/               # Virtual environment folder
|-- data/              # Folder for the dataset
|-- app.py             # Flask web application
|-- ransomware_detection.ipynb # Jupyter Notebook for data exploration and model training
|-- README.md          # Project documentation
|-- requirements.txt   # Dependencies
Ransomware Detection Web App
The web app allows users to input specific parameters related to file properties (like Machine, DebugSize, etc.) and predict whether the file is likely ransomware based on the machine learning model built with a Random Forest Classifier.

Users can visualize the number of detected ransomware and non-ransomware files with a bar chart in the app interface.
