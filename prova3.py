import json

# Função para carregar os dados do faturamento em formato JSON
def carregar_dados_json(arquivo_json):
    with open(arquivo_json, 'r') as f:
        return json.load(f)

# Função para calcular os resultados
def calcular_faturamento(dados):
    # Filtrando os dias com faturamento (ignorando 0 ou None)
    faturamentos_validos = [valor for valor in dados if valor is not None and valor > 0]
    
    if not faturamentos_validos:
        return None, None, 0  # Se não houver dias com faturamento
    
    # Menor e maior valor de faturamento
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)
    
    # Média mensal
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)
    
    # Contando os dias com faturamento superior à média
    dias_acima_media = sum(1 for valor in faturamentos_validos if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

# Exemplo de dados em formato JSON
dados_faturamento_json = """
{
    "faturamento": [200.50, 300.75, null, 500.00, 0, 450.00, 700.25, 800.50, null, 1000.00, 550.00, 0, 900.00]
}
"""

# Convertendo a string JSON em um dicionário
dados = json.loads(dados_faturamento_json)
faturamentos = dados["faturamento"]

# Calculando os resultados
menor, maior, dias_acima_media = calcular_faturamento(faturamentos)

# Exibindo os resultados
print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
