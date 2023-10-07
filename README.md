# Twitter Data Analysis - Technology, Economy, and Politics Communities Analysis

## Project Overview

This project aims to analyze Twitter data related to technology, economy, and politics communities in the United States. The analysis involves clustering, keyword analysis, and sentiment analysis, providing valuable insights into these domains.

## Disclaimer

1. K-means clustering's initial centroids are chosen randomly, causing slight variations in the clusters and visualizations each time the code is run. Despite this, the results remain consistent across different runs.
2. As of 5th May 2023, Twitter has revoked our developer access. The keys in the file `DataExtraction.py` are no longer valid. We have provided links to the downloaded dataset for reference.

## Libraries Used

The analysis utilized various Python libraries including but not limited to:
- Pandas
- Numpy
- Collections
- Textblob
- Scikit-learn
- NLTK
- Gensim
- Seaborn
- PyLDAvis
- Geopy
- Folium

## Data

The Twitter data was collected using the Twitter API and encompasses tweets related to technology, economy, and politics communities in the United States. The data was stored in CSV files and loaded into Pandas dataframes for analysis.

## Techniques Used

### Clustering
- **K-means**
- Silhouette scores
- MDS (Multi-Dimensional Scaling)

### Sentiment Analysis
- NRC Lexicon
- NRC VAD
- AFINN Analysis
- Vader Analysis
- Polarity and Subjectivity score

### Keyword Analysis
- LDA Modelling
- Word Cloud Analysis
- Summarization
