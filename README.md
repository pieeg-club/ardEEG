# ardEEG 
# ardEEG shield for Arduino UNO R4 to measure EEG, EMG, and ECG bio-signals.      

## To Buy - soon ardEEG will be available in the market at our partner shop [Elecrow](https://www.elecrow.com/pieeg.html)
[LinkedIn for updates](https://www.linkedin.com/company/96475004/admin/feed/posts/) (Not a medical device)  
  
#### It is not a medical device!!! And cannot be used for any medical purposes!!!

This project is the result of several years of work on the development of BCI. We believe that the easiest way to get started with biosignals is to use a shield.
We will try to reveal the process of reading EEG signals as fully and clearly as possible. 

#### Warnings
>[!WARNING]
> You are fully responsible for your personal decision to purchase this device and, ultimately, for its safe use. ardEEG is not a medical device and has not been certified by any government regulatory agency for use with the human body. Use it at your own risk.  

>[!CAUTION]
> The device must operate only from a battery - 5 V. Complete isolation from the mains power is required.! The device MUST not be connected to any kind of mains power, via USB or otherwise.   
> Power supply - only battery 5V

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





#### Device Pinout  
Shield connected with Arduino Uno R4 only at the next points:     
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/spi.png" width="50%" height="50%" alt="generals view">
</p>

 
#### Description of Code  
Arduino script does not allow reading data from ADS1299 with a frequency of 250 Hz. It's necessary to use .c or .cpp scripts for reading data in real-time and Python for signal processing and visualization.   


#### Video presentation
In this [video](https://youtu.be/s_5mDDUFp6E) you can see how to measure EEG  

[![Hardware demonstrations](https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/youtube.png)](https://youtu.be/s_5mDDUFp6E))   

#### For Beginners
During the measurement, in addition to artifacts caused by muscle activity, be concerned about the increased resistance between the body and the floor. For example, in the picture below, the moment when the feet touch the floor with and without an insulated shoe. Without insulated shoes - increased noise is noticeable.

####Artifact test. 
The process of measuring chewing and blinking artifacts using dry electrodes (Fz). Chewing occurred in the following sequence: 4 times, 3 times, 2, and 1 time, and the same for the blinking process. The y- axis is the processed EEG signal after passing filter bands of 1-40 Hz in microvolts and with 250 samples per
[Dataset]( https://github.com/Ildaron/ardEEG/tree/main/dataset/artefacts) 
<p align="center">
  <img src= "https://github.com/Ildaron/ardEEG/blob/main/supplementary_files/blink.bmp" width="50%" height="50%" alt="generals view">
</p>

####Alpha test. 
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
In process 


#### Contacts  
ildarr2016@gmail.com  
http://pieeg.com/
