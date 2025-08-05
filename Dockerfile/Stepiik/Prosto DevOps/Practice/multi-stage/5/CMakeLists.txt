cmake_minimum_required(VERSION 3.10)
project(cpp_docker_demo)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(cpp_app src/main.cpp)

install(TARGETS cpp_app DESTINATION bin)