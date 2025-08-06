Iris Dataset Analysis Web App
This project is a fully functional web application that performs an in-depth exploratory data analysis (EDA) of the classic Iris flower dataset. Built with a Python and Flask backend, the application dynamically generates and displays key statistical insights and visualizations, making the data easily understandable.

About The Project
The goal of this project is to demonstrate a complete data science workflow, from initial data analysis to deploying a user-friendly web application. The app provides an interactive interface to explore the Iris dataset's features, distributions, and relationships. The front end is designed to be clean, modern, and responsive, featuring a light/dark theme switcher for user comfort.

Features
Descriptive Statistics: View a complete summary table of the dataset's numerical features (mean, std, min, max, etc.).

Species Distribution: See the count of each of the three Iris species.

Dynamic Visualizations:

Histograms: To understand the distribution of each feature.

Box Plots: To compare feature distributions across the different species.

Pair Plot: To visualize the relationships between all pairs of features, colored by species.

Responsive Design: The interface works seamlessly on desktop and mobile devices.

Theme Switcher: Toggle between a light and dark mode for comfortable viewing.

Tech Stack
Backend: Python, Flask

Data Analysis: Pandas, Scikit-learn

Data Visualization: Matplotlib, Seaborn

Frontend: HTML, Tailwind CSS, JavaScript

Deployment: Render, Gunicorn

Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites
Python 3.9+

pip

Installation
Clone the repository:

git clone https://github.com/shreyas277092004/iris-analysis-app.git
cd iris-analysis-app
Create and activate a virtual environment:

# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install the required packages:

pip install -r requirements.txt
Run the application:

python app.py
Open your browser and navigate to http://127.0.0.1:5000.
