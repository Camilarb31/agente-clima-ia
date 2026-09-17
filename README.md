# 🌤️ Agente de Clima

Um agente de IA simples que responde perguntas sobre o clima atual de qualquer cidade do mundo, em português, usando a API gratuita do [OpenWeatherMap](https://openweathermap.org/api).

Projeto criado como primeiro exercício de construção de agentes com apoio do **IBM Bob**.

## ✨ Funcionalidades

- Recebe o nome de uma cidade digitado pelo usuário
- Consulta a previsão do tempo em tempo real
- Responde em linguagem natural, com temperatura, sensação térmica, umidade e vento
- Trata erros comuns (cidade não encontrada, falha de conexão, chave de API ausente)

## 📁 Estrutura do projeto

```
agente-clima/
├── weather_agent.py     # Código principal do agente
├── requirements.txt     # Dependências do projeto
├── .env.example         # Modelo para configurar a chave de API
├── .gitignore
└── README.md
```

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/agente-clima.git
cd agente-clima
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave de API

1. Crie uma conta gratuita em [openweathermap.org](https://openweathermap.org/api)
2. Copie sua chave de API
3. Renomeie `.env.example` para `.env` e cole sua chave:

```
OPENWEATHER_API_KEY=sua_chave_aqui
```

### 5. Execute o agente

```bash
python weather_agent.py
```

Exemplo de uso:

```
=== Agente de Clima ===
Digite o nome de uma cidade (ou 'sair' para encerrar).

Cidade: São Paulo

Agora em São Paulo, BR: nuvens dispersas, com 22.5°C (sensação térmica de 22.0°C).
Umidade: 68% | Vento: 3.1 m/s.
```

## 🛠️ Tecnologias usadas

- Python 3.10+
- [requests](https://pypi.org/project/requests/) — chamadas HTTP
- [python-dotenv](https://pypi.org/project/python-dotenv/) — variáveis de ambiente
- [OpenWeatherMap API](https://openweathermap.org/api) — dados de clima

## 🔮 Próximos passos (ideias de evolução)

- [ ] Adicionar previsão para os próximos dias
- [ ] Conectar a um modelo de linguagem (LLM) para respostas mais naturais e conversacionais
- [ ] Criar uma interface web simples (Flask/Streamlit)
- [ ] Adicionar suporte a múltiplos idiomas
- [ ] Publicar como bot de Telegram/WhatsApp

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
