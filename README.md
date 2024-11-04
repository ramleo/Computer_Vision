# computer_vision
Perfomed image classification

**PLEASE NOTE THAT ZIP FILE RELATED TO THIS PROJECT IS AVAILABLE IN MASTER BRANCH**

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
   - Step "5" is divided into 2 ipynb files and file no. 8 contains complete steps
   - FIRST CNN model
      - Initializing model
      - Checking model summary
      - Compiling the model
      - Fitting the model
      - Plotting history of the model
   - SECOND CNN model
      - Initializing model
      - Checking model summary
      - Compiling the model
      - Fitting the model
      - Plotting history of the model
6. Using Callbacks
   - THIRD CNN model
      - Initializing model
      - Checking model summary
      - Compiling the model
      - Model Callbacks
         - Early Stopping to observe if val_auc stopped improving for certain numbe of epochs, if yes then stop training
         - Learning Rate Scheduler to improve performance and reduce training time
         - Model Checkpoint to store best model
         - Reduce LR on plateau to reduce learning rate if there is no improvement in val_precision
      - Fitting the model
      - Plotting history of the model
7. Saved model from kaggle
   - Had to use kaggle notebook to perform CNN training as google colab GPU hours got exhausted
   - So downloaded the checkpoint folder from kaggle to local drive
8. Plot Model history using subplots
   - FOURTH CNN model
      - Initializing model
      - Checking model summary
      - Compiling the model
      - Model Callbacks
         - Early Stopping to observe if val_auc stopped improving for certain numbe of epochs, if yes then stop training
         - Learning Rate Scheduler to improve performance and reduce training time
         - Model Checkpoint to store best model
         - Reduce LR on plateau to reduce learning rate if there is no improvement in val_precision
      - Fitting the model
   - Plot history function
      - Creating a separate plot_history function for reusability
      - Calling plot_history function
9. Performed Data Augmentation
10. Used Transfer learning
11. Transfer learning and Fine-tuning
