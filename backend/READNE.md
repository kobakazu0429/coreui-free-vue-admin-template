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

## Databases

```sql
-- Create
CREATE DATABASE kure_kosen_map_api CHARACTER SET utf8mb4;

-- Drop
DROP DATABASE kure_kosen_map_api;
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

## Docs

### End Point

```plaintext
[GET]     /api/types/
[GET]     /api/groups/
[GET]     /api/categories/
[GET]     /api/formats/
[GET]     /api/attributes/
[GET]     /api/layers/
[GET]     /api/layers/<int:id>/

[POST]    /api/types/
[POST]    /api/groups/
[POST]    /api/categories/
[POST]    /api/formats/
[POST]    /api/attributes/
[POST]    /api/layers/

[PATCH]   /api/types/<int:id>/
[PATCH]   /api/groups/<int:id>/
[PATCH]   /api/categories/<int:id>/
[PATCH]   /api/formats/<int:id>/
[PATCH]   /api/attributes/<int:id>/
[PATCH]   /api/layers/<int:id>/

[DELETE]  /api/types/<int:id>/
[DELETE]  /api/groups/<int:id>/
[DELETE]  /api/categories/<int:id>/
[DELETE]  /api/formats/<int:id>/
[DELETE]  /api/attributes/<int:id>/
[DELETE]  /api/layers/<int:id>/
```
