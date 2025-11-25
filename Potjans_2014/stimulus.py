import numpy as np
from sim_params import sim_dict
import os

# Absolute path to the directory of this script
here = os.path.dirname(os.path.abspath(__file__))

data_dir = os.path.join(here, "data")
file_path = os.path.join(data_dir, "train_t12.2022.04.28_1.npy")

sentence_data = np.load(file_path)

col0 = sentence_data[:, 0]


bin_width_ms = 20.0
col0 = np.asarray(col0, dtype=float)

t_presim = float(sim_dict.get('t_presim', 0.0))

rate_times_ms = np.arange(col0.size, dtype=float) * bin_width_ms + t_presim
rate_values_hz = col0 * (1000.0 / bin_width_ms)

t_sim = col0.size * bin_width_ms

def getRateTimes():
    return rate_times_ms

def getRateValues():
    return rate_values_hz

def getTotalms():
    return t_sim + t_presim

def getStartms():
    return t_presim


def update_sim_dict():
    sim_dict.update({'t_sim': t_sim})