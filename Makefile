
check: check-pep8 check-tests

PEP8=$(shell which pep8)
check-pep8:
ifneq ($(PEP8),)
	$(PEP8) --ignore=E128,E501 --repeat knockin/*.py padkey/*.py
else
	@echo "pep8 not found; skipping test"
endif

COVERAGE=$(shell which coverage)
check-tests:
ifneq ($(COVERAGE),)
	$(COVERAGE) run manage.py test --settings=knockin.test
else
	@echo "coverage not found; skipping tests"
endif

.PHONY : htmlcov
htmlcov: check-tests
ifneq ($(COVERAGE),)
	$(COVERAGE) html \
                    --include="../knockin*" \
                    --omit="*/migrations*","*/knockin/tests*","*/padkey/tests*"
else
	@echo "html coverage reports not generated!"
endif
