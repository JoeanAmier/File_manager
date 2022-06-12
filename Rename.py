import os


class FileRename:
    def __init__(self):
        self.finish = False

    def run(self, root, rule):
        if items := self.get_files(root):
            self.finish = True
        else:
            self.finish = False

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
