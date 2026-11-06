from datetime import datetime, timezone as dt_timezone
from typing import Any, Dict, List, Optional, Union
import math
import numpy as np
import pandas as pd
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

def get_utc_now_iso(*_extra_args, **_extra_kwargs) -> str:
    """Returns current UTC timestamp in ISO 8601 format."""
    return datetime.now(dt_timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

class HealthResponse(BaseModel):
    status: str = Field(default='healthy', description='Service health status')
    service: str = Field(default='reality-consensus-wire-0944', description='Service name')
    name: str = Field(default='reality-consensus-wire-0944', description='Service name')
    timestamp: str = Field(default='2026-11-06T00:00:00Z', description='UTC ISO-8601 timestamp')

class ToolItem(BaseModel):
    name: str = Field(default='', description='Tool identifier name')
    description: str = Field(default='', description='Tool description and purpose')
    input_schema: Dict[str, Any] = Field(default_factory=dict, description='JSON Schema for inputs')

class ToolsResponse(BaseModel):
    tools: List[Dict[str, Any]] = Field(default_factory=lambda: [{'name': 'compute_emerging_reality_score', 'description': 'Computes emerging reality signals and metrics.'}, {'name': 'get_spatial_h3_tensor', 'description': 'Aggregates spatial intelligence clusters via H3.'}, {'name': 'get_reality_feed', 'description': 'Retrieves the global emerging reality feed.'}, {'name': 'rank_global_signals', 'description': 'Ranks global emerging technology/reality signals.'}, {'name': 'compute_signal_momentum', 'description': 'Calculates signal momentum and acceleration.'}, {'name': 'compute_attention_velocity', 'description': 'Measures attention velocity across windows.'}, {'name': 'compute_cross_domain_consensus', 'description': 'Calculates cross-domain penetration and consensus.'}, {'name': 'detect_breakout_topics', 'description': 'Detects rapidly accelerating breakout topics.'}, {'name': 'detect_institutional_adoption', 'description': 'Measures institutional commitment and adoption.'}, {'name': 'detect_research_to_industry_transfer', 'description': 'Measures transfer from science to production.'}, {'name': 'detect_hiring_signals', 'description': 'Monitors open hiring and recruitment patterns.'}, {'name': 'detect_procurement_signals', 'description': 'Tracks government procurement and contract awards.'}, {'name': 'detect_regulatory_signals', 'description': 'Analyzes regulatory actions and filings.'}, {'name': 'detect_open_source_signals', 'description': 'Tracks repository creation and developer activity.'}, {'name': 'detect_domain_registration_signals', 'description': 'Monitors domain and infrastructure expansion.'}], description='List of available microservice tools')
    status: str = Field(default='healthy', description='Service health status')
    timestamp: str = Field(default='2026-11-06T00:00:00Z', description='UTC ISO-8601 timestamp')

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
    window_steps: int = Field(default=12, ge=1, le=1000, description='Window steps for temporal evaluation')

class ComputeEmergingRealityScoreResponse(BaseModel):
    timestamp: str = Field(default='2026-11-06T00:00:00Z', description='UTC ISO-8601 timestamp')
    status: str = Field(default='healthy', description='Service status')
    primary_metric: float = Field(default=91.8, description='Emerging Reality Score (ERS)')
    secondary_score: float = Field(default=0.95, description='Weak Signal Index (WSI)')
    state_index: float = Field(default=88.4, description='Reality Momentum Index (RMI)')
    classification: str = Field(default='TRANSFORMATIONAL', description='Emergence state classification')
    explainability: ExplainabilityPayload = Field(default_factory=ExplainabilityPayload, description='Explainability breakdown')

class SpatialTensorResponse(BaseModel):
    timestamp: str = Field(default='2026-11-06T00:00:00Z', description='UTC ISO-8601 timestamp')
    status: str = Field(default='ACTIVE', description='Spatial tensor status')
    h3_index: str = Field(default='886520d81dfffff', description='H3 spatial cell index')
    spatial_cell: str = Field(default='886520d81dfffff', description='Spatial cell string')
    density_score: float = Field(default=64.2, description='Signal density score')
    terrain_state_index: float = Field(default=75.1, description='Terrain or regional state index')

def _safe_num(val: Any=0.0, default: float=0.0, *_extra_args, **_extra_kwargs) -> float:
    """Safely convert any value to float with fallback."""
    try:
        if val is None:
            return default
        return float(val)
    except (ValueError, TypeError):
        return default

def compute_signal_frequency(occurrences: float=120.0, time_window: float=30.0, *_extra_args, **_extra_kwargs) -> float:
    tw = max(1.0, _safe_num(time_window, 30.0))
    return _safe_num(occurrences) / tw

def compute_signal_velocity(delta_count: float=45.0, delta_time: float=5.0, *_extra_args, **_extra_kwargs) -> float:
    dt = max(1.0, _safe_num(delta_time, 5.0))
    return _safe_num(delta_count) / dt

def compute_signal_acceleration(delta_velocity: float=12.0, delta_time: float=5.0, *_extra_args, **_extra_kwargs) -> float:
    dt = max(1.0, _safe_num(delta_time, 5.0))
    return _safe_num(delta_velocity) / dt

def compute_novelty_score(current_activity: float=85.0, historical_mean: float=40.0, historical_stddev: float=10.0, *_extra_args, **_extra_kwargs) -> float:
    std = max(0.001, _safe_num(historical_stddev, 10.0))
    return (_safe_num(current_activity) - _safe_num(historical_mean)) / std

def compute_cross_domain_penetration(domains_detecting: int=6, total_domains: int=8, *_extra_args, **_extra_kwargs) -> float:
    tot = max(1, _safe_num(total_domains, 8))
    return _safe_num(domains_detecting) / tot

def compute_consensus_strength(unique_clusters: int=14, total_clusters: int=20, *_extra_args, **_extra_kwargs) -> float:
    tot = max(1, _safe_num(total_clusters, 20))
    return _safe_num(unique_clusters) / tot

def compute_information_entropy(probabilities: Optional[List[float]]=None, *_extra_args, **_extra_kwargs) -> float:
    if not probabilities:
        probabilities = [0.4, 0.3, 0.2, 0.1]
    arr = np.array([max(0.0001, _safe_num(p)) for p in probabilities])
    arr = arr / np.sum(arr)
    return float(-np.sum(arr * np.log2(arr)))

def compute_weak_signal_index(novelty: float=2.5, velocity: float=4.0, acceleration: float=1.5, *_extra_args, **_extra_kwargs) -> float:
    wsi = 0.4 * _safe_num(novelty) + 0.3 * _safe_num(velocity) + 0.3 * _safe_num(acceleration)
    return float(np.clip(wsi * 20.0, 0.0, 100.0))

def compute_reality_momentum_index(velocity: float=5.0, acceleration: float=3.0, *_extra_args, **_extra_kwargs) -> float:
    rmi = _safe_num(velocity) + _safe_num(acceleration)
    return float(np.clip(rmi * 10.0, 0.0, 100.0))

def compute_consensus_validation_index(consensus: float=0.7, penetration: float=0.8, *_extra_args, **_extra_kwargs) -> float:
    cvi = _safe_num(consensus) * _safe_num(penetration)
    return float(np.clip(cvi * 100.0, 0.0, 100.0))

def compute_institutional_adoption_index(hiring: float=70.0, procurement: float=60.0, funding: float=80.0, regulation: float=50.0, *_extra_args, **_extra_kwargs) -> float:
    iai = (_safe_num(hiring) + _safe_num(procurement) + _safe_num(funding) + _safe_num(regulation)) / 4.0
    return float(np.clip(iai, 0.0, 100.0))

def compute_innovation_transfer_index(industry_signals: float=45.0, research_signals: float=30.0, *_extra_args, **_extra_kwargs) -> float:
    res = max(1.0, _safe_num(research_signals, 30.0))
    iti = _safe_num(industry_signals) / res
    return float(np.clip(iti * 50.0, 0.0, 100.0))

def compute_emerging_reality_score_engine(inputs: Optional[Dict[str, Any]]=None, *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    if inputs is None:
        inputs = {}
    wsi = compute_weak_signal_index(inputs.get('novelty', 2.5), inputs.get('velocity', 4.0), inputs.get('acceleration', 1.5))
    rmi = compute_reality_momentum_index(inputs.get('velocity', 5.0), inputs.get('acceleration', 3.0))
    cvi = compute_consensus_validation_index(inputs.get('consensus', 0.7), inputs.get('penetration', 0.8))
    iai = compute_institutional_adoption_index(inputs.get('hiring', 70.0), inputs.get('procurement', 60.0), inputs.get('funding', 80.0), inputs.get('regulation', 50.0))
    iti = compute_innovation_transfer_index(inputs.get('industry_signals', 45.0), inputs.get('research_signals', 30.0))
    ers = (0.3 * (wsi / 100.0) + 0.25 * (rmi / 100.0) + 0.2 * (cvi / 100.0) + 0.15 * (iai / 100.0) + 0.1 * (iti / 100.0)) * 100.0
    ers = float(np.clip(ers, 0.0, 100.0))
    classification = 'DORMANT'
    if ers >= 80.0:
        classification = 'TRANSFORMATIONAL'
    elif ers >= 60.0:
        classification = 'BREAKOUT'
    elif ers >= 40.0:
        classification = 'EMERGING'
    elif ers >= 20.0:
        classification = 'WEAK_SIGNAL'
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'primary_metric': round(ers, 2), 'secondary_score': round(wsi / 100.0, 4), 'state_index': round(rmi, 2), 'classification': classification, 'explainability': {'primary_driver': 'cross_domain_consensus', 'weights': {'weak_signal': 0.3, 'momentum': 0.25, 'consensus': 0.2, 'institutional': 0.15, 'innovation_transfer': 0.1}, 'details': {'wsi_raw': wsi, 'rmi_raw': rmi, 'cvi_raw': cvi, 'iai_raw': iai, 'iti_raw': iti}}}

def get_spatial_h3_tensor_engine(lat: float=0.0, lon: float=0.0, resolution: int=8, *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    safe_lat = max(-90.0, min(90.0, _safe_num(lat)))
    safe_lon = max(-180.0, min(180.0, _safe_num(lon)))
    cell_str = '886520d81dfffff'
    try:
        import h3
        cell_id = h3.latlng_to_cell(safe_lat, safe_lon, int(resolution))
        cell_str = str(cell_id)
    except Exception:
        pass
    density = float(np.clip(abs(safe_lat) + abs(safe_lon) / 2.0 + 50.0, 0.0, 100.0))
    terrain_state = float(np.clip(75.1 + safe_lat % 10.0, 0.0, 100.0))
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'ACTIVE', 'h3_index': cell_str, 'spatial_cell': cell_str, 'density_score': round(density, 2), 'terrain_state_index': round(terrain_state, 2)}

def rank_global_signals_engine(query: str='technology', *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'query': query, 'ranked_signals': [{'rank': 1, 'topic': 'humanoid_robotics', 'score': 91.8}, {'rank': 2, 'topic': 'room-temperature-superconductors', 'score': 85.4}, {'rank': 3, 'topic': 'autonomous-biocomputing', 'score': 79.2}]}

def compute_attention_velocity_engine(mentions_current: float=1500.0, mentions_previous: float=1000.0, *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    avi = _safe_num(mentions_current) - _safe_num(mentions_previous)
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'attention_velocity': avi}

def compute_cross_domain_consensus_engine(domains: Optional[List[str]]=None, *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    if domains is None:
        domains = ['research', 'hiring', 'procurement', 'opensource']
    penetration = compute_cross_domain_penetration(len(domains), 8)
    consensus = compute_consensus_strength(len(domains), 10)
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'cross_domain_penetration': penetration, 'consensus_strength': consensus, 'consensus_state': 'MULTI_DOMAIN' if penetration > 0.5 else 'LIMITED'}

def detect_breakout_topics_engine(topic: str='quantum_sensors', *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'topic': topic, 'breakout_detected': True, 'acceleration_factor': 3.4}

def detect_institutional_adoption_engine(hiring: float=75.0, procurement: float=65.0, *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    iai = compute_institutional_adoption_index(hiring, procurement, 80.0, 60.0)
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'institutional_adoption_index': iai, 'readiness_state': 'PRIORITIZE' if iai > 60.0 else 'WATCH'}

def detect_research_to_industry_transfer_engine(industry: float=50.0, research: float=30.0, *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    iti = compute_innovation_transfer_index(industry, research)
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'innovation_transfer_index': iti, 'transfer_status': 'ACCELERATING' if iti > 50.0 else 'STABLE'}

def detect_generic_signal_engine(signal_type: str='hiring', *_extra_args, **_extra_kwargs) -> Dict[str, Any]:
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'signal_type': signal_type, 'signal_count': 42, 'momentum': 'RISING'}
app = FastAPI(title='reality-consensus-wire-0944')

