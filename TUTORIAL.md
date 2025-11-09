# Tutorial do Sistema Bancário – Git e Projeto

## 1. Clonando o repositório

Você pode clonar o repositório do GitLab usando **SSH** ou **HTTPS**.

**Via SSH:**

```bash
git clone git@gitlab.com:afya-an-lise-e-programa-o-orientada-a-objetos-02_2025/projeto-de-meio-de-curso/joao-paulo-e-juan-sobral.git
```

💡 Dica: SSH evita digitar usuário e senha a cada push, mas precisa ter chave SSH configurada no GitLab.


Após clonar, você terá a seguinte estrutura de pastas:

![imagem](https://gitlab.com/afya-an-lise-e-programa-o-orientada-a-objetos-02_2025/projeto-de-meio-de-curso/joao-paulo-e-juan-sobral/-/raw/main/docs/imgs/Captura%20de%20tela%202025-09-27%20224126.png?ref_type=heads)

Se você clonou com HTTPS mas deseja usar SSH no futuro, basta configurar o remote com:
```bash
git remote set-url origin git@gitlab.com:afya-an-lise-e-programa-o-orientada-a-objetos-02_2025/projeto-de-meio-de-curso/joao-paulo-e-juan-sobral.git
```

E pode verificar os remotes configurados com:
```bash
git remote -v
```

Para organizar melhor o trabalho e evitar conflitos na branch principal (main), é recomendado criar uma nova branch para desenvolver funcionalidades específicas. Por exemplo:
```bash
git checkout -b minha-branch
```

Ao modificar arquivos, você deve adicioná-los para o commit. Para adicionar todos os arquivos alterados:
```bash
git add .
```

Ou, se quiser adicionar apenas arquivos específicos:
```bash
git add src/app.py
```

Em seguida, crie um commit com uma mensagem clara sobre o que foi alterado:
```bash
git commit -m "Descrição do que foi feito"
```

Para enviar suas alterações ao repositório remoto, use o push. Se estiver na branch main:
```bash
git push origin main
```

Se estiver em outra branch, troque main pelo nome da branch:
```bash
git push origin minha-branch
```

Caso apareça a mensagem de erro non-fast-forward, significa que há alterações no remoto que você ainda não possui localmente. Neste caso, faça primeiro:
```bash
git pull origin main
```
E depois tente o push novamente.


Para manter seu repositório local atualizado com o remoto, use o pull:
```bash
git pull origin main
```

Algumas boas práticas incluem sempre escrever mensagens de commit claras e objetivas, fazer pull antes de iniciar alterações para evitar conflitos, utilizar branches para novas funcionalidades ou testes, e documentar alterações importantes no README ou em comentários no código.

Para rodar o projeto Python com interface Tkinter/CustomTkinter, utilize:
```bash
python src/app.py
```

Se ainda não tiver o CustomTkinter instalado:
```bash
pip install customtkinter
```

# Documentações:

* [Documentação Git](https://git-scm.com/doc)
* [Documentação Tkinter](https://github.com/TomSchimansky/CustomTkinter)
* [Relatório do Projeto](https://gitlab.com/afya-an-lise-e-programa-o-orientada-a-objetos-02_2025/projeto-de-meio-de-curso/joao-paulo-e-juan-sobral/-/blob/main/docs/relatorio.docx?ref_type=heads)