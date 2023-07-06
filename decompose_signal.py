import numpy as np

def get_trend(signal: np.ndarray, window=7) -> np.ndarray:
    return np.array([np.mean(signal[i:i+window]) for i in range(0, len(signal)-window)].append(signal[len(signal)-window:]))

def get_seasonal(signal: np.ndarray, window=30) -> np.ndarray:
    pass

def get_residuals(signal: np.ndarray) -> np.ndarray:
    pass

def print_naive_analysis(signal: np.ndarray, name: str) -> None:
    pass

if __name__ == '__main__':
    i=0
    X = np.array([i := i+np.random.random() for _ in range(100)])
    print(X)
    X_trend = get_trend(X)
    print(X_trend)