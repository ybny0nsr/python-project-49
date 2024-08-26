install:	 # Первое клонирование репозитория или восстановление зависимостей
	poetry install

brain-games:
	poetry run brain-games

build:		 # Сборка пакета
	poetry build

publish:	 # Публикация пакета
	poetry publish --dry-run

package-install: # Установка пакета в окружение пользователя
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:		# Линтер
	poetry run flake8 brain_games
