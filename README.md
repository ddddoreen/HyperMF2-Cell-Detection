

# Installation

Python>=3.8.0 environment, including PyTorch>=1.8.
The command is as follows.

```bash
conda create -n miccai python=3.8
conda activate miccai
pip install -r requirements.txt  # install
```
# Datasets

Please prepare the data in the YOLO dataset format. We will provide the preprocessed data, including images and labels, which can be directly used for training. Additionally, we will also provide the trained weights, which can be directly used for testing.
```bash
Dataset A:https://pan.baidu.com/s/15xMdcIaLJzcFiybftHPQQw?pwd=pgf2

Dataset B:https://pan.baidu.com/s/1w2bs7geX3UcitTC6KG0Bpw?pwd=759c

Dataset C:https://pan.baidu.com/s/1E8ECKxud7UDZawFm97iX0A?pwd=5jjh
```
# Training
Most of training configurations can change in the "Train settings" section of ultralytics/cfg/default.yaml. 
The key factors are model, data, img, epoches, batch, device and training hyperparameters.
For example, you can use "model: hyper-yolon.yaml" to train an object detection model.

```bash
python train.py 
```

# Evaluation
Most of evaluation configurations can change in the "Val/Test settings" section of ultralytics/cfg/default.yaml. 
The key factors are model(weight), data, img, batch, conf, iou, half.

```bash
python ultralytics/models/yolo/detect/val.py
```


# Acknowledgement
Our code is built based on the [YOLO](https://github.com/ultralytics/ultralytics).
