import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import modelos


escola = modelos.Escola("escola boa")

materia1 = modelos.MateriaAluno("Educação Física", 0.00)
materia2 = modelos.MateriaAluno("Matemática", 0.00)
materia3 = modelos.MateriaAluno("Química", 0.00)

aluno = modelos.Aluno(nome="JOAO", cpf="1623820382", senha_temp="123413", nascimento="10/20/2024", email="joao@gmail", materias=[materia1, materia2, materia3])
escola.cadastrarcliente(aluno)

escola.adicionarnota(aluno_id=aluno.userid, materia_nome="Educação Física", nova_nota=20)

for aluno in escola.alunos:
    for chave, valor in aluno.__dict__.items():
        print(chave, valor)
    print("-=")

print(aluno.senha)