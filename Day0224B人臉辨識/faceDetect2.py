import dlib

predictor = "shape_predictor_5_face_landmarks.dat"
sp = dlib.shape_predictor(predictor)
detector = dlib.get_frontal_face_detector()

img = dlib.load_rgb_image("media\\person5.jpg")
win = dlib.image_window()
win.clear_overlay()
win.set_image(img)

dets = detector(img, 1)
print("人臉數:{}".format(len(dets)))
for k,det in enumerate(dets):
    print("偵測人臉():左:{} 上:{} 右:{} 下:{}".format(k, det.left(), det.top(), det.right(), det.bottom()))
    win.add_overlay(det)
    shape = sp(img, det)
    win.add_overlay(shape)
    dlib.hit_enter_to_continue()