import os
import requests
import zipfile
from pathlib import Path

def save_data():
    # Setup path to the data folder
    data_path = Path("../data/")
    image_path = data_path / "pizza_steak_sushi"

    # if the image folder doesn't exist already, download and prepare it
    if image_path.is_dir():
        print(f"{image_path} directory exists")
    else:
        print(f"Did not find {image_path} directory, creating one...")
        image_path.mkdir(parents=True, exist_ok=True)

    # download the pizza, steak, sushi data
    with open(data_path / "pizza_steak_sushi.zip", "wb") as f:
        request = requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip")
        print("Downloading pizza, steak, sushi data...")
        f.write(request.content)

    # Unizip the zip file
    with zipfile.ZipFile(data_path / "pizza_steak_sushi.zip", "r") as zip_ref:
        print("Unzipping pizza, steak, sushi data...") 
        zip_ref.extractall(image_path)

    # Remove the zip file
    os.remove(data_path / "pizza_steak_sushi.zip")