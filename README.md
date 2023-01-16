## How about this repo?

* Here is the repository for the UI of the defect detection and segmentation with digital image processing with N.C.K.U. CSIE course.
* The project scope is Detection and Segmentation in the Powder Spreading Process of Magnetic Material Additive Manufacturing.
* If you want to know the algorithm, please refer to the following [link](https://github.com/NeroHin/defect-detection-and-segment-deep-learning).

### Result
  
![image](/image/powder_uneven_result.png)
![image](/image/powder_uncover_result.png)

### How to run?

1. install requirements
```bash
pip install -r requirements.txt
```

2. cd to the project directory
```bash
cd defect-segment-detection-ui/ui
```

3. run UI
```bash
python  defect-detection2.py
```
4. download the model with [release](https://github.com/NeroHin/defect-segment-detection-ui/releases/tag/weighted) and move it to the model directory
```bash

# move to yolov7
mv yolov7_best.pt ../script/yolov7

# move to unet
mv unet_best.pth ../script/unet

```