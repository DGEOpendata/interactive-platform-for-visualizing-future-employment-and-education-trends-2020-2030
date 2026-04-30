python
import pandas as pd
import plotly.express as px
from flask import Flask, render_template

# Load the dataset
data = pd.read_csv('Future_Qualifications_Specializations_2020_2030.csv')

# Initialize the Flask app
app = Flask(__name__)

# Route for the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Route for generating a line chart for a specific industry
@app.route('/visualize/<industry>')
def visualize(industry):
    industry_data = data[data['Industry'] == industry]
    fig = px.line(industry_data, x='Year', y='Demand', color='Specialization', title=f'Demand Trends in {industry}')
    graph_html = fig.to_html(full_html=False)
    return render_template('visualization.html', graph=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
