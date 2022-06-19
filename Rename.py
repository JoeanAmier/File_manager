import os


class FileRename:
    def __init__(self):
        self.root = None  # 文件夹路径
        self.files = None  # （文件名，文件扩展名）
        self.rule = None  # 处理规则
        self.finish = False

    def run(self, root, rule):
        if items := self.get_files(root):
            self.finish = True
        else:
            self.finish = False

    def get_files(self, root):
        if self.check_root(root) and any(x := os.listdir(root)):
            # 检查文件夹是否不为空
            def split_files(files):
                """分离文件名和扩展名"""
                return [os.path.splitext(i) for i in files]

            self.root = root
            self.files = split_files([i for i in x if os.path.isfile(os.path.join(root, i))])

    def type_filter(self, type_: list | tuple):
        """筛选指定类型的文件"""
        self.files = [i for i in self.files if i[1] in type_]

    @staticmethod
    def check_root(root):
        """检查路径是否为文件夹"""
        return os.path.exists(root) and os.path.isdir(root)

    def reset(self):
        self.root = None
        self.files = None
        self.rule = None
        self.finish = False


if __name__ == '__main__':
    FileRename().get_files(r'C:\Users\youyq\PycharmProjects\File_manager')
