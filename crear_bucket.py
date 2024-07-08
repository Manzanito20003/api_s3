import boto3
import botocore

def lambda_handler(event, context):
    # Entrada
    s3 = boto3.client('s3')
    bucket_name = event['body']['name']
    
    try:
        # Intentar crear el bucket
        s3.create_bucket(
            Bucket=bucket_name, 
          
        )
        
        # Salida
        return {
            'statusCode': 200,
            'body': "Se creó correctamente el bucket"
        }
        
    except botocore.exceptions.ClientError as e:
        # Manejar errores del cliente
        return {
            'statusCode': 500,
            'body': f"Error al crear el bucket: {e.response['Error']['Message']}"
        }
