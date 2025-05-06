import json

# Salva lista em arquivo JSON.
def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista, arquivo_aberto)

# Lê lista de arquivo JSON, retorna vazio se não encontrado.
def ler_arquivo(nome_arquivo):
    try:
        with open (nome_arquivo, 'r') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
            return lista
    except FileNotFoundError:
        return []

# Nomes dos arquivos JSON para cada entidade.
arquivo_estudantes = "listaestudantes.json"
arquivo_professores = "listaprofessores.json"
arquivo_disciplinas = "listadisciplinas.json"
arquivo_turmas = "listaturmas.json"
arquivo_matriculas = "listamatriculas.json"

# Lê dados iniciais dos arquivos para as listas.
lista_estudantes = ler_arquivo(arquivo_estudantes)
lista_professores = ler_arquivo(arquivo_professores)
lista_disciplinas = ler_arquivo(arquivo_disciplinas)
lista_turmas = ler_arquivo(arquivo_turmas)
lista_matriculas = ler_arquivo(arquivo_matriculas)

# Inclui novo registro na lista e salva no arquivo.
def incluir_registro(lista, nome_arquivo, campos):
    registro = {}
    for campo in campos:
        valor = input(f'Digite o {campo.replace("_"," do ")}: ')
        registro[campo] = int(valor) if campo.startswith("codigo") else valor
    lista.append(registro)
    salvar_arquivo(lista, nome_arquivo)
    print("Registro incluido com sucesso! ")

# Lista todos os registros do arquivo.
def listar_registros(nome_arquivo):
    lista = ler_arquivo(nome_arquivo)
    print ('\n   Lista de registros: ')
    if lista:
        for item in lista:
            print(f'   - {item}')
    else:
        print('*** A lista esta vazia ***')

# Edita um registro existente no arquivo.
def editar_registro(nome_arquivo, chave_primaria, campos):
    lista = ler_arquivo(nome_arquivo)
    codigo = int(input(f"Digite o {chave_primaria.replace('_',' ')} do registro a editar: "))
    for item in lista:
        if item[chave_primaria] == codigo:
            for campo in campos:
                novo_valor = input(f"Digite o novo {campo.replace('_', ' ')} (atual: {item[campo]}): ")
                item[campo] = int(novo_valor) if campo.startswith("codigo") else novo_valor
            salvar_arquivo(lista, nome_arquivo)
            print("Registro atualizado com sucesso.")
            return
    print("Registro não encontrado.")

# Exclui um registro do arquivo.
def excluir_registro(nome_arquivo, chave_primaria):
    lista = ler_arquivo(nome_arquivo)
    codigo = int(input(f"Digite o {chave_primaria.replace('_', ' ')} a excluir: "))
    for item in lista:
        if item[chave_primaria] == codigo:
            lista.remove(item)
            salvar_arquivo(lista, nome_arquivo)
            print("Registro excluído com sucesso.")
            return
    print("Registro não encontrado.")

# Exibe o menu principal e retorna a opção.
def menu_principal():
    while True:
        print('\n   --- MENU PRINCIPAL ---')
        print('   (1) Gerenciar estudantes')
        print('   (2) Gerenciar professores')
        print('   (3) Gerenciar disciplinas')
        print('   (4) Gerenciar turmas')
        print('   (5) Gerenciar matriculas')
        print('   (9) Sair')
        try:
            opcao_principal =int(input ('Informe a opção desejada: '))
            return opcao_principal
        except ValueError:
            print('Entrada inválida. Digite um número:')

# Exibe o menu de operações e retorna a opção.
def menu_operacoes():
    while True:
        print('\n   --- MENU OPERAÇÕES ---')
        print('   (1) Incluir')
        print('   (2) Listar')
        print('   (3) Editar')
        print('   (4) Excluir')
        print('   (5) Voltar ao menu principal')
        try:
            opcao_operacoes =int(input ('Informe a opção desejada: '))
            return opcao_operacoes
        except ValueError:
            print('Entrada inválida. Digite um número:')

