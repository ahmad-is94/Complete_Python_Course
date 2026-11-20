from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. Load a built-in dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Define the model and the grid of hyperparameters to test
model = RandomForestClassifier(random_state=42)
param_grid = {
    "n_estimators": [10, 50, 100],
    "max_depth": [2, 4, None],
    "min_samples_split": [2, 5]
}

# 3. Run Grid Search with 5-fold cross-validation
grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring="accuracy")
grid.fit(X_train, y_train)

# 4. Print the best combination and test accuracy
print(f"Best CV Accuracy: {grid.best_score_:.4f}")
print(f"Best Parameters:  {grid.best_params_}")
print(f"Test Accuracy:    {grid.score(X_test, y_test):.4f}")