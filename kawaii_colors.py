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
            "gray": "\033[30m",
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
        options: dict | None = None,
        color: IColor = Color,
    ):
        self.__msg: str | None = None
        if isinstance(options, dict):
            self.options = options
            self.__msg = color.set_color(
                text=msg,
                font_weight=options["font_weight"],
                color_code=options["color_code"],
            )
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

    def __str__(self) -> str:
        return self.msg


def decocolor(func):
    def wrapper(msg: str, kwords=None):
        colored_result = Cprint(func(msg), kwords)
        return colored_result, print(colored_result)

    return wrapper


@decocolor
def paint(text: str, kwords=None):
    return text


if __name__ == "__main__":
    text = "Python3 is Beautiful."
    colors = [
        "gray",
        "blue",
        "cyan",
        "green",
        "purple",
        "red",
        "white",
        "yellow",
    ]
    weights = [
        "bold",
        "bold_res",
        "italics",
        "italics_res",
        "underline",
        "underline_res",
    ]
    for c in colors:
        for w in weights:
            paint(text, {"font_weight": w, "color_code": c})
