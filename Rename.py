import os


class FileRename:
    def run(self, root, rule):
        pass

    def get_files(self, root):
        return x if self.check_root(root) and any(x := os.listdir(root)) else None

    @staticmethod
    def check_root(root):
        return os.path.exists(root) and os.path.isdir(root)

    @staticmethod
    def check_file(root):
        return os.path.exists(root) and os.path.isfile(root)


if __name__ == '__main__':
    FileRename()
