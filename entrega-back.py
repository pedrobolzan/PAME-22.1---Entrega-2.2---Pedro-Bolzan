from datetime import datetime

lista_alunos=[]
lista_professores=[]
lista_disciplinas=[]
lista_salas=[]

def menu():
    print('1 - Adicionar recursos')
    print('2 - Excluir recursos')
    print('3 - Exibir/Alterar dados')
    print('4 - Gerenciar recursos')
    print('0 - Sair do programa')

def menu1():
    print('1 - Adicionar sala de aula')
    print('2 - Adicionar professor')
    print('3 - Adicionar aluno')
    print('4 - Adicionar disciplina')
    print('0 - Voltar')

def menu2():
    print('1 - Excluir sala de aula')
    print('2 - Excluir professor')
    print('3 - Excluir aluno')
    print('4 - Excluir disciplina')
    print('0 - Voltar')

def menu3():
    print('1 - Listar dados')
    print('2 - Mostrar dados unicos')
    print('3 - Alterar dados')
    print('0 - Voltar')

def menu31():
    print('1 - Listar todas as salas de aula')
    print('2 - Listar todos os professores')
    print('3 - Listar todos os alunos')
    print('4 - Listar todos as disciplinas')
    print('0 - Voltar')

def menu32():
    print('1 - Mostrar dados unicos de salas de aula')
    print('2 - Mostrar dados unicos de professores')
    print('3 - Mostrar dados unicos de alunos')
    print('4 - Mostrar dados unicos de disciplinas')
    print('0 - Voltar')

def menu33():
    print('1 - Alterar dados de salas de aula')
    print('2 - Alterar dados de professores')
    print('3 - Alterar dados de alunos')
    print('4 - Alterar dados de disciplinas')
    print('0 - Voltar')

def menu4():
    print('1 - Associar um professor a uma disciplina')
    print('2 - Associar um aluno a uma disciplina')
    print('3 - Associar uma sala de aula a uma disciplina')
    print('4 - Desassociar um professor de uma disciplina')
    print('5 - Desassociar um aluno de uma disciplina')
    print('6 - Desassociar uma sala de aula de uma disciplina')
    print('0 - Voltar')

class classroomManager:

    def __init__(self, nome):
        self.nome = nome

class sala(classroomManager):
    
    def __init__(self, nome ,capacidade, abrir, fechar) -> None:
        super().__init__(nome)
        self.capacidade = capacidade
        self.ocupada = False
        self.horario = None
        self.dias = None
        self.abrir = abrir
        self.fechar = fechar
    
    def ocupar(self, dias, horario):
        if type(self.horario) == list:
            for i in range(len(self.horario)):
                for j in range(len(self.dias)):
                    if self.horario[i] == horario and self.dias[j] == dias:
                        return print(f"horario {horario} de {dias} já ocupado!")         
            self.horario.append(horario)
            self.dias.append(dias)
            self.aulas += 1
        else:
            self.horario = []
            self.horario.append(horario)
            self.dias = []
            self.dias.append(dias)
            self.designado = "Sim"
            self.aulas += 1
        if datetime.strptime(horario, "%H:%M") >= datetime.strptime(self.fechar, "%H:%M") or datetime.strptime(horario, "%H:%M") < datetime.strptime(self.abrir, "%H:%M"):
            return print("Fora de horário de funcionamento da sala!")
        else:
            self.ocupada = True
            return True
        
    def desocupar(self, dias, horario):
        for i in range(len(self.horario)):
            for j in range(len(self.dias)):
                if self.horario[i] == horario and self.dias[j] == dias:
                    self.horario.remove(self.horario[i])
                    self.dias.remove(self.dias[j])
                    self.ocupada = False
        return True

