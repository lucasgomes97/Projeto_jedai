import pyodbc
import requests


# Configuração da API do OpenAI - substitua 'your-api-key' pelo seu próprio
api_key = 'sua chave da Openai aqui'

def create_connection():
    server = r'seu server'  # Substitua pelo seu servidor SQL
    database = 'seu banco de dados'
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};')
    return conn

def fetch_max_question_id(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT MAX(id_questao) FROM dbo.prova_geografia")
        max_id = cursor.fetchone()
        if max_id and max_id[0]:
            return max_id[0]
        else:
            return 0
    except Exception as e:
        print(f"Erro ao buscar o máximo ID de questão: {e}")
        return None
    finally:
        cursor.close()

def question_exists(conn, question_text):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM dbo.prova_geografia WHERE questoes = ?", (question_text,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"Erro ao verificar se a questão já existe: {e}")
        return False
    finally:
        cursor.close()

def add_question_to_database(conn, id_questao, question_text, options_text, correct_answer, explanation):
    cursor = conn.cursor()
    try:
        id_unidade = 1
        # Formatando as alternativas de A a D junto com a pergunta
        formatted_question = f"{question_text}\n\n{options_text}"
        # Adicionando quebras de linha entre cada pergunta
        formatted_question = f"{formatted_question}\n\n"
        # Adicionando a questão ao banco de dados
        query = "INSERT INTO dbo.prova_geografia (id_unidade, id_questao, questoes, resposta_correta, explicacao) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (id_unidade, id_questao, formatted_question, correct_answer, explanation))
        conn.commit()
        print("Questão adicionada ao banco de dados com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar a questão ao banco de dados: {e}")
    finally:
        cursor.close()



def generate_questions():
    prompt = "Gerar uma questão de geografia em português pt-br com alternativas de A a D e explicacao da resposta. \nExplain:" #aqui vc coloca a pergunta que deseja fazer para o chat gpt.
    data = {
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 500,
        "stop": ["###"],  # Indica o fim da geração da questão
        "model": "gpt-3.5-turbo-instruct"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers)
    if response.status_code == 200:
        generated_questions = response.json().get('choices', [])
        if generated_questions:
            questions = []
            for choice in generated_questions:
                text = choice.get("text", "").strip()
                # Tenta encontrar a explicação dentro do texto da questão
                explanation_start = text.find("Explicação:")
                if explanation_start != -1:
                    # Se encontrarmos a explicação, pegamos o texto a partir desse ponto
                    explanation = text[explanation_start + len("Explicação:"):].strip()
                    # Remove a explicação do texto da questão
                    text = text[:explanation_start].strip()
                else:
                    explanation = "Não foi possível encontrar a explicação."
                # Adiciona o texto da questão e a explicação à lista de questões
                questions.append({"text": text, "explanation": explanation})
            return questions
        else:
            print("Nenhuma questão gerada pela API.")
            return []  # Retorna uma lista vazia se não houver questões geradas
    else:
        print("Erro ao gerar questões usando a API da OpenAI:", response.text)
        return []



def main():
    conn = create_connection()
    try:
        last_id = fetch_max_question_id(conn)
        id_questao = last_id + 1  # Começa a partir do próximo ID após o último no banco
        questions = generate_questions()
        if questions:
            for question_data in questions:
                try:
                    question_text = question_data["text"]
                    explanation = question_data["explanation"]
                    options_text = ""
                    correct_answer = 'A'  # Alterando para 'A' como padrão

                    if not question_exists(conn, question_text):
                        print("Question Text:", question_text)
                        print("Options Text:", options_text)
                        print("Correct Answer:", correct_answer)
                        print("Explanation:", explanation)
                        print("Inserindo no banco de dados...")
                        add_question_to_database(conn, id_questao, question_text, options_text, correct_answer, explanation)
                        print("Pergunta inserida no banco de dados com sucesso.")
                    else:
                        print("Questão já existe no banco de dados, pulando...")
                    id_questao += 1  # Incrementa o ID da questão apenas se ela não existir no banco de dados
                except Exception as e:
                    print(f"Erro ao processar a questão: {e}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
