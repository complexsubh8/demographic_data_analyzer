# Demographic Data Analyzer

This project is part of the freeCodeCamp **Data Analysis with Python** certification.

## Project Description

Using the 1994 Census dataset and the Pandas library, this project analyzes demographic information and answers several statistical questions about income, education, race, occupation, and working hours.

## Technologies Used

* Python
* Pandas

## Dataset

The dataset used is the Adult Census Income Dataset from the UCI Machine Learning Repository.

## Features

The program calculates:

* Number of people of each race
* Average age of men
* Percentage of people with a Bachelor's degree
* Percentage of people with advanced education earning more than 50K
* Percentage of people without advanced education earning more than 50K
* Minimum number of work hours per week
* Percentage of high earners among minimum-hour workers
* Country with the highest percentage of people earning more than 50K
* Most popular occupation in India among people earning more than 50K

## How to Run

1. Install Pandas:

```bash
pip install pandas
```

2. Place `adult.data.csv` in the project directory.

3. Run:

```bash
python main.py
```

## Example Output

* Average age of men: 39.4
* Percentage with Bachelor's degrees: 16.4%
* Highest earning country: Iran
* Highest earning country percentage: 41.9%
* Top occupation in India: Prof-specialty

## Project Structure

```
Demographic_Data_Analyzer/
│
├── adult.data.csv
├── demographic_data_analyzer.py
├── main.py
└── README.md
```

## Author

Subham Sarkar

## Certification

freeCodeCamp - Data Analysis with Python