class professor(classroomManager):
    
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.designado = "Não"
        self.aulas = 0
        self.horario = None
        self.dias = None

    def ocupar_horario (self, dias, horario):
        if type(self.horario) == list:
            for i in range(len(self.horario)):
                for j in range(len(self.dias)):
                    if self.horario[i] == horario and self.dias[j] == dias:
                        return print(f"horario {horario} de {dias} já ocupado!")         
            self.horario.append(horario)
            self.dias.append(dias)
            self.aulas += 1
        else:
            self.horario = []
            self.horario.append(horario)
            self.dias = []
            self.dias.append(dias)
            self.designado = "Sim"
            self.aulas += 1
        return True

    def desocupar_horario (self, dias, horario):
        for i in range(len(self.horario)):
            for j in range(len(self.dias)):
                if self.horario[i] == horario and self.dias[j] == dias:
                    self.horario.remove(self.horario[i])
                    self.dias.remove(self.dias[j])
                    self.aulas -= 1
        return True


class aluno(classroomManager):
   
    def __init__(self, nome) -> None:
        super().__init__(nome)
        self.inscrito = "Não"
        self.aulas = 0
        self.horario = None
        self.dias = None

    def ocupar_horario (self, dias, horario):
        if type(self.horario) == list:
            for i in range(len(self.horario)):
                for j in range(len(self.dias)):
                    if self.horario[i] == horario and self.dias[j] == dias:
                        return print(f"horario {horario} de {dias} já ocupado!")         
            self.horario.append(horario)
            self.dias.append(dias)
            self.aulas += 1
        else:
            self.horario = []
            self.horario.append(horario)
            self.dias = []
            self.dias.append(dias)
            self.inscrito = "Sim"
            self.aulas += 1
        return True
    
    def desocupar_horario (self, dias, horario):
        for i in range(len(self.horario)):
            for j in range(len(self.dias)):
                if self.horario[i] == horario and self.dias[j] == dias:
                    self.horario.remove(self.horario[i])
                    self.dias.remove(self.dias[j])
                    self.aulas -= 1
        return True

class disciplina(classroomManager):
  
    def __init__(self, nome, dias, horario, capacidade) -> None:
        super().__init__(nome)
        self.dias = dias
        self.horario = horario
        self.capacidade = capacidade
        self.professor = None
        self.sala = None
        self.inscritos = 0

    def ocupar_sala (self, sala, dias, horario):
        if self.sala == None:
            if sala.ocupada == False and self.capacidade <= sala.capacidade:
                sala.ocupar(dias, horario)
                self.sala=sala
        else:
            print(f"A disciplina {self.nome} já possui uma sala de aula designada!")

    def definir_professor (self, professor, dias, horario):
        if self.professor == None:
            if professor.ocupar_horario(dias, horario) == True:
                self.professor = professor
            else:
                print("Professor não disponivel!")
        else:
            print(f"A disciplina {self.nome} já possui um professor designado!")
    
    def adicionar_aluno(self, aluno, dias, horarios):
        if self.inscritos < self.capacidade:
            if aluno.ocupar_horario(dias, horarios) == True:
                self.inscritos += 1
            else:
                print("Aluno não disponivel")
        else:
            print("Capacidade máxima de disciplina cheia")

    def remover_professor (self, professor, dias, horario):
        if self.professor != None:
            if professor.desocupar_horario(dias, horario) == True:
                self.professor = None
            else:
                print("Professor não Existe!")
        else:
            print(f"A disciplina {self.nome} já não possui um professor designado!")

    def remover_aluno (self, aluno, dias, horario):
        if self.inscritos != None:
            if aluno.desocupar_horario(dias, horario) == True:
                self.inscritos -= 1
            else:
                print("Aluno não Existe!")
        else:
            print(f"A disciplina {self.nome} já não possui um professor designado!")

    def remover_sala (self, sala, dias, horario):
        if self.ocupada != True:
            if sala.desocupar(dias, horario) == True:
                self.sala = None
            else:
                print("Aluno não Existe!")
        else:
            print(f"A disciplina {self.nome} já não possui uma sala de aula designada!")

