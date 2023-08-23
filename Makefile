.PHONY: build

deps:
	pip install -r requirements.txt

build:
	pyinstaller labtool.spec

clean:
	rm -rf dist build