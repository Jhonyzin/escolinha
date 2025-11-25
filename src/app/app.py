import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import datetime

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import modelos

# --------------------------
# CONFIG
# --------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Paths
BG_PATH = "images.jpg"

# Cores padrão (Aluno)
AFYA_PINK = "#E4006F"
AFYA_PINK_LIGHT = "#FF6FA3"
CARD_BG = "#FFFFFF"
RIGHT_BG = "#F3F3F3"

# Cores professor
PROF_PRIMARY = "#6C2EB9"
PROF_ACCENT = "#E4006F"
PROF_CARD = "#FFFFFF"

APP_W, APP_H = 1000, 640

# --------------------------
# Aplicativo
# --------------------------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Demo - Login/Cadastro/Áreas")
        self.geometry(f"{APP_W}x{APP_H}")
        self.resizable(False, False)
        self.escola  =  modelos.Escola("Eds")
        self.usuario_atual = None
        self.login_role = ctk.StringVar(value="aluno")
        self.container = ctk.CTkFrame(self, fg_color=RIGHT_BG)
        self.container.pack(fill="both", expand=True)

        self.professordados = modelos.Professor(nome="Girafales", cpf="1323", nascimento="10/09/1990", email="girafales@gmail.com", materia="Educação Física")
        self.professordados.senha = "1234"

        self.escola.cadastrarfuncionario(self.professordados)

        try:
            raw = Image.open(BG_PATH).resize((int(APP_W * 0.48), APP_H), Image.LANCZOS)
            self.bg_img = ctk.CTkImage(light_image=raw, dark_image=raw, size=(int(APP_W * 0.48), APP_H))
        except Exception as e:
            print(f"Aviso: Imagem '{BG_PATH}' não encontrada ou erro ao carregar. Usando fallback.")
            self.bg_img = None

        self.frames = {}
        for F in (LoginFrame, RegisterFrame, StudentAreaFrame, ProfessorAreaFrame):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)

        self.show_frame("LoginFrame")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.lift()

    def set_role(self, role):
        self.login_role.set(role)
        login_frame = self.frames["LoginFrame"]
        login_frame.update_style_for_role(role)


