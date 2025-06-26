

<h1 align="center">📊 Previsão do Tempo – Data Pipeline</h1>

<p align="center"><strong>Automatize a coleta semanal de dados meteorológicos com Apache Airflow</strong></p>

---

## 🚀 Objetivo
Automatizar a coleta da previsão do tempo toda semana e armazenar os dados em arquivos organizados por semana, permitindo análises históricas e versionamento eficiente.

---

## 🛠 Tecnologias Utilizadas
- 🔹 [Python 3.11](https://www.python.org/)
- 🔹 [Apache Airflow](https://airflow.apache.org/)
- 🔹 [pandas](https://pandas.pydata.org/)
- 🔹 [API Open-Meteo](https://open-meteo.com/)
- 🔹 [Docker (opcional)](https://www.docker.com/) 

---

## 🧠 Como Funciona
1. A DAG do Airflow é agendada para rodar **toda segunda-feira**.  
2. Cria-se a pasta `semana={{ data }}` no momento da execução.  
3. A DAG consulta a previsão semanal em uma API pública.  
4. Os dados são salvos em formato **CSV** na pasta correspondente.

---

## ▶️ Execução Local

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/Ligia-lab/previsao_do_tempo_datapipeline.git
cd previsao_do_tempo_datapipeline
````

### 2️⃣ Crie o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Inicie o Airflow

```bash
airflow standalone
```

### 4️⃣ Disponibilize a DAG

```bash
cp dags/previsao_tempo_dag.py ~/airflow/dags/
# ou defina AIRFLOW__CORE__DAGS_FOLDER para a pasta do projeto
```

---

## 📅 Agendamento

```cron
0 0 * * 1   # toda segunda-feira 00:00 UTC
```

---
