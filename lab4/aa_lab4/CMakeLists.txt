cmake_minimum_required(VERSION 3.17)
project(untitled6)

find_package( Threads )
set(CMAKE_CXX_STANDARD 17)

add_executable(untitled6 main.cpp)
target_link_libraries( untitled6 ${CMAKE_THREAD_LIBS_INIT} )