import platform


def clean(text: str, rule: dict = None) -> str:
    if rule:
        for i in rule:
            text = text.replace(i, rule[i])
    else:
        system = platform.system()
        match system:
            case "Windows":
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
            case "Linux":
                pass
            case "MACOS":
                pass
            case _:
                replace = {}
        for i in replace:
            text = text.replace(i, replace[i])
    return text


if __name__ == '__main__':
    print(clean("1:2", {':': "-"}))
