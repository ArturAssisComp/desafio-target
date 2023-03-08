'''
Author: Artur Assis Alves
Date: 08/03/2023
Title: 
'''

'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP - R$67.836,43
RJ - R$36.678,66
MG - R$29.229,88
ES - R$27.165,48
Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representacao que cada estado teve dentro do valor total mensal da distribuidora.
'''
import pandas as pd


class RevenueData(object):
    def __init__(self, data_str):
        tmp = {'state':[], 'revenue':[]}
        raw_data = data_str.split('\n')
        for el in raw_data:
            if el.strip():
                state, value = el.strip().split('-')
                tmp['state'].append(state.strip()) 
                tmp['revenue'].append(value.strip('R$ ').replace('.', '').replace(',','.')) 
        df = pd.DataFrame(data=tmp)
        df['revenue'] = df['revenue'].astype('float')
        total_revenue = df['revenue'].sum()
        df['%'] = df['revenue']/total_revenue * 100
        self.result = df

        

    def summary(self):
        print(self.result)



if __name__=='__main__':
    print("\n\nResults:")
    data_str = \
    '''
    SP - R$67.836,43
    RJ - R$36.678,66
    MG - R$29.229,88
    ES - R$27.165,48
    Outros - R$19.849,53
    '''
    RevenueData(data_str).summary()
