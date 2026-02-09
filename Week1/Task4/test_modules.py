from modules.math_utils import add, divide
from modules.file_utils import write_file, read_file

print(add(5, 3))
print(divide(10, 2))

write_file("demo.txt", "Hello from modules!")
print(read_file("demo.txt"))
