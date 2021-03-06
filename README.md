# Deep Learning Models for NIDS using NSL-KDD and ICIDS2017 datasets 

## Requirements
1. `Python 3.6.7`
2. `Tesnsorflow`
3. `Keras framework`

## Models
1. LSTM model
2. GRU model
3. RNN model
4. DNN model
5. LRGC (LSTM, RNN, GRU and CNN combined)
6. Classic machine learning models (Naive Bayes, Ada Boost and more)

## Usage

[NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html) and [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) datasets must be in the `/data/nsl` and `/data/cicids/` folders. Each model is saved in a file run. to run them, simply use:

`python model_name.py`

for binary and multiclass classification comment/uncomment codes in each model
