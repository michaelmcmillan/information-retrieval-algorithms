TESTS="*_test.py"

test: 
	@python -B -m unittest discover -s test -p $(TESTS)

.PHONY: test
