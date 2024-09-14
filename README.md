# nagoyatv-hackathon-image-recognition

## Overview
[名古屋テレビ主催 全国学生対抗SFプロトタイピングハッカソン Electric Sheep](https://www.nagoyatv.com/hackathon-electricsheep/)

チーム えれちょ〜 作品

## Installation
1. Install poetry

```
curl -sSL https://install.python-poetry.org | python3 -
```
2. Installing libraries managed by poetry
```
poetry install
```

## Usage
```
poetry run python3 main.py
```

## Library
最後はCIで実装するつもりですが、ローカルで実行できるものには以下のものがあります。

- mypy

type hintsが無いとエラーを出してくれます。

ライブラリのimportエラーが発生するので以下のコマンドでtype hintsのみ検証できます。


```
mypy --strict --ignore-missing-imports FILENAME
```

- flake8

未使用のコードや暗黙的なエラーを見つけてくれます。

オプションは自由にしてくだ

```
flake8
```

## Architecture
- Provider
  - 座標だったり接近率だったり計算結果を提供する
- render
  - デバッグ時の描画処理を実装する
- util
  - 定数など
- test
  - UnitTest等の実装    
