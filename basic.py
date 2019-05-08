# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def print_version():
  print('tf.version: ' + str(tf.__version__))
  print('np.version: ' + str(np.__version__))
  print('matplotlib.version: ' + str(matplotlib.__version__))

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print('--------train data info--------')
print('train_images.shape: ' + str(train_images.shape))
print('train_labels: ' + str(train_labels))
print('len(train_labels): ' + str(len(train_labels)))

print('--------test data info--------')
print('test_images.shape: ' + str(test_images.shape))
print('test_labels: ' + str(test_labels))
print('len(test_labels): ' + str(len(test_labels)))

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)

train_images = train_images / 255.0
test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(train_images[i])    
    plt.grid(True)
    # plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])

plt.show()

def create_model():
  model = keras.Sequential([
      keras.layers.Flatten(input_shape=(28, 28)),
      keras.layers.Dense(128, activation=tf.nn.relu),
      keras.layers.Dense(10, activation=tf.nn.softmax)
  ])

  model.summary()

  model.compile(optimizer=tf.train.AdamOptimizer(),
      loss='sparse_categorical_crossentropy',
      metrics=['accuracy'])

  return model    

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap = plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
    100*np.max(predictions_array),
    class_names[true_label]),
    color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

def main():
  # print version info
  print_version()

  model = create_model()

  model.fit(train_images, train_labels, epochs=5)

  # 评估准确率
  test_loss, test_acc = model.evaluate(test_images, test_labels)

  print('Test accuracy:', test_acc)

  # 图形化方式显示准确率
  predictions = model.predict(test_images)

  num_rows = 5
  num_cols = 3
  num_images = num_rows*num_cols
  plt.figure(figsize=(2*2*num_cols, 2*num_rows))
  for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test_labels)
  plt.show()

  # 单个样本预测
  img = test_images[0]
  print(img.shape)
  img = (np.expand_dims(img,0))
  print(img.shape)

  predictions_single = model.predict(img)
  print(predictions_single)

  plot_value_array(0, predictions_single, test_labels)
  _ = plt.xticks(range(10), class_names, rotation=45)
  plt.show()

if __name__ == '__main__':
  main()
