import inspect

class DynamicCodeGenerator:
    def __init__(self, template):
        self.template = template
        self.generated_code = ""

    def generate_code(self, **kwargs):
        try:
            self.generated_code = self.template.format(**kwargs)
            return self.generated_code
        except KeyError as e:
            print(f"Błąd: Brakująca zmienna w szablonie - {e}")
            return None

    def validate_code(self):
        try:
            compiled_code = compile(self.generated_code, "<string>", "exec")
            return compiled_code is not None
        except SyntaxError as e:
            print(f"Błąd składniowy: {e}")
            return False

    def execute_code(self, function_name, *args):
        if not self.generated_code:
            print("Błąd: Kod nie został wygenerowany.")
            return None

        if not self.validate_code():
            print("Błąd: Kod zawiera błędy składniowe.")
            return None

        local_scope = {}
        exec(self.generated_code, {}, local_scope)

        if function_name in local_scope and inspect.isfunction(local_scope[function_name]):
            return local_scope[function_name](*args)
        else:
            print(f"Błąd: Funkcja {function_name} nie została znaleziona.")
            return None

template_code = """
def {function_name}({param}):
    return {expression}
"""

generator = DynamicCodeGenerator(template_code)


generated_code = generator.generate_code(function_name="dynamic_function", param="x", expression="x * 2 + 5")
print("Wygenerowany kod:\n", generated_code)

result = generator.execute_code("dynamic_function", 10)
print("Wynik wykonania funkcji:", result)
