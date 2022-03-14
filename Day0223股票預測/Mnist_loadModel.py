from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import load_model

def show_images_labels_predictions(images,labels,start_id,num=10):
    plt.gcf().set_size_inches(12,14)
    if num>25: num=25
    for i in range(0,num):
        ax=plt.subplot(5,5, i+1)
        ax.imshow(images[start_id], cmap='binary')
        if (len(predictions) > 0):
            title =' ai = ' + str(predictions[start_id])
            title += ('(o)' if predictions[start_id]==labels[start_id] else '(x)')
            title += '\nlabel = ' + str(labels[start_id])
        else:
            title = 'label = ' + str(labels[start_id])
        ax.set_title(title,fontsize=12)
        ax.set_xticks([]);ax.set_yticks([])
        start_id+=1
    plt.show()
    
    
(train_feature, train_label), (test_feature , test_label) = mnist.load_data()
test_feature_vector = test_feature.reshape(len(test_feature),784).astype('float32')
test_feature_normalize = test_feature_vector/255
model = load_model('Mnist_mlp_model.h5')

prediction=model.predict_classes(test_feature_normalize)
show_images_labels_predictions(test_feature, test_label, prediction, 0)