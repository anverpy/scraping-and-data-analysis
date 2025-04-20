# Introduction
## Data Cleaning After Web Scraping – Machine Learning & Data Analytics Category

# 📢 Disclaimer
This repository contains data that was obtained through web scraping from a publicly accessible website. The purpose of this project is purely educational and non-commercial. It is intended to explore data analysis, visualization, and machine learning techniques for academic learning and personal development.

We do not claim ownership of any content scraped from the website, and no data has been used for redistribution, resale, or to infringe on intellectual property rights. All efforts have been made to ensure ethical use of publicly available information.

If you are a representative of the original website and have any concerns, please feel free to contact me so the content can be reviewed or removed accordingly.

### 📌 This document summarizes the cleaning process applied to data scraped from web's results *Machine Learning* gigs. <br> The focus is on solving structural CSV issues caused by embedded commas in gig titles.

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

### - **`title_extractor.py`**: Extracts just the title column from malformed rows.
### - **`rid_bad_titles.py`**: Keeps only the last 6 fields, discarding corrupted titles.
### - At this point i erase all "," in Excel using `CTRL + B` but you can improve it by adding the function in any of these scripts.
### - **`merge_titles_untitleds.py`**: Merges the cleaned titles back with the corrected data.
### - **`merge_all.py`**: Concatenates two complete CSVs from separate scraping sessions cases. Be notice the csvs must to have the same headers names.
### - **`fill_gaps.py`**: Gaps in rating/reviews/seller_level filled with unranked/unreviwed/unleveled.
## Once made the data cleaning, we move forward to the next step.

<br>

# 📊 4. Visualitazion
## In the repository you have both .ipynb files with code to understand the generation of graphs.

<br>

# ✅ Outcome
## This process effectively recovered clean, structured data from corrupted CSVs — a common real-world <br>  challenge in web scraping and data analysis enviroments. <br> The structural reverse-engineering logic proved accurate, robust, and reusable solutions.
