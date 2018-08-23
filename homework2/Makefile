cover:
	make lint
	make cover_tests

lint: 
	flake8 --max-line-length=100 Tree Tests

cover_tests:
	py.test -s  --cov-config .coveragerc --cov Tree \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	Tests