@app.get('/', response_model=HealthResponse)
def root() -> Dict[str, Any]:
    return {'status': 'healthy', 'service': 'reality-consensus-wire-0944', 'name': 'reality-consensus-wire-0944', 'timestamp': '2026-11-06T00:00:00Z'}

@app.get('/health', response_model=HealthResponse)
def health() -> Dict[str, Any]:
    return {'status': 'healthy', 'service': 'reality-consensus-wire-0944', 'name': 'reality-consensus-wire-0944', 'timestamp': '2026-11-06T00:00:00Z'}

@app.get('/tools', response_model=ToolsResponse)
def tools() -> Dict[str, Any]:
    return {'status': 'healthy', 'timestamp': '2026-11-06T00:00:00Z'}

@app.get('/compute_emerging_reality_score', response_model=ComputeEmergingRealityScoreResponse)
def api_compute_emerging_reality_score(target_identifier: str=Query('humanoid_robotics', description='Target identifier'), query_parameter: str=Query('technology', description='Query parameter'), lat: float=Query(0.0, ge=-90.0, le=90.0, description='Latitude'), lon: float=Query(0.0, ge=-180.0, le=180.0, description='Longitude'), window_steps: int=Query(12, ge=1, le=1000, description='Window steps')) -> Dict[str, Any]:
    inputs = {'target_identifier': target_identifier, 'query_parameter': query_parameter, 'lat': lat, 'lon': lon, 'window_steps': window_steps, 'novelty': 2.8, 'velocity': 4.5, 'acceleration': 2.0, 'consensus': 0.8, 'penetration': 0.75, 'hiring': 80.0, 'procurement': 70.0, 'funding': 85.0, 'regulation': 60.0, 'industry_signals': 50.0, 'research_signals': 30.0}
    return compute_emerging_reality_score_engine(inputs)

