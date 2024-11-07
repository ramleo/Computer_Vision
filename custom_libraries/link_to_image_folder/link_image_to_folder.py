def save_images(df=None, feature1=None, feature2=None, train=True, validation=False): #base_dir=None,
  """This function does the following,
      1. Extracts image from the links.
      2. Creates necessary folders.
      3. Save each image in their respective folder.
      4. Convert each image into a numpy array.

  Arguments:
    df: Dataset to be used. Default None.
    feature1: A feature from the dataset. Default None.
    feature2: Another feature from the dataset. Default None.
    base_dir: Base directory for saving the images. Default None.
    train: If the dataset is a train dataset. Default True.
           If False then dataset is treated as test dataset.

  Output:
    Train and Test folders within Images folder, and each folder containing
    folders of desired image name with respctive images within those folders.

  Returns:
    Dataframe containing relevant categories and their numeric labels.
  """
  # Import relevant libraries
  import requests
  from io import BytesIO
  from os import mkdir, getcwd, makedirs
  from os.path import join, isdir
  from PIL.Image import open
  from pandas import Series
  from numpy import asarray, uint8, array
  from cv2 import (resize, cvtColor, imwrite,
                   INTER_LINEAR, COLOR_BGR2RGB)


  # Saving current directory path in variable
  cwd = getcwd()

  # If train parameter is set to True
  if train:

    path = join(cwd,"Images/train/")
    makedirs(cwd+"/Images/train/")
    print("Saving train images begins...")
    print()

  # If train parameter is set to True
  elif validation:

    path = join(cwd,"Images/validation")
    makedirs(cwd+"/Images/validation/")
    print("Saving validation images begins...")
    print()

  # If train parameter is set to False
  else:

    path = join(cwd,"Images/test/")
    makedirs(cwd+"/Images/test/")
    print("Saving test images begins...")
    print()

  target = []
  count = 0


  # Reset indices or else it throws error while performing for loop
  df.reset_index(inplace=True)

  # Looping through the rows of the feature containing image links
  for i in range(len(df[feature1])):

    count += 1
    print("===================================================================")
    print(f"Data point number {count}:")
    print("===================================================================")


    # Reading image from the link
    response = requests.get(df[feature1][i])
    im = open(BytesIO(response.content))
    # Creating a copy, just in case required
    img = im.copy()
    # Converting image to an numpy array
    img_array = asarray(img, dtype=uint8)
    # Resizing the image which required by VGG16 model
    img_array = resize(img_array, (224,224), interpolation = INTER_LINEAR)
    # Converting the color channel from BGR to RGB
    img_array = cvtColor(img_array, COLOR_BGR2RGB)

    # Creating a path to save the extracted images
    new_path = join(path,df[feature2][i])

    # Extracting id so that each data point is identified uniquely
    id = df[feature1][i].lower().split("/")[-1]
    if ("jpg" in id) or ("jpeg" in id) or ("png" in id) or ("bmp" in id):
      new_id = id
    else:
      new_id = id + ".jpg"

    # If directory does not already exist
    if not isdir(new_path):

      # Create a directory
      mkdir(path+df[feature2][i])
      # Naming the image
      image = df[feature2][i] + "_" + id
      # creating a full path of saved image
      full_path = join(path,image)

      # Saving the image to the created path
      imwrite(new_path + "/" + df[feature2][i] + "_" + id, img_array);

      # Appending the category of image of a list
      target.append(df[feature2][i])

    # If directory already exist
    else:

      # Naming the image
      image = df[feature2][i] + "_" + id
      # creating a full path of saved image
      full_path = join(path,image)

      # Saving the image to the created path
      imwrite(new_path + "/" + df[feature2][i] + "_" + id, img_array);

      # Appending the category of image of a list
      target.append(df[feature2][i])

    print(full_path)
    print(image)
    print()
    print("                                 ***                                 ")

  # Coverting list into numpy array
  target_array = array(target)

  # Converting numpy array into pandas Series object
  target = Series(target_array, name="Main_Category")

  # Saving the target variable to folder
  target.to_csv(path+"target.csv", index=False)

  print()
  print("Saving images finished.")
  print()