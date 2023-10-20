from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Load the data
from sklearn.datasets import load_iris
data = load_iris()
X = data.data
y = data.target

# Create training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)

# Automatically select a model using TPOT
tpot = TPOTClassifier(generations=5,
                      population_size=20,
                      random_state=17,
                      verbosity=2)
tpot.fit(X_train, y_train)

tpot.export("best_model.py")

# Get the best model
best_model = tpot.fitted_pipeline_

# Make prediction on the test data
y_pred = best_model.predict(X_test)

# Calculate th model's accuracy
accuracy = accuracy_score(y_test, y_pred)

# Visualize the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()



