import pandas as pan
import numpy as num

from sklearn.model_selection import train_test_split
data = pan.read_excel("Lab_Session_Data.xlsx", sheet_name="marketing_campaign")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Q4.
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)

# Q5.
print(neigh.score(X_test, y_test))

# Q6.
print(neigh.predict(X_test))