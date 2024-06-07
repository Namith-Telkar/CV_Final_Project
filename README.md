# Corneal Epithelium Image Clustering Codebase

This script performs various tasks related to image segmentation, including data preprocessing, model training, evaluation, and clustering of image features.

## Overview

- **Data Loading**: The script loads input images and corresponding masks from specified directories using OpenCV and NumPy.
- **Preprocessing**: Input images are resized, converted to grayscale, and normalized. Masks are label encoded using scikit-learn's LabelEncoder and one-hot encoded.
- **Data Splitting**: The dataset is split into training and testing sets, with a portion of the training set further split into training and validation sets.
- **Model Definition**: A UNet model is defined using Keras, with customization options such as pre-trained layers and input dimensions.
- **Model Compilation**: The model is compiled with the Adam optimizer and categorical cross-entropy loss function.
- **Model Training**: The model is trained on the training set with a specified batch size and number of epochs.
- **Model Evaluation**: The trained model is evaluated on the testing set, and accuracy metrics are computed.
- **Visualization**: Training and validation loss curves are plotted using Matplotlib. Additionally, sample test images along with their ground truth labels and model predictions are visualized.
- **Feature Extraction**: The script includes functionality to extract features from the last layer of the model.
- **Dimension Reduction and Clustering**: Features are processed using PCA (Principal Component Analysis) and clustered using KMeans algorithm.

## Usage

1. **Data Preparation**: Ensure that input images and corresponding masks are stored in separate directories (`data/images/` and `data/masks/`).
2. **Environment Setup**: Set up the Python environment with required libraries, such as TensorFlow, Keras, NumPy, OpenCV, and scikit-learn.
3. **Script Execution**: Run the script in a Python environment capable of executing Jupyter Notebooks.

## File Organization

- `multi_class_clustering.ipynb`: Jupyter Notebook containing the main script.
- `two_class_clustering.ipynb`: Jupyter Notebook containing the script for Normal and Abnormal image classifications.
- `unet_model.py`: Contains the definition of the UNet model.
- `/data`: Contains the input data and masks
- `/test_codes`: Contains the code for all the test models and scripts
- `README.md`: Documentation file providing an overview and usage instructions.

## Dependencies

- TensorFlow
- Keras
- NumPy
- OpenCV
- scikit-learn
- Matplotlib

---
