import os
import pandas as pd
from flask import Flask, render_template
from sklearn.datasets import load_iris
import seaborn as sns

# Add this line right after the imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Initialize the Flask application
app = Flask(__name__)

# --- Data Analysis and Visualization Setup ---
# Set a specific style for plots for a consistent look
sns.set_theme(style="whitegrid")
plt.style.use('seaborn-v0_8-whitegrid')

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
iris_df['species'] = iris_df['species'].apply(lambda x: iris.target_names[x])

# --- Data Analysis Functions ---

def get_descriptive_stats():
    """Returns the descriptive statistics of the Iris dataset."""
    return iris_df.describe().to_html(classes='table-auto w-full text-left', justify='left')

def get_species_distribution():
    """Returns the distribution of species in the dataset."""
    return iris_df['species'].value_counts().to_frame().to_html(classes='table-auto w-full text-left', justify='left')

def create_visualizations():
    """Creates and saves all the visualizations."""
    static_dir = 'static'
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # Common plot settings
    plot_bg_color = '#FFFFFF'
    plot_text_color = '#333333'

    # Histograms for each feature
    hist_fig = iris_df.hist(edgecolor='black', linewidth=1.2, figsize=(12, 8), grid=False, color='#60a5fa')
    plt.suptitle('Distribution of Iris Features', fontsize=16, color=plot_text_color)
    plt.gcf().set_facecolor(plot_bg_color)
    plt.savefig(os.path.join(static_dir, 'histograms.png'), facecolor=plot_bg_color)
    plt.close()

    # Box plots for each feature by species
    plt.figure(figsize=(12, 8), facecolor=plot_bg_color)
    for i, feature in enumerate(iris.feature_names):
        plt.subplot(2, 2, i+1)
        sns.boxplot(x='species', y=feature, data=iris_df, palette='viridis')
        plt.title(f'{feature} by Species', color=plot_text_color)
        plt.xlabel('Species', color=plot_text_color)
        plt.ylabel(feature, color=plot_text_color)
    plt.suptitle('Feature Comparison Across Species', fontsize=16, color=plot_text_color)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(os.path.join(static_dir, 'boxplots.png'), facecolor=plot_bg_color)
    plt.close()

    # Pair plot
    pair_plot = sns.pairplot(iris_df, hue='species', palette='viridis', height=2.5)
    pair_plot.fig.suptitle('Relationships Between Iris Features', y=1.02, fontsize=16, color=plot_text_color)
    pair_plot.fig.set_facecolor(plot_bg_color)
    pair_plot.savefig(os.path.join(static_dir, 'pairplot.png'), facecolor=plot_bg_color)
    plt.close()

# --- Flask Routes ---

@app.route('/')
def index():
    """Renders the main page with data analysis."""
    create_visualizations()
    descriptive_stats = get_descriptive_stats()
    species_distribution = get_species_distribution()
    
    return render_template('index.html', 
                           descriptive_stats=descriptive_stats,
                           species_distribution=species_distribution)

if __name__ == '__main__':
    app.run(debug=True)
