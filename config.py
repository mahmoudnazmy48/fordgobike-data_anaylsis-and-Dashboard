from pathlib import Path

# Project directory

BASE_DIR = Path(__file__).resolve().parent

# Dataset path

DATA_FILE = BASE_DIR / "data" / "fordgobike-tripdataFor201902.csv"

# Output directory

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "fordgobike_cleaned.csv"

# Dataset settings

DATA_YEAR = 2019
RANDOM_STATE = 42

# Datetime columns

DATETIME_COLUMNS = ["start_time", "end_time"]

# Integer columns

INTEGER_COLUMNS = ["member_birth_year"]

# Categorical columns

CATEGORICAL_COLUMNS = [
"start_station_id",
"start_station_name",
"end_station_id",
"end_station_name",
"user_type",
"bike_id",
"member_gender",
"bike_share_for_all_trip",
]

# Main analysis columns

SPECIFIC_NUMERIC_COLUMNS = [
"member_age",
"trip_duration_min",
"start_station_latitude",
"start_station_longitude",
"end_station_latitude",
"end_station_longitude",
]

CORRELATION_COLUMNS = [
"duration_sec",
"member_birth_year",
"member_age",
"bike_id",
]
