import re


def safe_calculator(func):
    def wrapper(expression):
        # Разрешенные символы: цифры, пробелы, операторы + - * / ( )
        if not re.fullmatch(r'[0-9+\-*/(). ]+', expression):
            return "Ошибка: Некорректные символы в выражении!"

        try:
            result = func(expression)
            return result
        except ZeroDivisionError:
            return "Ошибка: Деление на ноль!"
        except SyntaxError:
            return "Ошибка: Неверное выражение!"
        except Exception as e:
            return f"Ошибка: {e}"

    return wrapper


@safe_calculator
def calculate(expression):
    return eval(expression)  # Используем eval, но с проверкой


# Тестируем калькулятор
expressions = ["10 + 20", "100 / 0", "abc", "2 ** 3", "5 + (2 * 3)", "10 / (5 - 5)"]
for exp in expressions:
    print(f"{exp} = {calculate(exp)}")