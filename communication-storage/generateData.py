import csv
import os
import random
from time import time

# Dossiers pour stocker les données générées
OUTPUT_FOLDER_NAME = "generated_datasets"
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, OUTPUT_FOLDER_NAME)
os.makedirs(output_dir, exist_ok=True)

def generate_dataset(filename, num_points):
    print(f"Generating dataset: {filename} with {num_points} points...")
    start_time = time()

    with open(os.path.join(output_dir, filename), mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["x", "y"])  # En-têtes des colonnes
        for _ in range(num_points):
            x = random.random()
            y = random.random()
            writer.writerow([x, y])

    elapsed_time = time() - start_time
    print(f"Dataset {filename} generated in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    datasets = [
        ("small_dataset.csv", 10_000),  
        ("medium_dataset.csv", 1_000_000),
        #("large_dataset.csv", 50_000_000),
        # I disable the last one by default because it's really large
    ]

    for filename, num_points in datasets:
        generate_dataset(filename, num_points)

    print(f"All datasets have been generated in the '{output_dir}' folder.")
