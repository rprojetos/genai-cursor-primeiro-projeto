# Como conectar este projeto ao GitHub

## Passos para subir o projeto para o GitHub:

### 1. Criar um repositório no GitHub
1. Acesse [github.com](https://github.com)
2. Clique em "New repository" ou "Novo repositório"
3. Dê um nome ao repositório (ex: `hello-world-api`)
4. Deixe como público ou privado (sua escolha)
5. **NÃO** inicialize com README, .gitignore ou license (já temos esses arquivos)
6. Clique em "Create repository"

### 2. Conectar o repositório local ao GitHub
Após criar o repositório no GitHub, execute os seguintes comandos:

```bash
# Adicionar o repositório remoto (substitua SEU_USUARIO e NOME_DO_REPO)
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git

# Fazer push do código para o GitHub
git push -u origin main
```

### 3. Exemplo prático
Se seu usuário for `joaosilva` e o repositório se chamar `hello-world-api`:

```bash
git remote add origin https://github.com/joaosilva/hello-world-api.git
git push -u origin main
```

### 4. Verificar se deu certo
Após o push, você pode:
- Acessar o repositório no GitHub
- Ver todos os arquivos do projeto
- Usar a documentação automática da API

## Estrutura do projeto no GitHub:
```
hello-world-api/
├── main.py              # Aplicação FastAPI simplificada
├── requirements.txt     # Dependências
├── README.md           # Documentação
├── .gitignore          # Arquivos ignorados
└── GITHUB_SETUP.md     # Este arquivo
```

## Próximos passos:
1. Execute os comandos acima
2. Acesse seu repositório no GitHub
3. Compartilhe o link com outros desenvolvedores
4. Continue desenvolvendo e fazendo commits!

## Dica:
Para futuras atualizações, use:
```bash
git add .
git commit -m "Descrição das mudanças"
git push
``` 