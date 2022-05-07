dir_hw = src
dir_chk_hw = tools

node:

hw01: node
	python ./$(dir_chk_hw)/chk_hw01.py

hw02: node
	python ./$(dir_chk_hw)/chk_hw02.py

hw03: node
	python ./$(dir_chk_hw)/chk_hw03.py

hw04: node
	python ./$(dir_chk_hw)/chk_hw04.py

hw05: node
	python ./$(dir_chk_hw)/chk_hw05.py

