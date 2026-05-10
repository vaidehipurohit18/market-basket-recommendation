# Real-Time Product Recommendation System using Market Basket Analysis

## Overview

This project is an interactive Product Recommendation System built using Market Basket Analysis and Association Rule Mining techniques.

The system analyzes customer purchasing behavior and generates real-time product recommendations based on products selected by the user.

The dashboard dynamically updates recommendations using association rules generated through the Apriori Algorithm.

---

# Problem Statement

Retail businesses need intelligent recommendation systems to improve:

- Cross-selling
- Product bundling
- Customer experience
- Inventory management
- Sales performance

This project identifies products frequently purchased together and recommends related products in real time.

---

# Project Objectives

- Analyze customer purchase patterns
- Identify frequently purchased item combinations
- Generate association rules using Apriori Algorithm
- Build a real-time recommendation dashboard
- Provide dynamic product recommendations
- Visualize customer buying behavior

---

# Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- Streamlit
- Plotly
- mlxtend
- Joblib

## Tools
- Google Colab
- Visual Studio Code
- GitHub

---

# Machine Learning & Data Mining Concepts

The project uses:

- Market Basket Analysis
- Apriori Algorithm
- Association Rule Mining

Key metrics used:

- Support
- Confidence
- Lift

---

# Features of the Dashboard

The Streamlit dashboard includes:

- Real-time product recommendation engine
- Dynamic shopping cart
- Association-rule-based recommendations
- Product selection interface
- Recommendation ranking using confidence and lift
- Interactive recommendation updates
- Business insights dashboard

---

# How the Recommendation System Works

1. User selects products from the shopping cart.
2. The system checks association rules generated from transaction data.
3. Related products are identified using:
   - Confidence
   - Lift
   - Matching product patterns
4. Recommended products are displayed dynamically in real time.

---

# Example Recommendations

| Selected Product | Recommended Product |
|------------------|--------------------|
| Milk             | Bread, Butter      |
| Laptop           | Mouse, Keyboard    |
| Phone            | Charger, Earphones |
| Burger           | Fries, Soda        |

---

# Dataset

The project uses a simulated retail transaction dataset containing:

- Grocery products
- Electronics
- Beverages
- Household items
- Stationery products

The dataset was designed to simulate realistic customer purchasing patterns for recommendation generation.

---

# Project Structure

```text
market-basket-analysis/
│
├── app.py
├── association_rules.pkl
├── Market_Basket_Analysis.ipynb
├── requirements.txt
├── README.md
```
How to Run the Project
Step 1: Clone Repository
git clone YOUR_GITHUB_REPOSITORY_LINK
Step 2: Open Project Folder
cd market-basket-analysis
Step 3: Install Required Libraries
pip install -r requirements.txt
Step 4: Run Streamlit Dashboard
streamlit run app.py


# Demo
https://drive.google.com/file/d/1-BlADBcIoHP2I-CSHifID1CcIehD20Xk/view?usp=sharing

This recommendation system can be used in:

Retail Stores
E-commerce Platforms
Product Recommendation Systems
Cross-Selling Engines
Customer Analytics
Inventory Optimization
Marketing Campaigns
Future Improvements

Possible future enhancements:

Collaborative Filtering
Deep Learning Recommendation Systems
User Personalization
Real Retail Dataset Integration
Database Integration
Cloud Deployment
User Authentication
Real-Time Purchase Tracking
Conclusion

This project demonstrates how Association Rule Mining and Market Basket Analysis can be used to build an intelligent real-time recommendation system.

The project successfully:

Identified frequent product relationships
Generated association rules
Built a real-time recommendation engine
Developed an interactive Streamlit dashboard
Simulated real-world retail recommendation scenarios

This project highlights the practical application of Data Mining and Artificial Intelligence in Retail Analytics.

Author

Vaidehi Purohit

B.Tech Student | AI & Machine Learning Enthusiast
