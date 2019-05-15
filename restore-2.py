from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf
from tensorflow import keras

print('tf.version:' + str(tf.__version__))

(train_images,
 train_labels), (test_images,
                 test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0


# Returns a short sequential model
def create_model():
    model = tf.keras.models.Sequential([
        keras.layers.Dense(512, activation=tf.nn.relu, input_shape=(784, )),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(),
                  loss=tf.keras.losses.sparse_categorical_crossentropy,
                  metrics=['accuracy'])

    return model


def main():
    # include the epoch in the file name. (uses `str.format`)
    checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)

    # create a fresh model then evaluate
    model = create_model()
    loss, acc = model.evaluate(test_images, test_labels)
    print("Untrained model, accuracy: {:5.2f}%".format(100 * acc))

    # create a fresh model then load_weights, at last evaluate
    latest = tf.train.latest_checkpoint(checkpoint_dir)
    print('latest checkpoint: ' + latest)
    model = create_model()
    model.load_weights(latest)
    loss, acc = model.evaluate(test_images, test_labels)
    print("Restored model, accuracy: {:5.2f}%".format(100 * acc))


if __name__ == '__main__':
    main()
