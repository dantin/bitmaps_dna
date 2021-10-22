.PHONY: test
test:
	@echo "Run unit tests"
	@tox

.PHONY: clean
clean:
	@echo "Clean temp files"
	@rm -f *.log
	@rm -rf htmlcov/
	@rm -rf xgen.egg-info/
	@rm -rf dist/
	@find . -type d -path ./.tox -prune -false -o -name '__pycache__' -print0 | xargs -0 rm -rf

.PHONY: dist
dist:
	@python setup.py sdist
