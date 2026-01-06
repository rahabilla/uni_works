# Skill-Based Job Clustering Using Hierarchical Algorithms

This project is designed to collect job listings from [karkidi.com](https://www.karkidi.com) and categorize them based on required skills using a machine learning technique called Hierarchical (Agglomerative) Clustering. The objective is to identify natural groupings among job postings, making it easier to analyze market trends and assist job seekers in finding roles aligned with their skills.

---

##  Key Highlights

* Automatically extracts job titles, companies, locations, experience, summaries, and required skills from the site.
* Processes the skills section using standard NLP techniques like text cleaning and tokenization.
* Transforms skill descriptions into numerical features using TF-IDF vectorization.
* Uses **Agglomerative Clustering** to group similar jobs without needing predefined labels.
* Saves the:

  * Clustering model
  * TF-IDF vectorizer
  * Grouped job data
* **Optional Features**:

  * Set up skill-based alerts for users
  * Automate daily scraping and clustering for continuous updates

---

##  How to Set Up & Use

### Prerequisites

* Python 3.7 or above
* Required packages:

```bash
pip install -r requirements.txt
```

### Running the Main Script

Execute the following to perform scraping and clustering:

```bash
python daily_scrape_and_cluster.py
```

The script will:

* Scrape a set number of pages (default: 2)
* Clean and preprocess the 'skills' column
* Apply TF-IDF and perform clustering
* Save:

  * Model (`model/karkidi_model.pkl`)
  * Vectorizer (`model/karkidi_vectorizer.pkl`)
  * Clustered job data (`clustered_jobs.csv`)

---

##  Interactive Web App (Optional)

The included Streamlit app (`app.py`) offers a basic interface to:

* View job listings by cluster
* Filter results based on cluster ID
* (Optional) Notify users when new listings align with saved skills

Run the app locally with:

```bash
streamlit run app.py
```

---

##  Automating the Pipeline (Optional)

To schedule scraping and clustering regularly:

* **Linux/macOS**: Use `cron` jobs
* **Windows**: Use Task Scheduler
* **GitHub Actions**: Automate via CI/CD workflows

Reloading the Streamlit app will show updated results after each run.

---

##  Directory Layout

```bash

.
├── app.py                  # Streamlit-based user interface 
├── clustered_jobs.csv      # Output CSV of job listings with cluster labels
├── jobclassification.py    # Core script: scraping, preprocessing & clustering
├── karkidi_model.pkl       # Saved clustering model
├── karkidi_vectorizer.pkl  # Saved TF-IDF vectorizer
├── requirements.txt        # Required dependencies
└── README.md               # Project documentation


```


---
