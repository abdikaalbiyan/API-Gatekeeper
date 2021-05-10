# API-Gatekeeper
Create API to validate JSON input, send and write it into database


## Installation
- >python 3.7
- Enabled Cloud Pub/Sub API on Google Cloud Platform.
- Create service account as an owner (Save json file to app folder)
- Activate Cloud SDK on your local device. Check this [complete guide](https://cloud.google.com/sdk/docs/quickstart)
- Install postman to your browser for post json. For complete guide, check [this page](https://www.postman.com/downloads/).
- Clone this repository ```git clone https://github.com/abdikaalbiyan/API-Gatekeeper.git```
- ```pip3 install -r requirements.txt```



## Run
On your active python environtment:
- Run ```bash pubsub.sh``` to create pubsub topic, subscription, and create BigQuery dataset
- Run ```python3 main.py```
- Run ```python3 consumer.py```
- After ```consumer.py``` is activated, go to postman (request URL: http://localhost/api/v1) and post something to check.<br>
  Example:
  ```
  {"activities": [
      {
        "operation": "insert",
        "table": "tableexample",
        "col_names": ["ax", "bx"],
        "col_types": ["integer", "string"],
        "col_values": [1, "first"]
      },
      {
        "operation": "insert",
        "table": "tableexample",
        "col_names": ["cx", "bx"],
        "col_types": ["integer", "string"],
        "col_values": [2, "second"]
      },
      {
        "operation": "insert",
        "table": "tableexample",
        "col_names": ["cx", "bx"],
        "col_types": ["integer", "string"],
        "col_values": [3, "third"]
      }]
  }
  ```

