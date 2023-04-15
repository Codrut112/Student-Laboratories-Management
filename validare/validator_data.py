class Validator_data:
    def __init__(self):
        pass
    def valideaza(self,data):
        '''
        verifica daaca o data este valida
        :param data: list
        :return: True daca data este valida
                 False daca data este invalida
        '''
        if data[0] < 1 or data[1] < 1 or data[2] < 1 or data[1] > 12:
            return False
        luni = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if data[2] % 4 == 0:
            luni[2] += 1

        if data[0] > luni[data[1]]:
            return False
        return True