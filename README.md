Part 1.

URL: http://django-env.4uty6iem3a.us-west-2.elasticbeanstalk.com/

Used both methods to create via awsebcli and zip package upload via web interface.

Part 2.

1. Configured package.config in .ebextensions to pull binaries and unpack at the required path according to path defined in views.py
2. Configure routes and urls for pdfmanager to download_pdf.

URL: http://django-env.4uty6iem3a.us-west-2.elasticbeanstalk.com/download_pdf
