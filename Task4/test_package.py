from mypackage import Calculator
from mypackage.logger import log_info

calc = Calculator()
result = calc.add(10, 5)

log_info(f"Addition result: {result}")
print("Result:", result)
