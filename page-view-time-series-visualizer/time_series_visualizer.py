import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates=['date'],
                 index_col='date')
df = df[(df['value'] > df['value'].quantile(0.025))
        & (df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
  df_plot = df.copy()
  fig, ax = plt.subplots(figsize=(30, 10))
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")
  sns.lineplot(data=df_plot, palette=['r'])
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month_name()
  df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()
  fig, ax = plt.subplots(figsize=(20, 20))
  months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  sns.barplot(data=df_bar, x="year", y="value", hue="month", hue_order=months)
  ax.set_xlabel("Years")
  ax.set_ylabel("Average Page Views")
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]
  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(30, 10))
  sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  sns.boxplot(data=df_box, x="month", y="value", order=months, ax=axes[1])
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")
  fig.savefig('box_plot.png')
  return fig