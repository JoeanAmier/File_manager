import os


class Check:
    def __init__(self):
        self.root = None  # 文件夹路径
        self.files = []  # （文件名，文件扩展名）
        self.status = False  # 处理状态

    def run(self, root, type_=None):
        self.get_files(root)
        self.type_filter(type_)
        self.status = bool(self.files)

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
        if type_:
            self.files = [i for i in self.files if i[1] in type_]

    @staticmethod
    def check_root(root):
        """检查路径是否为文件夹"""
        return os.path.exists(root) and os.path.isdir(root)


if __name__ == "__main__":
    test = Check()
    test.run(r"C:\Users\youyq\PycharmProjects\File_manager")
    test.type_filter(('.py',))
    print(test.root)
    print(test.files)
    print(test.status)
