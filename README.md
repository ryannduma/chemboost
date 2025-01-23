# Intermetallics Module Documentation

## Overview

The intermetallics module provides utility functions for analyzing and classifying intermetallic compounds using SMACT (Semiconducting Materials from Analogy and Chemical Theory). The module includes tools for composition analysis, metal content evaluation, and intermetallic property scoring.

## Code Structure (`intermetallics.py`)

### Core Functions

1. **Composition Handling**

   - `_ensure_composition(composition)`: Internal utility to convert string formulas to pymatgen Composition objects
   - Handles both string and Composition inputs with proper error handling

2. **Element Analysis Functions**

   - `get_element_fraction(composition, element_set)`: Calculate fraction of elements from a given set
   - `get_metal_fraction(composition)`: Calculate fraction of metallic elements
   - `get_d_electron_fraction(composition)`: Calculate fraction of d-block elements
   - `get_distinct_metal_count(composition)`: Count unique metallic elements

3. **Chemical Property Analysis**

   - `get_pauling_test_mismatch(composition)`: Calculate electronegativity ordering deviation
   - Helps distinguish between ionic and metal-metal bonds

4. **Scoring System**
   - `intermetallic_score(composition)`: Calculate comprehensive intermetallic character (0-1)
   - Considers multiple factors:
     - Metal fraction (30% weight)
     - d-electron content (20% weight)
     - Number of metals (20% weight)
     - Valence electron count (15% weight)
     - Pauling electronegativity mismatch (15% weight)

## Workflow Example (Intermetallics Classification Notebook)

### Setup and Data Loading

```python
from matminer.datasets import load_dataset
import smact.intermetallics as im
```

### Feature Extraction Pipeline

1. Load composition data
2. Extract intermetallic features:
   - Metal fraction
   - d-electron fraction
   - Distinct metal count
   - Pauling mismatch
   - Intermetallic score

### Machine Learning Application

- Uses XGBoost classifier for metal vs. non-metal classification
- Features cross-validation and threshold tuning
- Includes hyperparameter optimization
- Provides performance evaluation metrics

### Key Components

1. Data preprocessing
2. Feature extraction using intermetallics module
3. Model training with cross-validation
4. Threshold optimization
5. Performance evaluation

## Usage Example

```python
from smact.intermetallics import intermetallic_score
from pymatgen.core import Composition

# Analyze a compound
composition = "Fe2Al"
score = intermetallic_score(composition)
metal_fraction = get_metal_fraction(composition)
```

## Dependencies

- pymatgen
- numpy
- smact
- (For classification notebook: scikit-learn, xgboost, pandas)
