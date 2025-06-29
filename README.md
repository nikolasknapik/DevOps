# Aplication excercise
# Introduction
This are quick excercises to demonstrate various DevOps skills. From the start I would like to state the I have never worked with any of these programs so I had to learn how to work with them in these two days. Which to say was very interesting and fun. It has given me a lot knowledge on these kind of tools and programs for which I am very glad.
# Section 1
## TASK A
This task demonstrates how to provision AWS infrastructure using Terraform insede a Docker container

### What it does
- Uses docker compose to run terraform in an isolated container
- Creates a AWS VPC setup including:
    - Public and private subnets
    - Internet Gateway for public subnets
    - NAT Gateway for prvite subnets
- Uses Terrafrom modules to organize the infrastructure code in /modules/network
- Defines variables.tf, outputs.tf for input and output handling

### How to use
1. Run container with docker compose
2. Inside the container, execute terraform init and terraform validate

Because I dont currently have an account on AWS I could not test if the infrastructure is able to acces it. I could just test if it is syntacticly correct

## TASK_B

This task sets up a simple Flask web application running inside a Docker container

### What it does
- Creates a minimal Flask app that displays "hacking" messages on user input
- Wraps the app in a Docker container using:
    - Dockerfile that defines the Python enviroment and how to run the app
    - docker-compose.yml - make it easy to build and run the app locally
### How to run

Run the task using dockerc compose up and the app will be availeable at http://localhost:5000/

# Section 2
Section 2 focues on real problem solving

The the text files in the section-2/ directory contain my answers to the problem. 

# Section 3
Similairly to the section 2. Section 3 consists of real world problems and how to solve them with me giving the steps of how to solve each problem. The text files can be found in the section-3/ directory.

# Summary
This application tasks made me test myself in topics I have not yet cover and I am gald that it did. It tought me much valuable information and pushed me another step froward in my IT path.