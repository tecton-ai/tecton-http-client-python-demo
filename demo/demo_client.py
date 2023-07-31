from datetime import timedelta
from typing import Final

from tecton_client.requests import GetFeaturesBatchRequest
from tecton_client.requests import GetFeaturesRequest
from tecton_client.requests import GetFeaturesRequestData
from tecton_client.requests import MetadataOptions
from tecton_client.responses import GetFeaturesBatchResponse
from tecton_client.responses import GetFeaturesResponse
from tecton_client.tecton_client import TectonClient


class DemoClient:
    # Workspace and Feature Service to query
    workspace_name: Final[str] = "tecton-fundamentals-tutorial-live"
    feature_service_name: Final[str] = "fraud_detection_feature_service"

    def __init__(self, url: str, api_key: str) -> None:
        # Create a TectonClient object to interact with the FeatureService API
        self.tecton_client: TectonClient = TectonClient(url, api_key)

    def get_features(self, join_key_map: dict, request_context_map: dict) -> GetFeaturesResponse:
        request_data = GetFeaturesRequestData(join_key_map, request_context_map)

        # Create a GetFeaturesRequest object to hold all the test_request data to be sent to the API
        request = GetFeaturesRequest(
            feature_service_name=self.feature_service_name,
            request_data=request_data,
            workspace_name=self.workspace_name,
            # Requesting SLO_INFO, EFFECTIVE_TIME, and FEATURE_STATUS explicitly in the test_request
            metadata_options={MetadataOptions.SLO_INFO, MetadataOptions.EFFECTIVE_TIME, MetadataOptions.FEATURE_STATUS},
        )

        try:
            # Use the Tecton Client get_features() function to send the test_request to the API and get a response
            response = self.tecton_client.get_features(request)
        except Exception as e:
            # Add exception handling logic here
            raise e

        return response

    def get_features_batch(self, join_key_map: dict, request_context_map: dict) -> GetFeaturesBatchResponse:
        request_data = GetFeaturesRequestData(join_key_map, request_context_map)

        # Create a GetFeaturesRequest object to hold all the test_request data to be sent to the API
        request = GetFeaturesBatchRequest(
            feature_service_name=self.feature_service_name,
            request_data_list=[request_data] * 100,
            workspace_name=self.workspace_name,
            # Requesting SLO_INFO, EFFECTIVE_TIME, and FEATURE_STATUS explicitly in the test_request
            metadata_options={MetadataOptions.SLO_INFO, MetadataOptions.EFFECTIVE_TIME, MetadataOptions.FEATURE_STATUS},
            micro_batch_size=2,
            timeout=timedelta(seconds=1),
        )

        try:
            # Use the Tecton Client get_features() function to send the test_request to the API and get a response
            response = self.tecton_client.get_features_batch(request)
        except Exception as e:
            # Add exception handling logic here
            raise e

        return response

    def close(self) -> None:
        # Always close the created client
        self.tecton_client.close()
