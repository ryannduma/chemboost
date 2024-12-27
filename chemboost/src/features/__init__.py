"""
Feature engineering and processing utilities.
"""

from .feature_engineering import (
    valence_electron_count,
    calculate_atomic_concentrations,
    calculate_electronegativity_difference,
    create_feature_matrix
)

__all__ = [
    'valence_electron_count',
    'calculate_atomic_concentrations',
    'calculate_electronegativity_difference',
    'create_feature_matrix'
] 