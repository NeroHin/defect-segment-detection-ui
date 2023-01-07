def xywh2xyxy(data:list, img_w:int, img_h:int) -> list:

    """Converts a bounding box from xyxy format to xywh format.

    Args:

        xyxy (list): A bounding box in xyxy format.

    Returns:

        list: A bounding box in xywh format.

    """

    bbox_width = float(data[2]) * img_w
    bbox_height = float(data[3]) * img_h
    center_x = float(data[0]) * img_w 
    center_y = float(data[1]) * img_h 
    
        
    min_x, min_y = center_x - (bbox_width / 2), center_y - (bbox_height / 2)
    max_x, max_y = center_x + (bbox_width / 2), center_y + (bbox_height / 2)
    print(min_x,min_y,max_x,max_y)

    return [min_x, min_y, max_x, max_y]
