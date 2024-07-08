
import boto3
import botocore

def lambda_handler(event, context):
    # Entrada
    s3 = boto3.client('s3')
    bucket_name = event['body']['name']
    directory_name = event.get('directory', event['body']['name_direct'])  # Nombre del directorio por defecto

    exists = True

    try:
        # Verificar si el bucket existe
        s3.head_bucket(Bucket=bucket_name)
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            exists = False

    if exists:
        try:
            # Crear una carpeta (directorio) en el bucket
            s3.put_object(Bucket=bucket_name, Key=(directory_name + '/'))
        except botocore.exceptions.ClientError as e:
            return {
                'statusCode': 500,
                'body': f"Error al crear el directorio: {e.response['Error']['Message']}"
            }

        # Salida
        return {
            'statusCode': 200,
            'body': "Se creó correctamente el directorio"
        }
    else:
        return {
            'statusCode': 404,
            'body': "El bucket no existe"
        }