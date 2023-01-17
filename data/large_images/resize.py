from PIL import Image
import os


def resize(in_dir, out_dir, width=640):
    for item in os.listdir(in_dir):
        if item[-4:].lower() == '.png':
            im = Image.open(item)
            f, _ = os.path.splitext(item)
            old_width, old_height = im.size
            imResize = im.resize(
                (width, int(old_height / old_width * width))
            )
            out_file = f'{out_dir}/resized_{f}.png'
            if not os.path.exists(os.path.dirname(out_file)):
                os.makedirs(os.path.dirname(out_file))
            imResize.save(out_file, 'png')


if __name__ == '__main__':
    resize(os.getcwd(), '../../resized_pos')
