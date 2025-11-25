from dataclasses import dataclass, field
import datetime
from typing import List, Optional
import uuid

class Escola():
    def __init__(self, nomeescola):
        self.nomeescola = nomeescola
        self.alunos = []
        self.funcionarios = []
        self.materias = ["Educação Física", "Matemática", "Português", "Física", "Química"]

    def cadastrarcliente(self, alunaos):
        self.alunos.append(alunaos)
    
    def cadastrarfuncionario(self, funcionarios):
        self.funcionarios.append(funcionarios)
    
    def adicionarnota(self, aluno_id: str, materia_nome: str, nova_nota: float):
        for aluno in self.alunos:
            if aluno.userid == aluno_id:
                for materia in aluno.materias:
                    if materia.nome == materia_nome:
                        materia.nota += nova_nota
                        return True
        return False

@dataclass
class Usuarios:
    nome: str
    cpf: str
    _senha: str = field(repr=False, default="", init=False)
    userid: str = field(default_factory=lambda:str(uuid.uuid4()), init=False)

    def set_senha(self, senha: str):
        if not isinstance(senha, str) or len(senha) < 4:
            raise ValueError("A senha deve conter mais de 4 caracteres!")
        self._senha = senha
    
    def verificar_senha(self, senha: str) -> bool:
        return self._senha == senha

    @property
    def senha(self):
        return"********"
    
    @senha.setter
    def senha(self, nova):
        self.set_senha(nova)

@dataclass
class Aluno(Usuarios):
    nascimento: int
    email: str
    materias: List[str] = field(default_factory=list)
    pai: List[str] =  field(default_factory=list)

@dataclass
class MateriaAluno:
    nome: str
    nota: float

@dataclass
class Professor(Usuarios):
    nascimento: str
    email: str
    materia: str

@dataclass
class Pai(Usuarios):
    nascimento: str
    email: str
