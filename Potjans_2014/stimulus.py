import numpy as np
from sim_params import sim_dict
import os

# Absolute path to the directory of this script
here = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(here, "data")
file_path = os.path.join(data_dir, "sentence_1_smoothed_rates.npy")

# --------------------------------------------------------------------
# Load stimulus data
# --------------------------------------------------------------------
rate_values_hz = np.load(file_path)

# Ensure data is 2D: (num_bins, num_channels)
if rate_values_hz.ndim != 1:
    raise Exception("RATE IS NOT A 1D LIST/ARRAY")

rate_values_hz = rate_values_hz.astype(float).tolist()

num_bins = len(rate_values_hz)

# --------------------------------------------------------------------
# Build time axis and convert to rates
# --------------------------------------------------------------------
bin_width_ms = 20.0  # ms per bin

t_presim = float(sim_dict.get('t_presim', 0.0))

# Time points for each bin (same for all channels)
rate_times_ms = np.arange(num_bins, dtype=float) * bin_width_ms + t_presim

# Total simulation time contributed by the stimulus (excluding t_presim)
t_sim = num_bins * bin_width_ms


# --------------------------------------------------------------------
# API
# --------------------------------------------------------------------
def getRateTimes():
    """
    Return the time points in ms for the bins.
    The time axis is the same for all channels, so `channel` is ignored.
    """
    return rate_times_ms


def getRateValues():
    """
    Return the rate values (Hz) for a given channel index.
    channel: int, 0-based index (0 <= channel < num_channels)
    """
    return rate_values_hz


def getTotalms():
    """Total simulation time in ms including presimulation period."""
    return t_sim + t_presim


def getStartms():
    """Start time in ms for the stimulus."""
    return t_presim


def update_sim_dict():
    """Update sim_dict with the total simulation time contributed by the stimulus."""
    sim_dict.update({'t_sim': t_sim})
