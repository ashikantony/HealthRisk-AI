from setuptools import setup, find_packages

setup(
    name="healthrisk-ai",
    version="1.0.0",
    description="Healthcare Intelligence and Financial Risk Analytics Platform",
    author="HealthRisk AI Team",
    python_requires=">=3.11",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "xgboost",
        "lightgbm",
        "torch",
        "tensorflow",
        "streamlit",
        "plotly",
        "shap",
        "lime"
    ]
)