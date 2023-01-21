import os
import random
import sys
from itertools import islice
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui


class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.init()
        self.show()

    def create_sub_menu(self):  # Função criar sub-menus
        ###########################
        # Menu de Pilotos
        ###########################

        self.subMenuPilotos = QAction('Pilotos', self)
        self.subMenuPilotos.triggered.connect(self.pilotos)
        self.subMenuPilotos.setIcon(QIcon("Imagens/capacete.png"))

        self.subMenuPilotosPais = QAction('Pilotos por País', self)
        self.subMenuPilotosPais.triggered.connect(self.pilotos_pais)
        self.subMenuPilotosPais.setIcon(QIcon("Imagens/globo.png"))

        self.subMenuPilotosEquipa = QAction('Pilotos por Equipa', self)
        self.subMenuPilotosEquipa.triggered.connect(self.pilotos_equipa)
        self.subMenuPilotosEquipa.setIcon(QIcon("Imagens/team.png"))

        self.Pilotos_menu.addAction(self.subMenuPilotos)
        self.Pilotos_menu.addAction(self.subMenuPilotosPais)
        self.Pilotos_menu.addAction(self.subMenuPilotosEquipa)

        ###########################
        # Menu de Circuitos
        ###########################

        self.subMenuCircuitos = QAction('Circuitos', self)
        self.subMenuCircuitos.triggered.connect(self.circuitos)
        self.subMenuCircuitos.setIcon(QIcon("Imagens/circuito.png"))

        self.subMenuCircuitoPais = QAction('Circuitos por País', self)
        self.subMenuCircuitoPais.triggered.connect(self.circuitos_pais)
        self.subMenuCircuitoPais.setIcon(QIcon("Imagens/globo.png"))

        self.Circuitos_menu.addAction(self.subMenuCircuitos)
        self.Circuitos_menu.addAction(self.subMenuCircuitoPais)

        ###############################
        # Menu de Grande Prémio
        ###############################

        self.subMenuCircuitoRealizarGP = QAction('Escolher Circuito', self)

        fonte_circuitos = open("Ficheiros/Circuito_2022.txt", 'r')
        circuitos = {}
        for c in islice(fonte_circuitos, 1, None):
            circuito = c.strip().split(',')
            circuitos[circuito[0]] = [circuito[1], circuito[2]]
        fonte_circuitos.close()

        for item in circuitos:
            self.subMenuCircuito_menu.addAction(item)

        self.subMenuVencedoresPorGP = QAction('Os 10 primeiros Pilotos do último GP', self)
        self.subMenuVencedoresPorGP.triggered.connect(self.dez_primeiros_gp)
        self.subMenuVencedoresPorGP.setIcon(QIcon("Imagens/vencedor.png"))

        self.subMenuTresPrimeirosPorGP = QAction('Os 3 primeiros Pilotos de cada GP', self)
        self.subMenuTresPrimeirosPorGP.triggered.connect(self.tres_primeiros_gp)
        self.subMenuTresPrimeirosPorGP.setIcon(QIcon("Imagens/top3.png"))

        self.subMenuTresMelhoresEquipasPorGP = QAction('As 3 melhores equipas dos GP', self)
        self.subMenuTresMelhoresEquipasPorGP.triggered.connect(self.tres_melhores_equipas_gp)
        self.subMenuTresMelhoresEquipasPorGP.setIcon(QIcon("Imagens/equipas.png"))

        self.subMenuClassificacaoGeralPorGP = QAction('Classificação Geral Campeonato - Pilotos', self)
        self.subMenuClassificacaoGeralPorGP.triggered.connect(self.classificacao_geral_gp_pilotos)
        self.subMenuClassificacaoGeralPorGP.setIcon(QIcon("Imagens/ranking.png"))

        self.subMenuClassificacaoGeralEquipasPorGP = QAction('Classificação Geral Campeonato - Equipas', self)
        self.subMenuClassificacaoGeralEquipasPorGP.triggered.connect(self.classificacao_geral_gp_equipas)
        self.subMenuClassificacaoGeralEquipasPorGP.setIcon(QIcon("Imagens/ranking.png"))

        self.GrandePremio_menu.addAction(self.subMenuVencedoresPorGP)
        self.GrandePremio_menu.addAction(self.subMenuTresPrimeirosPorGP)
        self.GrandePremio_menu.addAction(self.subMenuTresMelhoresEquipasPorGP)
        self.GrandePremio_menu.addAction(self.subMenuClassificacaoGeralPorGP)
        self.GrandePremio_menu.addAction(self.subMenuClassificacaoGeralEquipasPorGP)

        self.subMenuCircuito_menu.triggered.connect(self.grande_premio)

        ###########################
        # Menu de Campeonato MotoGP
        ###########################

        self.subMenuRealizarCampeonato = QAction('Realizar Campeonato', self)
        self.subMenuRealizarCampeonato.triggered.connect(self.realizar_campeonato)
        self.subMenuRealizarCampeonato.setIcon(QIcon("Imagens/bandeira.png"))

        self.subMenuDezPrimeirosCampeonato = QAction('Os 10 primeiros Pilotos do Campeonato', self)
        self.subMenuDezPrimeirosCampeonato.triggered.connect(self.dez_primeiros_campeonato)
        self.subMenuDezPrimeirosCampeonato.setIcon(QIcon("Imagens/top10.png"))

        self.subMenuTresPrimeirosGP = QAction('Os 3 primeiros Pilotos de cada GP', self)
        self.subMenuTresPrimeirosGP.triggered.connect(self.tres_primeiros_campeonato)
        self.subMenuTresPrimeirosGP.setIcon(QIcon("Imagens/top3.png"))

        self.subMenuTresMelhoresEquipas = QAction('As 3 melhores equipas do Campeonato', self)
        self.subMenuTresMelhoresEquipas.triggered.connect(self.tres_melhores_equipas_campeonato)
        self.subMenuTresMelhoresEquipas.setIcon(QIcon("Imagens/equipas.png"))

        self.subMenuClassificacaoGeral = QAction('Classificação Geral Campeonato - Pilotos', self)
        self.subMenuClassificacaoGeral.triggered.connect(self.classificacao_geral_campeonato_pilotos)
        self.subMenuClassificacaoGeral.setIcon(QIcon("Imagens/ranking.png"))

        self.subMenuClassificacaoGeralEquipas = QAction('Classificação Geral Campeonato - Equipas', self)
        self.subMenuClassificacaoGeralEquipas.triggered.connect(self.classificacao_geral_campeonato_equipas)
        self.subMenuClassificacaoGeralEquipas.setIcon(QIcon("Imagens/ranking.png"))

        self.Campeonato_menu.addAction(self.subMenuRealizarCampeonato)
        self.Campeonato_menu.addAction(self.subMenuDezPrimeirosCampeonato)
        self.Campeonato_menu.addAction(self.subMenuTresPrimeirosGP)
        self.Campeonato_menu.addAction(self.subMenuTresMelhoresEquipas)
        self.Campeonato_menu.addAction(self.subMenuClassificacaoGeral)
        self.Campeonato_menu.addAction(self.subMenuClassificacaoGeralEquipas)

        self.Fechar_aplicacao = QAction('Terminar Aplicação', self)
        self.Fechar_aplicacao.triggered.connect(self.sair)
        self.Fechar_aplicacao.setIcon(QIcon("Imagens/sair.png"))

        self.Sair_menu.addAction(self.Fechar_aplicacao)

    def create_menubar(self):  # Função criar barra de menus
        self.menu_bar = self.menuBar()
        self.Pilotos_menu = self.menu_bar.addMenu('Pilotos')
        self.Circuitos_menu = self.menu_bar.addMenu('Circuitos')
        self.GrandePremio_menu = self.menu_bar.addMenu('Grande Prémio')
        self.subMenuCircuito_menu = self.GrandePremio_menu.addMenu('Realizar GP')
        self.Campeonato_menu = self.menu_bar.addMenu('Campeonato')
        self.Sair_menu = self.menu_bar.addMenu('Sair')
        self.create_sub_menu()

    ###################################
    # Funções Menu de Campeonato MotoGP
    ###################################

    def pilotos(self):  # Função Pilotos
        print("\nLista de Pilotos MotoGP\n")
        # Importar ficheiro txt para o pandas DataFrame
        df = pd.read_csv("Ficheiros/Pilotos_2022.txt", sep=",")
        # Mostrar Pandas DataFrame
        print(df.to_string(index=False))

    def pilotos_pais(self):  # Função Pilotos por País
        print("\nLista de Pilotos MotoGP por País\n")
        df = pd.read_csv("Ficheiros/Pilotos_2022.txt", sep=",")
        PilotosPais = df.groupby("País")
        for Pais, Piloto in PilotosPais:
            print("=" * 80)
            print("País: "f"{Pais}")
            print("=" * 80)
            print(f" {Piloto!r}\n")

    def pilotos_equipa(self):  # Função Pilotos por Equipa
        print("\nLista de Pilotos MotoGP por Equipa\n")
        df = pd.read_csv("Ficheiros/Pilotos_2022.txt", sep=",")
        PilotosEquipa = df.groupby("Equipa")
        for Equipa, Piloto in PilotosEquipa:
            print("=" * 80)
            print("Equipa: "f"{Equipa}")
            print("=" * 80)
            print(f" {Piloto!r}\n")

    ###################################
    # Funções Menu de Circuito
    ###################################

    def circuitos(self):  # Função Circuitos
        print("\nLista de Circuitos\n")
        # Importar ficheiro txt para o pandas DataFrame
        df = pd.read_csv("Ficheiros/Circuito_2022.txt", sep=",")
        # Mostrar Pandas DataFrame
        print(df.to_string(index=False))

    def circuitos_pais(self):  # Função Circuitos por País
        print("\nLista de Circuitos MotoGP por País\n")
        df = pd.read_csv("Ficheiros/Circuito_2022.txt", sep=",")
        CircuitoPais = df.groupby("Pais")
        for Pais, Circuito in CircuitoPais:
            print("=" * 80)
            print("País: "f"{Pais}")
            print("=" * 80)
            print(f" {Circuito!r}\n")

    ###################################
    # Funções Menu de Grande Prémio
    ###################################

    def grande_premio(self, q):  # Função Realizar GP
        print('Realização do GP de ', q.text())
        fonte_pilotos = open("Ficheiros/Pilotos_2022.txt", 'r')
        fonte_pontos = open("Ficheiros/Pontos_2022.txt", 'r')
        pilotos = {}
        pontos = {}

        for x in islice(fonte_pilotos, 1, None):
            piloto = x.strip().split(',')
            pilotos[piloto[1]] = [piloto[0], piloto[2], piloto[3], piloto[4]]
        fonte_pilotos.close()

        for p in islice(fonte_pontos, 1, None):
            ponto = p.strip().split(',')
            pontos[ponto[0]] = ponto[1]
        fonte_pontos.close()

        resultados_gp = {}
        classificacaoFinal_gp = []
        classificacao_gp = []

        replica_pilotos = list(pilotos)
        i = 1
        while replica_pilotos:
            try:
                pontuacao = int(pontos[str(i)])
            except:
                pontuacao = 0
            piloto = random.choice(replica_pilotos)
            replica_pilotos.remove(piloto)
            piloto_pontuacao = [piloto, pontuacao]
            classificacao_gp.append(piloto_pontuacao)
            i += 1
            classificacaoFinal_gp.append(piloto_pontuacao)
        resultados_gp[q.text()] = classificacao_gp

        print(resultados_gp)
        d = resultados_gp

        if os.path.exists("Output/GP.txt"):
            df = pd.read_csv("Output/GP.txt", sep=",")
            if len(df.axes[1]) == 0:
                df = pd.DataFrame(data=d)
            else:
                print(len(df.axes[1]))
                i = 0
                for j in range(0, len(df.axes[1])):
                    i += 1
                df.insert(j, q.text(), d, True)
        else:
            df = pd.DataFrame(data=d)

        df[q.text()] = classificacao_gp
        print(df)
        # Criação do ficheiro de resultados dos circuitos do Campeonato MotoGP gerado
        df.to_csv('Output/GP.txt', header=True, index=False, sep=',', mode='w')
        # Criação do ficheiro de resultados dos pilotos Campeonato MotoGP gerado
        df = pd.DataFrame(data=classificacaoFinal_gp)
        headerList = ['Piloto', 'Pontos']
        df.to_csv('Output/GPClassificacoesPilotos.txt', header=headerList, index=False, sep=',',
                  mode='w')

        df = pd.read_csv("Output/GPClassificacoesPilotos.txt")
        df = df.groupby(['Piloto'])['Pontos'].sum()
        df = df.reset_index()
        df = df.sort_values(by='Pontos', ascending=False)
        df = df.reset_index()
        df['Piloto'] = df['Piloto'].str[:-1]
        headerList = ['Classificação', 'Piloto', 'Pontos']
        df.to_csv('Output/GPClassificacoesFinalPilotos.txt', header=headerList, index=False, sep=',',
                  mode='w')

        df = pd.read_csv("Output/GPClassificacoesFinalPilotos.txt")
        for j in range(0, len(df) + 1):
            df.iloc[j - 1, [0]] = [j]
            df.to_csv('Output/GPClassificacoesFinalPilotos.txt', header=headerList, index=False,
                      sep=',',
                      mode='w')

        # Classificação das Equipas por Circuito
        df = pd.read_csv("Output/GPClassificacoesPilotos.txt")
        equipas = pd.read_csv("Ficheiros/Pilotos_2022.txt", sep=",")
        ClassificacaoEquipa_gp = []
        for index, row in df.iterrows():
            EquipaPiloto = str(row['Piloto'])
            Equipa = equipas.loc[equipas['Piloto'] == EquipaPiloto, 'Equipa'].item()
            ClassificacaoEquipa_gp.append([Equipa, row['Pontos']])

        df = pd.DataFrame(data=ClassificacaoEquipa_gp)
        headerList = ['Equipa', 'Pontos']
        df.to_csv('Output/GPClassificacoesEquipas.txt', header=headerList, index=False, sep=',',
                  mode='w')

        # Classificação das Finais das Equipas
        df = pd.read_csv("Output/GPClassificacoesEquipas.txt")
        df = df.groupby(['Equipa'])['Pontos'].sum()
        df = df.reset_index()
        df = df.sort_values(by='Pontos', ascending=False)
        df = df.reset_index()

        headerList = ['Classificação', 'Equipa', 'Pontos']
        df.to_csv('Output/GPClassificacoesFinalEquipas.txt', header=headerList, index=False, sep=',',
                  mode='w')

        df = pd.read_csv("Output/GPClassificacoesFinalEquipas.txt")
        for j in range(0, len(df) + 1):
            df.iloc[j - 1, [0]] = [j]
            df.to_csv('Output/GPClassificacoesFinalEquipas.txt', header=headerList, index=False,
                      sep=',',
                      mode='w')

        print("\n\n GP", q.text(), "gerado com Sucesso! \n")
        fonte_pilotos.close()
        fonte_pontos.close()

    def dez_primeiros_gp(self):  # Função 10 primeiros Pilotos do(s) gerado(s)
        if os.path.exists("Output/GPClassificacoesFinalPilotos.txt") == False:
            print(
                "\nERRO: Tem de realizar pelo menos 1 GP antes de obter a Lista dos 10 primeiros classificados dos GP!!!\n")
        else:
            print("\n\nLista dos 10 Pilotos primeiros do último GP realizado\n")
            data = pd.read_csv("Output/GPClassificacoesFinalPilotos.txt")
            print(data.head(n=10).to_string(index=False))

    def tres_primeiros_gp(self): # Função 3 primeiros Pilotos do(s) gerado(s) em cada GP
        if os.path.exists("Output/GP.txt") == False:
            print(
                "\nERRO: Tem de realizar pelo menos 1 GP antes de obter a Lista dos 3 primeiros classificados por Circuito!!!\n")
        else:
            print("\n\nLista dos 3 Pilotos Vencedores de GP realizados\n")
            dataframe_collection = {}
            data = pd.read_csv("Output/GP.txt")

            for col in data.columns:
                new_data = [data.iloc[0][col] + " » 1º Classificado", data.iloc[1][col] + " » 2º Classificado",
                            data.iloc[2][col] + " » 3º Classificado"]
                dataframe_collection[col] = pd.DataFrame(new_data, columns=["Classificação Final"])

            for key in dataframe_collection.keys():
                print("\n" + "=" * 80)
                print("Top 3 do Circuito " + key)
                print("=" * 80)
                print(dataframe_collection[key].to_string(index=False))

    def tres_melhores_equipas_gp(self): # Função 3 melhores equipas do(s) gerado(s)
        if os.path.exists("Output/GPClassificacoesFinalEquipas.txt") == False:
            print(
                "\nERRO: Tem de realizar pelo menos 1 GP antes de obter a Lista das 3 primeiras Equipas por GP!!!\n")
        else:
            print("\n\nLista 3 primeiras Equipas dos GP realizados\n")
            data = pd.read_csv("Output/GPClassificacoesFinalEquipas.txt")
            print(data.head(n=3).to_string(index=False))

    def classificacao_geral_gp_pilotos(self): # Função Classificação Geral de Pilotos do(s) gerado(s)
        if os.path.exists("Output/GPClassificacoesFinalPilotos.txt") == False:
            print(
                "\nERRO: Tem de realizar pelo menos 1 GP antes de obter a Lista da Classificação de Pilotos dos GP realizados\n")
        else:
            print("\nClassificação Geral Pilotos dos GP realizados\n")
            data = pd.read_csv("Output/GPClassificacoesFinalPilotos.txt")
            print(data.to_string(index=False))

    def classificacao_geral_gp_equipas(self): # Função Classificação Geral de Equipas do(s) gerado(s)
        if os.path.exists("Output/GPClassificacoesFinalEquipas.txt") == False:
            print(
                "\nERRO: Tem de realizar pelo menos 1 GP antes de obter a Lista da Classificação de Equipas dos GP realizados\n")
        else:
            print("\nClassificação Geral de Equipas dos GP realizado\n")
            data = pd.read_csv("Output/GPClassificacoesFinalEquipas.txt")
            print(data.to_string(index=False))

    ###################################
    # Funções Menu do Campeonato
    ###################################

    def realizar_campeonato(self): # Função realiza Campeonato MotoGP
        fonte_pilotos = open("Ficheiros/Pilotos_2022.txt", 'r')
        fonte_circuitos = open("Ficheiros/Circuito_2022.txt", 'r')
        fonte_pontos = open("Ficheiros/Pontos_2022.txt", 'r')
        pilotos = {}
        circuitos = {}
        pontos = {}
        print("\n Realização do Campeonato MotoGP! \n")
        for x in islice(fonte_pilotos, 1, None):
            piloto = x.strip().split(',')
            pilotos[piloto[1]] = [piloto[0], piloto[2], piloto[3], piloto[4]]
        fonte_pilotos.close()

        for c in islice(fonte_circuitos, 1, None):
            circuito = c.strip().split(',')
            circuitos[circuito[0]] = [circuito[1], circuito[2]]
        fonte_circuitos.close()

        for p in islice(fonte_pontos, 1, None):
            ponto = p.strip().split(',')
            pontos[ponto[0]] = ponto[1]
        fonte_pontos.close()

        resultados_gp = {}
        classificacaoFinal_gp = []

        for gp in circuitos:
            replica_pilotos = list(pilotos)
            classificacao_gp = []
            i = 1
            while replica_pilotos:
                try:
                    pontuacao = int(pontos[str(i)])
                except:
                    pontuacao = 0
                piloto = random.choice(replica_pilotos)
                replica_pilotos.remove(piloto)
                piloto_pontuacao = [piloto, pontuacao]
                classificacao_gp.append(piloto_pontuacao)
                i += 1
                classificacaoFinal_gp.append(piloto_pontuacao)
            resultados_gp[gp] = classificacao_gp
        d = resultados_gp
        df = pd.DataFrame(data=d)
        print(df)
        # Criação do ficheiro de resultados dos circuitos do Campeonato MotoGP gerado
        df.to_csv('Output/CampeonatoMotoGP.txt', header=True, index=False, sep=',', mode='w')
        # Criação do ficheiro de resultados dos pilotos Campeonato MotoGP gerado
        df = pd.DataFrame(data=classificacaoFinal_gp)
        headerList = ['Piloto', 'Pontos']
        df.to_csv('Output/CampeonatoMotoGPClassificacoesPilotos.txt', header=headerList, index=False, sep=',',
                  mode='w')

        df = pd.read_csv("Output/CampeonatoMotoGPClassificacoesPilotos.txt")
        df = df.groupby(['Piloto'])['Pontos'].sum()
        df = df.reset_index()
        df = df.sort_values(by='Pontos', ascending=False)
        df = df.reset_index()
        df['Piloto'] = df['Piloto'].str[:-1]
        headerList = ['Classificação', 'Piloto', 'Pontos']
        df.to_csv('Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt', header=headerList, index=False, sep=',',
                  mode='w')

        df = pd.read_csv("Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt")
        j = 0
        for j in range(0, len(df) + 1):
            df.iloc[j - 1, [0]] = [j]
            df.to_csv('Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt', header=headerList, index=False,
                      sep=',',
                      mode='w')

        # Classificação das Equipas por Circuito
        df = pd.read_csv("Output/CampeonatoMotoGPClassificacoesPilotos.txt")
        j = 0
        equipas = pd.read_csv("Ficheiros/Pilotos_2022.txt", sep=",")
        ClassificacaoEquipa_gp = []
        for index, row in df.iterrows():
            EquipaPiloto = str(row['Piloto'])
            Equipa = equipas.loc[equipas['Piloto'] == EquipaPiloto, 'Equipa'].item()
            ClassificacaoEquipa_gp.append([Equipa, row['Pontos']])
        df = pd.DataFrame(data=ClassificacaoEquipa_gp)
        headerList = ['Equipa', 'Pontos']
        df.to_csv('Output/CampeonatoMotoGPClassificacoesEquipas.txt', header=headerList, index=False, sep=',',
                  mode='w')

        # Classificação Finais das Equipas
        df = pd.read_csv("Output/CampeonatoMotoGPClassificacoesEquipas.txt")
        df = df.groupby(['Equipa'])['Pontos'].sum()
        df = df.reset_index()
        df = df.sort_values(by='Pontos', ascending=False)
        df = df.reset_index()

        headerList = ['Classificação', 'Equipa', 'Pontos']
        df.to_csv('Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt', header=headerList, index=False, sep=',',
                  mode='w')

        df = pd.read_csv("Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt")
        j = 0
        for j in range(0, len(df) + 1):
            df.iloc[j - 1, [0]] = [j]
            df.to_csv('Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt', header=headerList, index=False,
                      sep=',',
                      mode='w')

        print("\n\n Campeonato MotoGP Gerado com Sucesso! \n")
        fonte_circuitos.close()
        fonte_pilotos.close()
        fonte_pontos.close()

    def dez_primeiros_campeonato(self):  # Função 10 primeiros Pilotos do Campeonato MotoGP
        if os.path.exists("Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt") == False:
            print(
                "\nERRO: Tem de realizar um Campeonato MotoGP antes de obter a Lista dos 10 primeiros classificados do Campeonato MotoGP!!!\n")
        else:
            print("\n\nLista 10 primeiros do Campeonato MotoGP\n")
            data = pd.read_csv("Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt")
            print(data.head(n=10).to_string(index=False))

    def tres_primeiros_campeonato(self): # Função 3 primeiros Pilotos do Campeonato MotoGP
        if os.path.exists("Output/CampeonatoMotoGP.txt") == False:
            print(
                "\nERRO: Tem de realizar um Campeonato MotoGP antes de obter a Lista dos 3 primeiros classificados por Circuito!!!\n")
        else:
            print("\n\nLista 3 primeiros de cada GP do Campeonato MotoGP")
            dataframe_collection = {}
            data = pd.read_csv("Output/CampeonatoMotoGP.txt")

            for col in data.columns:
                new_data = [data.iloc[0][col] + " » 1º Classificado", data.iloc[1][col] + " » 2º Classificado",
                            data.iloc[2][col] + " » 3º Classificado"]
                dataframe_collection[col] = pd.DataFrame(new_data, columns=["Classificação Final"])

            for key in dataframe_collection.keys():
                print("\n" + "=" * 80)
                print("Top 3 do Circuito " + key)
                print("=" * 80)
                print(dataframe_collection[key].to_string(index=False))

    def tres_melhores_equipas_campeonato(self): # Função 3 melhores equipas do Campeonato MotoGP
        if os.path.exists("Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt") == False:
            print(
                "\nERRO: Tem de realizar um Campeonato MotoGP antes de obter a Lista das 3 primeiras Equipas do Campeonato MotoGP!!!\n")
        else:
            print("\n\nLista 3 primeiras Equipas do Campeonato MotoGP\n")
            data = pd.read_csv("Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt")
            print(data.head(n=3).to_string(index=False))

    def classificacao_geral_campeonato_pilotos(self): # Função Classificação Geral de Pilotos do Campeonato MotoGP
        if os.path.exists("Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt") == False:
            print("\nERRO: Tem de realizar um Campeonato MotoGP antes de obter a Lista da Classificação de Pilotos\n")
        else:
            print("\nClassificação Geral Pilotos\n")
            data = pd.read_csv("Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt")
            print(data.to_string(index=False))

    def classificacao_geral_campeonato_equipas(self): # Função Classificação Geral de Equipas do Campeonato MotoGP
        if not os.path.exists("Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt"):
            print("\nERRO: Tem de realizar um Campeonato MotoGP antes de obter a Lista da Classificação de Equipas\n")
        else:
            print("\nClassificação Geral de Equipas\n")
            data = pd.read_csv("Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt")
            print(data.to_string(index=False))

    ###################################
    # Funções Menu do Sair
    ###################################
    def sair(self):  # Função terminar a aplicação
        print('Adeus!!!')
        quit()

    ###################################
    # Funções Início Programa
    ###################################
    def init(self):
        self.setWindowIcon(QtGui.QIcon('Imagens/logo.png'))
        self.resize(1024, 550)
        self.setWindowTitle("Simulador MotoGP 2022")
        self.create_menubar()
        self.setObjectName('MainWindow')

        stylesheet = '''
    #MainWindow {
        background-image: url('Imagens/background.jpg');
        background-repeat: no-repeat;
        background-position: center;
    }
'''
        self.setStyleSheet(stylesheet)
        # Remove ficheiros gerados dos anteriores Campeonatos
        if os.path.exists("Output/CampeonatoMotoGP.txt"):
            os.remove("Output/CampeonatoMotoGP.txt")
        if os.path.exists("Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt"):
            os.remove("Output/CampeonatoMotoGPClassificacoesFinalPilotos.txt")
        if os.path.exists("Output/CampeonatoMotoGPClassificacoesPilotos.txt"):
            os.remove("Output/CampeonatoMotoGPClassificacoesPilotos.txt")
        if os.path.exists("Ficheiros/MotoGP.txt"):
            os.remove("Ficheiros/MotoGP.txt")
        if os.path.exists("Output/CampeonatoMotoGPClassificacoesEquipas.txt"):
            os.remove("Output/CampeonatoMotoGPClassificacoesEquipas.txt")
        if os.path.exists("Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt"):
            os.remove("Output/CampeonatoMotoGPClassificacoesFinalEquipas.txt")

        # Remove ficheiros gerados dos anteriores GP
        if os.path.exists("Output/GP.txt"):
            os.remove("Output/GP.txt")
        if os.path.exists("Output/GPClassificacoesFinalPilotos.txt"):
            os.remove("Output/GPClassificacoesFinalPilotos.txt")
        if os.path.exists("Output/GPClassificacoesPilotos.txt"):
            os.remove("Output/GPClassificacoesPilotos.txt")
        if os.path.exists("Output/GPClassificacoesEquipas.txt"):
            os.remove("Output/GPClassificacoesEquipas.txt")
        if os.path.exists("Output/GPClassificacoesFinalEquipas.txt"):
            os.remove("Output/GPClassificacoesFinalEquipas.txt")

app = QApplication(sys.argv)
win = MainFrame()
sys.exit(app.exec_())
