# ChemBoost: SMACT-Based Intermetallics Classification using XGBoost

This project uses SMACT and XGBoost to classify intermetallic compounds as metals or non-metals based on their composition and properties. Its an attempt to develop a filter capable of dealing with covalent chemical environments that could in the future be essential in the enhancement of the SMACT filter.

## Features

- Loads and processes materials data from Matbench
- Calculates various compositional features including:
  - Valence Electron Count (VEC)
  - Electronegativity differences
  - Atomic concentrations
- Trains XGBoost classifier with hyperparameter optimization
- Provides visualization tools for model interpretation

## Setup

1. Create a conda environment:

```bash
conda create -n chemboost python=3.11
conda activate chemboost
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Project Structure

- `data/`: Contains the dataset files
- `notebooks/`: Jupyter notebooks for exploration and analysis
- `src/`: Source code
  - `data/`: Data loading utilities
  - `features/`: Feature engineering code
  - `models/`: Model training and evaluation
  - `visualization/`: Plotting utilities

## Usage

See `notebooks/XGB_Final_Classification.ipynb` for the main analysis pipeline.

## Dependencies

The main dependencies are:

- numpy >= 2.0.0
- pandas >= 2.0.0
- xgboost == 2.1.3
- scikit-learn == 1.5.2 **
- matminer >= 0.9.0
- pymatgen >= 2024.2.20
- smact >= 2.8
- shap >= 0.44.0

See `requirements.txt` for a complete list.

## Development

To contribute to the project:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## Troubleshooting

Common issues:

1. Import errors:
   - Ensure you're running from the project root directory
   - Verify the package is installed in development mode
   - Check that your conda environment is activated

2. Data loading errors:
   - Verify that `magpiery.csv` is present in the `data/` directory

3. Package Installation Errors
    - ** Scikit-learn version 1.6 modified the API around its "tags", and that's the cause of this error. XGBoost has made the necessary changes in PR11021, but at present that hasn't made it into a released version. You can either keep your sklearn version <1.6, or build XGBoost directly from github (or upgrade XGBoost, after a new version is released)

## License

MIT
