**Real-Time News Sentiment Dashboard**

This project involves building a real-time news sentiment classification and visualization dashboard. It collects the latest news headlines from **NewsAPI** (with **GNews** as a fallback), classifies each headline as **Positive** or **Negative**, and displays the results through a **Streamlit-based dashboard**.

---

### Features

* Retrieve real-time news from **NewsAPI** or **GNews**.
* Perform sentiment classification on headlines as **Positive** or **Negative** using **TextBlob**.
* Save classified results in **Parquet** format for historical tracking.
* Visualization components include:

  * Display of the most recent headlines with their sentiment labels.
  * Sentiment distribution represented using bar charts.
  * Positive sentiment trends over time illustrated through line charts.
* Fully deployable on **Streamlit Cloud**.

---

### Requirements

* **Python 3.9+**
* Required libraries:

  * `streamlit`
  * `pandas`
  * `plotly`
  * `textblob`
  * `gnews`
  * `requests`
  * `pyarrow`
