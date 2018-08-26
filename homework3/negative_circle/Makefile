cover:
	
	make cover_tests

lint: 
	flake8 --max-line-length=100 bellman_ford tests

cover_tests:
	py.test -s  --cov-config .coveragerc --cov bellman_ford \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	tests