# Campos para estudantes.
campos_estudantes = ["codigo_estudante", "nome_estudante", "cpf_estudante"]
arquivo_estudantes = "listaestudantes.json"

# Campos para professores.
campos_professores = ["codigo_professor", "nome_professor", "cpf_professor"]
arquivo_professores = "listaprofessores.json"

# Campos para disciplinas.
campos_disciplina = ["codigo_disciplina", "nome_disciplina"]
arquivo_disciplina = "listadisciplinas.json"

# Campos para turmas.
campos_turma = ["codigo_turma", "codigo_professor", "codigo_disciplina"]
arquivo_turma = "listaturmas.json"

# Campos para matrículas.
campos_matriculas = ["codigo_matriculas", "codigo_estudante"]
arquivo_matriculas = "listamatriculas.json"

# Loop principal do programa.
while True:
    opcao_principal = menu_principal()

    # Gerenciar estudantes.
    if opcao_principal == 1:
        while True:
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == 1:
                incluir_registro(lista_estudantes, arquivo_estudantes, campos_estudantes)
            if opcao_operacoes == 2:
                listar_registros(arquivo_estudantes)
            elif opcao_operacoes == 3:
                editar_registro(arquivo_estudantes, "codigo_estudante", campos_estudantes)
            elif opcao_operacoes == 4:
                excluir_registro(arquivo_estudantes, "codigo_estudante")
            elif opcao_operacoes == 5:
                break

    # Gerenciar professores.
    if opcao_principal == 2:
        while True:
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == 1:
                incluir_registro(lista_professores, arquivo_professores, campos_professores)
            if opcao_operacoes == 2:
                listar_registros(arquivo_professores)
            elif opcao_operacoes == 3:
                editar_registro(arquivo_professores, "codigo_professor", campos_professores)
            elif opcao_operacoes == 4:
                excluir_registro(arquivo_professores, "codigo_professor")
            elif opcao_operacoes == 5:
                break
    # Gerenciar disciplinas.
    if opcao_principal == 3:
        while True:
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == 1:
                incluir_registro(lista_disciplinas, arquivo_disciplinas, campos_disciplina)
            if opcao_operacoes == 2:
                listar_registros(arquivo_disciplinas)
            elif opcao_operacoes == 3:
                editar_registro(arquivo_disciplinas, "codigo_disciplina", campos_disciplina)
            elif opcao_operacoes == 4:
                excluir_registro(arquivo_disciplinas, "codigo_disciplina",)
            elif opcao_operacoes == 5:
                break
    # Gerenciar turmas.
    if opcao_principal == 4:
        while True:
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == 1:
                incluir_registro(lista_turmas, arquivo_turmas, campos_turma)
            if opcao_operacoes == 2:
                listar_registros(arquivo_turmas)
            elif opcao_operacoes == 3:
                editar_registro(arquivo_turmas, "codigo_turma", campos_turma)
            elif opcao_operacoes == 4:
                excluir_registro(arquivo_turmas, "codigo_turma")
            elif opcao_operacoes == 5:
                break
    # Gerenciar matrículas.
    if opcao_principal == 5:
        while True:
            opcao_operacoes = menu_operacoes()
            if opcao_operacoes == 1:
                incluir_registro(lista_matriculas, arquivo_matriculas, campos_matriculas)
            if opcao_operacoes == 2:
                listar_registros(arquivo_matriculas)
            elif opcao_operacoes == 3:
                editar_registro(arquivo_matriculas, "codigo_matriculas", campos_matriculas)
            elif opcao_operacoes == 4:
                excluir_registro(arquivo_matriculas, "codigo_matriculas")
            elif opcao_operacoes == 5:
                break

    # Sair do programa.
    elif opcao_principal == 9:
        break