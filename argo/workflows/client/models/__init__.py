# coding: utf-8

# flake8: noqa
"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    The version of the OpenAPI document: 2.11.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from argo.workflows.client.models.google_protobuf_any import GoogleProtobufAny
from argo.workflows.client.models.grpc_gateway_runtime_stream_error import GrpcGatewayRuntimeStreamError
from argo.workflows.client.models.v1_aws_elastic_block_store_volume_source import V1AWSElasticBlockStoreVolumeSource
from argo.workflows.client.models.v1_affinity import V1Affinity
from argo.workflows.client.models.v1_azure_disk_volume_source import V1AzureDiskVolumeSource
from argo.workflows.client.models.v1_azure_file_volume_source import V1AzureFileVolumeSource
from argo.workflows.client.models.v1_csi_volume_source import V1CSIVolumeSource
from argo.workflows.client.models.v1_capabilities import V1Capabilities
from argo.workflows.client.models.v1_ceph_fs_volume_source import V1CephFSVolumeSource
from argo.workflows.client.models.v1_cinder_volume_source import V1CinderVolumeSource
from argo.workflows.client.models.v1_config_map_env_source import V1ConfigMapEnvSource
from argo.workflows.client.models.v1_config_map_key_selector import V1ConfigMapKeySelector
from argo.workflows.client.models.v1_config_map_projection import V1ConfigMapProjection
from argo.workflows.client.models.v1_config_map_volume_source import V1ConfigMapVolumeSource
from argo.workflows.client.models.v1_container import V1Container
from argo.workflows.client.models.v1_container_port import V1ContainerPort
from argo.workflows.client.models.v1_create_options import V1CreateOptions
from argo.workflows.client.models.v1_downward_api_projection import V1DownwardAPIProjection
from argo.workflows.client.models.v1_downward_api_volume_file import V1DownwardAPIVolumeFile
from argo.workflows.client.models.v1_downward_api_volume_source import V1DownwardAPIVolumeSource
from argo.workflows.client.models.v1_empty_dir_volume_source import V1EmptyDirVolumeSource
from argo.workflows.client.models.v1_env_from_source import V1EnvFromSource
from argo.workflows.client.models.v1_env_var import V1EnvVar
from argo.workflows.client.models.v1_env_var_source import V1EnvVarSource
from argo.workflows.client.models.v1_event import V1Event
from argo.workflows.client.models.v1_event_series import V1EventSeries
from argo.workflows.client.models.v1_event_source import V1EventSource
from argo.workflows.client.models.v1_exec_action import V1ExecAction
from argo.workflows.client.models.v1_fc_volume_source import V1FCVolumeSource
from argo.workflows.client.models.v1_flex_volume_source import V1FlexVolumeSource
from argo.workflows.client.models.v1_flocker_volume_source import V1FlockerVolumeSource
from argo.workflows.client.models.v1_gce_persistent_disk_volume_source import V1GCEPersistentDiskVolumeSource
from argo.workflows.client.models.v1_git_repo_volume_source import V1GitRepoVolumeSource
from argo.workflows.client.models.v1_glusterfs_volume_source import V1GlusterfsVolumeSource
from argo.workflows.client.models.v1_http_get_action import V1HTTPGetAction
from argo.workflows.client.models.v1_http_header import V1HTTPHeader
from argo.workflows.client.models.v1_handler import V1Handler
from argo.workflows.client.models.v1_host_alias import V1HostAlias
from argo.workflows.client.models.v1_host_path_volume_source import V1HostPathVolumeSource
from argo.workflows.client.models.v1_iscsi_volume_source import V1ISCSIVolumeSource
from argo.workflows.client.models.v1_initializer import V1Initializer
from argo.workflows.client.models.v1_initializers import V1Initializers
from argo.workflows.client.models.v1_key_to_path import V1KeyToPath
from argo.workflows.client.models.v1_label_selector import V1LabelSelector
from argo.workflows.client.models.v1_label_selector_requirement import V1LabelSelectorRequirement
from argo.workflows.client.models.v1_lifecycle import V1Lifecycle
from argo.workflows.client.models.v1_list_meta import V1ListMeta
from argo.workflows.client.models.v1_local_object_reference import V1LocalObjectReference
from argo.workflows.client.models.v1_managed_fields_entry import V1ManagedFieldsEntry
from argo.workflows.client.models.v1_nfs_volume_source import V1NFSVolumeSource
from argo.workflows.client.models.v1_node_affinity import V1NodeAffinity
from argo.workflows.client.models.v1_node_selector import V1NodeSelector
from argo.workflows.client.models.v1_node_selector_requirement import V1NodeSelectorRequirement
from argo.workflows.client.models.v1_node_selector_term import V1NodeSelectorTerm
from argo.workflows.client.models.v1_object_field_selector import V1ObjectFieldSelector
from argo.workflows.client.models.v1_object_meta import V1ObjectMeta
from argo.workflows.client.models.v1_object_reference import V1ObjectReference
from argo.workflows.client.models.v1_owner_reference import V1OwnerReference
from argo.workflows.client.models.v1_persistent_volume_claim import V1PersistentVolumeClaim
from argo.workflows.client.models.v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition
from argo.workflows.client.models.v1_persistent_volume_claim_spec import V1PersistentVolumeClaimSpec
from argo.workflows.client.models.v1_persistent_volume_claim_status import V1PersistentVolumeClaimStatus
from argo.workflows.client.models.v1_persistent_volume_claim_volume_source import V1PersistentVolumeClaimVolumeSource
from argo.workflows.client.models.v1_photon_persistent_disk_volume_source import V1PhotonPersistentDiskVolumeSource
from argo.workflows.client.models.v1_pod_affinity import V1PodAffinity
from argo.workflows.client.models.v1_pod_affinity_term import V1PodAffinityTerm
from argo.workflows.client.models.v1_pod_anti_affinity import V1PodAntiAffinity
from argo.workflows.client.models.v1_pod_dns_config import V1PodDNSConfig
from argo.workflows.client.models.v1_pod_dns_config_option import V1PodDNSConfigOption
from argo.workflows.client.models.v1_pod_security_context import V1PodSecurityContext
from argo.workflows.client.models.v1_portworx_volume_source import V1PortworxVolumeSource
from argo.workflows.client.models.v1_preferred_scheduling_term import V1PreferredSchedulingTerm
from argo.workflows.client.models.v1_probe import V1Probe
from argo.workflows.client.models.v1_projected_volume_source import V1ProjectedVolumeSource
from argo.workflows.client.models.v1_quobyte_volume_source import V1QuobyteVolumeSource
from argo.workflows.client.models.v1_rbd_volume_source import V1RBDVolumeSource
from argo.workflows.client.models.v1_resource_field_selector import V1ResourceFieldSelector
from argo.workflows.client.models.v1_resource_requirements import V1ResourceRequirements
from argo.workflows.client.models.v1_se_linux_options import V1SELinuxOptions
from argo.workflows.client.models.v1_scale_io_volume_source import V1ScaleIOVolumeSource
from argo.workflows.client.models.v1_secret_env_source import V1SecretEnvSource
from argo.workflows.client.models.v1_secret_key_selector import V1SecretKeySelector
from argo.workflows.client.models.v1_secret_projection import V1SecretProjection
from argo.workflows.client.models.v1_secret_volume_source import V1SecretVolumeSource
from argo.workflows.client.models.v1_security_context import V1SecurityContext
from argo.workflows.client.models.v1_service_account_token_projection import V1ServiceAccountTokenProjection
from argo.workflows.client.models.v1_status import V1Status
from argo.workflows.client.models.v1_status_cause import V1StatusCause
from argo.workflows.client.models.v1_status_details import V1StatusDetails
from argo.workflows.client.models.v1_storage_os_volume_source import V1StorageOSVolumeSource
from argo.workflows.client.models.v1_sysctl import V1Sysctl
from argo.workflows.client.models.v1_tcp_socket_action import V1TCPSocketAction
from argo.workflows.client.models.v1_toleration import V1Toleration
from argo.workflows.client.models.v1_typed_local_object_reference import V1TypedLocalObjectReference
from argo.workflows.client.models.v1_volume import V1Volume
from argo.workflows.client.models.v1_volume_device import V1VolumeDevice
from argo.workflows.client.models.v1_volume_mount import V1VolumeMount
from argo.workflows.client.models.v1_volume_projection import V1VolumeProjection
from argo.workflows.client.models.v1_vsphere_virtual_disk_volume_source import V1VsphereVirtualDiskVolumeSource
from argo.workflows.client.models.v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm
from argo.workflows.client.models.v1_windows_security_context_options import V1WindowsSecurityContextOptions
from argo.workflows.client.models.v1alpha1_archive_strategy import V1alpha1ArchiveStrategy
from argo.workflows.client.models.v1alpha1_arguments import V1alpha1Arguments
from argo.workflows.client.models.v1alpha1_artifact import V1alpha1Artifact
from argo.workflows.client.models.v1alpha1_artifact_location import V1alpha1ArtifactLocation
from argo.workflows.client.models.v1alpha1_artifact_repository_ref import V1alpha1ArtifactRepositoryRef
from argo.workflows.client.models.v1alpha1_artifactory_artifact import V1alpha1ArtifactoryArtifact
from argo.workflows.client.models.v1alpha1_backoff import V1alpha1Backoff
from argo.workflows.client.models.v1alpha1_cache import V1alpha1Cache
from argo.workflows.client.models.v1alpha1_cluster_workflow_template import V1alpha1ClusterWorkflowTemplate
from argo.workflows.client.models.v1alpha1_cluster_workflow_template_create_request import V1alpha1ClusterWorkflowTemplateCreateRequest
from argo.workflows.client.models.v1alpha1_cluster_workflow_template_lint_request import V1alpha1ClusterWorkflowTemplateLintRequest
from argo.workflows.client.models.v1alpha1_cluster_workflow_template_list import V1alpha1ClusterWorkflowTemplateList
from argo.workflows.client.models.v1alpha1_cluster_workflow_template_update_request import V1alpha1ClusterWorkflowTemplateUpdateRequest
from argo.workflows.client.models.v1alpha1_condition import V1alpha1Condition
from argo.workflows.client.models.v1alpha1_continue_on import V1alpha1ContinueOn
from argo.workflows.client.models.v1alpha1_counter import V1alpha1Counter
from argo.workflows.client.models.v1alpha1_create_cron_workflow_request import V1alpha1CreateCronWorkflowRequest
from argo.workflows.client.models.v1alpha1_cron_workflow import V1alpha1CronWorkflow
from argo.workflows.client.models.v1alpha1_cron_workflow_list import V1alpha1CronWorkflowList
from argo.workflows.client.models.v1alpha1_cron_workflow_spec import V1alpha1CronWorkflowSpec
from argo.workflows.client.models.v1alpha1_cron_workflow_status import V1alpha1CronWorkflowStatus
from argo.workflows.client.models.v1alpha1_dag_task import V1alpha1DAGTask
from argo.workflows.client.models.v1alpha1_dag_template import V1alpha1DAGTemplate
from argo.workflows.client.models.v1alpha1_event import V1alpha1Event
from argo.workflows.client.models.v1alpha1_executor_config import V1alpha1ExecutorConfig
from argo.workflows.client.models.v1alpha1_gcs_artifact import V1alpha1GCSArtifact
from argo.workflows.client.models.v1alpha1_gauge import V1alpha1Gauge
from argo.workflows.client.models.v1alpha1_get_user_info_response import V1alpha1GetUserInfoResponse
from argo.workflows.client.models.v1alpha1_git_artifact import V1alpha1GitArtifact
from argo.workflows.client.models.v1alpha1_hdfs_artifact import V1alpha1HDFSArtifact
from argo.workflows.client.models.v1alpha1_http_artifact import V1alpha1HTTPArtifact
from argo.workflows.client.models.v1alpha1_histogram import V1alpha1Histogram
from argo.workflows.client.models.v1alpha1_info_response import V1alpha1InfoResponse
from argo.workflows.client.models.v1alpha1_inputs import V1alpha1Inputs
from argo.workflows.client.models.v1alpha1_link import V1alpha1Link
from argo.workflows.client.models.v1alpha1_lint_cron_workflow_request import V1alpha1LintCronWorkflowRequest
from argo.workflows.client.models.v1alpha1_log_entry import V1alpha1LogEntry
from argo.workflows.client.models.v1alpha1_memoization_status import V1alpha1MemoizationStatus
from argo.workflows.client.models.v1alpha1_memoize import V1alpha1Memoize
from argo.workflows.client.models.v1alpha1_metadata import V1alpha1Metadata
from argo.workflows.client.models.v1alpha1_metric_label import V1alpha1MetricLabel
from argo.workflows.client.models.v1alpha1_metrics import V1alpha1Metrics
from argo.workflows.client.models.v1alpha1_mutex import V1alpha1Mutex
from argo.workflows.client.models.v1alpha1_mutex_holding import V1alpha1MutexHolding
from argo.workflows.client.models.v1alpha1_mutex_status import V1alpha1MutexStatus
from argo.workflows.client.models.v1alpha1_node_status import V1alpha1NodeStatus
from argo.workflows.client.models.v1alpha1_node_synchronization_status import V1alpha1NodeSynchronizationStatus
from argo.workflows.client.models.v1alpha1_oss_artifact import V1alpha1OSSArtifact
from argo.workflows.client.models.v1alpha1_outputs import V1alpha1Outputs
from argo.workflows.client.models.v1alpha1_parameter import V1alpha1Parameter
from argo.workflows.client.models.v1alpha1_pod_gc import V1alpha1PodGC
from argo.workflows.client.models.v1alpha1_prometheus import V1alpha1Prometheus
from argo.workflows.client.models.v1alpha1_raw_artifact import V1alpha1RawArtifact
from argo.workflows.client.models.v1alpha1_resource_template import V1alpha1ResourceTemplate
from argo.workflows.client.models.v1alpha1_retry_strategy import V1alpha1RetryStrategy
from argo.workflows.client.models.v1alpha1_s3_artifact import V1alpha1S3Artifact
from argo.workflows.client.models.v1alpha1_script_template import V1alpha1ScriptTemplate
from argo.workflows.client.models.v1alpha1_semaphore_holding import V1alpha1SemaphoreHolding
from argo.workflows.client.models.v1alpha1_semaphore_ref import V1alpha1SemaphoreRef
from argo.workflows.client.models.v1alpha1_semaphore_status import V1alpha1SemaphoreStatus
from argo.workflows.client.models.v1alpha1_sequence import V1alpha1Sequence
from argo.workflows.client.models.v1alpha1_submit import V1alpha1Submit
from argo.workflows.client.models.v1alpha1_submit_opts import V1alpha1SubmitOpts
from argo.workflows.client.models.v1alpha1_suspend_template import V1alpha1SuspendTemplate
from argo.workflows.client.models.v1alpha1_synchronization import V1alpha1Synchronization
from argo.workflows.client.models.v1alpha1_synchronization_status import V1alpha1SynchronizationStatus
from argo.workflows.client.models.v1alpha1_ttl_strategy import V1alpha1TTLStrategy
from argo.workflows.client.models.v1alpha1_tar_strategy import V1alpha1TarStrategy
from argo.workflows.client.models.v1alpha1_template import V1alpha1Template
from argo.workflows.client.models.v1alpha1_template_ref import V1alpha1TemplateRef
from argo.workflows.client.models.v1alpha1_update_cron_workflow_request import V1alpha1UpdateCronWorkflowRequest
from argo.workflows.client.models.v1alpha1_user_container import V1alpha1UserContainer
from argo.workflows.client.models.v1alpha1_value_from import V1alpha1ValueFrom
from argo.workflows.client.models.v1alpha1_version import V1alpha1Version
from argo.workflows.client.models.v1alpha1_workflow import V1alpha1Workflow
from argo.workflows.client.models.v1alpha1_workflow_create_request import V1alpha1WorkflowCreateRequest
from argo.workflows.client.models.v1alpha1_workflow_event_binding import V1alpha1WorkflowEventBinding
from argo.workflows.client.models.v1alpha1_workflow_event_binding_spec import V1alpha1WorkflowEventBindingSpec
from argo.workflows.client.models.v1alpha1_workflow_lint_request import V1alpha1WorkflowLintRequest
from argo.workflows.client.models.v1alpha1_workflow_list import V1alpha1WorkflowList
from argo.workflows.client.models.v1alpha1_workflow_resubmit_request import V1alpha1WorkflowResubmitRequest
from argo.workflows.client.models.v1alpha1_workflow_resume_request import V1alpha1WorkflowResumeRequest
from argo.workflows.client.models.v1alpha1_workflow_retry_request import V1alpha1WorkflowRetryRequest
from argo.workflows.client.models.v1alpha1_workflow_set_request import V1alpha1WorkflowSetRequest
from argo.workflows.client.models.v1alpha1_workflow_spec import V1alpha1WorkflowSpec
from argo.workflows.client.models.v1alpha1_workflow_status import V1alpha1WorkflowStatus
from argo.workflows.client.models.v1alpha1_workflow_step import V1alpha1WorkflowStep
from argo.workflows.client.models.v1alpha1_workflow_stop_request import V1alpha1WorkflowStopRequest
from argo.workflows.client.models.v1alpha1_workflow_submit_request import V1alpha1WorkflowSubmitRequest
from argo.workflows.client.models.v1alpha1_workflow_suspend_request import V1alpha1WorkflowSuspendRequest
from argo.workflows.client.models.v1alpha1_workflow_template import V1alpha1WorkflowTemplate
from argo.workflows.client.models.v1alpha1_workflow_template_create_request import V1alpha1WorkflowTemplateCreateRequest
from argo.workflows.client.models.v1alpha1_workflow_template_lint_request import V1alpha1WorkflowTemplateLintRequest
from argo.workflows.client.models.v1alpha1_workflow_template_list import V1alpha1WorkflowTemplateList
from argo.workflows.client.models.v1alpha1_workflow_template_ref import V1alpha1WorkflowTemplateRef
from argo.workflows.client.models.v1alpha1_workflow_template_spec import V1alpha1WorkflowTemplateSpec
from argo.workflows.client.models.v1alpha1_workflow_template_update_request import V1alpha1WorkflowTemplateUpdateRequest
from argo.workflows.client.models.v1alpha1_workflow_terminate_request import V1alpha1WorkflowTerminateRequest
from argo.workflows.client.models.v1alpha1_workflow_watch_event import V1alpha1WorkflowWatchEvent
