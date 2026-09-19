import tensorflow as tf
from tensorflow.keras import layers, models
import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np

# -----------------------------
# 1. Load MNIST dataset
# -----------------------------
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# -----------------------------
# 2. Build the model
# -----------------------------
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# -----------------------------
# 3. Compile
# -----------------------------
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# -----------------------------
# 4. Train
# -----------------------------
model.fit(x_train, y_train, epochs=5)

# -----------------------------
# 5. Create drawing window
# -----------------------------
window = tk.Tk()
window.title("🤖 AI Digit Guesser")

canvas_size = 280

canvas = tk.Canvas(
    window,
    width=canvas_size,
    height=canvas_size,
    bg="black"
)

canvas.pack()

# Create an image that stores what we draw
image = Image.new("L", (canvas_size, canvas_size), 0)
draw = ImageDraw.Draw(image)


# -----------------------------
# 6. Draw with mouse
# -----------------------------
def paint(event):

    x = event.x
    y = event.y

    # Draw a white circle
    canvas.create_oval(
        x - 10, y - 10,
        x + 10, y + 10,
        fill="white",
        outline="white"
    )

    draw.ellipse(
        [x - 10, y - 10, x + 10, y + 10],
        fill=255
    )


canvas.bind("<B1-Motion>", paint)


# -----------------------------
# 7. Predict the digit
# -----------------------------
def predict():

    # Resize 280x280 → 28x28
    small_image = image.resize((28, 28))

    # Convert to numpy array
    img = np.array(small_image)

    # Normalize
    img = img / 255.0

    # Add batch dimension
    img = img.reshape(1, 28, 28)

    # Make prediction
    prediction = model.predict(img, verbose=0)

    # Find highest probability
    digit = prediction.argmax()

    # Confidence
    confidence = prediction[0][digit] * 100

    result_label.config(
        text=f"🤖 I think it's: {digit}\n"
             f"Confidence: {confidence:.2f}%"
    )


# -----------------------------
# 8. Clear the canvas
# -----------------------------
def clear():

    canvas.delete("all")

    draw.rectangle(
        [0, 0, canvas_size, canvas_size],
        fill=0
    )

    result_label.config(
        text="✏️ Draw a digit!"
    )


# -----------------------------
# 9. Buttons
# -----------------------------
predict_button = tk.Button(
    window,
    text="🤖 Predict",
    command=predict,
    font=("Arial", 14)
)

predict_button.pack(pady=5)


clear_button = tk.Button(
    window,
    text="🧹 Clear",
    command=clear,
    font=("Arial", 14)
)

clear_button.pack(pady=5)


# Result
result_label = tk.Label(
    window,
    text="✏️ Draw a digit!",
    font=("Arial", 18)
)

result_label.pack(pady=10)


# -----------------------------
# 10. Start the app
# -----------------------------
window.mainloop()