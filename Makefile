VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
SRC = markdown
DESTDIR = docs
TEMPLATE = scripts/document.py

build: $(TEMPLATE)
	DESTDIR=$(DESTDIR) $(PYTHON) $(TEMPLATE) $(SRC)/*

run: $(VENV)/bin/activate
	$(PYTHON) -m httpmdhtml.server -d docs --css_file styles/weg51005.css

setup: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	$(RM) -rf __pycache__
	$(RM) -rf $(VENV)
