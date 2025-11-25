import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# =========================================================
# APP PRINCIPAL
# =========================================================

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Sistema Escolar")
        self.geometry("600x420")

        self.frames = {}

        # Inicializar telas
        for F in (TelaInicial, TelaLogin, TelaAluno, TelaPai, TelaProfessor):
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

        ctk.CTkLabel(
            self,
            text="Sistema Escolar",
            font=("Arial", 26, "bold")
        ).pack(pady=40)

        ctk.CTkButton(
            self, text="Entrar",
            command=lambda: master.mostrar(TelaLogin)
        ).pack(pady=10)

        ctk.CTkLabel(
            self,
            text="Escolha seu tipo de login na próxima tela.",
            font=("Arial", 14)
        ).pack(pady=10)


# =========================================================
# TELA DE LOGIN
# =========================================================

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(self, text="Login", font=("Arial", 22, "bold")).pack(pady=20)

        ctk.CTkButton(self, text="Aluno",
                      command=lambda: master.mostrar(TelaAluno)).pack(pady=5)

        ctk.CTkButton(self, text="Pai",
                      command=lambda: master.mostrar(TelaPai)).pack(pady=5)

        ctk.CTkButton(self, text="Professor",
                      command=lambda: master.mostrar(TelaProfessor)).pack(pady=5)
        
        self.user_entry = ctk.CTkEntry(self, placeholder_text="Usuário / CPF")
        self.user_entry.pack(pady=10)

        self.senha_entry = ctk.CTkEntry(self, placeholder_text="Senha", show="*")
        self.senha_entry.pack(pady=10)

        ctk.CTkLabel(self, text="Entrar como:", font=("Arial", 14)).pack(pady=10)

        ctk.CTkButton(self, text="Voltar",
                      command=lambda: master.mostrar(TelaInicial)).pack(pady=15)


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