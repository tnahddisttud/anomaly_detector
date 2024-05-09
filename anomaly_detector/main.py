from detector import AnomalyDetector

if __name__ == "__main__":
  detector = AnomalyDetector()
  detector.preprocess_data()
  detector.train_models()
  anomaly_scores = detector.calculate_anomaly_scores()
  threshold = detector.evaluate_threshold(anomaly_scores)
  # Once model is trained, you can get the threshold value and make prediction
  # detector.predict(row, threshold)
