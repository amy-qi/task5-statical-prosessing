import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load  dataset
data = pd.read_csv('fastfood_calories.csv')  

# Check distribusi data menggunakan skewness and kurtosis
skewness = skew(data['calories'])
kurt = kurtosis(data['calories'])

print(f'Skewness: {skewness}')
print(f'Kurtosis: {kurt}')

# buat density plot (KDE)  data
plt.figure(figsize=(10, 6))
sns.kdeplot(data['calories'], fill=True)
plt.title('Density Plot of Calories Data')
plt.xlabel('Calories')
plt.ylabel('Density')
plt.show()

# Interpetasikan ndata dalam grafik berdasarkan skewness dan kurtosis
if skewness > 0:
    skewness_interpretation = "positively skewed (right-skewed)"
elif skewness < 0:
    skewness_interpretation = "negatively skewed (left-skewed)"
else:
    skewness_interpretation = "approximately symmetric"

if kurt > 3:
    kurtosis_interpretation = "leptokurtic (heavy-tailed)"
elif kurt < 3:
    kurtosis_interpretation = "platykurtic (light-tailed)"
else:
    kurtosis_interpretation = "mesokurtic (normal distribution-like)"

print(f'Skewness Interpretation: The data is {skewness_interpretation}')
print(f'Kurtosis Interpretation: The data is {kurtosis_interpretation}')
