from __future__ import absolute_import, division, print_function

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
    # Create a basic model instance
    model = create_model()
    model.summary()

    # include the epoch in the file name. (uses `str.format`)
    checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"

    cp_callback = tf.keras.callbacks.ModelCheckpoint(
        checkpoint_path,
        verbose=1,
        save_weights_only=True,
        # Save weights, every 5-epochs.
        period=5)

    model = create_model()
    model.fit(train_images,
              train_labels,
              epochs=50,
              callbacks=[cp_callback],
              validation_data=(test_images, test_labels),
              verbose=0)


if __name__ == '__main__':
    main()
