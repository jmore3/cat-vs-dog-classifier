# src/load_data.py
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from pathlib import Path

def create_data_generators(base_dir, target_size=(150, 150), batch_size=32):
    base_dir = Path(base_dir)

    datagen_train = ImageDataGenerator(rescale=1./255)
    datagen_val_test = ImageDataGenerator(rescale=1./255)

    train_gen = datagen_train.flow_from_directory(
        base_dir / 'train',
        target_size=target_size,
        batch_size=batch_size,
        class_mode='binary'
    )

    val_gen = datagen_val_test.flow_from_directory(
        base_dir / 'val',
        target_size=target_size,
        batch_size=batch_size,
        class_mode='binary'
    )

    test_gen = datagen_val_test.flow_from_directory(
        base_dir / 'test',
        target_size=target_size,
        batch_size=batch_size,
        class_mode='binary',
        shuffle=False
    )

    return train_gen, val_gen, test_gen

if __name__ == "__main__":
    train, val, test = create_data_generators("data/processed")
