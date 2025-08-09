from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Create directories if they don't exist
os.makedirs('data/formative', exist_ok=True)
os.makedirs('data/summative/train', exist_ok=True)
os.makedirs('data/summative/test', exist_ok=True)

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

os.makedirs('Formative_2_Supervised_Unsupervised', exist_ok=True)
os.makedirs('summative/train', exist_ok=True)
os.makedirs('summative/test', exist_ok=True)

# Download datasets
print("Downloading Streaming Service Dataset...")
api.dataset_download_files('akashanandt/streaming-service-data', 
                         path='summative', unzip=True)

print("Downloading Vehicle Damage Dataset...")
api.dataset_download_files('sudhanshu2198/ripik-hackfest', 
                         path='summative', unzip=True)

print("Download complete!")