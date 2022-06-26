import os


class FileRename:
    def __init__(self):
        self.root = None  # 文件夹路径
        self.files = None  # （文件名，文件扩展名）
        self.rule = None  # 处理规则
        self.status = None  # 处理状态

    def run(self, root, rule):
        self.get_files(root)

    def get_files(self, root):
        if self.check_root(root):
            # 获取文件夹的文件
            def split_files(files):
                """分离文件名和扩展名"""
                return [os.path.splitext(i) for i in files]

            _ = os.listdir(root)
            self.root = root
            self.files = split_files([i for i in _ if os.path.isfile(os.path.join(root, i))])

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
        self.status = None


if __name__ == '__main__':
    t = FileRename()
    t.get_files(r'C:\Users\youyq\PycharmProjects\File_manager')
    print(t.root)
    print(t.files)
