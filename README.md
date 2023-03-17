# Redpanda BYOC Demo


Here is a quick demo showcasing different ways you can connect to the Redpanda BYOC cluster. 

A simulator microservices(python) is deployed in Kubernetes and continuously publishes signal events, the Kubernetes cluster sits in its own VPC and is now connecting to the Redpanda cluster via VPC peering. 
Another consumer client(Java Quarkus) consumes the events externally. I have set up the BYOC in a public subnet, therefore it can connect via the internet gateway. 

The signal also triggers a Lambda serverless application, instead of using an MSK or SNS. The Lambda service also sits in its own VPC, in order to connect them, similar to AWS MSK and Kinesis,  establishing an VPC peering connection will do the trick. In my example, for better security, I have enabled SASL for authentication purposes. I choose to use the secret manager to store the credentials for Lamba triggers. In this case, make sure you update the access policy for your lambda role, so it has permission to get the credential stored. 

![Demo Architecture](images/demo-architecture.png)



## Setup (Prerequisite)

You will need to have an EKS already running in it's own VPC 
and an empty VPC with one AZ, private subnet. 
 - TODO automate EKS & 2 VPCs


## Create an BYOC Redpanda Cluster
See documentation or video

## Start the Consumers

### Running the external java consumer on your local machine. 

mvn quarkus:dev

### Running the serverless Lambda app.



## Deploy the Python publisher

Make sure you have access and logged into the EKS for running the microservice applications. 

Create a new namespace to run the microservices.

Add configuration with credentials needed to communicate to Redpanda cluster.

Deploy the python application and start sending random events into the cluster. 