def listar(sala, professor, aluno, disciplina):
    '''Função responsavel pela criação de listas de objetos'''
    if sala != None:
        lista_salas.append(sala)
    elif professor != None:
        lista_professores.append(professor)  
    elif aluno != None:
        lista_alunos.append(aluno)          
    elif disciplina != None:
        lista_disciplinas.append(disciplina)

def remover(resposta):
    '''Função que remove os objetos das listas'''
    if resposta == "1":
        for i in range(len(lista_salas)):
            print(f"{i+1} - {lista_salas[i].nome}")
        excluir = input("Qual sala deseja excluir? (Digite somente o numero)")
        del lista_salas[int(excluir)-1]
    elif resposta == "2":
        for i in range(len(lista_professores)):
            print(f"{i+1} - {lista_professores[i].nome}")
        excluir = input("Qual professor deseja excluir? (Digite somente o numero)")
        del lista_professores[int(excluir)-1]
    elif resposta == "3":
        for i in range(len(lista_alunos)):
            print(f"{i+1} - {lista_alunos[i].nome}")
        excluir = input("Qual aluno deseja excluir? (Digite somente o numero)")
        del lista_alunos[int(excluir)-1]
    elif resposta == "4":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        excluir = input("Qual disciplina deseja excluir? (Digite somente o numero)")
        del lista_disciplinas[int(excluir)-1]
    return print("removido com sucesso")

def dados_unicos(resposta):
    '''Função que exibe os dados unicos de objetos'''
    
    if resposta == "1":
        for i in range(len(lista_salas)):
            print(f"{i+1} - {lista_salas[i].nome}")
        exibir = input("Qual sala deseja analisar? (Digite somente o numero)")
        print(f"Nome: {lista_salas[int(exibir)-1].nome}")
        print(f"Capacidade: {lista_salas[int(exibir)-1].capacidade} alunos")
        print(f"Horário de abertura: {lista_salas[int(exibir)-1].abrir}")
        print(f"Horario de fechamento: {lista_salas[int(exibir)-1].fechar}")
    
    elif resposta == "2":
        for i in range(len(lista_professores)):
            print(f"{i+1} - {lista_professores[i].nome}")
        exibir = input("Qual professor deseja analisar? (Digite somente o numero)")
        print(f"Nome: {lista_professores[int(exibir)-1].nome}")
        print(f"Designado: {lista_professores[int(exibir)-1].designado}")
        print(f"Aulas assignado(a): {lista_professores[int(exibir)-1].aulas}")
    
    elif resposta == "3":
        for i in range(len(lista_alunos)):
            print(f"{i+1} - {lista_alunos[i].nome}")
        exibir = input("Qual aluno deseja analisar? (Digite somente o numero)")
        print(f"Nome: {lista_alunos[int(exibir)-1].nome}")
        print(f"Inscrito em alguma aula: {lista_alunos[int(exibir)-1].designado}")
        print(f"Aulas inscrito(a): {lista_alunos[int(exibir)-1].aulas} aulas")
    
    elif resposta == "4":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        exibir = input("Qual disciplina deseja analisar? (Digite somente o numero)")
        print(f"Nome: {lista_disciplinas[int(exibir)-1].nome}")
        print(f"dia: {lista_disciplinas[int(exibir)-1].dias}")
        print(f"horario: {lista_disciplinas[int(exibir)-1].horario}")
        print(f"Capacidade máxima de alunos: {lista_disciplinas[int(exibir)-1].capacidade}")
        print(f"Professor: {lista_disciplinas[int(exibir)-1].professor}")
        print(f"Sala: {lista_disciplinas[int(exibir)-1].sala}")

def exibir_lista(resposta):
    '''Função que exibe as listas'''
    if resposta == "1":
        for i in range(len(lista_salas)):
            print(f"{i+1} - {lista_salas[i].nome}")

    elif resposta == "2":
        for i in range(len(lista_professores)):
            print(f"{i+1} - {lista_professores[i].nome}")

    elif resposta == "3":
        for i in range(len(lista_alunos)):
            print(f"{i+1} - {lista_alunos[i].nome}")

    elif resposta == "4":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")

