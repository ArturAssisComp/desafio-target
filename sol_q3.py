'''
Author: Artur Assis Alves
Date: 08/03/2023
Title: 
'''

'''
3) Dado um vetor que guarda o valor de faturamento diario de uma distribuidora, faca um programa, na linguagem que desejar, que calcule e retorne:
- O menor valor de faturamento ocorrido em um dia do mes; --> Os valores sem faturamento (0) nao serao ignorados, pois so foi requisitado que fossem ignorados para calculo da media.
- O maior valor de faturamento ocorrido em um dia do mes;
- Numero de dias no mes em que o valor de faturamento diario foi superior a media mensal.

IMPORTANTE:
a) Usar o json ou xml disponivel como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no calculo da media;
'''
import pandas as pd


class RevenueData(object):
    def __init__(self, data_filename):
        with open(data_filename, 'r') as f:
            splitted_filename = data_filename.rsplit(".")
            if len(splitted_filename) != 2: raise ValueError(f"Filename {data_filename} is invalid. It must be .json")
            extension = splitted_filename[1]
            if extension == 'json':
                df = pd.read_json(f.read())
            else:
                raise ValueError(f"Filename {data_filename} is invalid. It must be or .json")
        self.data_filename = data_filename
        self.min_revenue = min(df["valor"]) #OBS: 0's will not be ignored.
        self.max_revenue = max(df["valor"]) 
        self.mean_revenue = df[df["valor"]>0]["valor"].mean()
        self.num_of_days_with_revenue_greater_than_mean = df[df["valor"] > self.mean_revenue]["valor"].count()

    def summary(self):
        print(f"File: {self.data_filename}\nMin Revenue: {self.min_revenue}\nMax Revenue: {self.max_revenue}\nNumber of Days With Revenue Greater than Mean: {self.num_of_days_with_revenue_greater_than_mean} days")



if __name__=='__main__':
    print("\n\nResults:")
    RevenueData("data/dados.json").summary()
