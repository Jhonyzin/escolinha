import customtkinter as ctk
from tkinter import messagebox
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models import modelos

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

escola = modelos.Escola("Escola do Professor Girafales")
aluno_atual = None

# =========================================================
# APP PRINCIPAL
# =========================================================

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title(escola.nomeescola)
        self.geometry("600x420")

        self.frames = {}

        # Inicializar telas
        for F in (TelaInicial, TelaLogin, TelaAluno, TelaPai, TelaProfessor, TelaCadastro):
            frame = F(self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)

        self.mostrar(TelaInicial)

    def mostrar(self, tela):
        frame = self.frames[tela]
        frame.tkraise()


# =========================================================
# TELA INICIAL
# =========================================================

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Fundo estilizado
        self.configure(fg_color="#1e1e2f")

        # Container central
        container = ctk.CTkFrame(self, corner_radius=20, fg_color="#2b2b40")
        container.pack(pady=80, padx=40, fill="both", expand=False)

        # Título
        ctk.CTkLabel(
            container,
            text="Sistema Escolar",
            font=("Arial", 30, "bold"),
            text_color="white"
        ).pack(pady=30)

        # Botão Login
        ctk.CTkButton(
            container,
            text="Login",
            height=45,
            width=200,
            font=("Arial", 18, "bold"),
            command=lambda: master.mostrar(TelaLogin)
        ).pack(pady=20)

        # Botão Cadastro
        ctk.CTkButton(
            container,
            text="Cadastro",
            height=45,
            width=200,
            font=("Arial", 18, "bold"),
            fg_color="#3a7bd5",
            hover_color="#326bb8",
            command=lambda: master.mostrar(TelaCadastro)
        ).pack(pady=10)

        # Texto inferior
        ctk.CTkLabel(
            container,
            text="Acesse ou crie sua conta",
            font=("Arial", 14),
            text_color="#d0d0d0"
        ).pack(pady=20)

# =========================================================
# TELA CADASTRO
# =========================================================

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Cadastro de Pai + Filho", font=("Arial", 26, "bold")).pack(pady=20)

        # ===========================
        # SEÇÃO DO PAI
        # ===========================
        pai_frame = ctk.CTkFrame(self, corner_radius=12)
        pai_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(pai_frame, text="Dados do Pai", font=("Arial", 20, "bold")).pack(pady=10)

        self.pai_nome = ctk.CTkEntry(pai_frame, placeholder_text="Nome completo")
        self.pai_nome.pack(pady=5)

        self.pai_email = ctk.CTkEntry(pai_frame, placeholder_text="E-mail")
        self.pai_email.pack(pady=5)

        self.pai_cpf = ctk.CTkEntry(pai_frame, placeholder_text="CPF")
        self.pai_cpf.pack(pady=5)

        self.pai_nasc = ctk.CTkEntry(pai_frame, placeholder_text="Nascimento (dd/mm/aaaa)")
        self.pai_nasc.pack(pady=5)

        self.pai_senha = ctk.CTkEntry(pai_frame, placeholder_text="Senha", show="*")
        self.pai_senha.pack(pady=10)

        # ===========================
        # SEÇÃO DO FILHO
        # ===========================
        filho_frame = ctk.CTkFrame(self, corner_radius=12)
        filho_frame.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(filho_frame, text="Dados do Filho", font=("Arial", 20, "bold")).pack(pady=10)

        self.f_nome = ctk.CTkEntry(filho_frame, placeholder_text="Nome completo")
        self.f_nome.pack(pady=5)

        self.f_email = ctk.CTkEntry(filho_frame, placeholder_text="E-mail")
        self.f_email.pack(pady=5)

        self.f_cpf = ctk.CTkEntry(filho_frame, placeholder_text="CPF")
        self.f_cpf.pack(pady=5)

        self.f_nasc = ctk.CTkEntry(filho_frame, placeholder_text="Nascimento (dd/mm/aaaa)")
        self.f_nasc.pack(pady=5)

        self.f_senha = ctk.CTkEntry(filho_frame, placeholder_text="Senha", show="*")
        self.f_senha.pack(pady=5)

        self.f_materias = ctk.CTkEntry(filho_frame, placeholder_text="Matérias (separadas por vírgula)")
        self.f_materias.pack(pady=10)

        # ===========================
        # BOTÕES
        # ===========================

        btns = ctk.CTkFrame(self)
        btns.pack(pady=15)

        ctk.CTkButton(
            btns,
            text="Cadastrar",
            fg_color="#4caf50",
            hover_color="#449d47",
            command=self.cadastrar
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            btns,
            text="Voltar",
            fg_color="#d9534f",
            hover_color="#c64541",
            command=lambda: master.mostrar(TelaInicial)
        ).pack(side="left", padx=10)

        self.master = master

    # ============================================
    # PROCESSAR CADASTRO (VOCÊ VAI LIGAR AO BACKEND DEPOIS)
    # ============================================
    def cadastrar(self):
        # Aqui você captura tudo
        dados_pai = {
            "nome": self.pai_nome.get(),
            "email": self.pai_email.get(),
            "cpf": self.pai_cpf.get(),
            "nasc": self.pai_nasc.get(),
            "senha": self.pai_senha.get()
        }

        dados_filho = {
            "nome": self.f_nome.get(),
            "email": self.f_email.get(),
            "cpf": self.f_cpf.get(),
            "nasc": self.f_nasc.get(),
            "senha": self.f_senha.get(),
            "materias": self.f_materias.get().split(",")
        }

        # Aqui somente exibe, depois você conecta com suas classes Python
        messagebox.showinfo(
            "Cadastro concluído",
            f"Pai cadastrado:\n{dados_pai}\n\nFilho cadastrado:\n{dados_filho}"
        )

