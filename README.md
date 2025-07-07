# Cat vs Dog Image Classifier

A machine learning project that detects whether an input image is a cat or a dog using TensorFlow/Keras.

---

## Project Status

- (Done) Initial project setup completed
- (Done) Data download & cleaning scripts implemented
- (Done) Dataset split into train / val / test sets
- (Done) Data loader built using TensorFlow’s ImageDataGenerator
- (Next step) Current checkpoint: Ready for model training

---

## Repository Structure

cat-vs-dog-classifier/
├── data/
│ ├── raw/ # Raw dataset (PetImages/)
│ └── processed/ # Cleaned & split dataset
├── models/ # Trained model files (not included in repo)
├── notebooks/ # Jupyter notebooks (future experiments)
├── src/
│ ├── prepare_data.py # Clean & split data
│ ├── load_data.py # Build image generators
│ ├── train_model.py # (Coming next) Train the CNN
│ └── predict.py # (Future) Inference script
├── .gitignore
├── requirements.txt
└── README.md

---

## Setup & Usage

1. **Clone the repository**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/cat-vs-dog-classifier.git
   cd cat-vs-dog-classifier

2. **Create and activate a virtual environment** 
    python -m venv venv
    source venv/Scripts/activate  # Git Bash / PowerShell on Windows

3. **Install dependencies**
    pip install -r requirements.txt

4. **Download the Microsoft "Cats vs Dogs" dataset**
    Extract the dataset into data/raw/PetImages/
        Expected structure:
        data/raw/PetImages/Cat/...
        data/raw/PetImages/Dog/...

5. **Prepare the dataset**
    python src/prepare_data.py

6. **Load data generators**
    python src/load_data.py
    # Should report train/val/test image counts

## Next Steps (Coming Soon)
    Build and train the CNN (src/train_model.py)

    Evaluate model performance on the test set

    Plot accuracy & loss graphs

    Add an inference script (predict.py)

    Optional: Create a web/CLI interface

## Requirements
Package	/ Description
tensorflow	/ Model building & training
numpy, matplotlib / Data handling & plotting
Pillow	/ Image loading and validation
scikit-learn / (Future) Model evaluation tools

See requirements.txt for full details.

## License & Credits
    Data: Microsoft"Cats vs Dogs" dataset
    Model: Designed for personal learning use
    Feel free to fork, experiment, and improve

## Current Checkpoint:
    Repository is clean, organized, and ready for the next phase—training the CNN model. My next steps include: training the CNN, visualize results, then add inference and front-end UI.