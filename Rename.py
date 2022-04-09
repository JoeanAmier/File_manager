import os


class FileRename:
    def run(self, root, rule):
        pass

    @staticmethod
    def check_root(root):
        return os.path.exists(root) and os.path.isdir(root)
