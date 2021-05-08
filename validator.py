from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
import time

from google.cloud import pubsub_v1

# https://pythonhosted.org/Flask-Inputs/#module-flask_inputs
# https://json-schema.org/understanding-json-schema/
# noinspection SpellCheckingInspection
message_payload = {
    "type": "object",
    "properties": {
        "activities": {
            "type": "array",
            "items": {"anyOf": [{"$ref": "#/$defs/insert"}, {"$ref": "#/$defs/delete"}]},
            "minItems": 1
        }
    },
    "$defs": {
        "insert": {
            "type": "object",
            "required": ["operation", "table", "col_names", "col_types", "col_values"],
            "properties": {
                "operation": {"const": "insert"},
                "table": {"type": "string"},
                "col_names": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "col_types": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "col_values": {
                    "type": "array"
                }
            }
        },
        "delete": {
            "type": "object",
            "required": ["operation", "table", "old_value"],
            "properties": {
                "operation": {"const": "delete"},
                "table": {"type": "string"},
                "old_value": {
                    "type": "object",
                    "required": ["col_names", "col_types", "col_values"],
                    "properties": {
                        "col_names": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "col_types": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "col_values": {
                            "type": "array"
                        }
                    }
                }
            }
        }
    }
}


class ActivitiesInput(Inputs):
    json = [JsonSchema(schema=message_payload)]

invalid_message = []

project_id = "academi-week2"
topic_id = "api-gatekeeper"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def validate_message(request):
    inputs = ActivitiesInput(request)
    if inputs.validate():
        # push to pubsub cluster
        future = publisher.publish(topic_path, str(request.data).encode("utf-8"))
        return print(future.result())
    else:
        invalid_message.append(inputs.errors[0])
        return "Invalid Message: " + str(len(invalid_message))