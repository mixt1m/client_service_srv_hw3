cmake_minimum_required(VERSION 3.8)
project(string_validation_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

set(rosidl_generate_interfaces_DIR ${ament_cmake_DIR}/../share/rosidl_generate_interfaces/cmake)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Str.srv"
  DEPENDENCIES
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()