# --------------------------
# LOGIN FRAME
# --------------------------
class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent, controller: App, **kwargs):
        super().__init__(parent, fg_color=RIGHT_BG, **kwargs)
        self.controller = controller

        left_w = int(APP_W * 0.48)
        left_frame = ctk.CTkFrame(self, width=left_w, height=APP_H, fg_color=AFYA_PINK, corner_radius=0)
        left_frame.place(x=0, y=0)
        
        if controller.bg_img:
            lbl = ctk.CTkLabel(left_frame, image=controller.bg_img, text="")
            lbl.place(relx=0.5, rely=0.5, anchor="center")
        else:
            ctk.CTkLabel(left_frame, text="Afya", font=("Segoe UI", 60, "bold"), text_color="white").place(relx=0.5,
                                                                                                           rely=0.5,
                                                                                                           anchor="center")

        card_width = APP_W - left_w - 40
        self.card = ctk.CTkFrame(self, width=card_width, height=460, fg_color=CARD_BG, corner_radius=20)
        self.card.place(x=left_w + 20, y=60)
        # Impede que o card encolha se os widgets forem menores
        self.card.pack_propagate(False)

        # Toggles
        role_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        role_frame.pack(pady=10)
        ctk.CTkLabel(role_frame, text="Entrar como:", font=("Segoe UI", 12)).pack(side="left", padx=(0, 10))
        aluno_btn = ctk.CTkRadioButton(role_frame, text="Aluno", variable=controller.login_role, value="aluno",
                                       command=lambda: controller.set_role("aluno"))
        prof_btn = ctk.CTkRadioButton(role_frame, text="Professor", variable=controller.login_role, value="professor",
                                      command=lambda: controller.set_role("professor"))
        aluno_btn.pack(side="left", padx=10)
        prof_btn.pack(side="left", padx=10)

        self.title_lbl = ctk.CTkLabel(self.card, text="Bem-vindo!", font=("Segoe UI", 24, "bold"), text_color=AFYA_PINK)
        self.title_lbl.pack(pady=(6, 4))
        self.subtitle = ctk.CTkLabel(self.card, text="Faça login na sua conta", font=("Segoe UI", 13),
                                     text_color="#555")
        self.subtitle.pack(pady=(0, 20))

        self.email_entry = ctk.CTkEntry(self.card, width=320, placeholder_text="Email")
        self.email_entry.pack(pady=8)
        self.pass_entry = ctk.CTkEntry(self.card, width=320, placeholder_text="Senha", show="*")
        self.pass_entry.pack(pady=8)

        self.login_btn = ctk.CTkButton(self.card, text="Login", width=200, command=self.perform_login, fg_color=AFYA_PINK)
        self.login_btn.pack(pady=15)

        self.create_btn = ctk.CTkButton(self.card, text="Criar conta", width=200, fg_color="#DDD", text_color="#333",
                                        hover_color="#CCC", command=lambda: controller.show_frame("RegisterFrame"))
        self.create_btn.pack(pady=(5, 6))

        demo_text = ("Aplicativo com direitos reservados")
        ctk.CTkLabel(self.card, text=demo_text, font=("Segoe UI", 10), text_color="#666").pack(pady=(6, 4))

        self.update_style_for_role(controller.login_role.get())

    def update_style_for_role(self, role):
        if role == "professor":
            self.title_lbl.configure(text_color=PROF_PRIMARY)
            self.login_btn.configure(fg_color=PROF_PRIMARY, hover_color=PROF_ACCENT, text_color="white")
            self.subtitle.configure(text="Login professor — insira credenciais")
        else:
            self.title_lbl.configure(text_color=AFYA_PINK)
            self.login_btn.configure(fg_color=AFYA_PINK, hover_color=AFYA_PINK_LIGHT, text_color="white")
            self.subtitle.configure(text="Login aluno — insira credenciais")

    def perform_login(self):
        role = self.controller.login_role.get()
        email = self.email_entry.get().strip()
        senha = self.pass_entry.get()

        if not email or not senha:
            messagebox.showerror("Erro", "Preencha email e senha.")
            return
        
        escola = self.controller.escola

        if role == "aluno":
            for aluno in getattr(escola, "alunos", []):
                if getattr(aluno, "email", "") == email and aluno.verificar_senha(senha):
                    self.controller.usuario_atual = aluno
                    messagebox.showinfo("Sucesso", f"Bem-vindo, {aluno.nome}!")
                    self.controller.show_frame("StudentAreaFrame")
                    frame = self.controller.frames.get("StudentAreaFrame")
                    if frame and hasattr(frame, "load_student"):
                        frame.load_student()
                    return

                messagebox.showerror("Erro", "Credenciais de aluno inválidas.")
                return
        if role == "professor":
            email = self.email_entry.get().strip()
            senha = self.pass_entry.get().strip()


            professores = self.controller.escola.funcionarios

            if not professores:
                messagebox.showerror("Erro", "Nenhum professor cadastrado no sistema.")
                return

            # Procura o professor
            for prof in professores:
                if prof.email == email and prof.verificar_senha(senha):
                    self.controller.usuario_atual = prof
                    prof_data = {
                        "name": prof.nome,
                        "email": prof.email,
                        "cpf": prof.cpf,
                        "subjects": [prof.materia]
                    }

                    frame = self.controller.frames.get("ProfessorAreaFrame")
                    if frame and hasattr(frame, "set_professor"):
                        frame.set_professor(prof_data)

                    self.controller.show_frame("ProfessorAreaFrame")
                    return

            messagebox.showerror("Erro", "Credenciais de professor inválidas.")
            return




