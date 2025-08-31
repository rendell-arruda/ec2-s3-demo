import os
import boto3
import pandas as pd
from datetime import datetime

# Bucket (pode definir aqui ou via variável de ambiente BUCKET_NAME)
BUCKET_NAME = os.getenv("BUCKET_NAME", "SE_BUCKET_AQUI")  # <-- troque depois

def gerar_csv():
    print("📊 [1/3] Gerando DataFrame de exemplo...")
    dados = {
        "id": [1, 2, 3],
        "nome": ["Alice", "Bob", "Carol"],
        "valor": [100, 200, 300],
    }
    df = pd.DataFrame(dados)

    # Nome único para o arquivo, com timestamp
    nome = f"dados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    print(f"📝 [2/3] Salvando arquivo CSV: {nome}")
    df.to_csv(nome, index=False)

    print("✅ CSV gerado com sucesso!")
    return nome

def enviar_para_s3(arquivo):
    print(f"☁️ [3/3] Enviando {arquivo} para o bucket S3 '{BUCKET_NAME}'...")
    s3 = boto3.client("s3")  # usa a role da EC2 (sem salvar credenciais)
    s3.upload_file(arquivo, BUCKET_NAME, f"demo/{arquivo}")
    print(f"🎉 Upload concluído: s3://{BUCKET_NAME}/demo/{arquivo}")

if __name__ == "__main__":
    print("🚀 Iniciando processo...")
    csv = gerar_csv()
    enviar_para_s3(csv)
    print("🏁 Processo finalizado com sucesso!")