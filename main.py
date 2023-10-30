from Models.frequency import Frequencia

# Type : int = int(input(
#     '''
#     [1] Qualitative
#     [2] Quantitative
#     '''))
num : int = int(input('Length of the sample: '))

object_frequency = Frequencia("Teste")

object_frequency.RandomNumbers(num)
#object_frequency.Classes()