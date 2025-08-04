## 💥Настройка Nginx для статики и API-эндпоинта
В этой задаче вы создадите Dockerfile с собственным конфигурационным файлом Nginx, где будут одновременно раздаваться статические файлы и возвращаться простой JSON на заданном эндпоинте.

### Сценарий
Предположим, вы делаете небольшой фронтенд-проект (HTML, CSS, JS), а для теста хотите эмулировать работу API на том же домене. В итоге:
- Все файлы из /usr/share/nginx/html будут доступны по любым запросам, например, /index.html, /style.css, /script.js.
- Если пользователь обратится к пути /api, мы не отдадим статический файл, а вернём простую JSON-ответ (например, {"msg": "Hello from Nginx JSON!"}).

### Техническое задание
1. Базовый образ — nginx:alpine.
2. Создать собственный файл конфигурации (например, default.conf), где:
    - Задать server с listen 80;.
    - location / — раздаёт статику из /usr/share/nginx/html (директивы root или alias).
    - location /api — возвращает JSON-ответ с помощью return 200 '{"msg": "Hello from Nginx JSON!"}';. Не забудьте выставить заголовок Content-Type: application/json перед командой return.
3. Скопировать статические файлы (например, index.html, style.css, script.js) в /usr/share/nginx/html.
4. Скопировать свой конфиг default.conf в /etc/nginx/conf.d/default.conf.
5. EXPOSE 80, но CMD не нужно прописывать, поскольку в nginx:alpine уже задан старт Nginx.

### Итог 
При запуске контейнера (например, -p 8080:80), если зайти на http://localhost:8080, будет открываться ваш index.html. Если обратиться к http://localhost:8080/api, в ответ придёт JSON {"msg": "Hello from Nginx JSON!"}.

### Структура папки
- `Dockerfile` — вы создаёте по требованиям выше.
- `default.conf` — ваш Nginx-конфиг.
- `index.html, style.css, script.js` — любые файлы, которые вы хотите раздавать.