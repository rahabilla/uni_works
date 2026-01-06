# Spam vs Ham Email Classifier

This project implements a binary text classification system aimed at distinguishing between spam and legitimate (ham) emails or messages by using traditional machine learning approaches.

## Features

- Preprocesses email text by performing tokenization, removing stopwords, and applying stemming.  
- Converts text into numerical features using TF-IDF vectorization.  
- Trains a Multinomial Naive Bayes classifier on the prepared dataset.  
- Provides an easy-to-use Streamlit web application for interactive message classification.  
- Includes example spam and ham messages for quick testing and demonstration.

## Dataset

The classifier is trained on a publicly available spam dataset containing two main columns:

- `label`: Indicates whether a message is spam or ham.  
- `text`: Contains the content of the email or SMS message.

## Installation

Clone the repository:

Install the necessary dependencies:

pip install -r requirements.txt

### Usage

Run the training script to preprocess the data, train the classifier, and save both the trained model and the TF-IDF vectorizer


### Run the Streamlit App
Start the interactive web app to classify messages:

streamlit run streamlit_app.py

### Dependencies
Python 3.7 or higher

pandas

numpy

scikit-learn

nltk

streamlit


The classifier performs well on balanced datasets but might occasionally miss some spam messages. You are encouraged to experiment with other algorithms or add features to improve the model’s performance.

### License
This project is open source and distributed under the MIT License.
