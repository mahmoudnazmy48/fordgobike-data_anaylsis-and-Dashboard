# Ford GoBike Streamlit Dashboard

## 1. Put the app in your project

Copy `streamlit_app.py` and the updated `requirements.txt` into the project root,
beside `config.py` and `run_pipeline.py`.

The app looks for data in this order:

1. `output/fordgobike_cleaned.csv`
2. `data/fordgobike_cleaned.csv`
3. `data/fordgobike-tripdataFor201902.csv`

You can also upload a CSV from the dashboard sidebar.

## 2. Prepare the data locally

From the project root, activate your virtual environment and run:

```bash
python run_pipeline.py
```

Make sure the pipeline successfully creates:

```text
output/fordgobike_cleaned.csv
```

## 3. Install and run Streamlit locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Streamlit will print a local address, usually `http://localhost:8501`.

## 4. Publish on Streamlit Community Cloud

1. Push the project to a GitHub repository.
2. Make sure the repository contains `streamlit_app.py`, `requirements.txt`,
   and the dataset file in one of the paths listed above.
3. Open Streamlit Community Cloud and sign in with GitHub.
4. Choose **Create app**, select the repository and branch.
5. Set the main file path to `streamlit_app.py`.
6. Deploy.

Important: Streamlit Cloud cannot read files from your personal Windows
`C:\Users\...` folders. The dataset must be included in the GitHub repository
(if its size and licensing allow), or loaded from a suitable hosted storage
location, or uploaded by the app user. Do not commit private credentials.

## Dashboard contents

- KPI cards: trip count, average trip duration, average member age, station count
- User type and gender distributions
- Member age and trip duration distributions
- Trip duration and age comparisons by user type
- Top start stations
- Selectable numeric correlation heatmap
- Sidebar filters and filtered CSV download

## Data limitation

The project README describes `start_time` and `end_time` as `MM:SS.f` values,
not full calendar timestamps. The dashboard therefore does not infer weekday,
month, or calendar-date patterns from those fields.
