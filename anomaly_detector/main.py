from detector import AnomalyDetector


detector = AnomalyDetector()
detector.preprocess_data()
detector.train_models()
anomaly_scores = detector.calculate_anomaly_scores()
threshold = detector.evaluate_threshold(anomaly_scores)
