import matplotlib.pyplot as plt
import seaborn as sns
import shap
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(y_true, y_pred):
    """Plot confusion matrix for model predictions.
    
    Args:
        y_true: Array of true labels
        y_pred: Array of predicted labels
        
    Returns:
        matplotlib.pyplot: Plot object containing the confusion matrix visualization
    """
    # Create figure with specified size
    plt.figure(figsize=(6, 5))
    
    # Calculate confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Create heatmap visualization
    sns.heatmap(
        cm, annot=True, fmt='d', cmap='Blues',
        xticklabels=['Non-metal', 'Metal'],
        yticklabels=['Non-metal', 'Metal']
    )
    
    # Add title and axis labels
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    
    return plt


def plot_shap_analysis(best_model, X_test, X):
    """Generate SHAP analysis plots for model interpretability.
    
    Creates three SHAP plots:
    1. Bar plot of feature importance
    2. Summary plot showing feature impact distribution
    3. Dependence plot for VEC (Valence Electron Count) feature
    
    Args:
        best_model: Trained XGBoost model
        X_test: Test features used for SHAP analysis
        X: Full feature dataset used for column names
        
    Returns:
        numpy.ndarray: SHAP values for the test set
    """
    # Initialize SHAP explainer
    explainer = shap.TreeExplainer(best_model)
    shap_values = explainer.shap_values(X_test)

    # Create bar plot of feature importance
    shap.summary_plot(shap_values, X_test, feature_names=X.columns, plot_type='bar')
    
    # Create summary plot showing feature impact distribution
    shap.summary_plot(shap_values, X_test, feature_names=X.columns)
    
    # Create dependence plot for VEC feature
    shap.dependence_plot('VEC', shap_values, X_test, feature_names=X.columns)
    
    return shap_values


def plot_feature_histograms(importance_df, X_test, y_test):
    """Plot histograms of top 20 most important features for metals and non-metals.
    
    Creates a 5x4 grid of histograms showing the distribution of feature values
    for both metal and non-metal classes.
    
    Args:
        importance_df: DataFrame containing feature importance information
        X_test: Test features for plotting distributions
        y_test: Test labels for separating metal/non-metal classes
    """
    # Extract top 20 features by importance
    top_20_features = importance_df['Feature'].head(20).tolist()

    # Set up subplot grid
    fig, axes = plt.subplots(5, 4, figsize=(20, 25))
    fig.suptitle('Histograms of Top 20 Features for Metals and Non-metals', fontsize=16)

    # Flatten 2D axes array to 1D for easier iteration
    axes = axes.flatten()

    # Create histogram for each feature
    for i, feature in enumerate(top_20_features):
        # Plot distribution for non-metals (class 0)
        axes[i].hist(X_test[y_test == 0][feature], bins=30, alpha=0.5, 
                    label='Non-metal', color='blue')
        # Plot distribution for metals (class 1)
        axes[i].hist(X_test[y_test == 1][feature], bins=30, alpha=0.5, 
                    label='Metal', color='red')
        
        # Add labels and legend
        axes[i].set_title(feature)
        axes[i].legend()
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Frequency')

    # Adjust subplot spacing and display
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()