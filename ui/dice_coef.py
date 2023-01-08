import numpy as np

def dice_coef(y_true:np.ndarray, y_pred:np.ndarray):
    smooth = 1
    y_true_f = y_true.flatten()
    y_pred_f = y_pred.flatten()
    intersection = np.sum(y_true_f * y_pred_f)

    return round((2. * intersection + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) + smooth),3)


def dice_average_sets(y_true:np.ndarray, y_pred:np.ndarray):
    assert y_true.shape[0] == y_pred.shape[0], "you should use same size data"
    dice = []
    for i in range(y_true.shape[0]):
        dice.append(dice_coef(y_true[i], y_pred[i]))
    print(np.mean(dice))
    
    return dice
