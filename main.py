# Created by Nishanta Parajuli
import tensorflow as tf

# Load the Keras model
keras_model_path = 'path/to/model.h5'
model = tf.keras.models.load_model(keras_model_path)

# Convert to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)
