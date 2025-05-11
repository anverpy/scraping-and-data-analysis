<!-- Professional & Friendly Project Banner -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"/>
  <img src="https://img.shields.io/badge/Last%20Update-May%202025-blueviolet" alt="Last Update"/>
  <img src="https://img.shields.io/badge/Notebooks-Jupyter-orange?logo=jupyter" alt="Jupyter Notebooks"/>
</p>

<p align="center">
  <img src="https://i.imgur.com/6wIQDeI.png" alt="Data Analytics Banner" width="85%"/>
</p>

<p align="center">
  <b>Data Cleaning & Visualization for Machine Learning & Data Analytics Gigs</b><br>
  <i>Fun, robust, and ready for real-world data challenges!</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Visualization-Dark%20Theme-22223b?style=flat-square&logo=visualstudio&logoColor=white" alt="Dark Theme"/>
  <img src="https://img.shields.io/badge/CSV%20Cleaning-Automated-ffb347?style=flat-square&logo=files&logoColor=white" alt="CSV Cleaning"/>
  <img src="https://img.shields.io/badge/Export-PNG%20Charts-4caf50?style=flat-square&logo=picture&logoColor=white" alt="PNG Export"/>
</p>

<!-- Fun Emoji Row -->
<p align="center" style="font-size:1.5em;">
</p>

# Data Cleaning After Web Scraping – Machine Learning & Data Analytics Category
 

## 📢 Disclaimer
This repository contains data that was obtained through web scraping from a publicly accessible website. The purpose of this project is purely educational and non-commercial. It is intended to explore data analysis, visualization, and machine learning techniques for academic learning and personal development.

We do not claim ownership of any content scraped from the website, and no data has been used for redistribution, resale, or to infringe on intellectual property rights. All efforts have been made to ensure ethical use of publicly available information.

If you are a representative of the original website and have any concerns, please feel free to contact me so the content can be reviewed or removed accordingly.

---

### 📌 This document summarizes the cleaning process applied to data scraped from web's results: Machine Learning and Data Analytics gigs. The focus is on solving structural CSV issues caused by embedded commas in gig titles.

### The project is now organized into dedicated folders for each type of analysis, with proper visualization exports and documentation.

---

### 🔍 Target Data Fields
Expected fields for each gig:
- `title`
- `seller`
- `rating`
- `reviews`
- `price`
- `seller_level`
- `video_consultation`

<br><br>
---
# 🧹 1. Data Cleaning

- ## 1.1 Some gig titles included commas without proper quoting, resulting in rows with more than 7 columns. Example:

```csv
 I will create Machine Learning, Deep Learning, and NLP,Andrew Veasman,4.9,152,"1499,90","Level 2",True
```

## If quotes aren't respected, this is parsed as `>7` columns, breaking the CSV structure.


- ## 1.2 There are blank spaces in the ratings, reviews and level sections because there is more gig data than sellers, and sellers who are not located at a certain level yet.
## What does this mean?
### Gigs get ratings and reviews based on the gig, not the seller.<br>Some sellers have two or more gigs published (we'll see this later in the visualization), so there are gigs that have no ratings <br>or reviews. (A clear example is Johannes M.)
<br><br>
---


# 🛠️ 2. Solution Strategy
## A reverse parsing approach was implemented:
### 1. For each row, take the last 6 elements (known fixed fields).
### 2. Consider everything before them as the actual `title`.
### 3. Fill Gaps in rating/reviews/seller_level with unranked/unreviwed/unleveled


<br>

# 🔧 3. Script Summary

## 3.1. Project Structure

All scripts are organized in the `scripts` directory, and there are two versions of the main script: the original `clean_data.py` and an English version `clean_data_en.py`:

```
├── scripts/                      # Script modules directory
│   ├── __init__.py               # Makes 'scripts' a Python package
│   ├── title_extractor.py        # Extracts titles from malformed rows
│   ├── rid_bad_titles.py         # Keeps only the last 6 fields (data fields)
│   ├── merge_titles_untitleds.py # Merges clean titles with data
│   ├── merge_all.py              # Concatenates multiple CSV files
│   └── fill_gaps.py              # Fills missing values
├── clean_data.py                 # Main script to run the entire cleaning process
├── clean_data_en.py              # English version of the main script
├── data-analytics/               # Data Analytics related files
│   ├── DA.ipynb                  # Main DA notebook
│   ├── DA_Dark.ipynb             # Dark-themed visualizations notebook
│   ├── DA-gigs.csv               # Data Analytics dataset
│   └── visualizations/           # Output visualizations for DA
│       └── DA_*.png              # Generated DA visualizations
├── machine-learning/             # Machine Learning related files
│   ├── ML.ipynb                  # ML analysis notebook
│   ├── ML-gigs.csv               # Machine Learning dataset
│   └── visualizations/           # Output visualizations for ML
│       └── ML_*.png              # Generated ML visualizations
└── [Other files]
```

## 3.2. Individual Scripts

### - **[`scripts/title_extractor.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/scripts/title_extractor.py)**: Extracts just the title column from malformed rows.
### - **[`scripts/rid_bad_titles.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/scripts/rid_bad_titles.py)**: Keeps only the last 6 fields, discarding corrupted titles.
### - **[`scripts/merge_titles_untitleds.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/scripts/merge_titles_untitleds.py)**: Merges the cleaned titles back with the corrected data.
### - **[`scripts/merge_all.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/scripts/merge_all.py)**: Concatenates two complete CSVs from separate scraping sessions. Note that CSVs must have the same header names.
### - **[`scripts/fill_gaps.py`](https://github.com/anverpy/scraping-and-data-analysis/blob/main/scripts/fill_gaps.py)**: Fills gaps in rating/reviews/seller_level with unranked/unreviwed/unleveled values.

## 3.3. Running the Cleaning Process

You can run the entire cleaning process using the main script:

```bash
python clean_data_en.py --csv machine-learning/ML-gigs.csv
```

Or for Data Analytics files:

```bash
python clean_data_en.py --csv data-analytics/DA-gigs.csv
```

You may still need to manually remove commas from the titles using Excel or another tool.

## Once the data cleaning is complete, we move forward to the visualization step.

<br>

# 📊 4. Visualization
## The visualizations have been organized into separate folders for Data Analytics and Machine Learning:

- `data-analytics/visualizations/` - Contains all Data Analytics related visualizations
- `machine-learning/visualizations/` - Contains all Machine Learning related visualizations

## The dark-themed visualizations provide better contrast and readability, with all visualizations exported as PNG files.

<br>

# ✅ Outcome
## This process effectively recovered clean, structured data from corrupted CSVs — a common real-world challenge in web scraping and data analysis environments. The structural reverse-engineering logic proved accurate, robust, and reusable solutions.

# 📁 Recent Improvements

## The project has been recently improved with the following enhancements:

1. **Organized Directory Structure**
   - Data Analytics files moved to `data-analytics/` folder
   - Machine Learning files moved to `machine-learning/` folder
   - Each folder has its own `visualizations/` subdirectory

2. **Dark-Themed Visualizations**
   - All visualizations now use a dark background theme
   - Text and chart elements optimized for readability on dark backgrounds
   - All charts exported as PNG files with proper transparency settings

3. **Simplified Dependencies**
   - Reduced requirements.txt to only include necessary libraries
   - Organized dependencies by purpose (data visualization, Jupyter, etc.)
   - Removed extraneous packages for a cleaner installation process
