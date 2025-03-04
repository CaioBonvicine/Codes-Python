from numpy import cov, var, std, mean, sqrt, array


class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__coeficiente_correlação = self.__correlação()
        self.__inclination = self.__inclinação()
        self.__intercept = self.__interceptação()

    def __correlação(self):
        covariação = cov(self.x, self.y, bias=True)[0][1]
        variancia_x = var(self.x)
        variancia_y = var(self.y)
        return covariação / sqrt(variancia_x * variancia_y)

    def __inclinação(self):
        stdx = std(self.x)
        stdy = std(self.y)
        return self.__coeficiente_correlação * (stdy / stdx)

    def __interceptação(self):
        media_x = mean(self.x)
        media_y = mean(self.y)
        return media_y - media_x * self.__inclination

    def previsão(self, valor):
        return self.__intercept + (self.__inclination * valor)


class Principal:
    def __init__(self):
        self.nome = '__main__'

    def execução(self):

        vetorX = [0 for x in range(5)]
        for i in range(0, 5):
            vetorX[i] = int(input("Digite um número para X: "))

        vetorY = [0 for Y in range(5)]
        for i in range(0, 5):
            vetorY[i] = int(input("Digite um número um para Y: "))

        x = array([vetorX[0], vetorX[1], vetorX[2], vetorX[3], vetorX[4]])
        y = array([vetorY[0], vetorY[1], vetorY[2], vetorY[3], vetorY[4]])
        lr = LinearRegression(x, y)

        Z = int(input("Digite o número de X que deseja prever para Y: "))
        previsão = lr.previsão(Z)
        print(previsão)


if __name__ == '__main__':
    p = Principal()
    p.execução()