def alterar_dados(resposta):
    '''Função que altera os dados unicos de objetos'''
    
    if resposta == "1":
        for i in range(len(lista_salas)):
            print(f"{i+1} - {lista_salas[i].nome}")
        exibir = input("Qual sala deseja alterar? (Digite somente o numero): ")
        print(f"Nome: {lista_salas[int(exibir)-1].nome}")
        print(f"Capacidade: {lista_salas[int(exibir)-1].capacidade} alunos")
        print(f"Horário de abertura: {lista_salas[int(exibir)-1].abrir}")
        print(f"Horario de fechamento: {lista_salas[int(exibir)-1].fechar}")
        lista_alunos[int(exibir)-1].nome = input("Insira novo nome: ")
        lista_salas[int(exibir)-1].capacidade = int(input("Insira nova capacidade: "))
        lista_salas[int(exibir)-1].abrir = input("Insira novo horário de abertura")
        lista_salas[int(exibir)-1].fechar = input("Insira novo horário de fechamento")
    
    elif resposta == "2":
        for i in range(len(lista_professores)):
            print(f"{i+1} - {lista_professores[i].nome}")
        exibir = input("Qual professor deseja alterar? (Digite somente o numero): ")
        print(f"Nome: {lista_professores[int(exibir)-1].nome}")
        print(f"Designado: {lista_professores[int(exibir)-1].designado}")
        print(f"Aulas assignado(a): {lista_professores[int(exibir)-1].aulas}")
        lista_alunos[int(exibir)-1].nome = input("Insira novo nome: ")
    
    elif resposta == "3":
        for i in range(len(lista_alunos)):
            print(f"{i+1} - {lista_alunos[i].nome}")
        exibir = input("Qual aluno deseja alterar? (Digite somente o numero): ")
        print(f"Nome: {lista_alunos[int(exibir)-1].nome}")
        print(f"Inscrito em alguma aula: {lista_alunos[int(exibir)-1].designado}")
        print(f"Aulas inscrito(a): {lista_alunos[int(exibir)-1].aulas} aulas")
        lista_alunos[int(exibir)-1].nome = input("Insira novo nome: ")
    
    elif resposta == "4":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        exibir = input("Qual disciplina deseja alterar? (Digite somente o numero): ")
        print(f"Nome: {lista_disciplinas[int(exibir)-1].nome}")
        print(f"dia: {lista_disciplinas[int(exibir)-1].dias}")
        print(f"horario: {lista_disciplinas[int(exibir)-1].horario}")
        print(f"Capacidade máxima de alunos: {lista_disciplinas[int(exibir)-1].capacidade}")
        print(f"Professor: {lista_disciplinas[int(exibir)-1].professor}")
        print(f"Sala: {lista_disciplinas[int(exibir)-1].sala}")
        lista_disciplinas[int(exibir)-1].nome = input("Insira novo nome: ")
        lista_disciplinas[int(exibir)-1].dias = input("Insira o(s) novo(s) dia(s) de aula: ")
        lista_disciplinas[int(exibir)-1].horario = input("Insira o novo horario de aula")
        lista_disciplinas[int(exibir)-1].capacidade = int(input("Insira a nova capacidade máxima de alunos: "))

