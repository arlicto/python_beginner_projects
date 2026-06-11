# Sonar Rock vs Mine Classification

A machine learning project using logistic regression to classify sonar signals as either rocks or mines.

## Dataset

The project uses sonar data with 60 features and a binary target variable (Rock/Mine).

## Model

- **Algorithm**: Logistic Regression
- **Train/Test Split**: 90% / 10% with stratified sampling
- **Framework**: scikit-learn

## Files

- `main.ipynb` - Jupyter notebook with complete ML pipeline
- `Copy of sonar data.csv` - Dataset for training and testing

## Requirements

- numpy
- pandas
- scikit-learn

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install numpy pandas scikit-learn jupyter
   ```

3. Run the notebook:
   ```bash
   jupyter notebook main.ipynb
   ```

## Project Structure

The notebook includes:
1. Data Collection and Processing
2. Exploratory Data Analysis
3. Train/Test Split
4. Model Training (Logistic Regression)
5. Model Evaluation
6. Predictive System

## Results

Model accuracy is evaluated on both training and test data to assess generalization.
