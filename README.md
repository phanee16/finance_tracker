# Personal Finance Tracker

## Overview
Creating a website for a graduate project that incorporates HTML, CSS, JavaScript, Python, SQL, and Streamlit can be a fun and rewarding experience. This project, "Personal Finance Tracker," aims to help users manage their finances by tracking expenses, visualizing spending patterns, and generating reports.

## Project Outline

### Front-End
- **HTML/CSS/JavaScript:**
  - Create user interface for adding expenses, viewing reports, and managing accounts.
  - Style the website for user-friendly and visually appealing experience.
  - Implement interactivity with JavaScript for form validation and dynamic updates.

### Back-End
- **Python:**
  - Handle server-side logic using Flask framework.
  - Manage user sessions and process form submissions.
- **SQL:**
  - Store user data, transaction records, and generate queries for reports.

### Data Visualization
- **Streamlit:**
  - Create an interactive dashboard for visualizing financial data.

### personal_finance_tracker/
├── app.py
├── templates/
│ ├── index.html
│ ├── add_transaction.html
│ └── report.html
├── static/
│ ├── css/
│ │ └── styles.css
│ └── js/
│ └── scripts.js
├── models.py
├── forms.py
├── database.db
└── streamlit_app.py

## Step-by-Step Guide

### 1. Set Up Your Environment
Install the necessary libraries and frameworks:
```bash
pip install Flask SQLAlchemy Streamlit
