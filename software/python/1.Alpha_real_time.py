from matplotlib import pyplot as plt
import socket
from scipy import signal


UDP_IP = "192.168.1.241"  
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
data_before_2 = [0]*sample_lens
data_before_3 = [0]*sample_lens
data_before_4 = [0]*sample_lens
data_before_5 = [0]*sample_lens
data_before_6 = [0]*sample_lens
data_before_7 = [0]*sample_lens
data_before_8 = [0]*sample_lens

ch_1 = []
ch_2 = []
ch_3 = []
ch_4 = []
ch_5 = []
ch_6 = []
ch_7 = []
ch_8 = []



fps = 250
highcut = 8
lowcut = 12

axis_x=0
y_minus_graph=50
y_plus_graph=50
x_minux_graph=5000
x_plus_graph=250


fig, axis = plt.subplots(4, 2, figsize=(5, 5))
plt.subplots_adjust(hspace=1)

axi = [(i, j) for i in range(4) for j in range(2)]
ch_name = 0
ch_name_title = [1,5,2,6,3,7,4,8]
for ax_row, ax_col in axi:
    
    axis[ax_row, ax_col].set_xlabel('Time')
    axis[ax_row, ax_col].set_ylabel('Amplitude')
    axis[ax_row, ax_col].set_title('Data after pass filter' + str(ch_name_title[ch_name]))
    ch_name = ch_name + 1


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
        ch_2.append(result[2])
        ch_3.append(result[3])
        ch_4.append(result[4])
        ch_5.append(result[5])
        ch_6.append(result[6])
        ch_7.append(result[7])
        ch_8.append(result[8])

        
        if len(ch_1) == sample_lens:
            #ch1
            data_after_1 = ch_1
            dataset_1 = data_before_1 + data_before_1 + data_before_1 + data_after_1
            data_before_1 = data_after_1

            data_filt_numpy_high_1 = butter_highpass_filter(dataset_1, highcut, fps)
            data_for_graph_1 = butter_lowpass_filter(data_filt_numpy_high_1, lowcut, fps)

            axis[0,0].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_1[-sample_lens:],color=(0, 1, 0))
            axis[0,0].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_1[5] - y_minus_graph,data_for_graph_1[15] + y_plus_graph])

            #ch2
            data_after_2 = ch_2
            dataset_2 = data_before_2 + data_before_2 + data_before_2 + data_after_2
            data_before_2 = data_after_2

            data_filt_numpy_high_2 = butter_highpass_filter(dataset_2, highcut, fps)
            data_for_graph_2 = butter_lowpass_filter(data_filt_numpy_high_2, lowcut, fps)

            axis[1,0].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_2[-sample_lens:],color=(0, 1, 0))
            axis[1,0].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_2[5] - y_minus_graph,data_for_graph_2[15] + y_plus_graph])

            #ch3
            data_after_3 = ch_3
            dataset_3 = data_before_3 + data_before_3 + data_before_3 + data_after_3
            data_before_3 = data_after_3

            data_filt_numpy_high_3 = butter_highpass_filter(dataset_3, highcut, fps)
            data_for_graph_3 = butter_lowpass_filter(data_filt_numpy_high_3, lowcut, fps)

            axis[2,0].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_3[-sample_lens:],color=(0, 1, 0))
            axis[2,0].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_3[5] - y_minus_graph,data_for_graph_3[15] + y_plus_graph])


            #ch4
            data_after_4 = ch_4
            dataset_4 = data_before_4 + data_before_4 + data_before_4 + data_after_4
            data_before_4 = data_after_4

            data_filt_numpy_high_4 = butter_highpass_filter(dataset_4, highcut, fps)
            data_for_graph_4 = butter_lowpass_filter(data_filt_numpy_high_4, lowcut, fps)

            axis[3,0].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_4[-sample_lens:],color=(0, 1, 0))
            axis[3,0].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_4[5] - y_minus_graph,data_for_graph_4[15] + y_plus_graph])

            #ch5
            data_after_5 = ch_5
            dataset_5 = data_before_5 + data_before_5 + data_before_5 + data_after_5
            data_before_5 = data_after_5

            data_filt_numpy_high_5 = butter_highpass_filter(dataset_5, highcut, fps)
            data_for_graph_5 = butter_lowpass_filter(data_filt_numpy_high_5, lowcut, fps)

            axis[0,1].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_5[-sample_lens:],color=(0, 1, 0))
            axis[0,1].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_5[5] - y_minus_graph,data_for_graph_5[15] + y_plus_graph])

            #ch6
            data_after_6 = ch_6
            dataset_6 = data_before_6 + data_before_6 + data_before_6 + data_after_6
            data_before_6 = data_after_6

            data_filt_numpy_high_6 = butter_highpass_filter(dataset_6, highcut, fps)
            data_for_graph_6 = butter_lowpass_filter(data_filt_numpy_high_6, lowcut, fps)

            axis[1,1].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_6[-sample_lens:],color=(0, 1, 0))
            axis[1,1].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_6[5] - y_minus_graph,data_for_graph_6[15] + y_plus_graph])

            #ch7
            data_after_7 = ch_7
            dataset_7 = data_before_7 + data_before_7 + data_before_7 + data_after_7
            data_before_7 = data_after_7

            data_filt_numpy_high_7 = butter_highpass_filter(dataset_7, highcut, fps)
            data_for_graph_7 = butter_lowpass_filter(data_filt_numpy_high_7, lowcut, fps)

            axis[2,1].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_7[-sample_lens:],color=(0, 1, 0))
            axis[2,1].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_7[5] - y_minus_graph,data_for_graph_7[15] + y_plus_graph])

            #ch8
            data_after_8 = ch_8
            dataset_8 = data_before_8 + data_before_8 + data_before_8 + data_after_8
            data_before_8 = data_after_8

            data_filt_numpy_high_8 = butter_highpass_filter(dataset_8, highcut, fps)
            data_for_graph_8 = butter_lowpass_filter(data_filt_numpy_high_8, lowcut, fps)

            axis[3,1].plot(range(axis_x, axis_x + sample_lens, 1), data_for_graph_8[-sample_lens:],color=(0, 1, 0))
            axis[3,1].axis([axis_x - x_minux_graph, axis_x + x_plus_graph, data_for_graph_8[5] - y_minus_graph,data_for_graph_8[15] + y_plus_graph])
            
            plt.pause(0.000001)
            axis_x=axis_x+sample_lens            
            data_1ch_test = []
            ch_1 = []
            data_2ch_test = []
            ch_2 = []
            data_3ch_test = []
            ch_3 = []
            data_4ch_test = []
            ch_4 = []
            data_5ch_test = []
            ch_5 = []
            data_6ch_test = []
            ch_6 = []
            data_7ch_test = []
            ch_7 = []
            data_8ch_test = []
            ch_8 = []



            
