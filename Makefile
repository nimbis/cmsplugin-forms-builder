
.PHONY: travis-tests test pep8 clean coverage doc check-venv

# clean out potentially stale pyc files
clean:
	@find . -name "*.pyc" -exec rm {} \;

# check that virtualenv is enabled
check-venv:
ifndef VIRTUAL_ENV
	$(error VIRTUAL_ENV is undefined, try "workon" command)
endif

# Install pip requirements.txt file
reqs: check-venv
	pip install -r requirements.txt

PEP8_OPTS=--repeat --exclude=static,migrations,south_migrations,js,doc --show-source
pep8:
	pycodestyle $(PEP8_OPTS) .

#
# flake8
#

FLAKE8_OPTS=--exclude=static,migrations,south_migrations,js,doc,travis_*
flake8: check-venv
	flake8 $(FLAKE8_OPTS) .

#
# unit tests
#

test: check-venv clean
	./manage.py test

#
# code coverage
#

COVERAGE_ARGS=--source=cmsplugin_forms_builder --omit=cmsplugin_forms_builder/tests.py
coverage:
	coverage erase
	-coverage run $(COVERAGE_ARGS) ./manage.py test
	coverage report
	coverage html
	@echo "See ./htmlcov/index.html for coverage report"

#
# TravisCI
#

travis-tests: check-venv
	@echo "travis_fold:start:flake8"
	make flake8
	@echo "travis_fold:end:flake8"

	@echo "travis_fold:start:pip_freeze"
	pip freeze -l
	@echo "travis_fold:end:pip_freeze"

	coverage erase
	@echo "travis_fold:start:test"
	coverage run $(COVERAGE_ARGS) ./manage.py test --keepdb -v 2
	@echo "travis_fold:end:test"

	@echo "travis_fold:start:coverage"
	coverage report
	coverage html
	@echo "travis_fold:end:coverage"
