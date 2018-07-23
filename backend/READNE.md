# README

## Python Version

```shell
$ python -V
Python 3.6.5

$ pip -V
pip 18.0 from /path/to/lib/python3.6/site-packages/pip (python 3.6)
```

## Setup

```shell
$ git clone git@github.com:kobakazu0429/kure_kosen_map_api.git
$ cd kure_kosen_map_api
$ pip install virtualenv
$ virtualenv --no-site-packages map_api
$ source map_api/bin/activate
$ pip install -r requirements.txt
```

## Virtualenv

### Create

```shell
# virtualenvの作成
$ virtualenv --no-site-packages map_api
```

### Activate

```shell
# virtualenvへ環境を変更
$ source map_api/bin/activate
```

### Deactivate

```shell
# virtualenvから抜ける
$ deactivate
```
