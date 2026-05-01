import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
  df = pd.read_csv('epa-sea-level.csv')

  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
  line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x = np.arange(df['Year'].min(), 2051, 1)
  y = line.slope * x + line.intercept
  plt.plot(x, y)
  df_from2000 = df[df['Year'] >= 2000]
  line = linregress(df_from2000['Year'],
                    df_from2000['CSIRO Adjusted Sea Level'])
  x = np.arange(df_from2000['Year'].min(), 2051, 1)
  y = line.slope * x + line.intercept
  plt.plot(x, y)
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.savefig('sea_level_plot.png')
  return plt.gca()
