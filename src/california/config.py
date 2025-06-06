from pathlib import Path

PROJECT_FOLDER = Path(__file__).resolve().parents[2]

# important folders
DATA_FOLDER = PROJECT_FOLDER / "data"
GEO_FOLDER = DATA_FOLDER / "geo"
RAW_DATA_FOLDER = DATA_FOLDER / "raw"
INTERIM_DATA_FOLDER = DATA_FOLDER / "interim"
PROCESSED_DATA_FOLDER = DATA_FOLDER / "processed"
MODELS_FOLDER = PROJECT_FOLDER / "models"
REPORTS_FOLDER = PROJECT_FOLDER / "reports"
REPORTS_FIGURES_FOLDER = REPORTS_FOLDER / "figures"

# data files
RAW_DATA_FILE = RAW_DATA_FOLDER / "housing.csv.zip"
INTERIM_DATA_FILE = INTERIM_DATA_FOLDER / "interim_data.parquet"
PROCESSED_DATA_FILE = PROCESSED_DATA_FOLDER / "processed_data.parquet"

# geo files
GEO_CALIFORNIA_COUNTIES_FILE = GEO_FOLDER / "california_counties.geojson"
GEO_MEDIAN_DF_FILE = GEO_FOLDER / "gdf_counties.parquet"

# model files
BEST_MODEL_FILE = MODELS_FOLDER / "best_model.joblib"
