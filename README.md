・ターミナル出力される文字にシンプルに色付けをして出力可能にするモジュール。

・呼び出し方法もシンプル

#### シンプルな呼び出し方法
```python
from colors import paint

text = "Python3 is Beatiful."
paint(text)
```


#### カスタマイズして呼び出す方法
```python
frmo colors import Cprint

text = "Python3 is Beatiful."
options = {"font_weight": "bold", "color_code": "red"}
print(Cprint(text, options=options))
```

