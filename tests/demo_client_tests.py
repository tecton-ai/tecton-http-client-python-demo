import os
from typing import Final

from demo.demo_client import DemoClient


class TestDemoClient:
    url: Final[str] = "https://app.tecton.ai"
    api_key: Final[str] = os.getenv("TECTON_API_KEY")

    client = DemoClient(url, api_key)

    # Required Join Key Map and Request Context Map data, to be encapsulated in the GetFeatureRequestData object
    join_key_map = {"user_id": "user_469998441571"}
    request_context_map = {"amt": 12345678.9, "merch_lat": 30.0, "merch_long": 35.0}

    def test_demo_client_get_features(self) -> None:
        response = self.client.get_features(
            join_key_map=self.join_key_map, request_context_map=self.request_context_map
        )

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

    def test_demo_client_get_features_batch(self) -> None:
        batch_response = self.client.get_features_batch(
            join_key_map=self.join_key_map, request_context_map=self.request_context_map
        )

        print("")
        print("---------------------------------------")

        print("Count of responses: ", len(batch_response.batch_response_list))
        print("Count of None responses: ", batch_response.batch_response_list.count(None))

        print("---------------------------------------")
        print("Total time taken: ", batch_response.request_latency.total_seconds())
        print("---------------------------------------")

        # Access SLO_INFO information if requested in the test_request
        if batch_response.batch_slo_info:
            print(vars(batch_response.batch_slo_info))

        # Get a mapping of name and feature value from the feature values in the response
        for response in batch_response.batch_response_list:
            if response:
                print({k: v.feature_value for k, v in response.feature_values.items()})


    def test_demo_client_get_feature_service_metadata(self) -> None:
        metadata_response = self.client.get_feature_service_metadata()

        print("")
        print("--------------------")
        print("Feature Service Type: ", metadata_response.feature_service_type)
        print("Input Join Keys: ", metadata_response.input_join_keys)
        print("Input Request Context Keys: ", metadata_response.input_request_context_keys)
        print("Feature Values: ", metadata_response.feature_values)
        print("Output Join Keys: ", metadata_response.output_join_keys)

        # Print the details of each feature in the response
        print("Input Join Keys:")
        for key, value in metadata_response.input_join_keys.items():
            print("Name: ", key)
            print("Type: ", value.data_type)

    def pytest_sessionfinish(self) -> None:
        self.client.close()
