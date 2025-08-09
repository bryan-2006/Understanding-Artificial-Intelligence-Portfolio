# Understanding Artificial Intelligence Portfolio

A comprehensive portfolio showcasing my journey through artificial intelligence concepts, techniques, and applications.

## Projects

This portfolio contains two main projects:

### 1. Formative Project: Supervised & Unsupervised Learning

Exploration of fundamental machine learning techniques using WHO Life Expectancy dataset.

- Classification and regression models
- Clustering and dimensionality reduction
- Performance evaluation and model selection

[View Formative Project Details](Formative_2_Supervised_Unsupervised/README.md)

### 2. Summative Project: Advanced ML Applications

Two distinct machine learning applications:

- Customer Spending Analysis: Predicting customer churn and spending patterns
- Vehicle Damage Inspection: Computer vision model to classify vehicle damage

[View Summative Project Details](summative/README.md)

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional)

### Installation

```bash
# Build the Docker image
docker build -t ai-portfolio -f DockerFile .

# Run the container
docker run -p 8888:8888 ai-portfolio


# To automate downloading data and placing it into directories

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r [requirements.txt](http://_vscodecontentref_/4)

# Download datasets by running this in project root
python [download_data.py](http://_vscodecontentref_/5)
```

### Technologies

- Python
- Tensorflow & Scikit-learm
- Pandas & NumPy
- Matplotlib & Seaborn
- Jupyter Notebook