# --------------------------
# CADASTRO DE ALUNO E PAI
# --------------------------
class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, controller: App, **kwargs):
        super().__init__(parent, fg_color=RIGHT_BG, **kwargs)
        self.controller = controller

        left_w = int(APP_W * 0.48)
        left_frame = ctk.CTkFrame(self, width=left_w, height=APP_H, fg_color=AFYA_PINK, corner_radius=0)
        left_frame.place(x=0, y=0)

        if controller.bg_img:
            lbl = ctk.CTkLabel(left_frame, image=controller.bg_img, text="")
            lbl.place(relx=0.5, rely=0.5, anchor="center")
        else:
            ctk.CTkLabel(left_frame, text="Afya", font=("Segoe UI", 60, "bold"), text_color="white").place(relx=0.5,
                                                                                                           rely=0.5,
                                                                                                           anchor="center")

        card = ctk.CTkFrame(self, width=APP_W - left_w - 40, height=600, fg_color=CARD_BG, corner_radius=18)
        card.place(x=left_w + 20, y=30)
        card.pack_propagate(False)

        title = ctk.CTkLabel(card, text="Cadastro do Pai e Aluno", 
                             font=("Segoe UI", 22, "bold"))
        title.pack(pady=(20, 10))

        # Container dos formulários
        self.form_container = ctk.CTkFrame(card, fg_color="transparent")
        self.form_container.pack(fill="both", expand=True)

        self.build_aluno_form()

        ctk.CTkButton(card, text="Voltar ao Login", command=lambda: controller.show_frame("LoginFrame"), width=200,
                      fg_color="#AAA", hover_color="#888").pack(pady=10)

    def build_aluno_form(self):
        self.aluno_form = ctk.CTkFrame(self.form_container, fg_color="transparent")

        ctk.CTkLabel(self.aluno_form, text="Dados do Filho", font=("Segoe UI", 14, "bold")).pack(pady=(2, 2))
        self.filho_nome = ctk.CTkEntry(self.aluno_form, placeholder_text="Nome completo", width=320)
        self.filho_cpf = ctk.CTkEntry(self.aluno_form, placeholder_text="CPF", width=320)
        self.filho_nasc = ctk.CTkEntry(self.aluno_form, placeholder_text="Data de Nascimento (dd/mm/aaaa)", width=320)
        self.filho_email = ctk.CTkEntry(self.aluno_form, placeholder_text="E-mail", width=320)
        self.filho_senha = ctk.CTkEntry(self.aluno_form, placeholder_text="Senha", width=320, show="*")
        self.filho_nome.pack(pady=4)
        self.filho_cpf.pack(pady=4)
        self.filho_nasc.pack(pady=4)
        self.filho_email.pack(pady=4)
        self.filho_senha.pack(pady=4)

        ctk.CTkLabel(self.aluno_form, text="Dados do Pai", font=("Segoe UI", 14, "bold")).pack(pady=(8, 2))
        self.pai_nome = ctk.CTkEntry(self.aluno_form, placeholder_text="Nome completo", width=320)
        self.pai_nascimento = ctk.CTkEntry(self.aluno_form, placeholder_text="Data de Nascimento (dd/mm/aaaa)", width=320)
        self.pai_cpf = ctk.CTkEntry(self.aluno_form, placeholder_text="CPF", width=320)
        self.pai_email = ctk.CTkEntry(self.aluno_form, placeholder_text="E-mail", width=320)
        self.pai_senha = ctk.CTkEntry(self.aluno_form, placeholder_text="Senha", width=320, show="*")
        self.pai_nome.pack(pady=5)
        self.pai_nascimento.pack(pady=5)
        self.pai_cpf.pack(pady=5)
        self.pai_email.pack(pady=5)
        self.pai_senha.pack(pady=5)
        

        ctk.CTkButton(self.aluno_form, text="Cadastrar Aluno (Pai cria)", width=300, command=self.criarconta).pack(
            pady=10)
        self.aluno_form.pack(fill="both", expand=True)

    def criarconta(self):
        # Coletando dados do Filho
        filho_nome = self.filho_nome.get().strip()
        filho_cpf = self.filho_cpf.get().strip()
        filho_nasc = self.filho_nasc.get().strip()
        filho_email = self.filho_email.get().strip()
        filho_senha = self.filho_senha.get().strip()
        materia1 = modelos.MateriaAluno("Educação Física", 0.00)
        materia2 = modelos.MateriaAluno("Matemática", 0.00)
        materia3 = modelos.MateriaAluno("Português", 0.00)
        materia4 = modelos.MateriaAluno("Física", 0.00)
        materia5 = modelos.MateriaAluno("Química", 0.00)

        # Coletando dados do pai
        pai_nome = self.pai_nome.get().strip()
        pai_nascimento = self.pai_nascimento.get().strip()
        pai_cpf = self.pai_cpf.get().strip()
        pai_email = self.pai_email.get().strip()
        pai_senha = self.pai_senha.get().strip()

        if not (filho_nome and filho_cpf and filho_nasc and pai_nome and pai_senha):
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
            return

        # ----- Conta pai -----
        contapai = modelos.Pai(
            nome=pai_nome,
            cpf=pai_cpf,
            nascimento=pai_nascimento,
            email=pai_email
        )
        contapai.senha = pai_senha

        # ----- Conta filho -----
        contafilho = modelos.Aluno(
            nome=filho_nome,
            cpf=filho_cpf,
            nascimento=filho_nasc,
            email=filho_email,
            materias=[materia1, materia2, materia3, materia4, materia5],
            pai=[contapai]
        )
        contafilho.senha = filho_senha

        # ----- CADASTRA NA ESCOLA -----
        self.controller.escola.cadastrarcliente(contafilho)

        messagebox.showinfo("Sucesso", "Aluno e pai cadastrado com sucesso!")

        # aqui retorna os dados e garante que tudo foi corretamente bravo
        for aluno in self.controller.escola.alunos:
            for chave, valor in aluno.__dict__.items():
                print(chave, valor)
            print("-=")

        # limpa campos
        self.filho_nome.delete(0, "end")
        self.filho_cpf.delete(0, "end")
        self.filho_email.delete(0,"end")
        self.filho_senha.delete(0, "end")
        self.filho_nasc.delete(0, "end")

        self.pai_nome.delete(0, "end")
        self.pai_cpf.delete(0, "end")
        self.pai_email.delete(0, "end")
        self.pai_senha.delete(0, "end")

