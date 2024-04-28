from matplotlib import pyplot as plt
import socket
from scipy import signal


UDP_IP = "" # IP PC   
UDP_PORT = 13900   
data_lenght = 1350
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ("ok1")
test = []
sock.bind((UDP_IP, UDP_PORT))
data_test= 0x7FFFFF
data_check=0xFFFFFF
result = data_lenght*[0]


sample_lens = 50

data_before_1 = [0]*sample_lens
ch_1 = []



fps = 250
highcut = 8
lowcut = 22

axis_x=0
y_minus_graph=50
y_plus_graph=50
x_minux_graph=5000
x_plus_graph=250


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


    

while True:
    data, addr = sock.recvfrom(data_lenght)  
    #print(data.decode())
    data_list = [byte for byte in data]
    output = data_list #[7:]
    #print(len(data_list))

    for c in range (0,data_lenght,27):
        for a in range (0,26,3):
            voltage_1=(output[a+c]<<8)| output[a+1+c]
            voltage_1=(voltage_1<<8)| output[a+2+c]
            
            convert_voktage=voltage_1|data_test

            if convert_voktage==data_check:
                voltage_1_after_convert=(16777214-voltage_1)
            else:
                voltage_1_after_convert=voltage_1
            channel_num =  (a/3)
                
            result[int (channel_num)]=round(1000000*4.5*(voltage_1_after_convert/16777215),2)
        ch_1.append(result[1])
        
        if len(ch_1) == sample_lens:
            
            data_after_1 = ch_1
            dataset_1 = data_before_1 + data_before_1 + data_before_1 + data_after_1
            data_before_1 = data_after_1

            data_filt_numpy_high_1 = butter_highpass_filter(dataset_1, highcut, fps)
            data_for_graph_1 = butter_lowpass_filter(data_filt_numpy_high_1, lowcut, fps)
            plt.xlabel('Time') 
            plt.ylabel('Amplitude')
            plt.title('Data after pass filter CH1')  # Set the title for the plot

            plt.plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_1[-sample_lens:],color=(0, 1, 0))
            plt.axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_1[5] - y_minus_graph,data_for_graph_1[15] + y_plus_graph])

            plt.pause(0.000001)
            axis_x=axis_x+sample_lens 
            data_1ch_test = []
            ch_1 = []    
