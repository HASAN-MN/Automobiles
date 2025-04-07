import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from ml.preprocess import load_data, preprocess_data

class AutomobileML:
    def __init__(self):
        self.models = {
            "Linear Regression": LinearRegression(),
            "Ridge Regression": Ridge(alpha=1.0),
            "SVM Regression": SVR(kernel='rbf', C=1.0, epsilon=0.1)
        }
        self.results = {}

    def train_and_evaluate(self):
        data = load_data()
        X, y = preprocess_data(data)

        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train each model
        for name, model in self.models.items():
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)

            mse = mean_squared_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)
            self.results[name] = {
                "mse": mse,
                "r2": r2,
                "predictions": predictions
            }

            print(f"{name} - MSE: {mse:.2f}, R²: {r2:.2f}")
            self.plot_predictions(y_test, predictions, name)

        self.correlation_analysis(data)

    def plot_predictions(self, y_test, predictions, model_name):
        
        plt.figure(figsize=(8, 4))
        plt.scatter(y_test, predictions, alpha=0.7, label="Predictions")
        plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle="--", label="Ideal")
        plt.xlabel("Actual Prices")
        plt.ylabel("Predicted Prices")
        plt.title(f"{model_name} - Predictions vs Actual Prices")
        plt.legend()
        plt.tight_layout()
        plt.show()

    def correlation_analysis(self, data):
       
        correlation_matrix = data[["listing_price", "listing_mileage"]].corr()
        print("\nCorrelation Analysis:")
        print(correlation_matrix)

        #correlation graph
        plt.figure(figsize=(6, 4))
        plt.scatter(data["listing_mileage"], data["listing_price"], alpha=0.6, color="blue")
        plt.xlabel("Mileage")
        plt.ylabel("Price")
        plt.title("Correlation: Price vs Mileage")
        plt.tight_layout()
        plt.show()
