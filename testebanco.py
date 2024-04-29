import pandas as pd
import streamlit as st
import pyodbc

# Defina sua conexão com o banco de dados
def create_connection():
    server = r'DESKTOP-LUCAS\SQLSERVER2022'  # Substitua pelo seu servidor SQL
    database = 'PythonSQL'
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};')
    return conn


def carregar_dados_prova_geografia():
    conn = create_connection()
    query = "SELECT questoes, resposta_correta, explicacao FROM prova_geografia"
    df = pd.read_sql(query, conn)
    perguntas = {}
    explicacoes = {}

    todas_alternativas = set()  # Para armazenar todas as alternativas disponíveis

    for index, row in df.iterrows():
        alternativas = row['questoes'].split('\n')[1:]  # Pegar todas as linhas após a primeira
        for alternativa in alternativas:
            letra = alternativa.strip().split(')')[0].lower()  # Extrair a letra da alternativa
            todas_alternativas.add(letra)

    for index, row in df.iterrows():
        alternativas = row['questoes'].split('\n')[1:]  # Pegar todas as linhas após a primeira
        alternativas_dict = {letra: f"{letra}) Sem alternativa disponível" for letra in
                             todas_alternativas}  # Inicializar com "Sem alternativa disponível"
        for alternativa in alternativas:
            letra = alternativa.strip().split(')')[0].lower()  # Extrair a letra da alternativa
            texto = alternativa.strip()[
                    3:]  # Extrair o texto da alternativa (ignorando a letra, o parêntese e o espaço)
            alternativas_dict[letra] = f"{letra}) {texto}"
        perguntas[index + 1] = {
            'questao': row['questoes'].split('\n')[0],  # Primeira linha contém a pergunta
            'alternativas': alternativas_dict,  # Restante são alternativas
            'resposta_correta': row['resposta_correta'],  # Adicionando a resposta correta
        }
        explicacao = row['explicacao']
        explicacoes[index + 1] = explicacao if explicacao else "Nenhuma explicação disponível."
    return perguntas, explicacoes


def apresentar_pergunta(pergunta, chave):
    st.write("### " + pergunta['questao'])
    st.write("")  # Adiciona uma linha em branco para criar espaço
    alternativas = pergunta['alternativas']
    todas_alternativas = {'a', 'b', 'c', 'd'}
    alternativas_ordenadas = {letra: alternativas.get(letra, "Sem alternativa disponível") for letra in todas_alternativas}
    for letra, texto_alternativa in sorted(alternativas_ordenadas.items()):
        st.write(texto_alternativa)
    resposta = st.radio(label="Escolha uma opção:", options=list(alternativas_ordenadas.keys()), key=f"radio-{chave}")
    if resposta:
        st.session_state['resposta_usuario'] = resposta



# Interface principal
st.title("Sistema de Provas para treino")
perguntas_geografia, explicacoes_geografia = carregar_dados_prova_geografia()

def escolher_prova():
    # Botão para iniciar a prova
    if st.button('Iniciar Prova'):
        st.session_state['prova_atual'] = 'geografia'  # Defina o nome da prova atual
        st.session_state['indice_pergunta'] = 0  # Resetar o índice da pergunta
        st.session_state['acertos'] = 0  # Resetar a contagem de acertos
        st.session_state['resposta_submetida'] = False  # Resetar a submissão de resposta
        st.session_state['resposta_usuario'] = ''  # Resetar a resposta do usuário
        st.rerun()

def executar_prova(perguntas, explicacoes):
    if 'indice_pergunta' not in st.session_state:
        st.session_state.indice_pergunta = 0
        st.session_state.acertos = 0
        st.session_state.resposta_submetida = False

    if 'resposta_contabilizada' not in st.session_state:
        st.session_state.resposta_contabilizada = False

    indice = st.session_state.indice_pergunta
    total_perguntas = len(perguntas)

    # Mostrar qual questão o usuário está e o total
    st.write(f"Questão {indice + 1} de {total_perguntas} - Acertos: {st.session_state.acertos}")

    # Verificar se todas as perguntas foram respondidas
    if indice >= total_perguntas:
        st.write(f"Você completou a prova! Acertos: {st.session_state.acertos} de {total_perguntas}")
        if st.button("Refazer a prova"):
            st.session_state.indice_pergunta = 0
            st.session_state.acertos = 0
            st.session_state.resposta_submetida = False
            st.session_state.resposta_contabilizada = False  # Certifique-se de que esta também está sendo redefinida
            st.rerun()
    else:
        # Obter a pergunta atual e suas informações
        pergunta_atual = perguntas.get(indice + 1)

        # Apresentar a pergunta e coletar a resposta
        apresentar_pergunta(pergunta_atual, f'radio-{indice}')

        if st.session_state.resposta_submetida:
            resposta_correta = pergunta_atual['resposta_correta'].lower()  # Convertendo para minúsculas
            # Mostrar se a resposta é correta ou incorreta
            if st.session_state['resposta_usuario'] == resposta_correta:
                if not st.session_state.resposta_contabilizada:
                    st.success("Resposta correta!")
                    st.session_state.acertos += 1
                    st.session_state.resposta_contabilizada = True
            else:
                st.error(f"Resposta incorreta. A resposta correta é: {resposta_correta}.")

            # Obter a explicação da coluna "explicacao"
            explicacao_atual = explicacoes.get(indice + 1)

            # Mostrar a explicação
            st.write("### Explicação:")
            st.write(explicacao_atual)

            # Botão para avançar para a próxima pergunta
            if st.button('Próxima pergunta'):
                st.session_state.indice_pergunta += 1
                st.session_state.resposta_submetida = False
                st.session_state.resposta_contabilizada = False  # Resetar para a próxima pergunta
                st.rerun()

        elif indice < total_perguntas and st.button('Confirmar resposta', key='confirmar_resposta', disabled=st.session_state.resposta_submetida):
            st.session_state.resposta_submetida = True

if 'prova_atual' not in st.session_state:
    escolher_prova()
else:
    executar_prova(perguntas_geografia, explicacoes_geografia)
