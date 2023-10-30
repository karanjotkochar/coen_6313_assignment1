COEN 6313
Assignment 1 

### Installing Dependencies
1. Unzip and extract the file to the system
2. Install the requiremnets for the Python files using command: (pip install -r requirements.txt)
3. For the successful running of both the servers and clients, one needs to have protobuf server installed. 
4. You can install it using this link (https://developers.google.com/protocol-buffers) and follow the instructions depending upon your OS.
5. (Additional) For generating python file from proto file in the same directory use command: (protoc -I. ./<filename>.proto --python_out=.)

### Running JSON Based (De) - Serialization:
1. Run 'python jsonServer.py' 
2. Your server should be running.
2. Run 'python jsonClient.py'
3. Enter the values as asked.
4. You should get a response.

### Running Binary Based Serialization:
1. Run 'python protoServer.py' 
2. Your server should be running.
2. Run 'python protoClient.py'
3. Enter the values as asked.
4. You should get a response.

### Deployment - Deployed our application on AWS EC2 instance.
.