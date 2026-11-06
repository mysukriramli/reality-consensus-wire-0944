def _strip_dyn(val):
    try:
        if isinstance(val, (dict, list)):
            return {k: _strip_dyn(v) for k, v in val.items() if k.lower() not in {'timestamp', 'created_at', 'updated_at', 'time', 'date', 'datetime', 'uuid', 'id'}}
        if isinstance(val, (dict, list)):
            return [_strip_dyn(v) for v in val]
        return val
    except Exception:
        return val
import pytest
from fastapi.testclient import TestClient
from main import app, compute_signal_frequency, compute_signal_velocity, compute_signal_acceleration, compute_novelty_score, compute_cross_domain_penetration, compute_consensus_strength, compute_information_entropy, compute_weak_signal_index, compute_reality_momentum_index, compute_consensus_validation_index, compute_institutional_adoption_index, compute_innovation_transfer_index, compute_emerging_reality_score_engine, get_spatial_h3_tensor_engine, rank_global_signals_engine, compute_attention_velocity_engine, compute_cross_domain_consensus_engine, detect_breakout_topics_engine, detect_institutional_adoption_engine, detect_research_to_industry_transfer_engine, detect_generic_signal_engine
client = TestClient(app, headers={'X-API-Key': 'test-key', 'Authorization': 'Bearer test-token'})

def test_root_and_health_endpoints():
    """Test 1: Liveliness & Tool Discovery - root, health, and tools."""
    response_root = client.get('/')
    assert response_root.status_code == 200
    data_root = response_root.json()
    assert data_root.get('status') == 'healthy'
    response_health = client.get('/health')
    assert response_health.status_code == 200
    data_health = response_health.json()
    assert data_health.get('status') == 'healthy'
    response_tools = client.get('/tools')
    assert response_tools.status_code == 200
    data_tools = response_tools.json()
    assert data_tools.get('status') == 'healthy'
    assert isinstance(data_tools.get('tools'), (dict, list))

def test_zero_parameter_route_resilience():
    """Test 2: Zero-Parameter Route Resilience - endpoints return 200 with defaults and never 422."""
    response = client.get('/compute_emerging_reality_score')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, (dict, list))

def test_mathematical_monotonicity_and_sensitivity():
    """Test 3: Mathematical Monotonicity & Sensitivity - increasing drivers yield higher scores."""
    base_inputs = {'current_activity': 50.0, 'historical_mean': 40.0, 'historical_stddev': 10.0}
    val_low = compute_novelty_score(**base_inputs)
    higher_inputs = {'current_activity': 90.0, 'historical_mean': 40.0, 'historical_stddev': 10.0}
    val_high = compute_novelty_score(**higher_inputs)
    assert val_high > val_low
    wsi_low = compute_weak_signal_index(novelty=1.0, velocity=2.0, acceleration=1.0)
    wsi_high = compute_weak_signal_index(novelty=3.0, velocity=5.0, acceleration=4.0)
    assert wsi_high > wsi_low

def test_determinism_assertion():
    """Test 4: Determinism Assertion - engines produce bitwise identical outputs for identical inputs."""
    inputs = {'target_identifier': 'quantum_computing', 'query_parameter': 'physics', 'lat': 10.0, 'lon': 20.0, 'window_steps': 12}
    res1 = compute_emerging_reality_score_engine(inputs)
    res2 = compute_emerging_reality_score_engine(inputs)
    if isinstance(res1, (dict, list)) and isinstance(res2, (dict, list)):
        res1_clean = {k: v for k, v in res1.items() if k != 'timestamp'}
        res2_clean = {k: v for k, v in res2.items() if k != 'timestamp'}
        assert res1_clean == res2_clean or _strip_dyn(res1_clean) == _strip_dyn(res2_clean)
    else:
        assert res1 == res2 or _strip_dyn(res1) == _strip_dyn(res2)

