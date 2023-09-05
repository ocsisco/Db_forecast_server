from dotenv import load_dotenv
import boto3
import os

load_dotenv()

AWS_ACCESS_KEY_ID=os.getenv("ENV_AWS_ACCES_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.getenv("ENV_AWS_SECRET_ACCESS_KEY")



"""Descarga las imagenes de S3"""

def download_s3_images(folderfrom,folderto,filename):

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    s3.download_file("awsradarimages", folderfrom + "/" + filename, folderto + "/" + filename)
    


"""Extrae lista de las imagenes disponibles en S3"""

def get_s3_imagelist_from(name_folder):

    images_list = []

    s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    response = s3.list_objects_v2(Bucket="awsradarimages", Prefix=name_folder)
    files = response.get("Contents")

    for file in files:

        image_name = file['Key']
        image_name = image_name.replace(name_folder+"/","")
        images_list.append(image_name)

    images_list.pop(0)

    return(images_list)

