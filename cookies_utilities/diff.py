import urllib.request
import base64
import glob
import os
import re
from typing import Optional


def get_remote_content(url, username=None, password=None, binary=False):
    req = urllib.request.Request(url)
    if username is not None:
        base64string = base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')
        req.add_header('Authorization', f'Basic {base64string}')
    try:
        with urllib.request.urlopen(req) as res:
            if res.getcode() != 200:
                return False, []
            if binary:
                return True, [res.length]
            content = res.read().decode('utf-8')
        content = content.split('\n')
    except:
        return False, []
    if content[-1] == '':
        content = content[:-1]
    content = [c + '\n' for c in content]
    return True, content


def get_local_content(file_path, binary=False):
    if not os.path.isfile(file_path):
        return False, []
    if binary:
        return True, [os.path.getsize(file_path)]
    with open(file_path, encoding='utf-8') as ifile:
        content = ifile.readlines()
    return True, content


def has_diff_contents(content_0, content_1):
    len_0 = len(content_0)
    len_1 = len(content_1)
    if len_0 != len_1:
        return True, f'Difference detected: number of lines ({len_0}, {len_1}).'
    for i, (line_0, line_1) in enumerate(zip(content_0, content_1)):
        if line_0 != line_1:
            return True, f'Difference detected: line {i}.'
    return False, 'No difference detected.'


def has_diff_paths(path_0, path_1, username=None, password=None, binary=False):
    exists_0, content_0 = get_remote_content(path_0, username, password, binary) \
        if path_0.startswith('https://') else get_local_content(path_0, binary)
    exists_1, content_1 = get_remote_content(path_1, username, password, binary) \
        if path_1.startswith('https://') else get_local_content(path_1, binary)
    if not exists_0:
        return True, 'Not exist.'
    if not exists_1:
        return True, 'Not exist.'
    return has_diff_contents(content_0, content_1)


def has_diff_local_and_remote(
    local_dir: str,
    remote_url: str,
    username: Optional[str] = None,
    password: Optional[str] = None,
    exts: str = 'html|css|js',
    binary_exts: str = 'png|jpg|pdf',
) -> None:
    """ Recursively checks whether the local directory is synchronized with the specified URL.
    
    For binary files, only their presence and file size will be checked without verifying the content differences.

    :param local_dir: The path to the local directory.
    :param remote_url: The URL to be checked against.
    :param username: The username for basic authentication. If the URL is protected, please specify (optional).
    :param password: The password for basic authentication. If the URL is protected, please specify (optional).
    :param exts: A pipe-separated list of file extensions to be checked. Default is "html|css|js" (optional).
    :param binary_exts: A pipe-separated list of binary file extensions to be checked. Default is "png|jpg|pdf" (optional).
    """
    for local_file in glob.glob(local_dir + '**', recursive=True):
        if not os.path.isfile(local_file):
            continue
        if re.match(f'.+\.({exts})$', local_file) is not None:
            binary = False
        elif re.match(f'.+\.({binary_exts})$', local_file) is not None:
            binary = True
        else:
            continue
        basename = local_file.replace('\\', '/')
        basename = basename.replace(local_dir, '')
        exists_diff, msg = has_diff_paths(
            local_file, remote_url + basename,
            username, password, binary)
        if not exists_diff:
            print(f'OK: {basename}')
        else:
            print(f'NG: {basename}')
            print(f'  --> {msg}')
