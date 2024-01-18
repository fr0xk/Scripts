from functools import partial
import argparse
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logger()

load_and_preprocess_image = lambda image_path, target_size: (
    tf.keras.preprocessing.image.img_to_array(
        tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
    ) / 255.0
) if os.path.exists(image_path) else None

load_and_preprocess_dataset = lambda image_paths, target_size: (
    np.array(
        list(filter(None, [load_and_preprocess_image(path, target_size) for path in image_paths]))
    )
)

create_autoencoder = lambda height, width, channels: (
    Model(
        Input(shape=(height, width, channels)),
        Conv2D(32, (3, 3), activation='relu', padding='same')(input_img) >>
        MaxPooling2D((2, 2), padding='same') >>
        Conv2D(64, (3, 3), activation='relu', padding='same') >>
        Conv2D(64, (3, 3), activation='relu', padding='same') >>
        UpSampling2D((2, 2)) >>
        Conv2D(channels, (3, 3), activation='sigmoid', padding='same'),
        name="autoencoder"
    ) >> (lambda autoencoder: autoencoder.compile(optimizer=Adam(lr=0.001), loss='mse') or autoencoder)
)

train_autoencoder = lambda autoencoder, train_data, val_data, epochs, batch_size, model_save_path: (
    autoencoder.fit(
        train_data, train_data,
        epochs=epochs,
        batch_size=batch_size,
        shuffle=True,
        validation_data=(val_data, val_data),
        callbacks=[
            EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True),
            ModelCheckpoint(model_save_path, save_best_only=True)
        ]
    ) if train_data.size > 0 else logger.error("No valid training data. Exiting.")
)

main = lambda args: (
    logger.info("Starting image denoising script."),
    args.image_paths and os.path.exists(args.model_save_path) or logger.error("Invalid image paths or model save path. Exiting."),
    (lambda target_size, dataset, train_data, val_data, autoencoder:
        target_size and dataset.size > 0 and train_data.size > 0 and (
            train_autoencoder(autoencoder, train_data, val_data, args.epochs, args.batch_size, args.model_save_path) or
            logger.info("Image denoising script completed.")
        )
    )(
        (args.height, args.width),
        load_and_preprocess_dataset(args.image_paths, (args.height, args.width)),
        *train_test_split(load_and_preprocess_dataset(args.image_paths, (args.height, args.width)), test_size=args.validation_split, random_state=42),
        create_autoencoder(args.height, args.width, args.channels)
    )
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Image Denoising Script')
    parser.add_argument('--height', type=int, default=256, help='Image height')
    parser.add_argument('--width', type=int, default=256, help='Image width')
    parser.add_argument('--channels', type=int, default=3, help='Number of image channels')
    parser.add_argument('--epochs', type=int, default=10, help='Number of training epochs')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
    parser.add_argument('--validation_split', type=float, default=0.2, help='Validation split ratio')
    parser.add_argument('--model_save_path', type=str, default='autoencoder_model.h5', help='Path to save the trained model')
    parser.add_argument('--image_paths', nargs='+', type=str, help='List of image paths for training')

    args = parser.parse_args()

    main(args)

