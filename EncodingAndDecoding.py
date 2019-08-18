#!/usr/bin/python
"""
    Purpose:Export images
"""
import base64
import os
from pprint import pprint

def get_current_working_dir():
    return os.path.abspath(os.curdir)


def get_base_64_folder():
    path = os.path.join(os.curdir, 'base64files')
    if not os.path.exists(path):
        os.umask(0)
        os.makedirs(path,0o777)
    return os.path.abspath(path)


def get_images_folder():
    path = os.path.join(os.curdir, 'ImagesToTransfer')
    if not os.path.exists(path):
        os.umask(0)
        os.makedirs(path,0o777)
    return os.path.abspath(path)


def encode_images():
    path = os.path.abspath(r'C:\Users\212702343\Pictures\Websites images')
    _cwd = get_current_working_dir()
    folder_path_files_to_save = get_base_64_folder()
    os.chdir(folder_path_files_to_save)
    for root, _dir, _image_files in os.walk(path):
        print(len([image for image in _image_files if image.endswith(
            '.jpg') or image.endswith('.jpeg')]))
        for _image in (image for image in _image_files if image.endswith('.jpg') or image.endswith('.jpeg')):
            with open(os.path.join(root, _image), 'rb') as image:
                image_read = image.read()
                image_64_encode = base64.encodestring(image_read)
                # folder_path_files_to_save = get_base_64_folder()
                _text_file_name = str(_image)+'.txt'
                # os.chdir(folder_path_files_to_save)
                with open(_text_file_name, 'wb') as fh:
                    fh.write(image_64_encode)
                    fh.close()
                image.close()
    os.chdir(_cwd)             

def decode_images():
    _cwd = get_current_working_dir()
    _images_folder = get_images_folder()
    _base_64_text_files = get_base_64_folder()
    for _root,_dir,_text_files in os.walk(get_base_64_folder()):
        for _base_64_text_file in (_text for _text in _text_files if _text.endswith('.txt')):
            os.chdir(_base_64_text_files)
            with open(_base_64_text_file,'rb') as _text_files:
                _base_64text = _text_files.read()
                image_64_decode = base64.decodestring(_base_64text)
                # os.chdir(_cwd)
                os.chdir(_images_folder)
                _filename_without_ext = os.path.splitext(_base_64_text_file)[0]
                with open(_filename_without_ext, 'wb') as image_result:
                    image_result.write(image_64_decode)
                    image_result.close()
                _text_files.close()
    os.chdir(_cwd)

if __name__ == "__main__":
    encode_images()
    decode_images()
