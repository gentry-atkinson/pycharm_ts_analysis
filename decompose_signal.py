import numpy as np
from matplotlib import pyplot as plt


def get_trend(signal: np.ndarray, window=7) -> np.ndarray:
    sig_len = signal.shape[-1]
    trend = np.array([np.mean(signal[i:i+window]) for i in range(0, sig_len-window)])
    for i in range(window, 0, -1):
        trend = np.append(trend, np.mean(signal[sig_len-i:]))
    return trend


def get_seasonal(signal: np.ndarray, window=30) -> np.ndarray:
    sig_len = signal.shape[-1]
    season = signal.copy()
    for anchor in range(0, sig_len-window, window):
        anchor_val = signal[anchor]
        for day in range(0, window):
            season[anchor+day] = season[anchor+day] - anchor_val
    else:
        anchor += window
        last_anchor_val = signal[anchor]
        while anchor < sig_len:
            season[anchor] -= last_anchor_val
            anchor += 1

    return season


def get_residuals(observed: np.ndarray, trend: np.ndarray, seasonal : np.ndarray) -> np.ndarray:
    return observed - trend - seasonal


def print_naive_analysis(signal: np.ndarray, name: str) -> None:
    sig_len = signal.shape[-1]
    sig_t = get_trend(signal)
    sig_s = get_seasonal(signal)
    sig_r = get_residuals(signal, sig_t, sig_s)

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)

    ax1.set_title("Observed")
    ax1.plot(range(sig_len), signal)

    ax2.set_title("Trend")
    ax2.plot(range(sig_len), sig_t)

    ax3.set_title("Seasonal")
    ax3.plot(range(sig_len), sig_s)

    ax4.set_title("Residual")
    ax4.plot(range(sig_len), sig_r)

    fig.tight_layout()
    plt.savefig(name + "_naive_analysis.png")


if __name__ == '__main__':
    i = 0
    X = np.array([i := (i+np.random.random()-0.3) for _ in range(100)])
    print(X.shape)
    X_trend = get_trend(X)
    print(X_trend.shape)
    X_season = get_seasonal(X)
    print(X_season.shape)
    X_residual = get_residuals(X, X_trend, X_season)
    print(X_residual.shape)

    print_naive_analysis(X, "test")
