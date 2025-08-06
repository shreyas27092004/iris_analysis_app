

# Iris Dataset Analysis Web App

A fully functional **web application** that performs in-depth **Exploratory Data Analysis (EDA)** on the classic **Iris flower dataset**.
Built with **Python** and **Flask**, the app dynamically generates statistical insights and visualizations to make the data easily understandable.

---

## **About the Project**

The goal of this project is to demonstrate a **complete data science workflow** — from initial dataset exploration to deploying a user-friendly web application.

The app provides an **interactive interface** for exploring the Iris dataset’s:

* Features
* Distributions
* Relationships

The **frontend** is clean, modern, and responsive, featuring a **light/dark theme switcher** for better user experience.

---

## **Features**

* **Descriptive Statistics**
  Summary table with mean, standard deviation, min, max, etc.

* **Species Distribution**
  Count of each Iris species.

* **Dynamic Visualizations**

  * **Histograms**: Feature distribution.
  * **Box Plots**: Compare feature values across species.
  * **Pair Plot**: Relationships between all features, colored by species.

* **Responsive Design**
  Works seamlessly on desktop and mobile devices.

* **Theme Switcher**
  Light/dark mode toggle.

---

## **Tech Stack**

**Backend:** Python, Flask
**Data Analysis:** Pandas, Scikit-learn
**Data Visualization:** Matplotlib, Seaborn
**Frontend:** HTML, Tailwind CSS, JavaScript
**Deployment:** Render, Gunicorn

---

## **Getting Started**

### **Prerequisites**

* Python **3.9+**
* `pip` (Python package manager)

---

### **Installation**

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/shreyas277092004/iris-analysis-app.git
cd iris-analysis-app
```

2️⃣ **Create & Activate Virtual Environment**

**For Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**For macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Application**

```bash
python app.py
```

5️⃣ **Open in Browser**
Visit:

```
http://127.0.0.1:5000
```