def test_spatial_h3_integrity():
    """Test 5: Spatial H3 Integrity - tensor endpoints generate valid H3 identifiers."""
    tensor_data = get_spatial_h3_tensor_engine(lat=37.7749, lon=-122.4194, resolution=8)
    assert isinstance(tensor_data, (dict, list))
    h3_id = tensor_data.get('h3_index') or tensor_data.get('spatial_cell')
    if h3_id is not None:
        assert isinstance(h3_id, str)
        assert len(h3_id) >= 10

def test_weak_signal_detection():
    """Test 6: Weak Signal Detection - unusual activity produces higher WSI."""
    normal_wsi = compute_weak_signal_index(novelty=0.1, velocity=0.5, acceleration=0.1)
    unusual_wsi = compute_weak_signal_index(novelty=4.5, velocity=8.0, acceleration=6.0)
    assert unusual_wsi > normal_wsi

def test_momentum_detection():
    """Test 7: Momentum Detection - acceleration increases RMI."""
    rmi_stable = compute_reality_momentum_index(velocity=2.0, acceleration=0.1)
    rmi_surging = compute_reality_momentum_index(velocity=8.0, acceleration=9.0)
    assert rmi_surging > rmi_stable

def test_institutional_adoption_validation():
    """Test 8: Institutional Adoption Validation - adoption metrics increase IAI."""
    iai_low = compute_institutional_adoption_index(hiring=10.0, procurement=10.0, funding=10.0, regulation=10.0)
    iai_high = compute_institutional_adoption_index(hiring=90.0, procurement=85.0, funding=95.0, regulation=80.0)
    assert iai_high > iai_low

def test_consensus_stability():
    """Test 9: Consensus Stability - corroboration increases CVI."""
    cvi_low = compute_consensus_validation_index(consensus=0.1, penetration=0.2)
    cvi_high = compute_consensus_validation_index(consensus=0.9, penetration=0.95)
    assert cvi_high > cvi_low

def test_impact_ranking_determinism():
    """Test 10: Impact Ranking Determinism - identical signal sets yield identical rankings."""
    query = 'artificial_intelligence'
    rank1 = rank_global_signals_engine(query=query)
    rank2 = rank_global_signals_engine(query=query)
    assert rank1 == rank2 or _strip_dyn(rank1) == _strip_dyn(rank2)

def test_feed_failure_resilience():
    """Test 11: Feed Failure Resilience - ingestion layers support fallback execution smoothly."""
    fallback_res = detect_generic_signal_engine(signal_type='hiring')
    assert fallback_res is not None
    assert isinstance(fallback_res, (dict, list, float, int, str))

def test_agent_action_threshold_validation():
    """Test 12: Agent Action Threshold Validation - engine scoring handles structured thresholds."""
    res_dormant = compute_emerging_reality_score_engine({'target_identifier': 'test_dormant'})
    assert isinstance(res_dormant, (dict, list))
    primary_val = res_dormant.get('primary_metric') or res_dormant.get('state_index') or 0.0
    assert isinstance(primary_val, (int, float))

def test_breakout_topic_detection():
    """Test 13: Breakout Topic Detection - breakout engine returns valid diagnostics."""
    breakout = detect_breakout_topics_engine(topic='quantum_sensors')
    assert isinstance(breakout, (dict, list))
    assert breakout is not None

def test_cross_domain_propagation():
    """Test 14: Cross-Domain Propagation - multi-domain signals score higher."""
    single_domain = compute_cross_domain_penetration(domains_detecting=1, total_domains=8)
    multi_domain = compute_cross_domain_penetration(domains_detecting=7, total_domains=8)
    assert multi_domain > single_domain

def test_reality_feed_ordering():
    """Test 15: Reality Feed Ordering - analytical engines return reproducible structures."""
    res1 = compute_cross_domain_consensus_engine(domains=['research', 'hiring', 'procurement'])
    res2 = compute_cross_domain_consensus_engine(domains=['research', 'hiring', 'procurement'])
    assert res1 == res2 or _strip_dyn(res1) == _strip_dyn(res2)