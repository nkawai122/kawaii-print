・ターミナル出力される文字にシンプルに色付けをして出力可能にするモジュール。

・呼び出し方法もシンプル

#### シンプルな呼び出し方法
```python
from kawaii_colors import paint

text = "Python3 is Beatiful."
paint(text)
```


#### カスタマイズして呼び出す方法
```python
from kawaii_colors import Cprint

text = "Python3 is Beatiful."
options = {"font_weight": "bold", "color_code": "red"}
print(Cprint(text, options=options))
```

### 連続して出力する方法
```python
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
```
