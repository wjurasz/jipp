import numpy as np
from functools import reduce

class MatrixProcessor:
    def __init__(self, matrices):
        self.matrices = [np.array(m) for m in matrices]

    def apply_operation(self, operation):
        if not self.matrices:
            return None

        try:
            result = reduce(lambda x, y: eval(f"x {operation} y"), self.matrices)
            return result
        except Exception as e:
            print(f"Błąd w operacji: {e}")
            return None


matrices = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]


processor = MatrixProcessor(matrices)


operation1 = "+"  
operation2 = "@"  
result_sum = processor.apply_operation(operation1)
result_product = processor.apply_operation(operation2)

print("Suma macierzy:\n", result_sum)
print("Iloczyn macierzy:\n", result_product)
