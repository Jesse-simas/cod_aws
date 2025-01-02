import boto3
from datetime import datetime

# Região e IDs das instâncias 
region = 'sa-east-1'
instances = ['(id da instacia)']
ec2 = boto3.client('ec2', region_name=region)

# Dias de feriados (formato 'YYYY-MM-DD')
feriados = {'2024-12-31','2025-01-01'}

def lambda_handler(event, context):
    # Obter a data atual no formato ISO (YYYY-MM-DD)
    data_atual = datetime.now().date().isoformat()

    # Verificar se hoje é feriado
    if data_atual in feriados:
        print(f'Hoje é {data_atual}. Não é permitido iniciar as instâncias.')
        return {
            'statusCode': 200,
            'body': f'Hoje é {data_atual}. Não é permitido iniciar as instâncias.'
        }

    # Iniciar as instâncias
    try:
        ec2.start_instances(InstanceIds=instances)
        print('Iniciando suas instâncias: ' + str(instances))
        return {
            'statusCode': 200,
            'body': f'Iniciando suas instâncias: {instances}'
        }
    except Exception as e:
        print(f'Erro ao iniciar as instâncias: {str(e)}')
        return {
            'statusCode': 500,
            'body': f'Erro ao iniciar as instâncias: {str(e)}'
        }