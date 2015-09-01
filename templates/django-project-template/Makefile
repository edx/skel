NODE_BIN=./node_modules/.bin
PROJECT_NAME={{ project_name }}

clean:
	find . -name '*.pyc' -delete
	coverage erase
	rm -rf assets coverage $(PROJECT_NAME)/static/build

requirements_js:
	npm install
	$(NODE_BIN)/bower install

requirements: requirements_js
	pip install -qr requirements/local.txt --exists-action w

validate_js:
	rm -rf coverage
	$(NODE_BIN)/gulp test
	$(NODE_BIN)/gulp lint
	$(NODE_BIN)/gulp jscs

validate_python: clean
	python manage.py compress --settings=$(PROJECT_NAME).settings.test -v0
	DISABLE_MIGRATIONS=True coverage run --branch --source=$(PROJECT_NAME) ./manage.py test $(PROJECT_NAME) \
	--settings=$(PROJECT_NAME).settings.test --with-ignore-docstrings --logging-level=DEBUG
	coverage report
	make quality

quality:
	pep8 --config=.pep8 $(PROJECT_NAME)
	pylint --rcfile=pylintrc $(PROJECT_NAME)

validate: validate_python validate_js

static:
	$(NODE_BIN)/r.js -o build.js
	python manage.py collectstatic --noinput -v0
	python manage.py compress -v0

html_coverage:
	coverage html && open htmlcov/index.html

extract_translations:
	cd $(PROJECT_NAME) && i18n_tool extract -v

dummy_translations:
	cd $(PROJECT_NAME) && i18n_tool dummy -v

compile_translations:
	cd $(PROJECT_NAME) && i18n_tool generate -v

fake_translations: extract_translations dummy_translations compile_translations

pull_translations:
	cd $(PROJECT_NAME) && tx pull -a

update_translations: pull_translations fake_translations

.PHONY: clean compile_translations dummy_translations fake_translations html_coverage pull_translations quality \
	requirements requirements_js static update_translations validate validate_js validate_python