# --------------------------
# AREA DO ALUNAO
# --------------------------
class StudentAreaFrame(ctk.CTkFrame):
    def __init__(self, parent, controller: App, **kwargs):
        super().__init__(parent, fg_color=RIGHT_BG, **kwargs)
        self.controller = controller

        # ---------- TOPO ----------
        top = ctk.CTkFrame(self, fg_color="transparent", height=50)
        top.pack(fill="x", pady=10, padx=20)

        ctk.CTkButton(
            top, text="Sair", width=100,
            fg_color="#999", hover_color="#666",
            command=lambda: controller.show_frame("LoginFrame")
        ).pack(side="right")

        self.title = ctk.CTkLabel(
            self, text="Área do Aluno",
            font=("Segoe UI", 26, "bold"),
            text_color=AFYA_PINK
        )
        self.title.pack(pady=(10, 6))

        # Informações do aluno
        self.info = ctk.CTkLabel(self, text="", font=("Segoe UI", 15))
        self.info.pack(pady=(0, 10))

        # Caixa principal
        self.list_frame = ctk.CTkFrame(self, fg_color=CARD_BG, corner_radius=15)
        self.list_frame.pack(fill="both", expand=True, padx=40, pady=20)

        ctk.CTkLabel(
            self.list_frame,
            text="Boletim Escolar",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=10)

        self.grades_box = ctk.CTkTextbox(
            self.list_frame, width=800, height=350,
            font=("Consolas", 14)
        )
        self.grades_box.pack(pady=10, padx=15, fill="both", expand=True)


    # -------------------------------------------------
    #               SETA O ALUNO LOGADO
    # -------------------------------------------------
    def load_student(self):
        aluno = self.controller.usuario_atual  # alunada

        if aluno is None:
            self.title.configure(text="Área do Aluno")
            self.info.configure(text="Nenhum aluno carregado.")
            return

        # Título com nome do aluno
        self.title.configure(text=f"Bem-vindo, {aluno.nome}")

        # Pai/responsável
        nome_pai = "-"
        if aluno.pai and len(aluno.pai) > 0:
            nome_pai = aluno.pai[0].nome

        # Idade
        idade = self._calcular_idade(aluno.nascimento)

        self.info.configure(
            text=f"Email: {aluno.email}  |  Responsável: {nome_pai}  |  Idade: {idade} anos"
        )

        self.refresh_grades(aluno)


    # -------------------------------------------------
    #                  BOLETIM
    # -------------------------------------------------
    def refresh_grades(self, aluno):
        self.grades_box.configure(state="normal")
        self.grades_box.delete("0.0", "end")

        if not aluno.materias:
            self.grades_box.insert("end", "Nenhuma matéria encontrada.\n")
        else:
            for materia in aluno.materias:
                self.grades_box.insert("end", f"DISCIPLINA: {materia.nome}\n")
                self.grades_box.insert("end", f"  Nota atual: {materia.nota:.1f}\n")
                self.grades_box.insert("end", "-" * 40 + "\n")

        self.grades_box.configure(state="disabled")


    # -------------------------------------------------
    #                 FUNÇÃO AUXILIAR
    # -------------------------------------------------
    def _calcular_idade(self, nascimento_str):
        try:
            dia, mes, ano = map(int, nascimento_str.split("/"))
            nasc = datetime.date(ano, mes, dia)
            hoje = datetime.date.today()
            idade = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
            return idade
        except:
            return "-"

