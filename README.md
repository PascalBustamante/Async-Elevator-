# Async Elevator

# Set-up
Requieres iapws and matplotlib packages, both available in PyPi. If you havn't already you should be using a virual enviroment to manage python packeges in a per project basis, [this link](https://docs.python.org/3/library/venv.html) is a great guide in doing so. 
> **_NOTE:_**  Setting-up a virtual enviroment is recommended, but not required. Also dont forget to activate your virtual enviroment:
> ```python
> C:\> <venv>\Scripts\activate
> ```
After you have set up your virtual enviroment you'll need to do the pip installs:
```python
C:\> pip3 install iapws
C:\> pip3 install matplotlib
```
Be sure to place this code inside the folder with the data that you want to process.

# Possible issues
  There is a bug when when inputing a path to a directory with .csv files other then the data we want. There are ways around this but without knowing more about naming conventions and how people store their data I decided to keep it as encompasing as possible. The solution is to have a seprate directory for these data files. 
  
  
## Runnig the code
When you run the code it'll ask you to input the path to the folder where the data is located, if no input is provided it will default to a relative path (meaning inside the same folder the code is in). 
  
##Functions 
  ### get_path()
  Returns a list of all paths to the data. It requests the user to input a path to the directory containing the data, if no input is given it will default to the current one and fetch all relative paths of all .csv files starting with 'OperationData_201'. This can lead to bugs if there are other .csv files in the directory.
  ### get_quarters(files)
  Has parameter files which should be a list of paths directing to the .csv files. Returns a list of yearly quarters (combines 3 files to make a quarter). It filters the rows and only adds those who's temperature is over 1000F and power is over 30MW.
  ### bar_chart_data(quarters)
  Takes the parameter quarters which should be a list of lists seperating the data into yearly quarters. The quarters are parsed by temperature, by segments of 50F each. Returns the y-axis of for the bar charts, in this case a set of 3 bars for each quarter. These bars are normalized to be per hour and values below 5 hours are deleted. At the end there is a check to see if there are any null bars and deleted. 
  
  ### bar_chart(bar_chart_data)
  Takes the parameter bar_chart_data which should be a list of bars containing the amount of time in hours that a the equipment has been online for at a temperature range. The position of the values in the bars corresponds to a specific quarter. Here the perameters for the graph are set and returns a container from matplotlib.
  
  ### calc_steam(quarters)
  Takes the parameter quarters and parses it for rows fitting the given constraints. Then it uses IAPWS97 to calculate the enthalpy for a given row. Returns an enthalpy array containg (time, enthalpy, color). The color is calculated based of the temperature of each row. 
  
  ### sca_graph(enthalpy_ar)
  takes the output of the last function and genrates a scater plot with colour based on the temperature of the given row. 
  
  # References
  https://matplotlib.org/stable/index.html
  https://docs.python.org/3/library/venv.html
  https://iapws.readthedocs.io/en/latest/modules.html#documentation
  
  