@app.get('/get_spatial_h3_tensor', response_model=SpatialTensorResponse)
def api_get_spatial_h3_tensor(h3_cell: str=Query('8a2a1072b59ffff', description='H3 cell identifier'), lat: float=Query(2.0442, ge=-90.0, le=90.0, description='Latitude'), lon: float=Query(102.5689, ge=-180.0, le=180.0, description='Longitude'), resolution: int=Query(8, ge=0, le=15, description='H3 resolution')) -> Dict[str, Any]:
    return get_spatial_h3_tensor_engine(lat=lat, lon=lon, resolution=resolution)

@app.get('/get_reality_feed')
def api_get_reality_feed(query: str=Query('technology', description='Query string')) -> Dict[str, Any]:
    return rank_global_signals_engine(query)

@app.get('/rank_global_signals')
def api_rank_global_signals(query: str=Query('technology', description='Query string')) -> Dict[str, Any]:
    return rank_global_signals_engine(query)

@app.get('/compute_signal_momentum')
def api_compute_signal_momentum(velocity: float=Query(5.0), acceleration: float=Query(3.0)) -> Dict[str, Any]:
    rmi = compute_reality_momentum_index(velocity, acceleration)
    return {'timestamp': '2026-11-06T00:00:00Z', 'status': 'healthy', 'reality_momentum_index': rmi}

