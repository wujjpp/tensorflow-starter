from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras

print('tf.version:' + str(tf.__version__))

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

# Returns a short sequential model
def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation=tf.nn.relu, input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation=tf.nn.softmax)
  ])

  model.compile(optimizer=tf.keras.optimizers.Adam(),
                loss=tf.keras.losses.sparse_categorical_crossentropy,
                metrics=['accuracy'])

  return model

def main():
  checkpoint_path = "training_1/cp.ckpt"
  
  # Create a fresh model for tesing
  model = create_model()

  # then evaluate
  loss, acc = model.evaluate(test_images, test_labels)
  print("Untrained model, accuracy: {:5.2f}%".format(100*acc))

  # Load saved checkpoint
  model.load_weights(checkpoint_path)
  loss,acc = model.evaluate(test_images, test_labels)
  print("Restored model, accuracy: {:5.2f}%".format(100*acc))

if __name__ == '__main__':
  main()  


