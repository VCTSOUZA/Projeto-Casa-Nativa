# Casa Nativa

Fundação de uma aplicação web para uma marca fictícia de decoração e artigos para casa, preparada para evoluir de forma segura.

## Tecnologias

- Python 3
- Flask
- Jinja2
- HTML5, CSS3 e JavaScript vanilla
- python-dotenv

## Estrutura

```text
app/
├── routes/       # Blueprints e rotas da aplicação
├── models/       # Reservado para modelos futuros
├── static/       # CSS, JavaScript e imagens
└── templates/    # Templates Jinja2
config.py         # Configurações por ambiente
run.py            # Ponto de entrada local
```

## Configuração

1. Clone o projeto e entre na pasta:

   ```powershell
   git clone <url-do-repositorio>
   cd "Projeto Casa Nativa"
   ```

2. Crie e ative o ambiente virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:

   ```powershell
   pip install -r requirements.txt
   ```

4. Crie o arquivo local de ambiente a partir do modelo:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Defina uma `SECRET_KEY` longa, aleatória e exclusiva no arquivo `.env`. Ela é obrigatória em produção e também deve ser configurada para usar recursos de sessão localmente.

6. Inicie a aplicação:

   ```powershell
   python run.py
   ```

   Acesse `http://127.0.0.1:5000/`.

## Segurança

- Secrets não devem ser incluídos em commits.
- O arquivo `.env` é local e não deve ser enviado ao Git.
- Nunca use DEBUG em produção.
- O projeto segue princípios de Secure by Design: configurações sensíveis vêm do ambiente, cookies têm padrões seguros e a produção exige `SECRET_KEY`.
