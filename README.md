# Anomaly Detector

This anomaly detector uses a combination of OneClassSVM and IsolationForest to detect anomalies in the resource metrics data.

### Project Structure
This project uses [poetry](https://python-poetry.org/) for dependency management. The project structure looks like this:
```text
.
├── anomaly_detector/
│   ├── resources/
│   │   └── metrics_data.csv   # Dataframe mapped with resource ID: 5.948095306408936e+17
│   ├── streaming/   # Example files to showcase realworld scenario
│   │   ├── producer.py
│   │   └── consumer.py
│   ├── dataloader.py   # utility to load abd preprocess metrics data
│   ├── detector.py   # File containing the AnomalyDetector class
│   └── main.py   # Main file with executable example
├── .gitignore
├── Observability_Anomaly_Detection.ipynb   # Notebook with thorough analysis and anomaly detection
├── README.md
└── pyproject.toml
```

### Set-up
Since we are using poetry for dependency management (ensure you have it installed), we can get started by running the following two commands:
1. To create a virtual environment
```commandline
poetry shell
```
2. Install dependencies

```commandline
poetry install
```
## Note
This python package contains an example implementation of what a real world production scenario would look like. The detailed modelling for anomaly detection is presented in the Jupyter Notebook
