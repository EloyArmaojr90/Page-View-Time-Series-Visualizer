import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col="date", sep =",")

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig , ax = plt.subplots(1,1, figsize = (19,5))
    df.plot(ax=ax)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.strftime('%B')
    mes = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Draw bar plot
    sns.set_style("ticks")
    
    # , palette="rocket"
    g = sns.catplot( x="year", kind="bar", hue="Month", y = "value", data=df_bar, hue_order=mes, ci=None, legend=False, palette="hls")
    fig = g.fig
    ax = g.ax
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend(loc='upper left', title="Month")
    plt.ylim(0,140000)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    # Draw box plots (using Seaborn)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    df_box.sort_values(by=['year','date'], ascending=[False, True], inplace=True)
    
    df_box["Page Views"] = df_box["value"]
    df_box["Month"] = df_box["month"]
    df_box["Year"] = df_box["year"]
    
    fig = plt.figure(figsize =(15,8))
    plt.subplot(1,2,1, title = "Year-wise Box Plot (Trend)")
    sns.boxplot(data=df_box, x = "Year", y = "value")
    plt.ylabel("Page Views")
    plt.ylim(0,200000)
    plt.subplot(1,2,2, title = "Month-wise Box Plot (Seasonality)")
    sns.boxplot(data=df_box, x = "Month", y = "value")
    plt.ylabel("Page Views")
    plt.ylim(0,200000)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
