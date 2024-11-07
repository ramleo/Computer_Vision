def plot_history(nrows=None, ncols=None, figsize=None, history=None, len_history=None, keys=None):
  """This function displays custom subplots.
  """
  
  # Import matplotlib library
  import matplotlib.pyplot as plt

  # Extracting axes information.
  fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)

  # Taking each axis in array of axes and setting them off,
  # This is done to remove any blank subplot.
  for ax in axs.flat:
    ax.set_axis_off()

  # Creating middle variable for reference.
  middle = len_history//2

  # Initiating count variable so as to extract keys information
  # from history variable.
  count=0

  # Alloting subplot to axes.
  for row in range(nrows):
    for col in range(ncols):

      # Alloting according to rows and columns.
      ax = axs[row,col]

      # Setting the axis on for plotting.
      ax.set_axis_on()

      # Extracting history information.
      ax.plot(history[keys[count]])
      ax.plot(history[keys[count+middle]])

      # Setting the title and labels.
      ax.set_title(f"Model {keys[count].upper()}")
      ax.set_xlabel("Epoch")
      ax.set_ylabel(f"{keys[count].upper()}")

      # Setting the legend.
      ax.legend([f"Train {keys[count].upper()}", f"Val {keys[count].upper()}"])

      # Increasing the count by 1.
      count+=1

      # To avoid index out of range error
      if count>(middle-1):
        break

  # Adding spaces between subplots.
  fig.tight_layout(pad=2)

  # Displaying subplots.
  plt.show();