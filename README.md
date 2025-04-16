# Introduction
## 🧹 Data Cleaning After Web Scraping – Machine Learning Category

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

---

# ⚠️ 1. The Problem
## Some gig titles included commas without proper quoting, resulting in rows with more than 7 columns. Example:

```csv
 I will create Machine Learning, Deep Learning, and NLP,Andrew Veasman,4.9,152,"1499,90","Level 2",True
```

## If quotes aren't respected, this is parsed as `>7` columns, breaking the CSV structure.
<br>

# 🛠️ 2. Solution Strategy
## A reverse parsing approach was implemented:
### 1. For each row, take the last 6 elements (known fixed fields).
### 2. Consider everything before them as the actual `title`.
### 3. Reassemble a row with exactly 7 columns.
### 4. Optionally, remove internal quotes or replace commas in `title` for analysis.

## This method works regardless of how many commas the `title` includes.
<br>

# 🔧 3. Script Summary

### - **`title_extractor.py`**: Extracts just the title column from malformed rows.
### - **`rid_bad_titles.py`**: Keeps only the last 6 fields, discarding corrupted titles.
### At this point i erase all "," in Excel using `CTRL + B` but you can improve it by adding the function in any of these scripts.
### - **`merge_titles_untitleds.py`**: Merges the cleaned titles back with the corrected data.
### - **`merge_all.py`**: Concatenates two complete CSVs from separate scraping sessions cases. Be notice the csvs must to have the same headers names.
## Once made the data cleaning, we move forward to the next step.

<br>

# 📊 4. Visualitazion
### - **`.py`**: Notes

# ✅ Outcome
### This process effectively recovered clean, structured data from corrupted CSVs — a common real-world <br>  challenge in web scraping and data analysis enviroments. <br> The structural reverse-engineering logic proved accurate, robust, and reusable solutions.
