# MedQuery

Chatbot que responde perguntas sobre um banco de dados hospitalar em **linguagem natural**. O usuário digita a pergunta em português, a IA converte automaticamente em uma consulta SQL, executa no banco e retorna o resultado — tudo direto pelo terminal.

```
O que você quer consultar? qual o paciente mais velho de cada cidade e quais medicos consultaram ele e quantas consultas ele fez

SQL gerado pela IA: SELECT p.city, CONCAT(p.first_name, ' ', p.last_name) AS paciente, ...

              city        paciente  idade  total_consultas                         medicos
0      Farroupilha  Maria Oliveira     35                2  Carlos Eduardo,Roberto Almeida
1    Caxias do Sul    Pedro Santos     62                2    Fernanda Costa,Mariana Souza
2  Bento Gonçalves  Lucas Ferreira     45                1                   Julio Moreira
```

## Sobre o projeto

Este projeto nasceu da vontade de unir três áreas: banco de dados, programação e inteligência artificial, aplicadas a um domínio que conheço bem — a rotina de sistemas hospitalares. Minha experiência trabalhando com TI hospitalar e com o sistema Tasy foi o que inspirou a escolha do tema e da modelagem do banco de dados usada aqui.

## Como funciona

1. O usuário digita uma pergunta em português no terminal (ex: *"quantos pacientes estão internados em Caxias do Sul?"*).
2. A pergunta é enviada para a API do **Gemini**, junto com o schema completo do banco de dados e um conjunto de regras de segurança.
3. A IA retorna apenas o comando SQL correspondente.
4. O comando passa por uma **validação de segurança**: só consultas (`SELECT`/`WITH`) são aceitas; qualquer comando que possa alterar ou apagar dados (`DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`, `TRUNCATE`) é bloqueado antes de chegar ao banco.
5. A query aprovada é executada no MySQL, e o resultado é formatado e exibido em uma tabela pelo Pandas.
6. O usuário pode fazer quantas perguntas quiser em sequência, até digitar `sair`.

## Tecnologias utilizadas

- **Python**
- **MySQL** — banco de dados relacional
- **Pandas** — formatação e exibição dos resultados
- **google-genai** — SDK oficial do Google para a API Gemini
- **python-dotenv** — gerenciamento seguro de variáveis de ambiente
- **Git/GitHub** — versionamento

## Estrutura do banco de dados

O banco modela um cenário hospitalar simplificado, com 5 tabelas relacionadas:

- **pacientes** — dados dos pacientes
- **medicos** — dados dos médicos, vinculados a um setor
- **consultas** — consultas realizadas, ligando pacientes e médicos
- **setores** — setores do hospital (ex: Cardiologia, UTI)
- **cirurgia** — cirurgias realizadas, ligando pacientes e médicos

## Como rodar o projeto

```bash
git clone https://github.com/Mutus142/MedQuery.git
cd MedQuery
pip install pandas mysql-connector-python python-dotenv google-genai
```

Crie um arquivo `.env` na raiz do projeto com suas próprias credenciais:

```
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=medquery
GEMINI_API_KEY=sua_chave_aqui
```

Execute:

```bash
python medquery.py
```

## Exemplos de perguntas que o chatbot responde

- Quantos pacientes estão internados?
- Qual médico possui mais consultas?
- Qual a média de idade dos pacientes?
- Liste os pacientes de Caxias do Sul.
- Qual o paciente mais velho de cada cidade e quantas consultas ele fez?

## Segurança

- Nenhuma credencial (senha do banco ou chave de API) fica exposta no código — tudo é lido de variáveis de ambiente via `.env`, que é ignorado pelo Git (`.gitignore`).
- A IA é instruída, via prompt, a gerar apenas comandos de leitura (`SELECT`).
- Uma segunda camada de validação, no próprio código Python, bloqueia qualquer comando que não seja uma consulta — independente do que a IA gerar.

## Status

Projeto funcional e em evolução. Próximos passos possíveis: tratamento de erros mais refinado, testes automatizados e, futuramente, uma interface visual.
