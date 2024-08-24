install:	 # Эта команда полезна при первом клонировании репозитория или после удаления зависимостей
	poetry install

brain-games:
	poetry run brain-games

build:		 # Сборка пакета
	poetry build

publish:	 # Публикация пакета
	poetry publish --dry-run

package-install: # Установка пакета в окружение пользователя
	python3 -m pip install --user dist/*.whl
