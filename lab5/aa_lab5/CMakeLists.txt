cmake_minimum_required(VERSION 3.17)
project(aa_lab5)

find_package( Threads )
set(CMAKE_CXX_STANDARD 17)

add_executable(aa_lab5 main.cpp)
target_link_libraries( aa_lab5 ${CMAKE_THREAD_LIBS_INIT} )