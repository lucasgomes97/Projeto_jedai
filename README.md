# Projeto_jedai


Olá e bem-vindo ao meu portfólio!

# Documentação para o Código de Geração de Questões e Prova de Geografia

## Introdução
Este documento descreve o funcionamento de dois códigos Python relacionados à geração e apresentação de questões de geografia, bem como a realização de uma prova interativa baseada nessas questões. Os códigos utilizam bibliotecas como PyODBC, requests, pandas e Streamlit.

## Geração de Questões de Geografia

### Funções Principais

#### 1. `generate_questions()`
Esta função utiliza a API do OpenAI para gerar automaticamente questões de geografia em português (pt-br), com alternativas de A a D e uma explicação associada à resposta correta. O texto de entrada é um prompt definido pelo usuário que indica a intenção de gerar uma questão de geografia. A função retorna uma lista de dicionários, cada um contendo o texto da questão e sua explicação.

#### 2. `main()`
A função principal do código é responsável por orquestrar o processo de geração de questões e sua inserção em um banco de dados SQL Server. Ela chama a função `generate_questions()` para obter as questões, verifica se cada questão já existe no banco de dados e, se não existir, a adiciona ao banco por meio da função `add_question_to_database()`.

### Banco de Dados SQL Server

#### Configuração da Conexão
A função `create_connection()` é responsável por criar uma conexão com o banco de dados SQL Server, utilizando a biblioteca PyODBC. Os parâmetros do servidor e do banco de dados devem ser configurados de acordo com o ambiente de execução.

#### Operações no Banco de Dados
- `fetch_max_question_id()`: Obtém o maior ID de questão presente na tabela do banco de dados.
- `question_exists()`: Verifica se uma determinada questão já existe no banco de dados.
- `add_question_to_database()`: Adiciona uma nova questão ao banco de dados.

## Aplicativo de Prova de Geografia Interativa

### Funções Principais

#### 1. `carregar_dados_prova_geografia()`
Esta função conecta-se ao banco de dados SQL Server e carrega os dados das questões de geografia, incluindo o texto da pergunta, as alternativas, a resposta correta e a explicação associada.

#### 2. `apresentar_pergunta()`
Esta função é responsável por apresentar uma pergunta ao usuário, exibindo o texto da pergunta e suas alternativas (A, B, C, D) em um formato interativo. O usuário pode selecionar uma opção e confirmar sua resposta.

#### Interface do Usuário

- **Iniciar Prova**: Botão para iniciar a prova de geografia.
- **Questão Atual**: Mostra a pergunta atual e suas opções de resposta.
- **Confirmação de Resposta**: Após selecionar uma opção, o usuário deve confirmar sua resposta.
- **Feedback da Resposta**: Após confirmar a resposta, o sistema fornece feedback indicando se a resposta está correta ou não, juntamente com uma explicação associada à resposta correta.
- **Próxima Pergunta**: Botão para avançar para a próxima pergunta após submeter a resposta.

## Conclusão
Este documento fornece uma visão geral das funcionalidades e operações dos códigos relacionados à geração e apresentação de questões de geografia, bem como à realização de uma prova interativa baseada nessas questões. Ele serve como uma guia para entender e utilizar esses códigos de forma eficaz.

Atenciosamente,

Lucas Gomes
## 🚀 Sobre mim:
## Olá eu sou o Lucas Gomes <br>🔭 Atualmente estou trabalhando como back-end em Python <br>📚 Estudante de Python ,Django Web Framework, Django Rest Framework E PÓS EM ENGENHARIA DE SOFTWARE <br>⚙  Engenheiro de produção, <br>🟢Green belt em lean Six Sigma, Lean Manufacturing, Scrum, Controle da qualidade, Segurança no trabalho <br>🖊Autocad profissional, Visual Basic, Ms Project<br>📩 E-mail para contato: lucasceo22@gmail.com<br>


## 🌐 Socials:
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/_lucasgomesoficial) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/search/results/all/?heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAACBd8AYBr29CVPTD8v1s4K8i3RuU6cSY6qo&keywords=lucas%20gomes&origin=RICH_QUERY_SUGGESTION&position=0&searchId=31b8c8c7-0a18-4981-b1eb-0cf7933d00b2&sid=LXI) [![Twitch](https://img.shields.io/badge/Twitch-%239146FF.svg?logo=Twitch&logoColor=white)](https://twitch.tv/lucashorse) 

# 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white) ![Adobe Photoshop](https://img.shields.io/badge/adobephotoshop-%2331A8FF.svg?style=for-the-badge&logo=adobephotoshop&logoColor=white) ![Inkscape](https://img.shields.io/badge/Inkscape-e0e0e0?style=for-the-badge&logo=inkscape&logoColor=080A13) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)   ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=lucasgomes97&theme=dark&hide_border=false&include_all_commits=true&count_private=true)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=lucasgomes97&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=lucasgomes97&theme=dark&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

## 🏆 GitHub Trophies
![](https://github-profile-trophy.vercel.app/?username=lucasgomes97&theme=tokyonight&no-frame=false&no-bg=false&margin-w=4)

### ✍️ Random Dev Quote
![](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=merko)

### 😂 Random Dev Meme
<img src="(https://drive.google.com/file/d/1Kwje_f06cKb165rsp1VZr4lmyOgD3150/view)" width="512px"/>

---
[![](https://visitcount.itsvg.in/api?id=lucasgomes97&icon=6&color=1)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->



## Suporte

Para suporte, mande um email para lucasceo22@gmail.com ou entre em contato pelo Whatsapp:(79)98806-9425


## Autores

- [@lucasgomes97](https://github.com/lucasgomes97)

