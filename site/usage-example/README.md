This is a basic example of how to use
the values for the serivces and 
attibultes to request pricing data
from the AWS SDK.

Notes:

- To run the script you'll need an AWS IAM
  account that's setup with programatic 
  access that allows it to access the pricing
  info via the SDK. (I don't currently have
  a guide for that)

- You'll need to have your local machine setup
  with those IAM crednetails in the location 
  required by boto3. (which is in 
  `~/.aws/credentails` for me)

- The script is in python 3

- It requires the `boto3` module
  to be installed. 

- If you're on a mac with python 3 installed
  you should be able to run:

  /bin/bash setup.bash

  That will create a virtual environment, 
  switch to it, and install `boto3`. 

- That should work on most linux distors 
  as well. 

- I don't know enough about windows to know
  how to automate the install. You'll have to 
  do that manually on your side. 



