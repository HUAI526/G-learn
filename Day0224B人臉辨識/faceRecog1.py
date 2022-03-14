import dlib, numpy

predictor = "shape_predictor_68_face_landmarks.dat"
recogmodel = "dlib_face_recognition_resnet_model_v1.dat"

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor)
facerec = dlib.face_recognition_model_v1(recogmodel)


def getFeature(imgfile):
    img = dlib.load_rgb_image(imgfile)
    dets = detector(img, 1)
    for det in dets:
        shape = sp(img, det)
        feature = facerec.compute_face_descriptor(img, shape)
        return numpy.array(feature)
    
def samePerson(pic1, pic2):
    feature1 = getFeature(pic1)
    feature2 = getFeature(pic2)
    dist = numpy.linalg.norm(feature1-feature2)
    print("歐式距離={}".format(dist))
    if dist < 0.3:
        print("{} 和 {} 為同一個人!".format(pic1, pic2))
        
    else:
        print("{} 和 {} 不是同一個人!".format(pic1, pic2))
    print()
    
samePerson("media\\david1.jpg", "media\\bear2.jpg")
samePerson("media\\david1.jpg", "media\\david2.jpg")