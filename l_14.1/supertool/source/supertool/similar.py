import os


def work(directory: str, print_flag: bool=True):
    """Output to console lists of the same files founded in the directory.

    :param directory: path to the directory to search in.
    :param print_flag: enable or disable printing result
    :return: None (writes messages to stdout)
    """
    hashes = {}  # here key is hash, value is a list of paths to files with such hash
    # fill 'hashes' by taking hash of each file
    for root, _, file_paths in os.walk(directory):
        for file_path in file_paths:
            full_file_path = os.path.join(root, file_path)
            file_hash = hash(open(full_file_path, 'rb').read())
            hashes[file_hash] = hashes.get(file_hash, []) + [full_file_path]  # update list of paths with new one

    if print_flag:
        # print results
        for values in hashes.values():
            if len(values) > 1:
                print(f'This {len(values)} files are the same:\n{values}')
    return hashes.values()
