# These targets are not files
.PHONY: install clean

install:
	pip install -r requirements.txt

clean:
	# Remove media
	find . -name "*.pyc" -exec rm -rf {} \;