# --------------------------
# AREA DO PROFESSOR
# --------------------------
class ProfessorAreaFrame(ctk.CTkFrame):
    def __init__(self, parent, controller: App, **kwargs):
        super().__init__(parent, fg_color=RIGHT_BG, **kwargs)
        self.controller = controller
        self.current_prof: Professor | None = None

        top = ctk.CTkFrame(self, fg_color="transparent")
        top.pack(fill="x", pady=10, padx=20)

        ctk.CTkButton(
            top, text="Sair", width=100, fg_color="#999", hover_color="#666",
            command=lambda: controller.show_frame("LoginFrame")
        ).pack(side="right")

        self.title = ctk.CTkLabel(
            self, text="Área do Professor",
            font=("Segoe UI", 26, "bold"), text_color=PROF_PRIMARY
        )
        self.title.pack(pady=(10, 5))

        self.info = ctk.CTkLabel(self, text="", font=("Segoe UI", 14))
        self.info.pack(pady=(0, 20))

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=30, pady=10)

        left = ctk.CTkFrame(content, width=400, fg_color="white", corner_radius=10)
        left.pack(side="left", fill="y", padx=(0, 20))
        left.pack_propagate(False)

        ctk.CTkLabel(
            left, text="Lista de Alunos",
            font=("Segoe UI", 16, "bold"), text_color=PROF_PRIMARY
        ).pack(pady=10)

        self.alunos_box = ctk.CTkTextbox(left, width=360, height=400)
        self.alunos_box.pack(padx=10, pady=10, fill="both", expand=True)

        right = ctk.CTkFrame(content, fg_color="white", corner_radius=10)
        right.pack(side="left", fill="both", expand=True)

        ctk.CTkLabel(
            right, text="Lançamento de Notas",
            font=("Segoe UI", 16, "bold"), text_color=PROF_PRIMARY
        ).pack(pady=20)

        form = ctk.CTkFrame(right, fg_color="transparent")
        form.pack()

        self.sel_email = ctk.CTkEntry(form, placeholder_text="Email do aluno", width=300)
        self.sel_subject = ctk.CTkEntry(form, placeholder_text="Disciplina (ex: Matemática)", width=300)
        self.sel_grade = ctk.CTkEntry(form, placeholder_text="Nota (ex: 8.5)", width=300)

        self.sel_email.pack(pady=10)
        self.sel_subject.pack(pady=10)
        self.sel_grade.pack(pady=10)

        ctk.CTkButton(
            form, text="Lançar Nota", command=self.add_grade,
            width=300, fg_color=PROF_PRIMARY, hover_color=PROF_ACCENT
        ).pack(pady=20)

        ctk.CTkButton(
            form, text="Atualizar Lista", command=self.refresh_students_list,
            width=300, fg_color="#999"
        ).pack(pady=5)

    def set_professor(self, prof_obj):
        if isinstance(prof_obj, dict):
            nome = prof_obj.get("name", "Professor")
            materia = prof_obj.get("subjects", [""])[0]
        else:
            nome = prof_obj.nome
            materia = prof_obj.materia

        self.title.configure(text=f"Painel Docente: {nome}")
        self.info.configure(text=f"Leciona: {materia}")
        self.current_prof = prof_obj
        self.refresh_students_list()


    def refresh_students_list(self):
        escola = self.controller.escola
        self.alunos_box.configure(state="normal")
        self.alunos_box.delete("0.0", "end")

        if not escola.alunos:
            self.alunos_box.insert("end", "Nenhum aluno cadastrado.\n")
        else:
            for aluno in escola.alunos:
                self.alunos_box.insert("end", f"{aluno.nome}\n")
                self.alunos_box.insert("end", f"   Email: {aluno.email}\n")
                self.alunos_box.insert("end", f"   CPF: {aluno.cpf}\n")
                self.alunos_box.insert("end", "-" * 30 + "\n")

        self.alunos_box.configure(state="disabled")

    def add_grade(self):
        email = self.sel_email.get().strip()
        materia_nome = self.sel_subject.get().strip()
        nota_texto = self.sel_grade.get().strip()

        if not email or not materia_nome or not nota_texto:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        try:
            nota = float(nota_texto.replace(",", "."))
        except:
            messagebox.showerror("Erro", "Nota inválida. Use números.")
            return

        escola = self.controller.escola

        # Procura o aluno por email
        aluno_encontrado = None
        for aluno in escola.alunos:
            if aluno.email == email:
                aluno_encontrado = aluno
                break

        if not aluno_encontrado:
            messagebox.showerror("Erro", "Aluno não encontrado com este email.")
            return

        # --------------------------------------------------------
        # GARANTE que as matérias do aluno são OBJETOS MateriaAluno
        # --------------------------------------------------------
        if not aluno_encontrado.materias or isinstance(aluno_encontrado.materias[0], str):
            aluno_encontrado.materias = [
                MateriaAluno(nome=m, nota=0.0) for m in escola.materias
            ]

        # Procura a matéria
        materia_obj = None
        for m in aluno_encontrado.materias:
            if m.nome.lower() == materia_nome.lower():
                materia_obj = m
                break

        if not materia_obj:
            messagebox.showerror("Erro", "Disciplina não encontrada no cadastro do aluno.")
            return

        # Soma a nota
        materia_obj.nota += nota

        messagebox.showinfo("Sucesso", f"Nota {nota} lançada para {aluno_encontrado.nome}.")
        self.sel_grade.delete(0, "end")
        self.refresh_students_list()

        

# --------------------------
# RUN
# --------------------------
if __name__ == "__main__":
    app = App()
    app.mainloop()