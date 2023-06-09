from collections.abc import Iterable
from typing import Any, Final

from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler

from suspension_data.constants import INPUT_DIM, TRAIN_EPOCHS
from suspension_data.models.models import SuspensionRecord


def split_data(
    records: Iterable[SuspensionRecord],
) -> tuple[list[tuple[int, ...]], list[int]]:
    train: Final[list[tuple[int, ...]]] = []
    test: Final[list[int]] = []

    for record in records:
        train.append(
            (
                record.gender.index,
                record.school_type.index,
                record.program.index,
                record.suspension_reason.index,
                record.year,
            )
        )
        test.append(record.count)

    scaler = StandardScaler()
    scaler.fit_transform(train)

    return train, test


def train_model_and_evaluate(
    feature_train, feature_test, target_train, target_test
) -> tuple[Sequential, float]:
    model = Sequential(
        [
            Dense(
                units=64,
                input_dim=INPUT_DIM,
                kernel_initializer="normal",
                activation="relu",
            ),
            Dense(units=64, kernel_initializer="normal", activation="relu"),
            Dense(units=64, kernel_initializer="normal", activation="relu"),
            Dense(units=1, kernel_initializer="normal", activation="linear"),
        ]
    )

    model.compile(
        loss="mean_squared_error",
        optimizer=Adam(learning_rate=0.001),
        metrics=["accuracy"],
    )
    model.fit(
        x=feature_train, y=target_train, epochs=TRAIN_EPOCHS, batch_size=10, verbose=1
    )

    return model, model.evaluate(feature_test, target_test, verbose=0)


def predict_from_model(
    model: Sequential, prediction_data: Iterable[Any]
) -> list[float]:
    return model.predict(prediction_data)