def associar_desassociar(resposta):
    '''Função responsável por associar e desassociar objetos'''
    if resposta == "1":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        ndisc = input("Qual disciplina está precisando de professor? (Digite somente o numero): ")

        for i in range(len(lista_professores)):
            print(f"{i+1} - {lista_professores[i].nome}")
        nprof = input("Qual professor associar à disciplina? (Digite somente o numero): ")
        lista_disciplinas[int(ndisc)-1].definir_professor(lista_professores[int(nprof)-1], lista_disciplinas[int(ndisc)-1].dias, lista_disciplinas[int(ndisc)-1].horario)
        return print("Professor designado à disciplina com sucesso!")

    elif resposta == "2":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        ndisc = input("Qual disciplina está recebendo alunos? (Digite somente o numero): ")

        for i in range(len(lista_alunos)):
            print(f"{i+1} - {lista_alunos[i].nome}")
        naluno = input("Qual aluno associar à disciplina? (Digite somente o numero): ")
        lista_disciplinas[int(ndisc)-1].adicionar_aluno(lista_alunos[int(naluno)-1], lista_disciplinas[int(ndisc)-1].dias, lista_disciplinas[int(ndisc)-1].horario)
        return print("Aluno adicionado à disciplina com sucesso!")

    elif resposta == "3":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        ndisc = input("Qual disciplina está sendo alocada? (Digite somente o numero): ")

        for i in range(len(lista_salas)):
            print(f"{i+1} - {lista_salas[i].nome}")
        nsala = input("Qual sala será utilizada? (Digite somente o numero): ")
        lista_disciplinas[int(ndisc)-1].ocupar_sala(lista_salas[int(nsala)-1], lista_disciplinas[int(ndisc)-1].dias, lista_disciplinas[int(ndisc)-1].horario)
        return print("Disciplina alocada à sala com sucesso!")

    elif resposta == "4":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        ndisc = input("Qual disciplina está ficando sem professor? (Digite somente o numero): ")

        for i in range(len(lista_professores)):
            print(f"{i+1} - {lista_professores[i].nome}")
        nprof = input("Qual professor deixará a disciplina? (Digite somente o numero): ")
        lista_disciplinas[int(ndisc)-1].remover_professor(lista_professores[int(nprof)-1], lista_disciplinas[int(ndisc)-1].dias, lista_disciplinas[int(ndisc)-1].horario)

    elif resposta == "5":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        ndisc = input("Qual disciplina terá aluno removido? (Digite somente o numero): ")

        for i in range(len(lista_alunos)):
            print(f"{i+1} - {lista_alunos[i].nome}")
        naluno = input("Qual aluno sairá da disciplina? (Digite somente o numero): ")
        lista_disciplinas[int(ndisc)-1].remover_aluno(lista_alunos[int(naluno)-1], lista_disciplinas[int(ndisc)-1].dias, lista_disciplinas[int(ndisc)-1].horario)
    
    elif resposta == "6":
        for i in range(len(lista_disciplinas)):
            print(f"{i+1} - {lista_disciplinas[i].nome}")
        ndisc = input("Qual disciplina está ficando sem sala? (Digite somente o numero): ")

        for i in range(len(lista_salas)):
            print(f"{i+1} - {lista_salas[i].nome}")
        nsala = input("Qual sala será liberada? (Digite somente o numero): ")

        lista_disciplinas[int(ndisc)-1].remover_sala(lista_salas[int(nsala)-1], lista_disciplinas[int(ndisc)-1].dias, lista_disciplinas[int(ndisc)-1].horario)
    
