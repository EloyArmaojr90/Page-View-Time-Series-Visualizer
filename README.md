# <h1 align=center>**`MEDICAL DATA VISUALIZER`**</h1>


## **Introduction**

In this project, you will visualize time series data using a line chart, bar chart, and box charts. Pandas, Matplotlib and Seaborn were used to visualize a dataset containing the number of page views each day in the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. With these data visualizations it was possible to understand the patterns in the visits and identify the annual and monthly growth. This project was carried out by ELOY ARMAO, a student of the DATA SCIENCE career at the HENRY academy. More information about the academy in the following link https://www.soyhenry.com/carrera-data-science

You will also find a file called `time_series_visualizer.ipynb` where the questions of the work proposal will be resolved in a more dynamic way.

## **Tasks**

+ Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.

+ Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.

+ Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.

+ Create a draw_bar_plot function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of Months. On the chart, the label on the x axis should be Years and the label on the y axis should be Average Page Views.

+ Create a draw_box_plot function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be Year-wise Box Plot (Trend) and the title of the second chart should be Month-wise Box Plot (Seasonality). Make sure the month labels on bottom start at Jan and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

More information can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

## **Used libraries**

+ Pandas

+ Seaborn

+ Motplotlib