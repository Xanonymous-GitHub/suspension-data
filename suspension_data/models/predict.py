from typing import Iterable

import numpy as np
from keras.layers import Dense
from keras.models import Sequential

from suspension_data.models.models import SuspensionRecord

num_classes = 5
input_dim = 5
train_epochs = 50


def split_data(records: Iterable[SuspensionRecord]) -> tuple[list[list], list[int]]:
    train: list[list] = []
    test: list[int] = []

    for record in records:
        record_data = list(record.serializable_dict.values())
        test.append(record_data.pop())
        train.append(record_data)

    return train, test


def train_model_and_predict(x_train, x_test, y_train):
    model = Sequential()
    model.add(Dense(units=256, input_dim=input_dim, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=256, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=256, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=num_classes, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x=x_train, y=y_train, validation_split=0.0, epochs=train_epochs, batch_size=32, verbose=1)

    y_test = []
    predict_results = model.predict(x_test)
    for result in predict_results:
        y_test.append(np.argmax(result))
    return y_test
