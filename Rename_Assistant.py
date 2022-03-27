import os

class FileManager:
    def delete_text(
            folder,
            first_num=0,
            last_num=None,
            format_=None,
            re_=None,
            run=False):
        """重命名：删除文本"""
        files = format_filtering(folder, format_)
        modify = [i[first_num:last_num] for i in files]
        if not run:
            return modify

    def format_filtering(folder, format_=None):
        """获取文件夹内指定格式的文件"""
        files = os.listdir(folder)
        if format_:
            values = []
            for i in format_.split(';'):
                for j in files:
                    if j.endswith(i):
                        values.append(j)
            return values
