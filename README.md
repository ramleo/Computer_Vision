# computer_vision
Perfomed image classification.
The data was scraped from online shopping website, it was extracted from 3 different tags and hence there are 3 "csv" files to import.

Steps:

1. Importing Dataset
   - Import libraries
   - Check head of dataset
   - Check shape of dataset
   - Check data types and size of dataset
   - Check for null values
2. Preprocessing Dataset
   - Removed null values
   - Combined categories with similar names into a single catergory to reduce cardinality
   - Removed category "Not Available" as it is not helpful
   - Plotting target variable to check imbalance in the variable
   - Performed train and test splitting
3. Save image to folder
   - Step "3" is divided into 3 ipynb files and file no. 5 contains complete steps
   - Use image links to extract images and saving them as numpy arrays
   - Saving images in train folder
   - Saving images in test folder
   - Creating an "Image" folder and saving the train and test images and converting into a zip file
   - Renaming the folder name of each category by replacing spaces and "&" character with "_"
4. Prefetch data
   - Use data generators to import train and test datasets
   - Initially experimented the train test split with custom function (out of curiosity)
   - Rescaling the datasets
   - Prefetch the train and test datasets to make the training process more efficient
5. Build CNN models
6. Using Callbacks
7. Saved model from kaggle
8. Plot Model history using subplots
9. Performed Data Augmentation
10. Used Transfer learning
11. Transfer learning and Fine-tuning
