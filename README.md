# ECG variability database

## 1. Introduction
This repository contains a database of ECGs collected from a volunteer with different bit resolutions and activity rates. These files have been used to test the effects of data variability on side channel attacks to wearable sensors. All files have been obtained using a custom-made t-shirt with conductive pads and the data was collected using a Bitalino at maximum sample rate (1 kHz).

## 2. Files
All files are given in CSV format separated by tabs (`\t`). The files are divided among folders:

* *ecg_10bit*: contains data acquired at 10 bit resolution for two scenarios:
	* *rest_10bit*: volunteer at rest, clean ECG
	* *noisy_10_bit*: volunteer moving, noisy ECG
* *ecg_16_bit*: contains data acquired at 10 bit resolution for four scenarios:
	* *good_16bit*: volunteer lying down, clean ECG
	* *average_16bit*: volunteer at rest, mostly clean ECG with some noise
	* *noisy_16bit*: volunteer moving around, ECG with some noise
	* *verynoisy_16bit*: volunteer moving around and using the stairs, ECG with noise, some segments clip at zero or maximum values
* *ecg_extra*: other ECGs recorded with 16 bit resolution

## 3. License
