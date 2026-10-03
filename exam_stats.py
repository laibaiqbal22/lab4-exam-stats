import numpy as np
import pandas as pd
from scipy import stats

scores = pd.Series([72, 65, 88, np.nan, 54, 91, 76, np.nan, 83, 69])

# (a) descriptive statistics
print(scores.describe())

# (b) shape of the distribution (missing values dropped first)
clean = scores.dropna()
print("Skewness:", stats.skew(clean))
print("Kurtosis:", stats.kurtosis(clean))

# (c) missing values
print("Missing values:", scores.isnull().sum())

# (d) fill with the mean
filled = scores.fillna(scores.mean())
print("Filled scores:")
print(filled)
