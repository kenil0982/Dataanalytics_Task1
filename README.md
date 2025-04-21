# Dataanalytics_Task1
 Objective: Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats).  Tools: Excel / Python (Pandas)  Deliverables: Cleaned dataset + short summary of change
BlinkIT Grocery Data – Data Cleaning Assignment
📌 Objective
This project focuses on cleaning and preprocessing the BlinkIT Grocery dataset. The goal is to ensure the data is accurate, consistent, and ready for analysis or modeling by applying best practices using both Microsoft Excel and Python (Pandas).

📂 Files Included

File Name	Description
BlinkIT_Grocery_Data.xlsx	Raw dataset
BlinkIT_Grocery_Cleaned.xlsx	Cleaned version using Excel
BlinkIT_Grocery_Cleaned.csv	Cleaned version using Python (Kaggle ready)
cleaning_script.py or Notebook	Python script/notebook for data cleaning
README.md	Documentation file (this file)
🧹 Cleaning Steps Performed
Both in Excel and Python, the following data cleaning steps were implemented:

Handled Missing Values

Filled missing values in Item Weight using the column mean.

Removed Duplicates

Dropped exact duplicate rows based on all columns.

Standardized Text Values

Normalized values in Item Fat Content:
LF and low fat → Low Fat, reg → Regular

Date Conversion

Converted Outlet Establishment Year into proper datetime format (01-01-YYYY).

Renamed Column Headers

Made all headers lowercase and replaced spaces with underscores.

Fixed Data Types

Rating converted to integer

Sales ensured as float

🧠 Tools Used

Tool	Purpose
Microsoft Excel	Manual data cleaning and formula-based processing
Python (Pandas)	Automated and scalable cleaning script
Kaggle	Notebook environment for script testing
🚀 How to Run (Python Script)
Upload the raw file (BlinkIT_Grocery_Data.csv) on Kaggle or local.

Run cleaning_script.py or copy the code into a notebook.

Output: BlinkIT_Grocery_Cleaned.csv will be generated.
