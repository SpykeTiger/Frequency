import unittest
from Models.frequency import Frequency

class TesteFrequency:
    def teste_classe(self):
        obj = Frequency("Valor")
        resultado = obj.Classes()
        self.assertEqual(resultado, "Resultado esperado metódo 1")

    def teste_metodo2(self):
        pass


if __name__ == '__main__':
    unittest.main()

#python -m unittest discover testes