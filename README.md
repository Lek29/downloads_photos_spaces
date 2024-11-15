# Скачивание фотографий с разных источников.

## Описание проекта.
Этот проект представляет собой скрипт на Python, который позволяет скачивать фотографии с различных источников, таких как SpaceX, NASA APOD (Astronomy Picture of the Day) и EPIC API. Скрипт использует API для получения ссылок на фотографии и сохраняет их в указанные директории.

## Установка
### Требования
* Python 3.6 или выше.
* Библиотеки: `requests`, `python-dotenv`.

### Установка зависимостей.
1.**Установите необходимые библиотеки:**
   - Убедитесь, что у вас установлен Python.
   - Установите зависимости с помощью файла `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
2. Создайте файл .env в корне проекта и добавьте ваш API-ключ NASA:
   ```
   API_KEY_NASA=ваш_api_ключ
   ```
### Клонирование репозитория.
Клонируйте репозиторий на ваш локальный компьютер:
```
git clone https://github.com/ваш_логин/ваш_репозиторий.git
cd ваш_репозиторий
```
## Использование.
1. Запустите скрипт:
  ```python
    python main.py
```
2. Скрипт выполнит следующие действия:

  * Скачает фотографии с последнего запуска SpaceX.

  * Скачает фотографии с Astronomy Picture of the Day (APOD) от NASA.

  * Скачает фотографии с EPIC API от NASA.

3. Скачанные фотографии будут сохранены в следующие директории:

  * nasa_apod_directory для фотографий APOD.

  * nasa_epic_directory для фотографий EPIC.

## Возможные ошибки и их решение.
**Ошибка: API_KEY_MISSING**
**Описание**: Если вы видите сообщение "API_KEY_MISSING", это означает, что API-ключ не был предоставлен.

**Решение**:

* Убедитесь, что вы добавили API-ключ в файл .env.

* Проверьте, что файл .env находится в корневой директории проекта.
**Ошибка: HTTPError**
  
**Решение**:

* Проверьте правильность URL и параметров запроса.

* Убедитесь, что API-ключ действителен и не истек.

**Ошибка: FileNotFoundError**
**Описание:** Если директория для сохранения файлов не существует и не может быть создана, вы можете увидеть ошибку FileNotFoundError.

**Решение:**

* Убедитесь, что у вас есть права на запись в указанную директорию.

* Проверьте путь к директории и исправьте его, если необходимо.
