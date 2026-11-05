from pymongo.errors import DuplicateKeyError
from conexao import banco

alunos = banco['alunos_p01']
alunos.create_index('matricula', unique=True)

while True:
    print('\n[1] Cadastrar [2] Listar [3] Alterar [4] Excluir [5] buscar por curso [0] Sair')
    opcao = input('Opção: ').strip()
    if opcao == '1':
        while True:
            matricula = input('Matrícula: ').strip()
            if not matricula:
                print('A matrícula não pode ficar em branco. Tente novamente.')
                continue
            if not matricula.isascii() or not matricula.isdigit():
                print('A matrícula deve conter apenas números. Tente novamente.')
                continue
            if len(matricula) != 8:
                print('A matrícula deve ter 8 numeros. Tente novamente.')
                continue

            break

        nome = input('Nome: ').strip()
        curso = input('Curso: ').strip()
        if not all([nome, curso]):
            print('Preencha todos os campos.')
            continue
        try:
            alunos.insert_one({
                'matricula': matricula,
                'nome': nome,
                'curso': curso
            })
            print('Aluno cadastrado!')
        except DuplicateKeyError:
            print('Matrícula já cadastrada.')

    elif opcao == '2':
        for aluno in alunos.find({}, {'_id': 0}).sort('nome', 1):
            print(aluno)

    elif opcao == '3':
        matricula = input('Matrícula: ').strip()
        novo_curso = input('Novo curso: ').strip()
        if novo_curso:
            r = alunos.update_one({'matricula': matricula}, {'$set': {'curso': novo_curso}})
            print('Atualizado!' if r.matched_count else 'Aluno não encontrado.')

    elif opcao == '4':
        matricula = input('Matrícula: ').strip()
        r = alunos.delete_one({'matricula': matricula})
        print('Excluído!' if r.deleted_count else 'Aluno não encontrado.')

    elif opcao == '5':
        curso = input('Curso: ').strip()
        for aluno in alunos.find({'curso': curso}, {'_id': 0}).sort('nome', 1):
            print(aluno)

    elif opcao == '0':
        break
    else:
        print('Opção inválida.')