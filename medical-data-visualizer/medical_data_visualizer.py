import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')
df['overweight'] = (df['weight'] / ((df['height'] / 100)**2) > 25).astype(int)

for key in ['cholesterol', 'gluc']:
  df[key] = (df[key] > 1).astype(int)

def draw_cat_plot():
  df_cat = pd.melt(df,
                   value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active',
                     'overweight'
                   ],
                   id_vars=['cardio'])
  df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
  df_cat.rename(columns={0: 'total'}, inplace=True)
  fig = sns.catplot(data=df_cat,
                    kind="bar",
                    col="cardio",
                    x="variable",
                    y="total",
                    hue="value")
  fig.figure.savefig('catplot.png')
  return fig.figure

def draw_heat_map():
  df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
               (df['height'] >= df['height'].quantile(0.025)) &
               (df['height'] <= df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(0.025)) &
               (df['weight'] <= df['weight'].quantile(0.975))]
  corr = df_heat.corr()
  mask = np.triu(np.ones_like(corr, dtype=bool))
  fig, ax = plt.subplots(figsize=(20, 20))
  sns.heatmap(corr, mask=mask, annot=True, fmt="0.1f")
  fig.savefig('heatmap.png')
  return fig