# =========================================================
# TELA DE LOGIN
# =========================================================

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Login", font=("Arial", 26, "bold")).pack(pady=30)

        # ---------------------------------------------------------------------
        # SELETOR: TIPO DE USUÁRIO
        # ---------------------------------------------------------------------
        ctk.CTkLabel(self, text="Selecione o tipo de usuário:", font=("Arial", 14)).pack()

        self.tipo_usuario = ctk.StringVar(value="")   # vai guardar: aluno/pai/professor

        opcoes = ctk.CTkOptionMenu(
            self,
            values=["Aluno", "Pai", "Professor"],
            variable=self.tipo_usuario
        )
        opcoes.pack(pady=10)

        # ---------------------------------------------------------------------
        # CAMPOS DE LOGIN
        # ---------------------------------------------------------------------
        self.user_entry = ctk.CTkEntry(self, placeholder_text="Usuário / CPF", width=250)
        self.user_entry.pack(pady=10)

        self.senha_entry = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=250)
        self.senha_entry.pack(pady=10)

        # ---------------------------------------------------------------------
        # BOTÃO LOGIN
        # ---------------------------------------------------------------------
        ctk.CTkButton(
            self,
            text="Entrar",
            width=200,
            command=self.realizar_login
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="Voltar",
            command=lambda: master.mostrar(TelaInicial)
        ).pack(pady=10)

        self.master = master

    # -------------------------------------------------------------------------
    # FUNÇÃO DE LOGIN (AQUI VOCÊ LIGA AO BACKEND DEPOIS)
    # -------------------------------------------------------------------------
    def realizar_login(self):
        tipo = self.tipo_usuario.get()
        usuario = self.user_entry.get()
        senha = self.senha_entry.get()

        if tipo == "":
            messagebox.showwarning("Aviso", "Escolha o tipo de usuário.")
            return
        
        if usuario.strip() == "" or senha.strip() == "":
            messagebox.showwarning("Aviso", "Preencha usuário e senha.")
            return
        

        
        if tipo == "Aluno":
            self.master.mostrar(TelaAluno)
        elif tipo == "Pai":
            self.master.mostrar(TelaPai)
        elif tipo == "Professor":
            self.master.mostrar(TelaProfessor)


# =========================================================
# TELA DO ALUNO
# =========================================================

class TelaAluno(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Área do Aluno", font=("Arial", 24, "bold")).pack(pady=20)

        self.box = ctk.CTkTextbox(self, width=400, height=200)
        self.box.pack(pady=10)
        self.box.insert("0.0", "Aqui o aluno verá suas notas.\n\n(Preencha com backend depois.)")

        ctk.CTkButton(self, text="Sair", command=lambda: master.mostrar(TelaInicial)).pack(pady=20)


# =========================================================
# TELA DO PAI
# =========================================================

class TelaPai(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Área dos Pais", font=("Arial", 24, "bold")).pack(pady=20)

        self.box = ctk.CTkTextbox(self, width=400, height=200)
        self.box.pack(pady=10)
        self.box.insert("0.0", "Aqui o pai verá as notas do aluno.\n\n(Preencha com backend depois.)")

        ctk.CTkButton(self, text="Sair", command=lambda: master.mostrar(TelaInicial)).pack(pady=20)


# =========================================================
# TELA DO PROFESSOR
# =========================================================

class TelaProfessor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Área do Professor", font=("Arial", 24, "bold")).pack(pady=15)

        ctk.CTkLabel(self, text="Nome do aluno").pack()
        self.aluno_nome_entry = ctk.CTkEntry(self, width=250)
        self.aluno_nome_entry.pack(pady=5)

        ctk.CTkLabel(self, text="Matéria").pack()
        self.materia_entry = ctk.CTkEntry(self, width=250)
        self.materia_entry.pack(pady=5)

        ctk.CTkLabel(self, text="Nota").pack()
        self.nota_entry = ctk.CTkEntry(self, width=250)
        self.nota_entry.pack(pady=5)

        ctk.CTkButton(self, text="Adicionar Nota", command=self.add_nota).pack(pady=20)

        ctk.CTkButton(self, text="Sair", command=lambda: master.mostrar(TelaInicial)).pack(pady=10)

    def add_nota(self):
        aluno = self.aluno_nome_entry.get()
        materia = self.materia_entry.get()
        nota = self.nota_entry.get()

        messagebox.showinfo("Sucesso", f"Nota adicionada!\nAluno: {aluno}\nMatéria: {materia}\nNota: {nota}")



# =========================================================
# EXECUTAR APP
# =========================================================

if __name__ == "__main__":
    app = App()
    app.mainloop()