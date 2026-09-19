import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load and normalize MNIST dataset
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0

# Reshape for CNN/Augmentation layers (28x28x1)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# 2. Define Data Augmentation Sequential Block
data_augmentation = tf.keras.Sequential([
    layers.RandomRotation(0.1),    # Random rotation up to 10%
    layers.RandomTranslation(0.1, 0.1), # Random horizontal/vertical shift
    layers.RandomZoom(0.1),        # Random zoom
])

# 3. Build Neural Network Architecture
model = models.Sequential([
    # Input & Augmentation
    layers.Input(shape=(28, 28, 1)),
    data_augmentation,
    
    # Convolutional Layers with LeakyReLU
    layers.Conv2D(32, (3, 3)),
    layers.LeakyReLU(alpha=0.1),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3)),
    layers.LeakyReLU(alpha=0.1),
    layers.MaxPooling2D((2, 2)),
    
    # Fully Connected Layers
    layers.Flatten(),
    layers.Dense(128),
    layers.LeakyReLU(alpha=0.1),
    layers.Dropout(0.3), # Regularization to prevent overfitting
    layers.Dense(10, activation='softmax')
])

# 4. Compile with Adam Optimizer
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Train and Evaluate
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test)
)

# Test evaluation
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"\nFinal Test Accuracy: {test_acc * 100:.2f}%")