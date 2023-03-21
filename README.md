# nam-model-center

This project is **DEPRECATED** in favor of: [ToneStack](https://github.com/avanzzzi/tonestack)

A central repository for Neural Amp Modeler (NAM) Models.

This service aims to be a place that allows the users to:
* Browse existing Neural Amp Modeler models.
* Download existing Neural Ammp Modeler models.
* Upload and share your own models.
* Keep private models.
* Search Neural Amp Models by metadata.

## Development

* Flask
* SQLAlchemy (sqlite/postgresql)
* mongodb
* Docker
* Jinja Templates (early)
* React

## Installation

clone:
```
$ git clone https://github.com/avanzzzi/nam-model-center
$ cd nam-model-center
```
with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```
init database then run:
```
$ flask initdb
$ gunicorn "nmc:create_app()" --bind localhost:5000 --workers=3 --log-level INFO
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
