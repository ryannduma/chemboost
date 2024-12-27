from setuptools import setup, find_packages

setup(
    name="chemboost",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "xgboost==2.1.3",
        "scikit-learn==1.5.2",
        "matminer>=0.9.0",
        "pymatgen>=2024.2.20",
        "smact>=2.8",
        "shap>=0.44.0",
    ],
) 