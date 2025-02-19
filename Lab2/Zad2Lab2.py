import numpy as np

class MatrixOperations:
    def __init__(self):
        self.matrices = {}

    def add_matrix(self, name, matrix):
        if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
            self.matrices[name] = np.array(matrix)
        else:
            raise ValueError("Niepoprawny format macierzy")

    def validate_operation(self, operation):
        try:
            exec(f"result = {operation}", {}, self.matrices.copy())
            return True
        except Exception as e:
            print(f"Błąd walidacji operacji: {e}")
            return False

    def execute_operation(self, operation):
        if self.validate_operation(operation):
            local_scope = self.matrices.copy()  
            exec(f"result = {operation}", {}, local_scope)
            return local_scope["result"]
        else:
            return None

mat_ops = MatrixOperations()

mat_ops.add_matrix("A", [[1, 2], [3, 4]])
mat_ops.add_matrix("B", [[5, 6], [7, 8]])

operation1 = "A + B"
operation2 = "A @ B"
operation3 = "A.T"

result1 = mat_ops.execute_operation(operation1)
result2 = mat_ops.execute_operation(operation2)
result3 = mat_ops.execute_operation(operation3)

print("Wynik dodawania macierzy:\n", result1)
print("Wynik mnożenia macierzy:\n", result2)
print("Transpozycja macierzy:\n", result3)
