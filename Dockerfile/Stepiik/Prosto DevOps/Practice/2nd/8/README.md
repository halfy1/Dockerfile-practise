Rust CLI с продвинутыми инструкциями (SHELL, ARG, STOPSIGNAL)
В этом задании вы создадите Dockerfile для небольшого CLI-приложения на Rust. Задача — показать, как использовать SHELL, ARG, STOPSIGNAL и LABEL в одном образе.

Сценарий
Допустим, у вас есть Rust-приложение (файл main.rs), которое при запуске выводит информацию и обрабатывает входящие аргументы. При остановке контейнера вы хотите отправлять не стандартный сигнал SIGTERM, а SIGINT, чтобы Rust-приложение корректно завершалось.

Также вы хотите иметь ARG BUILD_MODE (например, debug или release), чтобы определять, как компилировать приложение. Плюс вы любите пользоваться bash вместо sh, поэтому настройте это через SHELL.

Техническое задание (ТЗ)
Базовый образ — rust:1.68 (или любая актуальная версия Rust).
ARG BUILD_MODE=debug:
Если BUILD_MODE=release, то компилируем cargo build --release.
Иначе компилируем cargo build (debug).
Добавьте RUN, который «выбирает» режим в зависимости от BUILD_MODE.

SHELL: Переключитесь на ["/bin/bash", "-c"], если хотите использовать команды bash (например, if/else логика в RUN).
Укажите SIGINT в качестве сигнала остановки.
LABEL: Укажите maintainer и version, чтобы в docker image inspect было понятно, кто отвечает за образ.
COPY Cargo.toml, Cargo.lock, main.rs (в папку /app) и компилируйте код. В итоге получите бинарник, скажем, /app/target/release/mycli или /app/target/debug/mycli.
CMD — пусть указывает на итоговый бинарник. Например, ["/app/target/debug/mycli"] (если BUILD_MODE=debug) или ["/app/target/release/mycli"] (если BUILD_MODE=release). Можно прописать это в RUN логике или через ENV. Или просто выбрать одно из двух на этапе сборки.
Итог:
При запуске контейнера (например, docker run --rm my-rust-cli) ваш CLI-приложение будет работать. Если вы сделаете docker stop, Docker пошлёт SIGINT, и приложение может корректно завершиться.
Если захотите собрать в релизном режиме:
docker build --build-arg BUILD_MODE=release -t my-rust-cli .
Тогда получатся оптимизированные бинарники (Cargo при release сам положит их в target/release).