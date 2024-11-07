
def rename_file(dir_path):
  """This function removes "&", " " from the file name and replaces it with "_".

  Args:
    dir_path: Path to the directory containing the files to be renamed.
  Returns:
    None
  Output:
    Replaces the "&" and " " characters in the file names with "_" inplace.
  """

  # Import libraries
  import os

  # loop through all files in the directory
  for filename in os.listdir(dir_path):

      # check if the file is a text file
      if filename.endswith((".jpg", ".png", ".bmp", ".jpeg", ".jpeg?q=70")):

          # construct the old file path
          old_file_path = os.path.join(dir_path, filename)

          # construct the new file name
          splitted = filename.split("_")
          name = splitted[0]
          # name_first = re.sub("[ & | ]", '_', name)
          name = name.replace(" & ", "_")
          name = name.replace(" and ", "_")
          name = name.replace(",", "_")
          name_first = name.replace(" ", "_")
          name_rest = "_".join(splitted[1:])
          name_complete = f"{name_first}_{name_rest}"

          # construct the new file path
          new_file_path = os.path.join(dir_path, name_complete)

          # use the rename() method to rename the file
          os.rename(old_file_path, new_file_path)