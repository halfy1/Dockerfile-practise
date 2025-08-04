## 💥 Nginx с базовой авторизацией (Basic Auth)

В этом задании вы создадите Dockerfile для Nginx, где часть ресурсов будет защищена базовой авторизацией. При попытке доступа к защищённому пути сервер попросит ввести логин и пароль, указанные в htpasswd-файле.

### Сценарий

Допустим, вы хотите раздавать статический контент (например, index.html) публично, но путь /protected должен быть доступен только авторизованным пользователям. При обращении к /protected без корректных учётных данных сервер вернёт ошибку авторизации (401 Unauthorized).

### Техническое задание (ТЗ)

1. Базовый образ — nginx:alpine.
2. Скопировать ваш статический файл (index.html) в /usr/share/nginx/html. (Например, index.html может содержать «Welcome to public page».)
3. Создать в локальной папке файл default.conf, где:
    - listen 80;
    - location / раздаёт статику (укажите root или alias в /usr/share/nginx/html).
    - location /protected включает базовую авторизацию:
    ```bash
    auth_basic "Restricted Content";
    auth_basic_user_file /etc/nginx/htpasswd;
    ```
    И, например, просто return 200 "Protected resource!"; (или что-то подобное).
4. Скопировать локальный default.conf в /etc/nginx/conf.d/default.conf.
5. Создать файл htpasswd (лежит рядом с Dockerfile), где прописан логин/пароль в формате, распознаваемом Nginx. Например, с помощью команды (в Linux/Mac):
    ```bash
    htpasswd -cb htpasswd admin admin123
    ```
    Тогда в файле htpasswd будет что-то вроде:
    ```bash
    admin:$apr1$qf...$...
    ```
6. Скопировать этот htpasswd файл в /etc/nginx/htpasswd.
7. EXPOSE 80 (порт для Nginx).
8. Не нужно прописывать CMD, так как в базовом образе уже указано, как запускать Nginx.

### Итог 

При запуске контейнера (например, -p 8080:80), http://localhost:8080 будет отдавать index.html, а при обращении к http://localhost:8080/protected сервер потребует ввести логин admin и пароль admin123. Если авторизация корректна — вернёт «Protected resource!», иначе 401 Unauthorized.

### Структура папки
- `Dockerfile` — вы создаёте по ТЗ.
- `default.conf` — ваш Nginx-конфиг, где прописаны location / и location /protected c базовой авторизацией.
- `htpasswd` — файл с логином и паролем в формате, поддерживаемом Nginx.
- `index.html` — ваш статический файл (например, «Welcome to public page!»).