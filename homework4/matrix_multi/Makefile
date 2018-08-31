cover:
	
	make cover_tests

lint: 
	flake8 --max-line-length=100 mat_multi tests

cover_tests:
	py.test -s  --cov-config .coveragerc --cov mat_multi \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	tests
