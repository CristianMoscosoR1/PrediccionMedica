from sklearn.preprocessing import StandardScaler

def scale_features(data):
    """Escala las características numéricas usando StandardScaler."""
    scaler = StandardScaler()
    return scaler.fit_transform(data)