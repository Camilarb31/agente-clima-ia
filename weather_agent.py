"""
Agente de Clima
----------------
Um agente simples que recebe o nome de uma cidade, busca a previsão
do tempo atual usando a API gratuita do OpenWeatherMap e responde
em linguagem natural.

Uso:
    python weather_agent.py
    (depois digite o nome de uma cidade quando solicitado)

Requisitos:
    - Uma chave de API gratuita do OpenWeatherMap (https://openweathermap.org/api)
    - Definir a variável de ambiente OPENWEATHER_API_KEY (veja .env.example)
"""

import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def buscar_clima(cidade: str) -> dict:
    """Consulta a API do OpenWeatherMap para uma cidade específica."""
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br",
    }
    resposta = requests.get(BASE_URL, params=params, timeout=10)
    resposta.raise_for_status()
    return resposta.json()


def formatar_resposta(dados: dict) -> str:
    """Transforma os dados brutos da API em uma resposta amigável."""
    cidade = dados.get("name", "essa cidade")
    pais = dados.get("sys", {}).get("country", "")
    temp = dados["main"]["temp"]
    sensacao = dados["main"]["feels_like"]
    descricao = dados["weather"][0]["description"]
    umidade = dados["main"]["humidity"]
    vento = dados["wind"]["speed"]

    return (
        f"Agora em {cidade}, {pais}: {descricao}, com {temp:.1f}°C "
        f"(sensação térmica de {sensacao:.1f}°C).\n"
        f"Umidade: {umidade}% | Vento: {vento} m/s."
    )


def perguntar_ao_agente(cidade: str) -> str:
    """Função principal do agente: recebe uma cidade e devolve a resposta."""
    if not API_KEY:
        return (
            "Erro: variável de ambiente OPENWEATHER_API_KEY não definida. "
            "Veja o arquivo .env.example para instruções."
        )

    try:
        dados = buscar_clima(cidade)
    except requests.exceptions.HTTPError as erro:
        if erro.response.status_code == 404:
            return f"Não encontrei a cidade '{cidade}'. Verifique o nome e tente novamente."
        return f"Ocorreu um erro ao consultar o clima: {erro}"
    except requests.exceptions.RequestException as erro:
        return f"Erro de conexão: {erro}"

    return formatar_resposta(dados)


def main():
    print("=== Agente de Clima ===")
    print("Digite o nome de uma cidade (ou 'sair' para encerrar).\n")

    while True:
        cidade = input("Cidade: ").strip()
        if cidade.lower() in ("sair", "exit", "quit"):
            print("Até logo!")
            sys.exit(0)
        if not cidade:
            continue

        resposta = perguntar_ao_agente(cidade)
        print(f"\n{resposta}\n")


if __name__ == "__main__":
    main()
