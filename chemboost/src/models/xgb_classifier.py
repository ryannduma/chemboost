from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np


def train_xgb_model(X, y, param_grid=None):
    """Train XGBoost model with GridSearchCV.
    
    Args:
        X: Feature matrix
        y: Target labels
        param_grid: Dictionary of parameters for GridSearchCV. If None, uses default parameters.
        
    Returns:
        tuple: (grid_search, X_train, X_test, y_train, y_test)
    """
    if param_grid is None:
        param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [4, 6, 8],
            'learning_rate': [0.01, 0.1],
            'subsample': [0.8, 1.0],
            'colsample_bytree': [0.8, 1.0]
        }
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    xgb_classifier = XGBClassifier(
        eval_metric='logloss',
        random_state=42,
        use_label_encoder=False
    )
    
    grid_search = GridSearchCV(
        estimator=xgb_classifier,
        param_grid=param_grid,
        scoring='accuracy',
        cv=5,
        n_jobs=-1
    )
    
    grid_search.fit(X_train, y_train)
    return grid_search, X_train, X_test, y_train, y_test