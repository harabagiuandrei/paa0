import tensorflow as tf
from tensorflow.keras import layers, models

def left_hemisphere_network():
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=(input_size,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(output_size, activation='softmax')  # For classification or specific tasks
    ])
    return model