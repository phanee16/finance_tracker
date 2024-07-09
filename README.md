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
* **app.py:** The main Flask application file that defines routes and application logic.
* **templates/**: Contains HTML templates used for rendering the user interface.
    * **index.html:** The main page of the application.
    * **add_transaction.html:** The template for adding new transactions.
    * **report.html:** The template for displaying financial reports.
* **static/**: Stores static assets like CSS and JavaScript files.
    * **css/**: Contains custom CSS styles for the application.
        * **styles.css:** The main CSS file.
    * **js/**: Holds JavaScript code for interactivity.
        * **scripts.js:** The main JavaScript file.
* **models.py:** Defines the data models for transactions and other relevant data.
* **forms.py:** Defines forms used for user input and validation.
* **database.db:** The SQLite database file used to store your financial data (can be renamed for other databases).
* **streamlit_app.py** (Optional): Contains an alternative implementation using Streamlit for a more interactive experience.


## Features

- **Add Transactions:** Users can add new transactions including amount, category, and date.
- **View Reports:** Detailed reports of transactions including total expenses, income, and spending patterns.
- **Interactive Dashboard:** Utilize Streamlit to create an interactive dashboard for visualizing financial data.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Pip package manager installed.

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/phanee16/finance_tracker.git
   cd personal_finance_tracker

2. **Install Required Libraries:**
   ```bash
   pip install Flask SQLAlchemy Streamlit

3. **Initialize the database & Run the Flask application:::**

    ```bash
    python app.py

4. **Run the Streamlit dashboard:**
    ```bash
    streamlit run streamlit_app.py

