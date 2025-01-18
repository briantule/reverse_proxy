# Getting started with the Reverse Proxy (Flask) Application

This guide will walk you through the process of cloning, setting up, and running the Flask-based reverse proxy application.

## Prerequisites

Ensure you have the following installed:

- **Git**: To clone the repository
- **Python 3.x**: To run the application
- **pip**: To install dependencies
- A reverse proxy server (e.g., **Nginx** or **Apache**) for production environments (optional)

## Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone git@github.com:briantule/reverse_proxy.git
```

Navigate to the project directory:
```bash
cd reverse_proxy
```

## Step 2: Set Up the Virtual Environment
It is recommended to use a virtual environment to manage dependencies for this application. Follow these steps:
1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate the virtual environment:
- On macOS/Linux:
```bash
source venv/bin/activate
```

- On Windows:
```bash
venv\Scripts\activate
```

3. Install the dependencies
```bash
pip install -r requirements.txt
```

## Step 3: Running the Application
Once the environment is set up, you can run the Flask application locally. Two terminals will be needed to test.
1. Run the reverse proxy application on terminal 1:
```bash
python src/reverse_proxy/router.py
```

1. Run the sample client application on terminal 2:
```bash
python src/utils/client.py
```

## Step 4: Test the Application
### Get:
```bash
curl http://localhost:8100/status
```
```bash
curl http://localhost:8100/greet
```

### Post:
```bash
curl -X POST http://localhost:8100/echo \
     -H "Content-Type: application/json" \
     -d '{"key": "value"}'
```

```bash
curl -X POST http://localhost:8100/form-submit \
     -F "key1=value1" \
     -F "key2=value2"
```

### Put:
```bash
curl -X PUT http://localhost:8100/update-message \
     -H "Content-Type: application/json" \
     -d '{"message": "Some new message"}'
```

### Delete:
```bash
curl -X DELETE http://localhost:8100/delete-item/123 \
     -H "Content-Type: application/json" \
     -d '{"reason": "A solid reason"}'
```



# Assignment Questions:

## How could someone get started with your codebase?
Please view the **Getting started with the Reverse Proxy (Flask) Application** section starting from the top. Thie first second of this read me will instruct users on how they can get started with this codebase.

## What resources did you use to build your implementation?
Resources used for the implemntation of this project are listed below:

[1] “Reverse Proxy , API Gateway | API Essentials,” YouTube, https://www.youtube.com/watch?v=c8pV3F6GD3o (accessed Jan. 18, 2025). 

[2] “Proxy vs Reverse Proxy (Real-world Examples),” YouTube, https://www.youtube.com/watch?v=4NB0NDtOwIQ&t=192s (accessed Jan. 18, 2025). 

[3] Thebytestream, “Reverse proxy,” Medium, https://thebytestream.medium.com/reverse-proxy-d0ff1b7b2231 (accessed Jan. 18, 2025). 

These resources were sufficient in providing the basic concept of a reverse proxy and what implementation could look like.

## Explain any design decisions you made, including limitations of the system.
The stack was chosen based off of familiarity with the language and ease of use for http handling. For an entry into understanding reverse proxy, users can benefit from the easy integration and minimal overhead of this tech stack.

From a systems design aspect, there are several limitations including:
- **Lack of Caching:** Requests of the same data multiple times would be inneficient 
- **System resilience:** This is a single server running this application so this poses as a single point of failure. If the system were to go down or become unavailable, the entire service would now be unavailable.
- **Scalability:** Because this is a single server running this application, there is currently no support for scalability. Requests are being processed one at a time so an increase in load will not scale well.
- **Load Balancing:** There is now current system to handle the distribution of incomming traggic as this is just a single server used to test the proxy. Incoming traffic will be inefficiently processed one request at a time potentially leading to a proxy instance being overwhelmed.
- **Authentication and Authorization:** This sample proxy currently does not support/enforce any form of authentication or authorization. Technically, anyone who has access to this proxy will be able to make requests. In an applied environemnt, this poses risks on exposeing sensitive data or misuse.

## How would you scale this?
There are several ways in which this application can be scaled. Although this is more of a proof of concept application, we can think beyond the scope exploring how we can handle increased load, reliability, and maintainence. Some steps I may take include:

- **Horizontal Scaling:** This POC is meant to be run on just a single system. In production/professional environments, I would look to deploy multiple instances of this reverse proxy so that multiple requests could be handled concurrently recuding the stress on a particular server. 
- **Load Balancing:** This builds on with horizontal scaling, as I would look to implement mechanisms to effectively distribute requests across the multiple servers running this reverse proxy. This would reduce the load/stress towards an individual server increasing the reliability as we increase the amount of requests made.
- **Caching:** Another way in which we can reduce the load on our server would be to introduce caching. Frequently requested data can be stored for quicker response times again taking away stress from the proxy level of this system.
- **Rate Limiting:** Scaling also means that we should implement methods to protect our system from failing when the load size as increase on it. Throttling/Rate limiting reuqests is a great way for us to protect our system ensuring availability and fair use of its resources. 

## How would you make it more secure?
There are a lot of methods in which we can make our reverse proxy more secure. These methods would be used to ensure that our data is being protected from each requests and our services are being protected from abuse. Some potential solutions I would look to implement in the future include:

- **Authentication and Authorization:** One of the most simplests ways in which we can make this more secure would be to integrate forms of authentication and authorization. We would be able to control and monitor who has access to our services and data.
- **Logging/Monitoring:** Logging would be really beneficial especially with the implemntation of authentication and authorization. Some applications of this include being able to view all authentication attempts, monitoring any suspicious request attempts or patterns or detecting any sensitive information such as secrests, tokens, etc.
- **Encription:** Encripting all of our communication would provide the extra layer of projection to our system as this would ensure that the data can not be intercepted by attackers during transit.
- **Rate Limiting:** Mentioned in the previous question not only would rate limiting project our system and increase the availability of our system, it also projects our proxy from potential abuse and DoS attacks.