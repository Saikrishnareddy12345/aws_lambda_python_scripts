import json
import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')
def lambda_handler(event, context):
    # TODO implement
    try:
        # TODO: write code...
        instanc_id='i-0ceccfd29fee7faa8'
        stop=ec2.start_instances(InstanceIds=[instanc_id])
        print("started the instance...")
        return stop
    except Exception as e:
        print(f'error starting the instance {instanc_id}: {str(e)}')
        raise e
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    #}
