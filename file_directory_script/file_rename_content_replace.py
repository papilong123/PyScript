import os

path_example = r"C:\Users\directory"


def rename_multi_file(path):
    paths = path.replace("\\", "//")
    paths = paths + "//"
    for _, filename in enumerate(os.listdir(paths)):
        new = filename.replace(" ", "")
        os.rename(os.path.join(paths, filename), os.path.join(paths, new))


def replace_file_content(path):
    paths = path.replace("\\", "//")
    paths = paths + "//"
    for _, filename in enumerate(os.listdir(paths)):
        # 传入文件(file),将旧内容(old_content)替换为新内容(new_content)
        def replace(file, old_content, new_content):
            content = read_file(file)
            content = content.replace(old_content, new_content)
            rewrite_file(file, content)

        # 读文件内容
        def read_file(file):
            with open(file, encoding='UTF-8') as f:
                read_all = f.read()
                f.close()

            return read_all

        # 写内容到文件
        def rewrite_file(file, data):
            with open(file, 'w', encoding='UTF-8') as f:
                f.write(data)
                f.close()

        # 替换操作(将test.txt文件中的'Solution'替换为文件名'filename')
        replace(os.path.join(paths, filename), "Solution", filename[0: filename.index(".", 0, len(filename))])
