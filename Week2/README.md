# Week 2: Data Handling & Visualization – Titanic EDA

## Overview
This project performs an **Exploratory Data Analysis (EDA)** on the Titanic dataset. The goal is to understand the dataset, clean and preprocess the data, visualize patterns, and gain insights about the survival rates of passengers.

## Dataset
The dataset is sourced from [Kaggle / DataScienceDojo Titanic Dataset](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv).  
It contains information about passengers aboard the Titanic, such as:

- PassengerId
- Survived (0 = No, 1 = Yes)
- Pclass (Passenger class)
- Name
- Sex
- Age
- SibSp (Number of siblings/spouses aboard)
- Parch (Number of parents/children aboard)
- Ticket
- Fare
- Cabin
- Embarked (Port of embarkation)

## Tools & Libraries Used
- Python 3.x
- [NumPy](https://numpy.org/) – numerical computations
- [Pandas](https://pandas.pydata.org/) – data handling and manipulation
- [Matplotlib](https://matplotlib.org/) – data visualization
- [Seaborn](https://seaborn.pydata.org/) – advanced visualizations
- [Jupyter Notebook / Google Colab](https://colab.research.google.com/) – notebook environment

## Steps Performed
1. **Data Loading & Inspection**  
   - Loaded dataset from GitHub URL
   - Inspected columns, datatypes, and missing values

2. **Data Cleaning & Preprocessing**  
   - Filled missing `Age` values with median
   - Filled missing `Embarked` values with mode
   - Dropped the `Cabin` column (too many missing values)

3. **Exploratory Data Analysis (EDA)**  
   - Analyzed survival rate by `Sex`, `Pclass`, and `Embarked`
   - Visualized distributions of `Age`, `Fare`, and other numerical features
   - Created correlation heatmaps to identify feature relationships

4. **Insights & Observations**  
   - Females had a higher survival rate than males
   - Passengers in higher classes (Pclass=1) survived more
   - Age distribution shows children had slightly higher survival chances
   - Fare and class are positively correlated

## How to Run
1. Open the notebook in **Google Colab** or **Jupyter Notebook**
2. Ensure the following libraries are installed:
   ```bash
   pip install numpy pandas matplotlib seaborn
   ```
3. Run the notebook step by step to see the data analysis and visualizations.