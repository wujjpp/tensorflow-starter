from __future__ import absolute_import, division, print_function

# import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print('tf.version: ' + str(tf.__version__))

dataset_path = keras.utils.get_file(
    "auto-mpg.data",
    "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
)

column_names = [
    'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration',
    'Model Year', 'Origin'
]
raw_dataset = pd.read_csv(dataset_path,
                          names=column_names,
                          na_values="?",
                          comment='\t',
                          sep=" ",
                          skipinitialspace=True)

dataset = raw_dataset.copy()

# display last 5 rows
print('------dataset.tail()------')
print(dataset.tail())
print('======================================')
print('------dataset.length------')
print(len(dataset))
print('------dataset.isna().sum()------')
print(dataset.isna().sum())

print('======================================')
print('------dataset.dropna()------')
dataset = dataset.dropna()
print('------dataset.length------')
print(len(dataset))
print('------dataset.isna().sum()------')
print(dataset.isna().sum())

print('======================================')
print('------dataset.pop(\'Origin\')------')
origin = dataset.pop('Origin')
dataset['USA'] = (origin == 1) * 1.0
dataset['Europe'] = (origin == 2) * 1.0
dataset['Japan'] = (origin == 3) * 1.0
print(dataset.tail())

# split data to train and test
print('======================================')
print('------split data to rain train and test------')
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
print(len(train_dataset), len(test_dataset), len(dataset))

sns.pairplot(train_dataset[["MPG", "Cylinders", "Displacement", "Weight"]],
             diag_kind="kde")
# plt.show()

print('======================================')
print('------train_dataset.describe()------')
train_stats = train_dataset.describe()
print(train_stats)
train_stats.pop("MPG")
print('------train_dataset.transpose()------')
train_stats = train_stats.transpose()
print(train_stats)

# prepare train labels & test labels, after operation, the train_dataset
# and test_dataset doesn't contains MPG column
train_labels = train_dataset.pop('MPG')
test_labels = test_dataset.pop('MPG')

# prepare normalized data, it is what we will use to train the model.
print('======================================')


def norm(x):
    return (x - train_stats['mean']) / train_stats['std']


normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)
print('------train_dataset.tail()------')
print(train_dataset.tail())
print('------normed_train_data.tail()------')
print(normed_train_data.tail())

# build the model
print('======================================')


def build_model():
    model = keras.Sequential([
        layers.Dense(64,
                     activation=tf.nn.relu,
                     input_shape=[len(train_dataset.keys())]),
        layers.Dense(64, activation=tf.nn.relu),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mean_squared_error',
                  optimizer=optimizer,
                  metrics=['mean_absolute_error', 'mean_squared_error'])
    return model


model = build_model()
print('------show model summary------')
print(model.summary())

# Now try out the model. Take a batch of 10 examples from the training data
# and call model.predict on it.
print('------try out the model for 10 example')
example_batch = normed_train_data[:10]
example_result = model.predict(example_batch)

print(example_result)


# Display training progress by printing a single dot for each completed epoch,
# for display progress
class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0:
            print('')
        print('.', end='')


# The patience parameter is the amount of epochs to check for improvement
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

EPOCHS = 1000

history = model.fit(normed_train_data,
                    train_labels,
                    epochs=EPOCHS,
                    validation_split=0.2,
                    verbose=0,
                    callbacks=[early_stop, PrintDot()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print()
print(hist.tail())


# display history as figure
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label='Train Error')

    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label='Val Error')

    plt.ylim([0, 5])
    plt.legend()

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label='Train Error')

    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label='Val Error')

    plt.ylim([0, 20])
    plt.legend()


plot_history(history)

# evaluate normed test data
loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=0)

print("Testing set Mean Abs Error: {:5.2f} MPG".format(mae))

test_predictions = model.predict(normed_test_data).flatten()
plt.figure()
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [MPG]')
plt.ylabel('Predictions [MPG]')
plt.axis('equal')
plt.axis('square')
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.ylim()[1]])
_ = plt.plot([-100, 100], [-100, 100])

plt.figure()
error = test_predictions - test_labels
plt.hist(error, bins=25)
plt.xlabel("Prediction Error [MPG]")
_ = plt.ylabel("Count")

plt.show()
