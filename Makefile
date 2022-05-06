dir_hw = src
dir_check = tools

node:
	npm install

lab01: node
	python ./$(dir_check)/check01.py

lab02: node
	python ./$(dir_check)/check02.py

lab03: node
	python ./$(dir_check)/check03.py

lab04: node
	python ./$(dir_check)/check04.py

lab05: node
	python ./$(dir_check)/check05.py

