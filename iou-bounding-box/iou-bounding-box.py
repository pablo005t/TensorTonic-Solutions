def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    W_a = box_a[2] - box_a[0]
    H_a = box_a[3] - box_a[1]
    W_b = box_b[2] - box_b[0]
    H_b = box_b[3] - box_b[1]
    A_a = W_a * H_a
    A_b = W_b * H_b
    if box_a[2] < box_b[0] and box_a[3] < box_b[1]:
        return 0
    else: 
        Intersection_0 = max(box_a[0],box_b[0])
        Intersection_1 = max(box_a[1],box_b[1])
        Intersection_2 = min(box_a[2],box_b[2])
        Intersection_3 = min(box_a[3],box_b[3])
        H_I = Intersection_3 - Intersection_1
        W_I = Intersection_0 - Intersection_2
        A_I = H_I * W_I
        union = A_b + A_a + A_I
        IoU = - A_I / union
        return IoU