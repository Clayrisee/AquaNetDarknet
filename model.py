import os

def detect_pothole(img_path):
    os.system("cd darknet && ./darknet detector test data/obj.data cfg/custom-yolov4-detector.cfg \
              ../model/custom-yolov4-detector_final.weights .{} -thresh 0.35 -dont_show -map".format(img_path))