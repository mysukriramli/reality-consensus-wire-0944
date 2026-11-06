from datetime import timezone as dt_timezone
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

def get_utc_now_iso() -> str:
    """Returns current UTC timestamp in ISO 8601 format."""
    return datetime.now(dt_timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

class HealthResponse(BaseModel):
    status: str = Field(default='healthy', description='Service health status')
    timestamp: str = Field(default_factory=get_utc_now_iso, description='UTC ISO-8601 timestamp')

class ToolItem(BaseModel):
    name: str = Field(default='', description='Tool identifier name')
    description: str = Field(default='', description='Tool description and purpose')
    input_schema: Dict[str, Any] = Field(default_factory=dict, description='JSON Schema for inputs')

class ToolsResponse(BaseModel):
    tools: List[Dict[str, Any]] = Field(default_factory=list, description='List of available microservice tools')
    status: str = Field(default='healthy', description='Service health status')
    timestamp: str = Field(default_factory=get_utc_now_iso, description='UTC ISO-8601 timestamp')

class ScoreWeights(BaseModel):
    weak_signal: float = Field(default=0.3, description='Weight for Weak Signal Index')
    momentum: float = Field(default=0.25, description='Weight for Reality Momentum Index')
    consensus: float = Field(default=0.2, description='Weight for Consensus Validation Index')
    institutional: float = Field(default=0.15, description='Weight for Institutional Adoption Index')
    innovation_transfer: float = Field(default=0.1, description='Weight for Innovation Transfer Index')

class ExplainabilityPayload(BaseModel):
    primary_driver: str = Field(default='cross_domain_consensus', description='Primary contributing trend driver')
    weights: ScoreWeights = Field(default_factory=ScoreWeights, description='Deterministic component weights')
    details: Dict[str, Any] = Field(default_factory=dict, description='Additional contextual diagnostic details')

class ComputeEmergingRealityScoreRequest(BaseModel):
    target_identifier: str = Field(default='humanoid_robotics', description='Target topic, technology, or asset identifier')
    query_parameter: str = Field(default='technology', description='Category or filtering parameter')
    lat: float = Field(default=0.0, ge=-90.0, le=90.0, description='Latitude coordinate clamped to [-90, 90]')
    lon: float = Field(default=0.0, ge=-180.0, le=180.0, description='Longitude coordinate clamped to [-180, 180]')
    window_steps: int = Field(default=12, ge=1, le=1000, description='Temporal window steps for analysis')
    lookback_days: int = Field(default=180, ge=1, le=3650, description='Historical lookback window in days')

class ComputeEmergingRealityScoreResponse(BaseModel):
    timestamp: str = Field(default_factory=get_utc_now_iso, description='UTC ISO-8601 timestamp')
    status: str = Field(default='healthy', description='Execution status')
    primary_metric: float = Field(default=91.8, description='Emerging Reality Score (ERS)')
    secondary_score: float = Field(default=0.95, description='Normalized secondary confidence coefficient')
    state_index: float = Field(default=88.4, description='Composite state index')
    classification: str = Field(default='TRANSFORMATIONAL', description='Emergence state classification')
    explainability: ExplainabilityPayload = Field(default_factory=ExplainabilityPayload, description='Deterministic scoring breakdown')

class GetSpatialH3TensorRequest(BaseModel):
    lat: float = Field(default=2.0442, ge=-90.0, le=90.0, description='Latitude coordinate')
    lon: float = Field(default=102.5689, ge=-180.0, le=180.0, description='Longitude coordinate')
    resolution: int = Field(default=8, ge=0, le=15, description='Uber H3 spatial resolution index (0-15)')

class GetSpatialH3TensorResponse(BaseModel):
    h3_index: str = Field(default='886520d81dfffff', description='15-character H3 spatial index')
    spatial_cell: str = Field(default='886520d81dfffff', description='Spatial cell identifier')
    density_score: float = Field(default=64.2, description='Calculated signal density score')
    terrain_state_index: float = Field(default=75.1, description='Spatial terrain state index')
    status: str = Field(default='ACTIVE', description='Spatial grid activity status')
    timestamp: str = Field(default_factory=get_utc_now_iso, description='UTC ISO-8601 timestamp')

class UniversalToolRequest(BaseModel):
    target_identifier: str = Field(default='global_signal_feed', description='Target identifier or topic')
    query_parameter: str = Field(default='all', description='Query or filter parameter')
    lat: float = Field(default=0.0, ge=-90.0, le=90.0, description='Latitude coordinate')
    lon: float = Field(default=0.0, ge=-180.0, le=180.0, description='Longitude coordinate')
    window_steps: int = Field(default=12, ge=1, le=1000, description='Analysis window steps')
    lookback_days: int = Field(default=180, ge=1, le=3650, description='Lookback window in days')
    resolution: int = Field(default=8, ge=0, le=15, description='H3 Resolution')
    limit: int = Field(default=50, ge=1, le=1000, description='Result limit')

class UniversalToolResponse(BaseModel):
    timestamp: str = Field(default_factory=get_utc_now_iso, description='UTC ISO-8601 timestamp')
    status: str = Field(default='healthy', description='Execution status')
    tool_name: str = Field(default='agent_tool', description='Executed tool name')
    primary_metric: float = Field(default=85.0, description='Primary calculated analytical index')
    results: List[Dict[str, Any]] = Field(default_factory=list, description='Structured intelligence records')
    metadata: Dict[str, Any] = Field(default_factory=dict, description='Execution metadata and diagnostics')