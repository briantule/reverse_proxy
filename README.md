# Getting started with the Reverse Proxy (Flask) Application

This guide will walk you through the process of cloning, setting up, and running the Flask-based reverse proxy application.

## Step 0: Understanding this POC

This POC will have two main files: router.py and client.py. Router.py will act as our reverse proxy service and client.py will act as our web service. We will run both services on their respective ports (8100 & 5001).

Requests made to the reverse proxy (port 8100) will be redirected to the web server (port 5001). The respective responses from the web server will then get directred back to the client. The same pattern flow is applied for all api standard request types GET, POST, PUT, DELETE. Thus, this will facilitate the basic logic of a reverse proxy. 

This skeleton code can be used to explore the basic priciples, applications and benefits of a reverse proxy. Some improvements (scalability and security) that can be built from this would include load balancing, caching, and encryption.

## Prerequisites

Ensure you have the following installed:

- **Git**: To clone the repository
- **Python 3.x**: To run the application
- **pip**: To install dependencies

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
python3 -m venv venv
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
pip3 install -r requirements.txt
```

## Step 3: Running the Application
Once the environment is set up, you can run the Flask application locally. Two terminals will be needed to test.
1. Run the reverse proxy application on terminal 1:
```bash
python3 src/reverse_proxy/router.py
```

2. Run the sample service application on terminal 2:
```bash
python3 src/utils/service.py
```

## Step 4: Test the Application
With the system running, feel free to use the sample curl commands (in terminal) or resort to other methods for making these API calls such as browser or Postman.

### GET:
1. **Status Endpoint**
- **Route:** `/status`  
- **Method:** `GET`  
- **Description:** Returns a simple message confirming the Flask application is running.  
- **Response Example:** Flask application is up and running!
- **Curl Example:**
```bash
curl http://localhost:8100/status
```

2. **Greet Endpoint**
- **Route:** `/greet`  
- **Method:** `GET`  
- **Description:** Returns a greeting message in JSON format.  
- **Response Example:**
```json
{
  "message": "Hey, Cohere! My name is Brian."
}
```
- **Curl Example:**
```bash
curl http://localhost:8100/greet
```

### POST:
1. **Echo Endpoint**
- **Route:** `/echo`  
- **Method:** `POST`  
- **Description:** Accepts a JSON payload and returns the same payload in the response.
- **Request Example:** 
```json
{
  "key": "value"
}
```
- **Response Example:**
```json
{
  "key": "value"
}
```
- **Curl Example:**
```bash
curl -X POST http://localhost:8100/echo \
     -H "Content-Type: application/json" \
     -d '{"key": "value"}'
```

2. **Form Submit Endpoint**
- **Route:** `/form-submit`  
- **Method:** `POST`  
- **Description:** Accepts form data and returns the submitted data in the response.
- **Request Example:** 
key1=value1,
key2=value2
- **Response Example:**
```json
{
  "key1": "value1",
  "key2": "value2"
}
```
- **Curl Example:**
```bash
curl -X POST http://localhost:8100/form-submit \
     -F "key1=value1" \
     -F "key2=value2"
```

### PUT:
1. **Update Message Endpoint**
- **Route:** `/update-message`  
- **Method:** `PUT`  
- **Description:** Updates a message based on the provided JSON payload and returns the updated message in the response.
- **Request Example:** 
```json
{
  "message": "Some new message"
}
```
- **Response Example:**
```json
{
  "updated_message": "Some new message"
}
```
- **Curl Example:**
```bash
curl -X PUT http://localhost:8100/update-message \
     -H "Content-Type: application/json" \
     -d '{"message": "Some new message"}'
```

### DELETE:
1. **Delete Item Endpoint**
- **Route:** `/delete-item/<item_id>`  
- **Method:** `DELETE`  
- **Description:** Deletes the specified item by its item_id and accepts an optional JSON payload with a reason for deletion. Returns a confirmation message.
- **Request Example:** 
  - **URL Parameter:** item_id = 123
  - **JSON Payload:**
```json
{
  "reason": "A solid reason"
}
```
- **Response Example:**
```json
{
  "item_id": 123,
  "status": "deleted",
  "reason": "A solid reason"
}
```
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