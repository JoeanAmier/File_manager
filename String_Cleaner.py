import platform


def clean(string, **kwargs):
    system = platform.system()
    replace = {
        "/": "",
    }
    if system == "Windows":
        pass


if __name__ == '__main__':
    clean()
