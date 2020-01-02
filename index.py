from pdf2image import convert_from_bytes
import os
import boto3

s3 = boto3.resource("s3")
s3_bucket = s3.Bucket("notrfiler")


def index(event, context):
    eventkey = event['Records'][0]['s3']['object']['key']
    print(eventkey)
    base = os.path.basename(eventkey)
    nameonly = os.path.splitext(base)[0]
    print(base)
    s3.meta.client.download_file('notrfiler', eventkey, '/tmp/'+base)
    f = open('/tmp/'+base, 'rb')
    infile = f.read()
    f.close()

    poppler_path = "lib/usr/bin"
    images = convert_from_bytes(infile,
                                dpi=30,
                                # poppler_path=poppler_path,
                                first_page=0,
                                last_page=1,
                                )

    images[0].save('/tmp/' + nameonly + 'png', 'PNG')
    f = open('/tmp/' + nameonly + 'png', 'rb')
    s3_bucket.put_object(Key='preview/'+nameonly + '.png', Body=f, ACL="public-read")

    return 'ok'

