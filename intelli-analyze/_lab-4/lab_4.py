def process_path(img_path):
    global genres_list
    img_id = str(img_path).split(os.sep)[-1].split('.')[0]
    # label = data.loc(data['id']==img_id)['genres_list'].values()
    label = data.loc[data['id'] == img_id,['genres_list']]
    #label = list(filter(lambda x: x if x in genres_list, label))
    _ = list(filter(lambda x: x in genres_list, label['genres_list']))
    label = _[0] if len(_)>0 else []
    return (tf.io.read_file(img_path), label)

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from PIL import Image
from ast import literal_eval
import os.path
import os

images = '../_lab-4/movies_posters/'
batch_size = 32
(img_width, img_height) = (190, 281)

data = pd.read_csv('../_lab-4/final_dataset.csv', header=0, 
        usecols=['id', 'genres_list', 'title', 'popularity', 'release_date', 'vote_average', 'vote_count', 'link'],
        dtype=object, converters={'genres_list': literal_eval}, parse_dates=True)
data.convert_dtypes()

genres_list = data['genres_list'].explode().unique()[:20]

list_ds = tf.data.Dataset.list_files(images+'*.jpg')
labeled_ds = list_ds.map(process_path)

SIZE = len(labeled_ds)

train_ds = labeled_ds.take(SIZE // 100 * 80) 
test_ds = labeled_ds.skip(SIZE // 100 * 80)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.shuffle(1000).prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

num_genres = len(genres_list)

model = tf.keras.Sequential([
    layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_genres)
    ])

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
images_ds, labels_ds = tuple(zip(*train_ds))
model.fit(images_ds, labels_ds, batch_size=batch_size, epochs=2)