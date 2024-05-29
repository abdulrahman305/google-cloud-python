# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.visionai_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.app_platform import AppPlatformAsyncClient, AppPlatformClient
from .services.health_check_service import (
    HealthCheckServiceAsyncClient,
    HealthCheckServiceClient,
)
from .services.live_video_analytics import (
    LiveVideoAnalyticsAsyncClient,
    LiveVideoAnalyticsClient,
)
from .services.streaming_service import (
    StreamingServiceAsyncClient,
    StreamingServiceClient,
)
from .services.streams_service import StreamsServiceAsyncClient, StreamsServiceClient
from .services.warehouse import WarehouseAsyncClient, WarehouseClient
from .types.annotations import (
    AppPlatformCloudFunctionRequest,
    AppPlatformCloudFunctionResponse,
    AppPlatformEventBody,
    AppPlatformMetadata,
    ClassificationPredictionResult,
    ImageObjectDetectionPredictionResult,
    ImageSegmentationPredictionResult,
    NormalizedPolygon,
    NormalizedPolyline,
    NormalizedVertex,
    ObjectDetectionPredictionResult,
    OccupancyCountingPredictionResult,
    PersonalProtectiveEquipmentDetectionOutput,
    StreamAnnotation,
    StreamAnnotations,
    StreamAnnotationType,
    VideoActionRecognitionPredictionResult,
    VideoClassificationPredictionResult,
    VideoObjectTrackingPredictionResult,
)
from .types.common import Cluster, GcsSource, OperationMetadata
from .types.health_service import ClusterInfo, HealthCheckRequest, HealthCheckResponse
from .types.lva import (
    AnalysisDefinition,
    AnalyzerDefinition,
    AttributeValue,
    OperatorDefinition,
    ResourceSpecification,
    RunMode,
    RunStatus,
)
from .types.lva_resources import Analysis, Operator, Process
from .types.lva_service import (
    BatchRunProcessRequest,
    BatchRunProcessResponse,
    CreateAnalysisRequest,
    CreateOperatorRequest,
    CreateProcessRequest,
    DeleteAnalysisRequest,
    DeleteOperatorRequest,
    DeleteProcessRequest,
    GetAnalysisRequest,
    GetOperatorRequest,
    GetProcessRequest,
    ListAnalysesRequest,
    ListAnalysesResponse,
    ListOperatorsRequest,
    ListOperatorsResponse,
    ListProcessesRequest,
    ListProcessesResponse,
    ListPublicOperatorsRequest,
    ListPublicOperatorsResponse,
    OperatorQuery,
    Registry,
    ResolveOperatorInfoRequest,
    ResolveOperatorInfoResponse,
    UpdateAnalysisRequest,
    UpdateOperatorRequest,
    UpdateProcessRequest,
)
from .types.platform import (
    AcceleratorType,
    AddApplicationStreamInputRequest,
    AddApplicationStreamInputResponse,
    AIEnabledDevicesInputConfig,
    Application,
    ApplicationConfigs,
    ApplicationInstance,
    ApplicationNodeAnnotation,
    ApplicationStreamInput,
    AutoscalingMetricSpec,
    BigQueryConfig,
    CreateApplicationInstancesRequest,
    CreateApplicationInstancesResponse,
    CreateApplicationRequest,
    CreateDraftRequest,
    CreateProcessorRequest,
    CustomProcessorSourceInfo,
    DataType,
    DedicatedResources,
    DeleteApplicationInstancesRequest,
    DeleteApplicationInstancesResponse,
    DeleteApplicationRequest,
    DeleteDraftRequest,
    DeleteProcessorRequest,
    DeployApplicationRequest,
    DeployApplicationResponse,
    Draft,
    GcsOutputConfig,
    GeneralObjectDetectionConfig,
    GetApplicationRequest,
    GetDraftRequest,
    GetInstanceRequest,
    GetProcessorRequest,
    Instance,
    ListApplicationsRequest,
    ListApplicationsResponse,
    ListDraftsRequest,
    ListDraftsResponse,
    ListInstancesRequest,
    ListInstancesResponse,
    ListPrebuiltProcessorsRequest,
    ListPrebuiltProcessorsResponse,
    ListProcessorsRequest,
    ListProcessorsResponse,
    MachineSpec,
    MediaWarehouseConfig,
    ModelType,
    Node,
    OccupancyCountConfig,
    PersonalProtectiveEquipmentDetectionConfig,
    PersonBlurConfig,
    PersonVehicleDetectionConfig,
    Processor,
    ProcessorConfig,
    ProcessorIOSpec,
    ProductRecognizerConfig,
    RemoveApplicationStreamInputRequest,
    RemoveApplicationStreamInputResponse,
    ResourceAnnotations,
    StreamWithAnnotation,
    TagParsingConfig,
    TagRecognizerConfig,
    UndeployApplicationRequest,
    UndeployApplicationResponse,
    UniversalInputConfig,
    UpdateApplicationInstancesRequest,
    UpdateApplicationInstancesResponse,
    UpdateApplicationRequest,
    UpdateApplicationStreamInputRequest,
    UpdateApplicationStreamInputResponse,
    UpdateDraftRequest,
    UpdateProcessorRequest,
    VertexAutoMLVideoConfig,
    VertexAutoMLVisionConfig,
    VertexCustomConfig,
    VideoStreamInputConfig,
)
from .types.streaming_resources import (
    GstreamerBufferDescriptor,
    Packet,
    PacketHeader,
    PacketType,
    RawImageDescriptor,
    SeriesMetadata,
    ServerMetadata,
)
from .types.streaming_service import (
    AcquireLeaseRequest,
    CommitRequest,
    ControlledMode,
    EagerMode,
    EventUpdate,
    Lease,
    LeaseType,
    ReceiveEventsControlResponse,
    ReceiveEventsRequest,
    ReceiveEventsResponse,
    ReceivePacketsControlResponse,
    ReceivePacketsRequest,
    ReceivePacketsResponse,
    ReleaseLeaseRequest,
    ReleaseLeaseResponse,
    RenewLeaseRequest,
    RequestMetadata,
    SendPacketsRequest,
    SendPacketsResponse,
)
from .types.streams_resources import Channel, Event, Series, Stream
from .types.streams_service import (
    CreateClusterRequest,
    CreateEventRequest,
    CreateSeriesRequest,
    CreateStreamRequest,
    DeleteClusterRequest,
    DeleteEventRequest,
    DeleteSeriesRequest,
    DeleteStreamRequest,
    GenerateStreamHlsTokenRequest,
    GenerateStreamHlsTokenResponse,
    GetClusterRequest,
    GetEventRequest,
    GetSeriesRequest,
    GetStreamRequest,
    GetStreamThumbnailRequest,
    GetStreamThumbnailResponse,
    ListClustersRequest,
    ListClustersResponse,
    ListEventsRequest,
    ListEventsResponse,
    ListSeriesRequest,
    ListSeriesResponse,
    ListStreamsRequest,
    ListStreamsResponse,
    MaterializeChannelRequest,
    UpdateClusterRequest,
    UpdateEventRequest,
    UpdateSeriesRequest,
    UpdateStreamRequest,
)
from .types.warehouse import (
    AddCollectionItemRequest,
    AddCollectionItemResponse,
    AnalyzeAssetMetadata,
    AnalyzeAssetRequest,
    AnalyzeAssetResponse,
    AnalyzeCorpusMetadata,
    AnalyzeCorpusRequest,
    AnalyzeCorpusResponse,
    Annotation,
    AnnotationCustomizedStruct,
    AnnotationList,
    AnnotationMatchingResult,
    AnnotationValue,
    Asset,
    AssetSource,
    BoolValue,
    CircleArea,
    ClipAssetRequest,
    ClipAssetResponse,
    Collection,
    CollectionItem,
    Corpus,
    CreateAnnotationRequest,
    CreateAssetRequest,
    CreateCollectionMetadata,
    CreateCollectionRequest,
    CreateCorpusMetadata,
    CreateCorpusRequest,
    CreateDataSchemaRequest,
    CreateIndexEndpointMetadata,
    CreateIndexEndpointRequest,
    CreateIndexMetadata,
    CreateIndexRequest,
    CreateSearchConfigRequest,
    CreateSearchHypernymRequest,
    Criteria,
    DataSchema,
    DataSchemaDetails,
    DateTimeRange,
    DateTimeRangeArray,
    DeleteAnnotationRequest,
    DeleteAssetMetadata,
    DeleteAssetRequest,
    DeleteCollectionMetadata,
    DeleteCollectionRequest,
    DeleteCorpusRequest,
    DeleteDataSchemaRequest,
    DeleteIndexEndpointMetadata,
    DeleteIndexEndpointRequest,
    DeleteIndexMetadata,
    DeleteIndexRequest,
    DeleteSearchConfigRequest,
    DeleteSearchHypernymRequest,
    DeployedIndex,
    DeployedIndexReference,
    DeployIndexMetadata,
    DeployIndexRequest,
    DeployIndexResponse,
    FacetBucket,
    FacetBucketType,
    FacetGroup,
    FacetProperty,
    FacetValue,
    FloatRange,
    FloatRangeArray,
    GenerateHlsUriRequest,
    GenerateHlsUriResponse,
    GenerateRetrievalUrlRequest,
    GenerateRetrievalUrlResponse,
    GeoCoordinate,
    GeoLocationArray,
    GetAnnotationRequest,
    GetAssetRequest,
    GetCollectionRequest,
    GetCorpusRequest,
    GetDataSchemaRequest,
    GetIndexEndpointRequest,
    GetIndexRequest,
    GetSearchConfigRequest,
    GetSearchHypernymRequest,
    ImageQuery,
    ImportAssetsMetadata,
    ImportAssetsRequest,
    ImportAssetsResponse,
    Index,
    IndexAssetMetadata,
    IndexAssetRequest,
    IndexAssetResponse,
    IndexedAsset,
    IndexEndpoint,
    IndexingStatus,
    IngestAssetRequest,
    IngestAssetResponse,
    IntRange,
    IntRangeArray,
    ListAnnotationsRequest,
    ListAnnotationsResponse,
    ListAssetsRequest,
    ListAssetsResponse,
    ListCollectionsRequest,
    ListCollectionsResponse,
    ListCorporaRequest,
    ListCorporaResponse,
    ListDataSchemasRequest,
    ListDataSchemasResponse,
    ListIndexEndpointsRequest,
    ListIndexEndpointsResponse,
    ListIndexesRequest,
    ListIndexesResponse,
    ListSearchConfigsRequest,
    ListSearchConfigsResponse,
    ListSearchHypernymsRequest,
    ListSearchHypernymsResponse,
    Partition,
    RemoveCollectionItemRequest,
    RemoveCollectionItemResponse,
    RemoveIndexAssetMetadata,
    RemoveIndexAssetRequest,
    RemoveIndexAssetResponse,
    SchemaKeySortingStrategy,
    SearchAssetsRequest,
    SearchAssetsResponse,
    SearchCapability,
    SearchCapabilitySetting,
    SearchConfig,
    SearchCriteriaProperty,
    SearchHypernym,
    SearchIndexEndpointRequest,
    SearchIndexEndpointResponse,
    SearchResultItem,
    StringArray,
    UndeployIndexMetadata,
    UndeployIndexRequest,
    UndeployIndexResponse,
    UpdateAnnotationRequest,
    UpdateAssetRequest,
    UpdateCollectionRequest,
    UpdateCorpusRequest,
    UpdateDataSchemaRequest,
    UpdateIndexEndpointMetadata,
    UpdateIndexEndpointRequest,
    UpdateIndexMetadata,
    UpdateIndexRequest,
    UpdateSearchConfigRequest,
    UpdateSearchHypernymRequest,
    UploadAssetMetadata,
    UploadAssetRequest,
    UploadAssetResponse,
    UserSpecifiedAnnotation,
    ViewCollectionItemsRequest,
    ViewCollectionItemsResponse,
    ViewIndexedAssetsRequest,
    ViewIndexedAssetsResponse,
)

