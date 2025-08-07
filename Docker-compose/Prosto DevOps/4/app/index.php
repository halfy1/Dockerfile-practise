<?php
$host = 'db';      // Имя сервиса в docker-compose
$user = 'devuser'; // Имя пользователя из переменных окружения
$password = 'devpass'; // Пароль из переменных окружения
$db = 'test_db';   // Имя базы данных из переменных окружения

// Создаем соединение
$conn = new mysqli($host, $user, $password, $db);

// Проверяем соединение
if ($conn->connect_error) {
    die("Ошибка подключения к базе данных: " . $conn->connect_error);
}

echo "<h1>Веб-приложение с базой данных</h1>";
echo "<p>Успешное подключение к MySQL!</p>";

// Создание таблицы, если она не существует
$sql = "CREATE TABLE IF NOT EXISTS visitors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

if ($conn->query($sql) === TRUE) {
    echo "<p>Таблица visitors создана или уже существует.</p>";
} else {
    echo "<p>Ошибка создания таблицы: " . $conn->error . "</p>";
}

// Записываем информацию о новом посещении
$sql = "INSERT INTO visitors (visit_time) VALUES (NOW())";
$conn->query($sql);

// Получаем все записи о посещениях
$sql = "SELECT * FROM visitors ORDER BY visit_time DESC";
$result = $conn->query($sql);

echo "<h2>История посещений:</h2>";
echo "<table border='1'>";
echo "<tr><th>ID</th><th>Время посещения</th></tr>";

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"]. "</td><td>" . $row["visit_time"]. "</td></tr>";
    }
} else {
    echo "<tr><td colspan='2'>Нет записей о посещениях</td></tr>";
}

echo "</table>";

$conn->close();
?>