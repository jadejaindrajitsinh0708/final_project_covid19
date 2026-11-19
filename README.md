# 🦠 COVID-19 Data Analysis Project

## 📌 Project Overview
This project is based on **COVID-19 Data Analysis using Python**. It helps users explore, clean, analyze, and visualize COVID-19 data using different Python libraries.

The project uses a CSV dataset (`covid19.csv`) to perform various data analysis operations and generate meaningful insights through charts and statistical summaries.

## 🎯 Project Objectives
- Load COVID-19 data from a CSV file.
- Explore dataset information.
- Identify and handle missing values.
- Remove duplicate records.
- Check invalid values.
- Perform statistical and country-wise analysis.
- Visualize COVID-19 data using different charts.
- Display final analysis results.

## 🛠️ Technologies & Libraries Used

- **Python** – Programming Language
- **Pandas** – Data manipulation and analysis
- **Seaborn** – Data visualization
- **Matplotlib** – Graphical representation
- **Git Hub**
- **Git**
## 📂 Project Structure

```text
COVID-19-Data-Analysis/
│
├── covid19.csv
├── main.py
└── README.md
```

## 📊 Project Features

### 1. Explore Dataset
Users can explore the dataset through the following options:

- Display First 5 Rows
- Display Last 5 Rows
- Display Column Names
- Display Data Types
- Display Dataset Information
- Display Statistical Summary

### 2. Clean Dataset
This section provides different data cleaning operations:

- Check Missing Values
- Remove Missing Values
- Fill Missing Values
- Check Duplicate Rows
- Remove Duplicate Rows
- Check Invalid Values (Negative Confirmed, Deaths, and Recovered Cases)

### 3. Data Analysis
The project performs the following analysis:

- Total Confirmed Cases
- Total Deaths
- Total Recovered Cases
- Total Active Cases
- Maximum and Minimum Confirmed Cases
- Average Confirmed Cases
- Country-wise Confirmed Cases
- Country-wise Deaths
- Top 10 Countries with Highest Confirmed Cases

### 4. Data Visualization
Different charts are used to understand COVID-19 data visually.

- **Bar Chart:** Top 10 Countries with Highest Confirmed Cases.
- **Pie Chart:** COVID-19 Cases Distribution.
- **Line Chart:** Confirmed Cases Trend Over Time.
- **Scatter Plot:** Confirmed vs Recovered Cases.
- **Histogram:** Confirmed Cases Distribution.

### 5. Analysis Results
Displays the overall analysis results, including:

- Total Confirmed Cases
- Total Deaths
- Total Recovered
- Total Active Cases
- Maximum Confirmed Cases
- Minimum Confirmed Cases
- Average Confirmed Cases
- Total Number of Countries

## 📁 Dataset Information

The project uses a CSV file named `covid19.csv`.

Important dataset columns:

| Column Name | Description |
|---|---|
| Country_Region | Country Name |
| Confirmed | Total Confirmed Cases |
| Deaths | Total Deaths |
| Recovered | Total Recovered Cases |
| Active | Total Active Cases |
| Last_Update | Last Updated Date |

**Note:** The dataset should contain the above-mentioned columns for the program to work correctly.

## ⚙️ Installation & Requirements

Make sure Python is installed on your system.

Install the required libraries using:

```bash
pip install pandas seaborn matplotlib
```

## ▶️ How to Run the Project

**Step 1:** Download or clone the project.

```bash
git clone <your-repository-link>
```

**Step 2:** Open the project folder.

```bash
cd COVID-19-Data-Analysis
```

**Step 3:** Make sure `covid19.csv` is available in the project folder.

**Step 4:** Run the Python program.

```bash
python covid19_analysis.py
```

**Step 5:** Enter the CSV filename when prompted.

```text
Enter CSV File Name: covid19.csv
```

**Step 6:** Select an option from the main menu to explore, clean, analyze, and visualize the dataset.

## 📈 Expected Output

The program provides:
- Dataset exploration details.
- Missing and duplicate values information.
- Statistical analysis of COVID-19 cases.
- Country-wise COVID-19 statistics.
- Different graphical visualizations.
- Final analysis summary.


## 👨‍💻 Author
 INDRAJIT SINH JADEJA

