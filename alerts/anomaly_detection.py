import numpy as np

def detect_anomalies(series, threshold=2.0):
    mean = np.mean(series)
    std = np.std(series)
    z_scores = (series - mean) / std
    return np.abs(z_scores) > threshold
