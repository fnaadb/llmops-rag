from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    MonitorSchedule,
    CronTrigger,
    MonitorDefinition,
    ServerlessSparkCompute,
    MonitoringTarget,
    AlertNotification,
    GenerationSafetyQualityMonitoringMetricThreshold,
    GenerationSafetyQualitySignal,
    BaselineDataRange,
    LlmData,
)
from azure.ai.ml.entities._inputs_outputs import Input
from azure.ai.ml.constants import MonitorTargetTasks, MonitorDatasetContext
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
# Update your Azure resources details
subscription_id = "713a6867-f4a6-47da-8425-c1ea4c0ff132"
resource_group = "rg-dev-rag-llmops"
aoai_deployment_name = "gpt-4"
aoai_connection_name = "aoai-connection"
project_name = "ai-project-t6qylx4fcm3po"  # Ex: ai-project-lh7b37cbhixdq
endpoint_name = "rag-5959-endpoint"  # Ex: rag-PCLN-endpoint
deployment_name = "rag-5959-deployment"  # Ex: rag-PCLN-deployment