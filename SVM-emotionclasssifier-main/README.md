# Emotion Classification Using SVM

## Project Overview
Text data from social media and other online platforms contain rich emotional expressions. Accurately identifying emotions from such text can support applications in sentiment analysis, mental health monitoring, customer feedback systems, and more.

This project builds a machine learning model to classify emotions expressed in English-language short texts using Support Vector Machines (SVM). The dataset contains messages pre-labeled with one of six basic emotions.

The goals are to:
- Preprocess raw text data
- Compare different SVM kernel functions for classification performance
- Train a final SVM model using the best kernel
- Apply clustering for exploratory analysis of emotional content

---

## Dataset
- The dataset used (`emotions (1).csv`) includes:
  - `text`: The textual content
  - `label`: The emotion label (one of six basic emotions)

---

## Project Structure

- **Data Preprocessing:**  
  Clean text by removing URLs, mentions, hashtags, punctuation, numbers, and stopwords.

- **Feature Extraction:**  
  Convert text into numeric features using TF-IDF vectorization.

- **Clustering:**  
  Perform K-Means clustering on TF-IDF vectors to explore groupings of emotional expressions.

- **Model Training and Evaluation:**  
  - Compare SVM models with different kernels: linear, polynomial, and RBF.
  - Evaluate models on a subset for kernel comparison.
  - Train a final linear SVM model on the full dataset.
  - Evaluate using accuracy, classification reports, and confusion matrices.

- **Model Persistence:**  
  Save the trained model and vectorizer for future predictions.

---

## Dependencies

- Python 3.x
- pandas
- scikit-learn
- nltk
- matplotlib
- seaborn
- joblib
- re

Make sure to download NLTK stopwords:
```python
import nltk
nltk.download('stopwords')
