from kaggle.api.kaggle_api_extended import KaggleApi
import os
import shutil

# Helper function to move files from nested directories ex. test/test -> test/
def move_files_to_parent(source_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, source_dir)  # Move file to the parent directory
    # Remove empty subdirectories
    for root, dirs, files in os.walk(source_dir):
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

# Create directories if they don't exist
print("Creating necessary directories...")
os.makedirs('Formative_2_Supervised_Unsupervised', exist_ok=True)
os.makedirs('summative/train', exist_ok=True)
os.makedirs('summative/test', exist_ok=True)
print("Directories created successfully.")

# Initialize Kaggle API
print("Initializing Kaggle API...")
api = KaggleApi()
try:
    api.authenticate()
    print("Kaggle API authenticated successfully.")
except Exception as e:
    print(f"Error during Kaggle API authentication: {e}")
    exit(1)

# Download datasets
try:
    print("Downloading Streaming Service Dataset...")
    print("Dataset URL: https://www.kaggle.com/datasets/akashanandt/streaming-service-data")
    api.dataset_download_files('akashanandt/streaming-service-data', 
                               path='Formative_2_Supervised_Unsupervised', unzip=True)
    print("Streaming Service Dataset downloaded successfully.")
except Exception as e:
    print(f"Error downloading Streaming Service Dataset: {e}")

try:
    print("Downloading Vehicle Damage Dataset...")
    print("Dataset URL: https://www.kaggle.com/datasets/sudhanshu2198/ripik-hackfest")
    api.dataset_download_files('sudhanshu2198/ripik-hackfest', 
                               path='summative', unzip=True)
    print("Vehicle Damage Dataset downloaded successfully.")
    
    # Move files from nested directories to train/ and test/
    print("Organizing Vehicle Damage Dataset...")
    move_files_to_parent('summative/train')
    move_files_to_parent('summative/test')
    print("Vehicle Damage Dataset organized successfully.")
except Exception as e:
    print(f"Error downloading Vehicle Damage Dataset: {e}")

print("Download process complete!")