HOST_PYTHON=$(shell which python3.8 || which python3.7 || which python3.6)
VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

OK_VENV=.venv
OK_PIP=.ok_pip
OK_REQ=.ok_reqs


all: $(OK_REQ)

clean: 
	rm -f .ok_*

envclean: clean
	rm -rf $(VENV)
	rm -rf __pycache__

run:
	$(PYTHON) app.py

$(OK_VENV):
	$(HOST_PYTHON) -m venv .venv && touch $@

$(OK_PIP): $(OK_VENV)
	$(PIP) install --upgrade pip && touch $@

$(OK_REQ): $(OK_PIP) requirements.txt
	$(PIP) install -r requirements.txt && touch $@
