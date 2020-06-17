from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from random import randint

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outubro',
            'Novembro',
            'Dezembro',
        ]
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets"""
        datasets = [
            'Programação para Leigos',
            'Algoritmos e Lógica de Programação',
            'Programação em C',
            'Programação em Java',
            'Programação em Python',
            'Banco de Dados'
        ]
        return datasets

    def get_data(self):
        """
        Retorna 6 datasets para plotar o gráfico.

        Cada linha representa um dataset;
        Cada coluna representa um label.

        A quantidade de dados precisa ser  igual aos datasets/labels

        12 labels, então 12 colunas;
        6 datasets, logo 6 linhas.
        """

        dados = []
        for c in range(6):
            for l in range(12):
                dado = [
                    randint(1, 200),  # Jan
                    randint(1, 200),  # Fev
                    randint(1, 200),  # Mar
                    randint(1, 200),  # Abr
                    randint(1, 200),  # Mai
                    randint(1, 200),  # Jun
                    randint(1, 200),  # Jul
                    randint(1, 200),  # Ago
                    randint(1, 200),  # Set
                    randint(1, 200),  # Out
                    randint(1, 200),  # Nov
                    randint(1, 200),  # Dez
                ]
            dados.append(dado)
        return dados