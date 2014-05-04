doc:
	python -c 'import pypandoc; print pypandoc.convert("README.md", "rst")' > README.rst

register: doc
	python setup.py register

upload: doc
	python setup.py sdist upload
