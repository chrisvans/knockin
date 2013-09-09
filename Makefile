
check: check-pep8

PEP8=$(shell which pep8)
check-pep8:
ifneq ($(PEP8),)
	$(PEP8) --ignore=E128,E501 --repeat knockin/*.py padkey/*.py
else
	@echo "pep8 not found; skipping test"
endif
