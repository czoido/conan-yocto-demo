cmake_minimum_required(VERSION 2.8.12)
project(YoctoLedBlink)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(yocto_led main.cpp)
target_link_libraries(yocto_led ${CONAN_LIBS})