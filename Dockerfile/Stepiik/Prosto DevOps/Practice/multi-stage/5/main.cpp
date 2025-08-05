#include <iostream>
#include <vector>
#include <string>
#include <ctime>

int main() {
    std::cout << "=== C++ Application ===" << std::endl;
    
    // Показать текущее время
    time_t now = time(0);
    std::string dt = ctime(&now);
    std::cout << "Текущее время: " << dt << std::endl;
    
    // Демонстрация работы с вектором
    std::vector<std::string> messages = {
        "Это приложение собрано с использованием multi-stage Docker сборки",
        "Финальный образ не содержит компилятора GCC и инструментов сборки",
        "Размер образа значительно меньше, чем при использовании единого образа"
    };
    
    std::cout << "Информация:" << std::endl;
    for (size_t i = 0; i < messages.size(); ++i) {
        std::cout << " - " << messages[i] << std::endl;
    }
    
    std::cout << "\nПриложение успешно запущено!" << std::endl;
    return 0;
}