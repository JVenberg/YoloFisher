import os
import random
import shutil


def get_split(image_dir, label_dir, split=0.8):
    imgs = [(
        os.path.join(
            image_dir,
            img
        ),
        os.path.join(
            label_dir,
            os.path.splitext(os.path.basename(img))[0] + '.txt'
        )
    ) for img in os.listdir(image_dir) if img.endswith('.png')]

    for img, label in imgs:
        assert os.path.exists(img), img
        assert os.path.exists(label), label

    random.shuffle(imgs)
    return imgs[:int(split * len(imgs))], imgs[int(split * len(imgs)):]


def copy_into_partition(train, val, dir='partitioned_data'):
    shutil.rmtree(dir)
    os.makedirs(os.path.join(dir, 'images/train/'), exist_ok=True)
    os.makedirs(os.path.join(dir, 'images/val/'), exist_ok=True)
    os.makedirs(os.path.join(dir, 'labels/train/'), exist_ok=True)
    os.makedirs(os.path.join(dir, 'labels/val/'), exist_ok=True)
    for img, label in train:
        shutil.copy(img, os.path.join(dir, 'images/train/'))
        shutil.copy(label, os.path.join(dir, 'labels/train/'))
    for img, label in val:
        shutil.copy(img, os.path.join(dir, 'images/val/'))
        shutil.copy(label, os.path.join(dir, 'labels/val/'))


if __name__ == '__main__':
    train, val = get_split('data/images', 'data/labels')
    copy_into_partition(train, val)
