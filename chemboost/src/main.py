from data import load_matbench_data, load_element_data
from features import create_feature_matrix
from models import train_xgb_model
from visualisation import plot_confusion_matrix, plot_shap_analysis, plot_feature_histograms

def main():
    # Load data
    df = load_matbench_data()
    element_data = load_element_data("data/magpiery.csv")
    
    # Create features
    X = create_feature_matrix(df)
    y = df['is_metal']
    
    # Train model
    grid_search, X_train, X_test, y_train, y_test = train_xgb_model(X, y)
    
    # Make predictions
    y_pred = grid_search.predict(X_test)
    
    # Generate plots
    plot_confusion_matrix(y_test, y_pred)
    shap_values = plot_shap_analysis(grid_search.best_estimator_, X_test, X)
    
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best score: {grid_search.best_score_:.4f}")

if __name__ == "__main__":
    main() 