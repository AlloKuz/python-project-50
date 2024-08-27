### Hexlet tests and linter status:
[![Actions Status](https://github.com/AlloKuz/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AlloKuz/python-project-50/actions)
[![Python CI](https://github.com/AlloKuz/python-project-50/actions/workflows/build.yaml/badge.svg)](https://github.com/AlloKuz/python-project-50/actions/workflows/build.yaml)
<a href="https://codeclimate.com/github/AlloKuz/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/cc4fcd2766c14da697a0/maintainability" /></a>
<a href="https://codeclimate.com/github/AlloKuz/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/cc4fcd2766c14da697a0/test_coverage" /></a>

# Генератор отличий

Программа позволяет пользователю получить различия двух json или yaml файлов, и вывести их на печать или в json формат.

# Установка и запуск

```bash
make install

make gendiff
```

# Аргументы командной строки

`gendiff filepath1 filepath2 [-f json|plain|stylish]`

Где:
* `filename{1,2}` -- пути до файлов

* `-f`, `--format` [json/plain/stylish] -- формат вывода различий


### Example:

<a href="https://asciinema.org/a/sugv4onehOrZRP0OWerMCzkWN" target="_blank"><img src="https://asciinema.org/a/sugv4onehOrZRP0OWerMCzkWN.svg" /></a>
