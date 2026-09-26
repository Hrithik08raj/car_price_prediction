# 🚗 Car Price Prediction

A machine learning web application that predicts the estimated resale price of a used car based on its **car model, company, manufacturing year, kilometers driven, and fuel type**.

The project covers the complete workflow from **data cleaning and preprocessing to machine learning model training and deployment through a FastAPI web application**.

---

## 📌 Project Overview

Used-car prices depend on several factors such as the vehicle's age, brand, model, fuel type, and kilometers driven.

This project uses historical used-car listing data to build a machine learning model that estimates the price of a car based on these features.

The project includes:

- Data cleaning and preprocessing
- Exploratory data preparation
- Categorical feature encoding
- Train/test splitting
- Linear Regression model development
- Model evaluation using R² score
- Model serialization using Pickle
- FastAPI backend
- Interactive web interface for price prediction

---

## 🎯 Objectives

The main objectives of this project are:

- Clean and prepare raw used-car listing data.
- Transform categorical and numerical features into a format suitable for machine learning.
- Train a regression model to predict used-car prices.
- Evaluate model performance using the R² metric.
- Save the trained model for reuse.
- Build a web application that allows users to enter vehicle details and receive an estimated price.

---

## 📂 Dataset

The original dataset contains used-car listing information with the following columns:

| Feature | Description |
|---|---|
| `name` | Car model/name |
| `company` | Car manufacturer |
| `year` | Manufacturing year |
| `Price` | Listed car price |
| `kms_driven` | Kilometers driven |
| `fuel_type` | Fuel type |

The original dataset contains **892 records**.

After data cleaning and preprocessing, the final dataset contains **816 records**.

---

## 🧹 Data Cleaning & Preprocessing

Several data-quality issues were handled before training the model.

### 1. Year Cleaning

Rows containing non-numeric values in the `year` column were removed.

The `year` column was then converted from object/string format to integer.

### 2. Price Cleaning

Rows containing:

```text
Ask For Price
