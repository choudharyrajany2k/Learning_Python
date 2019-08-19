#!/env/bin/python
"""
    Purpose: Zipping and unzipping a byte file 
"""
import os
import re

_FILE_SEPERATOR = b'=========='
def join_multi_text_files(_path,_zipped_file_name):
    os.chdir(_path)
    if os.path.exists(_zipped_file_name):
        os.remove(_zipped_file_name)
    read_content = []
    
    for _root,_dir,files in os.walk(_path):
        with open(_zipped_file_name,'wb') as _zipped_Content:
            for _file in (_file for _file in files if _file.endswith('.txt')):
                with open(_file,'rb') as _text_file:
                    read_content.append(_FILE_SEPERATOR+ _text_file.read()+_FILE_SEPERATOR) #+=_FILE_SEPERATOR+ _text_file.read()+_FILE_SEPERATOR
                    _text_file.close()
            _zipped_Content.writelines(read_content)
            _zipped_Content.close()

def get_all_files_from_re(text):
    result = re.findall(r'==========(.*?)==========', text)
    print(result)
    return result


def unzip_multi_files(_path,_zippedfile_name):
    os.chdir(_path)
    with open(_zippedfile_name,'rb') as _zipped_file_handle:
        _read_text = _zipped_file_handle.readlines()
        _list_files = get_all_files_from_re(_read_text.decode('utf-8'))
        _zipped_file_handle.close()

if __name__ == "__main__":
    _ziped_file_name = "ZippedContentText.txt"
    _path = os.path.abspath(os.path.join(os.curdir,'python','base64files'))
    join_multi_text_files(_path,_ziped_file_name)
    unzip_multi_files(_path,_ziped_file_name)
