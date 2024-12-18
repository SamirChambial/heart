# -*- coding: utf-8 -*-
"""Covid-19 Cases Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eKdWmCp5T8fsLSgbX4IsG2zveTk559BU
"""

!pip install fbprophet

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from fbprophet import Prophet
from sklearn.metrics import r2_score

plt.style.use("ggplot")

df0 = pd.read_csv("CONVENIENT_global_confirmed_cases.csv")
df1 = pd.read_csv("CONVENIENT_global_deaths.csv")