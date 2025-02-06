def right_hemisphere_network():
    model = models.Sequential([
        layers.Conv2D(64, (3, 3), activation='relu', input_shape=(image_height, image_width, channels)),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(256, activation='tanh'),  # Non-linear to mimic abstract thought
        layers.Dense(output_size, activation='softmax')  # Classification or creative output
    ])
    return model