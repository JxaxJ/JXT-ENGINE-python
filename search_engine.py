import os

def search_files(search_term, dir_, cif=False):
    """
    Ищет файлы, содержащие заданный поисковый запрос в заданной директории и ее поддиректориях.
    :param cif:
    """
    valid_extensions = ('.py', '.ui', '.txt', '.hdf5', '.ini', '.xml', '.iml', '.md', '.mgt')
    results = []
    for root, _, files in os.walk(dir_):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if cif:
                if ext in valid_extensions:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            results.append(file_path)
                            if 'GCInfo'.lower() in f.read().lower():
                                print('True')
                                print(file_path)
                    except:
                        pass
                else:
                    file_path = os.path.join(root, file)
                    results.append(file_path)
            else:
                file_path = os.path.join(root, file)
                results.append(file_path)

    return results

def valid_extension(dir_):
    ext = []
    for root, _, files in os.walk(dir_):
        for file in files:
            extensions = os.path.splitext(file)[-1].lower()
            if extensions and not extensions in ext:
                ext.append(extensions)
    print(ext)


print(search_files(search_term='main', dir_="C:/Users/79607/Pictures", cif=True))
''''''