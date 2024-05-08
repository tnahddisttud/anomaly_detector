import numpy as np
from dataloader import load_data, get_relevant_df
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    def __init__(self, path='./resources/metrics_data.csv'):
        self.df_scaled = None
        self.df_pca = None
        self.data = load_data(path)
        self.scaler = StandardScaler()
        self.pca = PCA()
        self.ocsvm = OneClassSVM(kernel='poly', gamma=0.1, nu=0.1)
        self.iforest = IsolationForest(n_estimators=100, max_samples='auto', contamination=float(0.1), random_state=42)

    def preprocess_data(self):
        self.df_scaled = self.scaler.fit_transform(self.data)
        self.df_pca = self.pca.fit_transform(self.df_scaled)

    def train_models(self):
        self.ocsvm.fit(self.df_pca)
        self.iforest.fit(self.df_pca)

    def calculate_anomaly_scores(self):
        anomaly_scores_ocsvm = self.ocsvm.decision_function(self.df_pca)
        anomaly_scores_iforest = self.iforest.decision_function(self.df_pca)
        anomaly_scores_combined = 0.5 * anomaly_scores_iforest + 0.5 * anomaly_scores_ocsvm
        return anomaly_scores_combined

    def predict_anomaly(self, datapoint):
        datapoint_scaled = self.scaler.transform([datapoint])
        datapoint_pca = self.pca.transform(datapoint_scaled)
        anomaly_score = self.ocsvm.decision_function(datapoint_pca)[0]
        anomaly_score = np.abs(anomaly_score)
        return anomaly_score

    def evaluate_threshold(self, anomaly_scores):
        threshold = np.percentile(anomaly_scores, 95)
        return threshold

    def predict(self, row, threshold):
        datapoint = get_relevant_df(row).to_numpy().data
        anomaly_score = self.predict_anomaly(datapoint)
        if anomaly_score > threshold:
            return "Anomaly"
        else:
            return "Normal"
