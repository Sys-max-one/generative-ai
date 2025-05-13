import json
#1. import boto3
#Boto3 is the AWS SDK for Python
import boto3
import time
import base64

#2. Create client connection for Bedrock and S3 Services
bedrock_client = boto3.client('bedrock-runtime')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print(boto3.__version__)

#3. Store the input data (prompt) in a variable
    input_prompt = event['prompt']
    print(input_prompt)

#4. Create a Request Syntax
#https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-diffusion-1-0-text-image.html
    bedrock_response = bedrock_client.invoke_model(
        body=json.dumps({
            "text_prompts": [
                {
                    "text": input_prompt
    #                "weight": float
                }
            ],
#        "height": int,
#        "width": int,
#        "cfg_scale": 10,
#        "clip_guidance_preset": string,
#        "sampler": string,
#        "samples",
        "seed": 0,
        "steps": 30,
#        "style_preset": string,
#        "extras" :JSON object
        }),
        contentType='application/json',
        accept='application/json',
        modelId='stability.stable-diffusion-xl-v1'
    #    trace='ENABLED'|'DISABLED'|'ENABLED_FULL',
    #    guardrailIdentifier='string',
    #    guardrailVersion='string',
    #    performanceConfigLatency='standard'|'optimized'
    )
    print(bedrock_response)
#5.
#   5a. Retrieve from Dictionary,
#   5b. Convert Streaming Body to Byte using json load
    bedrock_response_body_bytes = json.loads(bedrock_response['body'].read())

#6.
#   6a. Retrieve data with artifact key
#   6b. Import Base 64
#   6c. Decode from Base64
    bedrock_response_body_bytes_base64 = bedrock_response_body_bytes['artifacts'][0]['base64']
    bedrock_response_body_bytes_base64_decode = base64.b64decode(bedrock_response_body_bytes_base64)

#7.
#   7a. Upload the File to S3 using Put Object Method
#   7c. Generate the image name to be stored in S3
    s3_bucket = 'YOUR_BUCKET_NAME'
    s3_bucket_key = 'UNIQUE_IMAGE_NAME' + '.png'
    s3_client.put_object(
        Body=bedrock_response_body_bytes_base64_decode,
        Bucket=s3_bucket,
        Key=s3_bucket_key,
        ContentType='image/png'
    )

#increase timeout for lambda function bcs of generating image, creating presigned url
#by going into Configuration of lambda function and increase timeout to 1 min

#8. Generate Pre-Signed URL
    s3_presigned_url = s3_client.generate_presigned_url(
        ClientMethod='get_object', #because from AWS API Gateway it will be GET call
        Params={
            'Bucket': s3_bucket,
            'Key': s3_bucket_key
        },
        ExpiresIn=3600
    )


    print(s3_presigned_url)

    return {
        'statusCode': 200,
        'body': s3_presigned_url
    }