def main():
    while True:
        menu()
        resposta = input('Digite uma das opcoes acima: ')
        if resposta == '1':
            while True:
                menu1()    
                resposta = input('Digite uma das opcoes acima: ')
                if resposta == '1':
                    nome_sala = input('Digite o nome da sala de aula: ')
                    capacidade_sala = input('Digite a capacidade maxima de alunos na sala de aula: ')
                    horario_abrir = input("Digite o horario de abertura da sala (ex: 08:00): ")
                    horario_fechar = input("Digite o horario de fechamento da sala (ex: 17:00): ")
                    sl = sala(nome_sala, int(capacidade_sala), horario_abrir, horario_fechar)
                    listar(sl, None, None, None)
                elif resposta == '2':
                    nome_professor = input('Digite o nome do professor ou professora: ')
                    prof = professor(nome_professor)
                    listar(None, prof, None, None)
                elif resposta == '3':
                    nome_aluno = input('Digite o nome do aluno ou aluna: ')
                    aln = aluno(nome_aluno)
                    listar(None, None, aln, None)
                elif resposta == '4':
                    nome_disciplina = input('Digite o nome da disciplina: ')
                    dia_disciplina = input('Digite o(s) dia(s) da disciplina (ex: segunda; terça e quinta): ')
                    horario_disciplina = input("Digite o horario da disciplina (ex: 10:00): ")
                    capacidade_disciplina = input("Digite a capacidade de alunos na disciplina: ")
                    disc = disciplina(nome_disciplina, dia_disciplina, horario_disciplina, capacidade_disciplina)
                    listar(None, None, None, disc)
                elif resposta == '0':
                    main()
                else:
                    print('Opcao invalida')
        elif resposta == '2':
            while True:    
                menu2()
                resposta = input('Digite uma das opcoes acima: ')
                if resposta == '1':
                    remover(resposta)
                    main()
                elif resposta == '2':
                    remover(resposta)
                    main()             
                elif resposta == '3':
                    remover(resposta)
                    main()
                elif resposta == '4':
                    remover(resposta)
                    main()
                elif resposta == '0':
                    main()
                else:
                    print('Opcao invalida')
        elif resposta == '3':
            while True:
                menu3()
                resposta = input('Digite uma das opcoes acima: ')
                if resposta == '1':
                    while True:
                        menu31()
                        resposta = input('Digite uma das opcoes acima: ')
                        if resposta == '1':
                            exibir_lista(resposta)
                            main()
                        elif resposta == '2':
                            exibir_lista(resposta)
                            main()
                        elif resposta == '3':
                            exibir_lista(resposta)
                            main()
                        elif resposta == '4':
                            exibir_lista(resposta)
                            main()
                        elif resposta == '0':
                            main()
                        else:
                            print('Opcao invalida')
                elif resposta == '2':
                    while True:
                        menu32()
                        resposta = input('Digite uma das opcoes acima: ')
                        if resposta == '1':
                            dados_unicos(resposta)
                            main()
                        elif resposta == '2':
                            dados_unicos(resposta)
                            main()
                        elif resposta == '3':
                            dados_unicos(resposta)
                            main()
                        elif resposta == '4':
                            dados_unicos(resposta)
                            main()
                        elif resposta == '0':
                            main()
                        else:
                            print('Opcao invalida')
                elif resposta == '3':
                    while True:
                        menu33()
                        resposta = input('Digite uma das opcoes acima: ')
                        if resposta == '1':
                            alterar_dados(resposta)
                            main()
                        elif resposta == '2':
                            alterar_dados(resposta)
                            main()
                        elif resposta == '3':
                            alterar_dados(resposta)
                            main()
                        elif resposta == '4':
                            alterar_dados(resposta)
                            main()
                        elif resposta == '0':
                            main()
                        else:
                            print('Opcao invalida')
                elif resposta == '0':
                    main()
                else:
                    print('Opcao invalida')
        elif resposta == '4':
            while True:
                menu4()
                resposta = input('Digite uma das opcoes acima: ')
                if resposta == '1':
                    associar_desassociar(resposta)
                    main()                    
                elif resposta == '2':
                    associar_desassociar(resposta)
                    main()   
                elif resposta == '3':
                    associar_desassociar(resposta)
                    main()   
                elif resposta == '4':
                    associar_desassociar(resposta)
                    main()   
                elif resposta == '5':
                    associar_desassociar(resposta)
                    main()   
                elif resposta == '6':
                    associar_desassociar(resposta)
                    main()   
                elif resposta == '0':
                    main()
                else:
                    print('Opcao invalida')
        elif resposta == '0':
            return print('Ate mais tarde')
        else:
            print('Opcao invalida')

if __name__ == "__main__":
    main()