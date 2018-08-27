cover:
	make cover_tests

lint: 
	flake8 --max-line-length=100 dijkstra tests

cover_tests:
	py.test -s  --cov-config .coveragerc --cov dijkstra \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	tests
