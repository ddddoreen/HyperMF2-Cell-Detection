import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('Yours/ultralytics/cfg/models/hyper-yolo/hyper-yolo.yaml')   
    model.train(data='Yours/ultralytics-main/data_5.yaml',
                imgsz=640,
                epochs=150,
                batch=8,
                workers=4,
                device='0',
                optimizer='SGD',
                close_mosaic=10,
                project='runs/train',
                name='exp',
                single_cls=False,
                cache=False,
                )