__all__ = (
    "AppPlatformAsyncClient",
    "HealthCheckServiceAsyncClient",
    "LiveVideoAnalyticsAsyncClient",
    "StreamingServiceAsyncClient",
    "StreamsServiceAsyncClient",
    "WarehouseAsyncClient",
    "AIEnabledDevicesInputConfig",
    "AcceleratorType",
    "AcquireLeaseRequest",
    "AddApplicationStreamInputRequest",
    "AddApplicationStreamInputResponse",
    "AddCollectionItemRequest",
    "AddCollectionItemResponse",
    "Analysis",
    "AnalysisDefinition",
    "AnalyzeAssetMetadata",
    "AnalyzeAssetRequest",
    "AnalyzeAssetResponse",
    "AnalyzeCorpusMetadata",
    "AnalyzeCorpusRequest",
    "AnalyzeCorpusResponse",
    "AnalyzerDefinition",
    "Annotation",
    "AnnotationCustomizedStruct",
    "AnnotationList",
    "AnnotationMatchingResult",
    "AnnotationValue",
    "AppPlatformClient",
    "AppPlatformCloudFunctionRequest",
    "AppPlatformCloudFunctionResponse",
    "AppPlatformEventBody",
    "AppPlatformMetadata",
    "Application",
    "ApplicationConfigs",
    "ApplicationInstance",
    "ApplicationNodeAnnotation",
    "ApplicationStreamInput",
    "Asset",
    "AssetSource",
    "AttributeValue",
    "AutoscalingMetricSpec",
    "BatchRunProcessRequest",
    "BatchRunProcessResponse",
    "BigQueryConfig",
    "BoolValue",
    "Channel",
    "CircleArea",
    "ClassificationPredictionResult",
    "ClipAssetRequest",
    "ClipAssetResponse",
    "Cluster",
    "ClusterInfo",
    "Collection",
    "CollectionItem",
    "CommitRequest",
    "ControlledMode",
    "Corpus",
    "CreateAnalysisRequest",
    "CreateAnnotationRequest",
    "CreateApplicationInstancesRequest",
    "CreateApplicationInstancesResponse",
    "CreateApplicationRequest",
    "CreateAssetRequest",
    "CreateClusterRequest",
    "CreateCollectionMetadata",
    "CreateCollectionRequest",
    "CreateCorpusMetadata",
    "CreateCorpusRequest",
    "CreateDataSchemaRequest",
    "CreateDraftRequest",
    "CreateEventRequest",
    "CreateIndexEndpointMetadata",
    "CreateIndexEndpointRequest",
    "CreateIndexMetadata",
    "CreateIndexRequest",
    "CreateOperatorRequest",
    "CreateProcessRequest",
    "CreateProcessorRequest",
    "CreateSearchConfigRequest",
    "CreateSearchHypernymRequest",
    "CreateSeriesRequest",
    "CreateStreamRequest",
    "Criteria",
    "CustomProcessorSourceInfo",
    "DataSchema",
    "DataSchemaDetails",
    "DataType",
    "DateTimeRange",
    "DateTimeRangeArray",
    "DedicatedResources",
    "DeleteAnalysisRequest",
    "DeleteAnnotationRequest",
    "DeleteApplicationInstancesRequest",
    "DeleteApplicationInstancesResponse",
    "DeleteApplicationRequest",
    "DeleteAssetMetadata",
    "DeleteAssetRequest",
    "DeleteClusterRequest",
    "DeleteCollectionMetadata",
    "DeleteCollectionRequest",
    "DeleteCorpusRequest",
    "DeleteDataSchemaRequest",
    "DeleteDraftRequest",
    "DeleteEventRequest",
    "DeleteIndexEndpointMetadata",
    "DeleteIndexEndpointRequest",
    "DeleteIndexMetadata",
    "DeleteIndexRequest",
    "DeleteOperatorRequest",
    "DeleteProcessRequest",
    "DeleteProcessorRequest",
    "DeleteSearchConfigRequest",
    "DeleteSearchHypernymRequest",
    "DeleteSeriesRequest",
    "DeleteStreamRequest",
    "DeployApplicationRequest",
    "DeployApplicationResponse",
    "DeployIndexMetadata",
    "DeployIndexRequest",
    "DeployIndexResponse",
    "DeployedIndex",
    "DeployedIndexReference",
    "Draft",
    "EagerMode",
    "Event",
    "EventUpdate",
    "FacetBucket",
    "FacetBucketType",
    "FacetGroup",
    "FacetProperty",
    "FacetValue",
    "FloatRange",
    "FloatRangeArray",
    "GcsOutputConfig",
    "GcsSource",
    "GeneralObjectDetectionConfig",
    "GenerateHlsUriRequest",
    "GenerateHlsUriResponse",
    "GenerateRetrievalUrlRequest",
    "GenerateRetrievalUrlResponse",
    "GenerateStreamHlsTokenRequest",
    "GenerateStreamHlsTokenResponse",
    "GeoCoordinate",
    "GeoLocationArray",
    "GetAnalysisRequest",
    "GetAnnotationRequest",
    "GetApplicationRequest",
    "GetAssetRequest",
    "GetClusterRequest",
    "GetCollectionRequest",
    "GetCorpusRequest",
    "GetDataSchemaRequest",
    "GetDraftRequest",
    "GetEventRequest",
    "GetIndexEndpointRequest",
    "GetIndexRequest",
    "GetInstanceRequest",
    "GetOperatorRequest",
    "GetProcessRequest",
    "GetProcessorRequest",
    "GetSearchConfigRequest",
    "GetSearchHypernymRequest",
    "GetSeriesRequest",
    "GetStreamRequest",
    "GetStreamThumbnailRequest",
    "GetStreamThumbnailResponse",
    "GstreamerBufferDescriptor",
    "HealthCheckRequest",
    "HealthCheckResponse",
    "HealthCheckServiceClient",
    "ImageObjectDetectionPredictionResult",
    "ImageQuery",
    "ImageSegmentationPredictionResult",
    "ImportAssetsMetadata",
    "ImportAssetsRequest",
    "ImportAssetsResponse",
    "Index",
    "IndexAssetMetadata",
    "IndexAssetRequest",
    "IndexAssetResponse",
    "IndexEndpoint",
    "IndexedAsset",
    "IndexingStatus",
    "IngestAssetRequest",
    "IngestAssetResponse",
    "Instance",
    "IntRange",
    "IntRangeArray",
    "Lease",
    "LeaseType",
    "ListAnalysesRequest",
    "ListAnalysesResponse",
    "ListAnnotationsRequest",
    "ListAnnotationsResponse",
    "ListApplicationsRequest",
    "ListApplicationsResponse",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListClustersRequest",
    "ListClustersResponse",
    "ListCollectionsRequest",
    "ListCollectionsResponse",
    "ListCorporaRequest",
    "ListCorporaResponse",
    "ListDataSchemasRequest",
    "ListDataSchemasResponse",
    "ListDraftsRequest",
    "ListDraftsResponse",
    "ListEventsRequest",
    "ListEventsResponse",
    "ListIndexEndpointsRequest",
    "ListIndexEndpointsResponse",
    "ListIndexesRequest",
    "ListIndexesResponse",
    "ListInstancesRequest",
    "ListInstancesResponse",
    "ListOperatorsRequest",
    "ListOperatorsResponse",
    "ListPrebuiltProcessorsRequest",
    "ListPrebuiltProcessorsResponse",
    "ListProcessesRequest",
    "ListProcessesResponse",
    "ListProcessorsRequest",
    "ListProcessorsResponse",
    "ListPublicOperatorsRequest",
    "ListPublicOperatorsResponse",
    "ListSearchConfigsRequest",
    "ListSearchConfigsResponse",
    "ListSearchHypernymsRequest",
    "ListSearchHypernymsResponse",
    "ListSeriesRequest",
    "ListSeriesResponse",
    "ListStreamsRequest",
    "ListStreamsResponse",
    "LiveVideoAnalyticsClient",
    "MachineSpec",
    "MaterializeChannelRequest",
    "MediaWarehouseConfig",
    "ModelType",
    "Node",
    "NormalizedPolygon",
    "NormalizedPolyline",
    "NormalizedVertex",
    "ObjectDetectionPredictionResult",
    "OccupancyCountConfig",
    "OccupancyCountingPredictionResult",
    "OperationMetadata",
    "Operator",
    "OperatorDefinition",
    "OperatorQuery",
    "Packet",
    "PacketHeader",
    "PacketType",
    "Partition",
    "PersonBlurConfig",
    "PersonVehicleDetectionConfig",
    "PersonalProtectiveEquipmentDetectionConfig",
    "PersonalProtectiveEquipmentDetectionOutput",
    "Process",
    "Processor",
    "ProcessorConfig",
    "ProcessorIOSpec",
    "ProductRecognizerConfig",
    "RawImageDescriptor",
    "ReceiveEventsControlResponse",
    "ReceiveEventsRequest",
    "ReceiveEventsResponse",
    "ReceivePacketsControlResponse",
    "ReceivePacketsRequest",
    "ReceivePacketsResponse",
    "Registry",
    "ReleaseLeaseRequest",
    "ReleaseLeaseResponse",
    "RemoveApplicationStreamInputRequest",
    "RemoveApplicationStreamInputResponse",
    "RemoveCollectionItemRequest",
    "RemoveCollectionItemResponse",
    "RemoveIndexAssetMetadata",
    "RemoveIndexAssetRequest",
    "RemoveIndexAssetResponse",
    "RenewLeaseRequest",
    "RequestMetadata",
    "ResolveOperatorInfoRequest",
    "ResolveOperatorInfoResponse",
    "ResourceAnnotations",
    "ResourceSpecification",
    "RunMode",
    "RunStatus",
    "SchemaKeySortingStrategy",
    "SearchAssetsRequest",
    "SearchAssetsResponse",
    "SearchCapability",
    "SearchCapabilitySetting",
    "SearchConfig",
    "SearchCriteriaProperty",
    "SearchHypernym",
    "SearchIndexEndpointRequest",
    "SearchIndexEndpointResponse",
    "SearchResultItem",
    "SendPacketsRequest",
    "SendPacketsResponse",
    "Series",
    "SeriesMetadata",
    "ServerMetadata",
    "Stream",
    "StreamAnnotation",
    "StreamAnnotationType",
    "StreamAnnotations",
    "StreamWithAnnotation",
    "StreamingServiceClient",
    "StreamsServiceClient",
    "StringArray",
    "TagParsingConfig",
    "TagRecognizerConfig",
    "UndeployApplicationRequest",
    "UndeployApplicationResponse",
    "UndeployIndexMetadata",
    "UndeployIndexRequest",
    "UndeployIndexResponse",
    "UniversalInputConfig",
    "UpdateAnalysisRequest",
    "UpdateAnnotationRequest",
    "UpdateApplicationInstancesRequest",
    "UpdateApplicationInstancesResponse",
    "UpdateApplicationRequest",
    "UpdateApplicationStreamInputRequest",
    "UpdateApplicationStreamInputResponse",
    "UpdateAssetRequest",
    "UpdateClusterRequest",
    "UpdateCollectionRequest",
    "UpdateCorpusRequest",
    "UpdateDataSchemaRequest",
    "UpdateDraftRequest",
    "UpdateEventRequest",
    "UpdateIndexEndpointMetadata",
    "UpdateIndexEndpointRequest",
    "UpdateIndexMetadata",
    "UpdateIndexRequest",
    "UpdateOperatorRequest",
    "UpdateProcessRequest",
    "UpdateProcessorRequest",
    "UpdateSearchConfigRequest",
    "UpdateSearchHypernymRequest",
    "UpdateSeriesRequest",
    "UpdateStreamRequest",
    "UploadAssetMetadata",
    "UploadAssetRequest",
    "UploadAssetResponse",
    "UserSpecifiedAnnotation",
    "VertexAutoMLVideoConfig",
    "VertexAutoMLVisionConfig",
    "VertexCustomConfig",
    "VideoActionRecognitionPredictionResult",
    "VideoClassificationPredictionResult",
    "VideoObjectTrackingPredictionResult",
    "VideoStreamInputConfig",
    "ViewCollectionItemsRequest",
    "ViewCollectionItemsResponse",
    "ViewIndexedAssetsRequest",
    "ViewIndexedAssetsResponse",
    "WarehouseClient",
)