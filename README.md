<div align="center">

# ardEEG

**Measure EEG with an Arduino.**

Low-cost, open-source 8-channel shield for the Arduino UNO R4 WiFi that measures EEG, EMG and ECG with the TI ADS1299 and streams over Wi-Fi.

[📖 Documentation](https://docs.pieeg.com/hardware/devices/ardeeg/) ·
[🚀 How to Start](https://docs.pieeg.com/hardware/devices/ardeeg/setup/) ·
[🛒 Buy](https://pieeg.com/ardeeg/) ·
[💬 Discord](https://discord.gg/5Ps24p47)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_shield.jpg" alt="ardEEG shield" width="420">

</div>

> [!WARNING]
> ardEEG is **not a medical device** and has not been certified by any regulator for use with the human body. It cannot be used for any medical purpose. You use it at your own risk.

> [!CAUTION]
> **Battery only.** While electrodes are on a person, the Arduino and the shield run from a **small 5 V power bank** (up to 1 A, up to 1,000 mAh). Connect the Arduino to a computer only to upload the sketch, with no electrodes on anyone. The board has **no isolation**. Read the [Safety page](https://docs.pieeg.com/hardware/devices/ardeeg/safety/).

## At a glance

| | |
|---|---|
| **Channels** | 8 biosignal inputs, plus reference and bias |
| **Converter** | TI ADS1299, 24-bit, simultaneous sampling |
| **Sample rate** | 250 SPS |
| **Internal noise** | About 0.5 µV RMS per channel |
| **Signals** | EEG, EMG, ECG |
| **Host** | Arduino UNO R4 **WiFi** |
| **Link to the computer** | Wi-Fi, UDP port 13900 |
| **Electrodes** | Dry or wet Ag/AgCl, 2.54 mm header |
| **Power** | Small 5 V power bank: up to 1 A, up to 1,000 mAh |
| **Software** | Arduino sketch + Python script (this repo) |

## How it works

```
 Electrodes 1–8 ─┐
 Reference (ear) ┼─► ardEEG ──SPI──► Arduino UNO R4 ──Wi-Fi──► Python on
 Bias (ear) ─────┘   (ADS1299)       WiFi                       your computer
                                       ▲
             5 V power bank ───────────┘
```

The Arduino reads every sample over SPI, packs 50 samples into one UDP packet and sends it over Wi-Fi to a Python script on your computer.

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_kit.jpg" alt="ardEEG kit: cap, shield on the Arduino, power bank" width="420">

## Quick start

1. **Find your computer's IP address** on the Wi-Fi network (`ipconfig` on Windows → IPv4 Address). Example: `192.168.1.241`.
2. **Edit the sketch** [`software/arduino/1.Send_data_via_wifi.ino`](software/arduino/1.Send_data_via_wifi.ino):

```cpp
char ssid[] = "Wifi Name";                 // your Wi-Fi name (2.4 GHz)
char pass[] = "password";                  // your Wi-Fi password
...
udp.beginPacket("192.168.1.241", 13900);   // your computer's IP address
```

3. **Upload** it with the Arduino IDE (board: **Arduino UNO R4 WiFi**), then unplug the USB cable.
4. **Mount** the shield, **connect** 8 electrodes, a reference ear clip and a bias ear clip, and **power** the Arduino from the power bank.
5. **Run the receiver** [`software/python/1.Alpha_real_time.py`](software/python/1.Alpha_real_time.py), with `UDP_IP` set to the same IP address:

```bash
pip install matplotlib scipy
cd software/python
python 1.Alpha_real_time.py
```

A window opens with 8 live graphs (8–12 Hz alpha band by default).

> [!IMPORTANT]
> The **same IP address** (your computer's) must be in the sketch and in the Python script, and both devices must be on the **same 2.4 GHz Wi-Fi network**.

Full walkthrough: **[docs.pieeg.com → ardEEG → How to Start](https://docs.pieeg.com/hardware/devices/ardeeg/setup/)**

## Wiring

| Input | Electrode | Purpose |
|---|---|---|
| **Channels 1–8** | EEG electrodes in a cap (10-20 system) | Signal |
| **Reference** | Ear clip on one earlobe | Common 0 µV point for all channels |
| **Bias** | Ear clip on the other earlobe | Cancels common-mode noise (mains hum) |

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_connection.png" alt="ardEEG wiring: channels 1–8, reference and bias" width="700">

Suggested positions: **F7, Fz, F8, C3, C4, T5, Pz, T6**.

### Arduino pinout

The shield uses only these pins, plus power and ground. All other pins are free for your own projects.

| Arduino pin | Signal |
|---|---|
| D13 | SPI clock (SCK) |
| D12 | SPI MISO |
| D11 | SPI MOSI |
| D10 | Chip select |
| D7 | DRDY (data ready) |

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_pinout.png" alt="ardEEG pins on the Arduino headers" width="600">

## Software

| File | What it does |
|---|---|
| [`software/arduino/1.Send_data_via_wifi.ino`](software/arduino/1.Send_data_via_wifi.ino) | Sets up the ADS1299, reads samples, sends 50-sample UDP packets over Wi-Fi |
| [`software/python/1.Alpha_real_time.py`](software/python/1.Alpha_real_time.py) | Receives packets, converts to µV, filters and plots 8 channels |
| [`software/python/speed_test_250_samples.py`](software/python) | Checks the data arrives at the full 250 SPS |

**Change the filter:** the receiver shows 8–12 Hz by default. For blinks and chewing, set `highcut = 1` and `lowcut = 40` near the top of the script (the two names are swapped; the values are the band edges).

**Data format:** each sample is 27 bytes (3 status + 8 channels × 3 bytes, 24-bit big-endian two's complement). Each UDP packet is 1,350 bytes = 50 samples. Details: [Specification](https://docs.pieeg.com/hardware/devices/ardeeg/specification/).

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_8ch.jpg" alt="8 channels in the Python receiver" width="450">

## Example signals

**EEG: alpha test** (electrode at Fz, eyes closed and open, filtered 8–12 Hz) · [dataset](dataset/alpha)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_alpha.png" alt="Alpha test with ardEEG" width="500">

**EEG: chewing and blinking** (electrode at Fz, 4-3-2-1 times, filtered 1–40 Hz) · [dataset](dataset/artefacts)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_artifacts.png" alt="Chewing and blinking artifacts" width="500">

**Internal noise** (about 0.5 µV RMS per channel) · [dataset](dataset/internal_noise)

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_noise.png" alt="ardEEG internal noise on 8 channels" width="700">

## Where to use

<img src="https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_applications.jpg" alt="ardEEG applications: robotic arm, computer, exoskeleton, drone, toy car" width="650">

## Video

[![How to measure EEG with ardEEG](https://raw.githubusercontent.com/pieeg-club/PiEEG-docs/main/public/images/hardware/2026/10/ardeeg_video.jpg)](https://youtu.be/s_5mDDUFp6E)

## What's in this repository

| Folder | Content |
|---|---|
| [`software/arduino`](software/arduino) | Arduino sketch (older versions in `arxive`) |
| [`software/python`](software/python) | Real-time receiver and speed tests |
| [`dataset`](dataset) | Alpha, artifacts and internal-noise recordings, with plotting scripts |
| [`doc`](doc) | Notebook: how to reduce noise during EEG measurement |
| [`supplementary_files`](supplementary_files) | Images used in the original README |

## Documentation

| Page | |
|---|---|
| [ardEEG Intro](https://docs.pieeg.com/hardware/devices/ardeeg/) | Overview, comparison with PiEEG-8 |
| [What's in the Box](https://docs.pieeg.com/hardware/devices/ardeeg/required-equipment/) | What you need besides the shield |
| [How to Start](https://docs.pieeg.com/hardware/devices/ardeeg/setup/) | IP address, sketch upload, first signal |
| [Electrodes & Pinout](https://docs.pieeg.com/hardware/devices/ardeeg/connections/) | Wiring, montage, Arduino pins |
| [Software](https://docs.pieeg.com/hardware/devices/ardeeg/software/) | Sketch, Python receiver, filter, speed test |
| [Signals & Datasets](https://docs.pieeg.com/hardware/devices/ardeeg/examples/) | Example recordings and datasets |
| [Specification](https://docs.pieeg.com/hardware/devices/ardeeg/specification/) | Data format, µV conversion, ADS1299 registers |
| [Troubleshooting](https://docs.pieeg.com/hardware/devices/ardeeg/troubleshooting/) | Upload, Wi-Fi, UDP and signal fixes |
| [Safety](https://docs.pieeg.com/hardware/devices/ardeeg/safety/) | Battery-only operation and responsible use |

Also: [Manual on Google Colab](https://colab.research.google.com/drive/1xW6fwzVdLH83zHoorjeWai6SdZoOanfA)

## Citation

If you use ardEEG in research, please cite:

```
I. Rakhmatulin. Low-Cost Shield ardEEG to Measure EEG with Arduino Uno R4 WiFi.
Preprints 2024, 2024051643. DOI: 10.20944/preprints202405.1643.v1
```

## License

Software and SDK: **MIT**. Hardware use is subject to the terms in [`license.txt`](license.txt).

## Contact

- 🌐 [pieeg.com](https://pieeg.com/)
- 📖 [docs.pieeg.com](https://docs.pieeg.com/)
- 💬 [Discord](https://discord.gg/5Ps24p47)
- ✉️ [pieeg@pieeg.com](mailto:pieeg@pieeg.com)
