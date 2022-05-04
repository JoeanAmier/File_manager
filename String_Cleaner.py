import platform


def clean(text: str, rule: dict = None) -> str:
    system = platform.system()
    if system == "Windows":
        replace = {
            "/": "",
            "\\": "",
            "|": "",
            "<": "",
            ">": "",
            '"': "",
            "?": "",
            ":": "",
            "*": "",
        }
        if rule:
            for i in rule:
                replace[i] = rule[i]
        for i in replace:
            text = text.replace(i, replace[i])
    return text


if __name__ == '__main__':
    print(clean("1:2", {':': "-"}))
