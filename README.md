# ardEEG shield for Arduino UNO R4 to measure EEG, EMG, and ECG bio-signals.      
[Manual](https://colab.research.google.com/drive/1xW6fwzVdLH83zHoorjeWai6SdZoOanfA#scrollTo=nqHXFBm6J2XF)
## To Buy -   ardEEG is available in the  [market](https://pieeg.com/ardeeg/)
[LinkedIn for updates](https://www.linkedin.com/company/96475004/admin/feed/posts/) 

## Easy start

Just only 2 script one for [Arduino](https://github.com/Ildaron/ardEEG/blob/main/software/arduino/1.Send_data_via_wifi.ino) and for Python [Python](https://github.com/Ildaron/ardEEG/blob/main/software/python/1.Alpha_real_time.py) in Windows (etc) and full support from [PiEEG](https://pieeg.com/)))



This project is the result of several years of work on the development of BCI. We believe that the easiest way to get started with biosignals is to use a shield.
We will try to reveal the process of reading EEG signals as fully and clearly as possible. 


[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=DIY%20Brain-Computer%20Interface%20PIEEG%20&url=https://github.com/Ildaron/EEGwithRaspberryPI&hashtags=RaspberryPI,EEG,python,opensource)


#### How it Works   
Connect the shield to Arduino Uno R4 WiFi and after that connect the device to a battery (power supply) and connect electrodes.
Full galvanic isolation from mains is required.  
Electrodes are positioned according to the International 10-20 system    ​


<p align="center">
  <img src="https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/ard_EEG_general.png" width="50%" height="50%" alt="generals view">
</p>

<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/ardeeg.png" width="70%" height="70%" alt="generals view">
</p>





## Device Pinout, where to use and how connect

Device Pinout (Shield connected with Arduino Uno R4 only at the next points and power)  
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/spi.png" width="50%" height="50%" alt="generals view">
</p>

Where to use
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/genereal.jpg" width="80%" height="80%" alt="generals view">
</p>

How connect
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/connections2.bmp" width="80%" height="80%" alt="generals view">
</p>



#### Video presentation
In this [video](https://youtu.be/s_5mDDUFp6E) you can see how to measure EEG  

[![Hardware demonstrations](https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/youtube.png)](https://youtu.be/s_5mDDUFp6E))   

#### Artifact test  
The process of measuring chewing and blinking artifacts using dry electrodes (Fz). Chewing occurred in the following sequence: 4 times, 3 times, 2, and 1 time, and the same for the blinking process. The y- axis is the processed EEG signal after passing filter bands of 1-40 Hz in microvolts and with 250 samples per second  
[Dataset]( https://github.com/Ildaron/ardEEG/tree/main/dataset/artefacts)   
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/blink.bmp" width="50%" height="50%" alt="generals view">
</p>

#### Alpha test  
The process of recording an EEG signal from an electrode (Fz) with eyes open and closed. The y- axis is the processed EEG signal after passing filter bands of 8-12Hz in microvolts and with 250 samples per second

[Dataset](https://github.com/Ildaron/ardEEG/tree/main/dataset/alpha) 
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/aplha.bmp" width="50%" height="50%" alt="generals view">
</p>

8 channels reading example
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/graph.jpg" width="50%" height="50%" alt="generals view">
</p>


#### Citation  
Rakhmatulin, I. Low-Cost Shield ardEEG to Measure EEG with Arduino Uno R4 WiFi. Preprints 2024, 2024051643. https://doi.org/10.20944/preprints202405.1643.v1  


#### Contacts   
http://pieeg.com/  
[LinkedIn](https://www.linkedin.com/company/96475004/admin/feed/posts/)   
[Youtube](https://www.youtube.com/channel/UCVF-3Bp34LINLOQsyWNpcow)


#### Warnings
>[!WARNING]
> You are fully responsible for your personal decision to purchase this device and, ultimately, for its safe use. PiEEG is not a medical device and has not been certified by any government regulatory agency for use with the human body. Use it at your own risk.

>[!CAUTION]
> The device must operate only from a battery - 5 V. Complete isolation from the mains power is required.! The device MUST not be connected to any kind of mains power, via USB or otherwise.     
> Power supply - only battery 5V
> It is not a medical device!!! And cannot be used for any medical purposes  
