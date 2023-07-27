import os
from typing import Final

from demo.demo_client import DemoClient


def test_demo_client_get_features() -> None:
    url: Final[str] = "https://app.tecton.ai"
    api_key: Final[str] = os.getenv("TECTON_API_KEY")

    client = DemoClient(url, api_key)

    # Required Join Key Map and Request Context Map data, to be encapsulated in the GetFeatureRequestData object
    join_key_map = {"user_id": "user_469998441571"}
    request_context_map = {"amt": 12345678.9, "merch_lat": 30.0, "merch_long": 35.0}

    response = client.get_features(join_key_map=join_key_map, request_context_map=request_context_map)

    # Access SLO_INFO information if requested in the test_request
    print(vars(response.slo_info))

    # Get a mapping of name and feature value from the feature values in the response
    print({k: v.feature_value for k, v in response.feature_values.items()})

    # Print the details of each feature in the response
    for name, feature in response.feature_values.items():
        print("--------------------")
        print("Name in response: ", name)
        print("Feature Namespace: ", feature.feature_namespace)
        print("Feature Name: ", feature.feature_name)
        print("Feature Value: ", feature.feature_value)

        # Data type of the feature value
        print("Feature Value Type: ", feature.data_type)

        # These two fields are only available if requested in the metadata options of the test_request
        print("Feature Status: ", feature.feature_status)
        print("Feature Effective Time: ", feature.effective_time)

    # Always close the created client
    client.close()
