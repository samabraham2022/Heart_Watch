#Import all the libraries
from keras.models import load_model
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objs as go
import plotly.express as px
from scipy.signal import medfilt, butter, filtfilt
import pywt
from sklearn.model_selection import train_test_split
import scipy.signal
from keras.models import Sequential
from keras.layers import LSTM, Dense, Reshape
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import roc_auc_score
model = load_model('model.h5')
def featureselection(X_train):
    X_train=np.array(X_train)
    features = []
    # Extracting features for each sample
    for i in range(1):
        print(i)
        #Finding the R-peaks
        r_peaks = scipy.signal.find_peaks(X_train[i])[0]
        #Initialize lists to hold R-peak and T-peak amplitudes
        r_amplitudes = []
        t_amplitudes = []
        # Iterate through R-peak locations to find corresponding T-peak amplitudes
        for r_peak in r_peaks:
        # Find the index of the T-peak (minimum value) in the interval from R-peak to R-peak + 200 samples
            t_peak = np.argmin(X_train[i][r_peak:r_peak+200]) + r_peak
            #Append the R-peak amplitude and T-peak amplitude to the lists
            r_amplitudes.append(X_train[i][r_peak])
            t_amplitudes.append(X_train[i][t_peak])
        # extracting singular value metrics from the r_amplitudes
        std_r_amp = np.std(r_amplitudes)
        mean_r_amp = np.mean(r_amplitudes)
        median_r_amp = np.median(r_amplitudes)
        sum_r_amp = np.sum(r_amplitudes)
        # extracting singular value metrics from the t_amplitudes
        std_t_amp = np.std(t_amplitudes)
        mean_t_amp = np.mean(t_amplitudes)
        median_t_amp = np.median(t_amplitudes)
        sum_t_amp = np.sum(t_amplitudes)
        # Find the time between consecutive R-peaks
        rr_intervals = np.diff(r_peaks)
        # Calculate the time duration of the data collection
        time_duration = (len(X_train[i]) - 1) / 1000 # assuming data is in ms
        # Calculate the sampling rate
        sampling_rate = len(X_train[i]) / time_duration
        # Calculate heart rate
        duration = len(X_train[i]) / sampling_rate
        heart_rate = (len(r_peaks) / duration) * 60
        # QRS duration
        qrs_duration = []
        for j in range(len(r_peaks)):
            qrs_duration.append(r_peaks[j]-r_peaks[j-1])
        # extracting singular value metrics from the qrs_durations
        std_qrs = np.std(qrs_duration)
        mean_qrs = np.mean(qrs_duration)
        median_qrs = np.median(qrs_duration)
        sum_qrs = np.sum(qrs_duration)
        # Extracting the singular value metrics from the RR-interval
        std_rr = np.std(rr_intervals)
        mean_rr = np.mean(rr_intervals)
        median_rr = np.median(rr_intervals)
        sum_rr = np.sum(rr_intervals)
        # Extracting the overall standard deviation
        std = np.std(X_train[i])
        # Extracting the overall mean
        mean = np.mean(X_train[i])
        # Appending the features to the list
        features.append([mean, std, std_qrs, mean_qrs,median_qrs, sum_qrs, std_r_amp, mean_r_amp, median_r_amp, sum_r_amp, std_t_amp, mean_t_amp, median_t_amp, sum_t_amp, sum_rr, std_rr, mean_rr,median_rr, heart_rate])
    # Converting the list to a numpy array
    features = np.array(features)
    num_features = features.shape[1]
    # Reshape the features data to be in the right shape for LSTM input
    features = features.reshape(features.shape[0], features.shape[1], 1)
    return features
def format_data(ecg_data):
    ecg_data=pd.DataFrame(ecg_data)
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(-1, 1))
    ecg_data = scaler.fit_transform(ecg_data)
    from scipy.signal import medfilt, butter, filtfilt
    import pywt
    import numpy as np
    #filtering the raw signals
    # Median filtering
    ecg_medfilt = medfilt(ecg_data, kernel_size=3)
    # Low-pass filtering
    lowcut = 0.05
    highcut = 20.0
    nyquist = 0.5 * 360.0
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(4, [low, high], btype='band')
    #ecg_lowpass = filtfilt(b, a, ecg_data)
    # Wavelet filtering
    coeffs = pywt.wavedec(ecg_data, 'db4', level=1)
    threshold = np.std(coeffs[-1]) * np.sqrt(2*np.log(len(ecg_data)))
    coeffs[1:] = (pywt.threshold(i, value=threshold, mode='soft') for i in coeffs[1:])
    ecg_wavelet = pywt.waverec(coeffs, 'db4')
    return ecg_wavelet
def model_predict(l):
    test=format_data(l)
    test=featureselection(l)
    pred=model.predict(test)
    if pred>=0.5:
        return 0
    else:
        return 1
inp = [0.7125066,-1.1320792,-2.9739224,-4.3536077,-4.2092953,-3.3701396,-2.3888554,-1.6274182,-1.6139765,-1.0295064,-0.39771585,-0.3644773,-0.42755912,-0.38292042,-0.31544206,-0.25437758,-0.30843848,-0.33732134,-0.37498693,-0.40493767,-0.46383809,-0.4385745,-0.43548363,-0.46681684,-0.49702559,-0.51571999,-0.5579556,-0.68920402,-0.67743294,-0.71222411,-0.77849015,-0.79858769,-0.92473316,-0.89981472,-0.93373255,-0.91727094,-0.88661404,-0.89649851,-0.83942334,-0.86097536,-0.78527906,-0.77904402,-0.65617521,-0.49958196,-0.49661735,-0.28159794,-0.25726899,-0.18999761,-0.15819207,-0.18205221,-0.085795903,-0.017493272,-0.049312009,-0.0014951784,-0.12088383,-0.066927619,-0.061237041,-0.011137098,-0.081267864,-0.095634942,-0.082587542,-0.083429735,-0.006766283,0.067348157,0.17254522,0.18137849,0.14396784,0.10514342,0.23271294,0.37389181,0.29246474,0.35861995,0.46181416,0.55458142,0.55309288,0.54139729,0.62162143,0.5734197,0.53817807,0.59688723,0.58713937,0.52807235,0.50706869,0.4896769,0.53420094,0.43291029,0.4693079,0.46264228,0.39917341,0.39199179,0.34465011,0.36123529,0.41014108,0.28632576,0.33879387,0.4084739,0.40226493,0.61838852,0.92969708,1.050583,1.1055125,1.2683189,1.5014475,1.7310197,1.8003672,1.6298024,1.6082378,1.368541,1.2017647,1.0268043,0.82428008,0.67159484,0.49834036,0.14232364,-0.054244961,-0.097500253,-0.064028647,-0.10560225,-0.15830046,-0.1289438,-0.16725139,-0.15391527,-0.14177636,-0.016588432,-0.11318458,-0.16583041,-0.14902949,-0.13018339,0.010624351,0.24575479,1.0924611,1.5074773,1.6191065,2.1709991,2.3665558,1.8727767,1.0689129,0.72222343,1.0059861,0.058005928]

print(model_predict([inp]))