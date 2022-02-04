# Github_csv_Scraper
This python is for scraping csv file from Github.

How to use it?

1. Assign the address of the page that stores all the csv to my_url.

2. Assign the path you want to store all the CSV files to target_path.

3. Assign the link of raw data that does not include the file name(XXX.csv) to content.

4. Run the code and you'll find the files are in your target directory

Let's take a look at an example:

Assume that you want to download all the csv files from https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks/data.

You simply assign this address to my_url, and then assign the path of your target directory to target_path.

After that, open whatever file in the webpage and click "raw" (to see the raw file).

You'll see that the address becomes different
(https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/BicycleWeather.csv).

Copy the address of that page and exclude the file name (i.e. https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/) and assign it to content.
