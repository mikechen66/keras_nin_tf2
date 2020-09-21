
# nin.py

"""
NIN(Network in Network) is the creative DNN model in which GAN(Global Averag Pooling) is adpted to elimitate the large quantity 
of parameters. In contrast, AlexNet deep learning structure is a combination of CNN+FC that incure a huge RAM occupation. CNN 
is responsible for extracting features, and FC is responsible for feature classification. NIN uses mlpconv and GAP to organicall
combine the two parts of CNN and streamline FC with making it more interpretable. 

Reference:
https://arxiv.org/pdf/1312.4400.pdf
"""


# -import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D, GlobalAveragePooling2D, AveragePooling2D
from keras import optimizers
from keras.layers.normalization import BatchNormalization
from keras.regularizers import l2


def nin(input_shape, num_classes):

    model = Sequential()

    model.add(Conv2D(filters=192, kernel_size=(5,5), padding='same', activation="relu", kernel_regularizer=l2(1e-4), input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=160, kernel_size=(1,1), padding='same', activation="relu", kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=96, kernel_size=(1,1), padding='same', activation="relu", kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))
    model.add(Dropout(0.5))

    model.add(Conv2D(filters=192, kernel_size=(5,5), padding='same', activation="relu", kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=192, kernel_size=(1,1), padding='same', activation="relu", kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=192, kernel_size=(1,1), padding='same', activation="relu", kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))
    model.add(Dropout(0.5))

    model.add(Conv2D(filters=192, kernel_size=(3,3), padding='same', activation="relu", kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=192, kernel_size=(1,1), padding='same', activation="relu" , kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=10, kernel_size=(1,1), padding='same', activation="relu", kernel_regularizer=l2(1e-4)))
    model.add(BatchNormalization())

    model.add(GlobalAveragePooling2D())
    model.add(Activation(activation="softmax"))

    return model


if __name__ == '__main__':

    IMAGE_WIDTH = 227
    IMAGE_HEIGHT = 227
    CHANNELS = 3
    NUM_CLASSES = 1000

    # Assign the vlaues 
    INPUT_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, CHANNELS)

    # Call the model 
    model = nin(INPUT_SHAPE, NUM_CLASSES)

    # show the full model structure
    model.summary()

