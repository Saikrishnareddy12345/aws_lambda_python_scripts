import json,boto3

def lambda_handler(event, context):
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    instance_id="i-0ceccfd29fee7faa8"
    try:
        # TODO: write code...
        ec2=boto3.client('ec2',region_name='ap-south-1')
        stop=ec2.stop_instances(InstanceIds=[instance_id])
        print("stoping instance")
        return stop
    except Exception as e:
        print(f"instance is not found")
        raise e
    
