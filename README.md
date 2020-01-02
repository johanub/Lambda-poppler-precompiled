# Lambda-poppler-precompiled
pdf to img, pdf to text.. and so on!!

I have created this repo out of furstration by the lack of documantation and general help in concern to working with pdf documents on aws lambda.

## Getting Started

These instructions will get you a copy of the project up to run it on lambda

### Installing

A step by step on how to setup using my sample script witch uses poppler to create thumbnails for pdf files.

1. Clone the project
```
git clone https://github.com/johanub/Lambda-poppler-precompiled
```

2. Edit the index.py file to use your bucket
```
s3_bucket = s3.Bucket("<your-bucket>")
```

3. Navigate into the project directorty and zip the files using this command
```
zip -r -X "app.zip" *
```
4. Now go to the aws lambda console and and go into layer

5. Make a new layer with the ```poppler.zip``` file. For runtime just choose all the python runtimes.
<img src="https://github.com/johanub/Lambda-poppler-precompiled/blob/master/step-by-step-pictures/layer-pic.png">

6. Create a new lambda function and upload the file```app.zip``` 

7. Select the layer witch we just made.
<img src="https://github.com/johanub/Lambda-poppler-precompiled/blob/master/step-by-step-pictures/lambda-pic.png">

8. Setup a trigger on the s3 bucket where the pdf's will be uploaded

9. Go to the bucket and make a directory called ```previews```
Explain how to run the automated tests for this system

10. Upload a pdf to your s3 and see the magic


## Based on
* **Pavinthan** - *Poppler for aws lambda* - [Pavinthan](https://github.com/jeylabs/aws-lambda-poppler-layer)