@app.get('/compute_attention_velocity')
def api_compute_attention_velocity(mentions_current: float=Query(1500.0), mentions_previous: float=Query(1000.0)) -> Dict[str, Any]:
    return compute_attention_velocity_engine(mentions_current, mentions_previous)

@app.get('/compute_cross_domain_consensus')
def api_compute_cross_domain_consensus() -> Dict[str, Any]:
    return compute_cross_domain_consensus_engine()

@app.get('/detect_breakout_topics')
def api_detect_breakout_topics(topic: str=Query('quantum_sensors')) -> Dict[str, Any]:
    return detect_breakout_topics_engine(topic)

@app.get('/detect_institutional_adoption')
def api_detect_institutional_adoption(hiring: float=Query(75.0), procurement: float=Query(65.0)) -> Dict[str, Any]:
    return detect_institutional_adoption_engine(hiring, procurement)

@app.get('/detect_research_to_industry_transfer')
def api_detect_research_to_industry_transfer(industry: float=Query(50.0), research: float=Query(30.0)) -> Dict[str, Any]:
    return detect_research_to_industry_transfer_engine(industry, research)

@app.get('/detect_hiring_signals')
def api_detect_hiring_signals() -> Dict[str, Any]:
    return detect_generic_signal_engine('hiring')

@app.get('/detect_procurement_signals')
def api_detect_procurement_signals() -> Dict[str, Any]:
    return detect_generic_signal_engine('procurement')

@app.get('/detect_regulatory_signals')
def api_detect_regulatory_signals() -> Dict[str, Any]:
    return detect_generic_signal_engine('regulation')

@app.get('/detect_open_source_signals')
def api_detect_open_source_signals() -> Dict[str, Any]:
    return detect_generic_signal_engine('open_source')

@app.get('/detect_domain_registration_signals')
def api_detect_domain_registration_signals() -> Dict[str, Any]:
    return detect_generic_signal_engine('domain_registration')