from abc import ABCMeta, abstractmethod


class IColor(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def set_color(text: str, font_weight: str, color_code: str) -> str:
        pass


class Color(IColor):
    @staticmethod
    def set_color(text: str, font_weight: str, color_code: str) -> str:
        colors = {
            "bold": "\033[30m",
            "blue": "\033[34m",
            "cyan": "\033[36m",
            "green": "\033[32m",
            "purple": "\033[35m",
            "red": "\033[31m",
            "white": "\033[37m",
            "yellow": "\033[33m",
        }

        weights = {
            "bold": "\033[1m",
            "bold_res": "\033[22m",
            "italics": "\033[3m",
            "italics_res": "\033[23m",
            "underline": "\033[4m",
            "underline_res": "\033[24m",
        }

        text_color = colors[color_code]
        weight = weights[font_weight]
        reset = "\033[00m"
        msg = f"{weight}{text_color}" f"{text}{reset}"
        return msg


class Cprint:
    def __init__(
        self,
        msg: str | None,
        color: IColor = Color,
        options: dict | None = None,
    ):
        self.__msg: str | None = None
        if options:
            self.options = options
        else:
            self.options = {"font_weight": "bold", "color_code": "green"}
            self.__msg = color.set_color(text=msg, **self.options)

    @property
    def msg(self) -> str | None:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):

        if msg is None:
            return
        else:
            self.__msg = msg

    def __str__(self):
        return self.msg


def decocolor(func):
    def wrapper(msg: str):
        colored_result = Cprint(func(msg))
        return colored_result, print(colored_result)

    return wrapper


@decocolor
def paint(text: str):
    return text


if __name__ == "__main__":
    text = "Python3 is Beautiful."
    colored_text = Color.set_color(
        text=text, font_weight="bold", color_code="green"
    )
    print(colored_text)
    print(Cprint(text))
    paint(text)
