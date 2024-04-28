import pandas as pd
from  matplotlib import pyplot as plt
from scipy import signal
import numpy as np


# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = pd.ExcelFile('artefacts.xlsx')
data_alpha = excel_file.parse(excel_file.sheet_names[0])
#data_alpha = data_alpha[:4000]

fps = 250
highcut = 1
lowcut = 40

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y
def butter_highpass(cutoff, fs, order=3):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a
def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y


data_alpha_list =  (list(data_alpha["Value"]))

data_alpha_high = butter_highpass_filter(data_alpha_list, highcut, fps)
alpha_low_high = butter_lowpass_filter(data_alpha_high, lowcut, fps)

plt.plot(alpha_low_high)
plt.show()

