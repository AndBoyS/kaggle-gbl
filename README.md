Создание виртуальной среды

```shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Обновление зависимостей

```shell
pip freeze > requirements.in
pip-compile requirements.in
```