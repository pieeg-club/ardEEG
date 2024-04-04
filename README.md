# EEGduino
Arduino for measure EEG, EMG, and ECG bio-signals

# Easy way to the neuroscience world with a shield for Arduino.    

## To Buy - soon EEGduino will be available in the market at our partner shop [Elecrow](https://www.elecrow.com/pieeg.html)
[LinkedIn for updates](https://www.linkedin.com/company/96475004/admin/feed/posts/) (Not a medical device)  
  
#### It is not a medical device!!! And cannot be used for any medical purposes!!!

This project is the result of several years of work on the development of BCI. We believe that the easiest way to get started with biosignals is to use a shield.
We will try to reveal the process of reading EEG signals as fully and clearly as possible. 

#### Warnings
>[!WARNING]
> You are fully responsible for your personal decision to purchase this device and, ultimately, for its safe use. EEGduino is not a medical device and has not been certified by any government regulatory agency for use with the human body. Use it at your own risk.  

>[!CAUTION]
> The device must operate only from a battery - 5 V. Complete isolation from the mains power is required.! The device MUST not be connected to any kind of mains power, via USB or otherwise.   
> Power supply - only battery 5V, please read the datasheet!!!!!  

[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=DIY%20Brain-Computer%20Interface%20PIEEG%20&url=https://github.com/Ildaron/EEGwithRaspberryPI&hashtags=RaspberryPI,EEG,python,opensource)


#### How it Works   

Connect the shield to Arduino Uno R4 WiFi and after that connect the device to a battery (power supply) and connect electrodes.
Full galvanic isolation from mains required.  
Electrodes positioned according to the International 10-20 system, right.    
![alt tag](https://github.com/Ildaron/EEGwithRaspberryPI/blob/master/Supplementary%20files/fig.7.bmp "general view")​

#### Device Pinout  
Shield connected with Arduino Uno R4 only at the next points:     
 
#### Description of Code  
Arduino script does not allow reading data from ADS1299 with a frequency of 250 Hz. It's necessary to use .c or .cpp scripts for reading data in real-time and Python for signal processing and visualization.   


#### Video - Control Robot Toy by Blinking  
In process 


#### For Beginners
During the measurement, in addition to artifacts caused by muscle activity, be concerned about the increased resistance between the body and the floor. For example, in the picture below, the moment when the feet touch the floor with and without an insulated shoe. Without insulated shoes - increased noise is noticeable.




#### Citation  
In process 


#### Contacts  
ildarr2016@gmail.com  
http://pieeg.com/
