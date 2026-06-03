#!/usr/bin/env python3
"""Graph query tool — queries the pre-compiled knowledge graph AND analysis data.
Usage: python3 graph_query.py <keyword> [depth]
Returns: connected nodes, source files, and relationships.
"""
import json, sys, os, glob

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
GRAPH_FILE = os.path.join(BASE_DIR, '.project-analysis', 'graphify-out', 'graph.json')
ANALYSIS_DIR = os.path.join(BASE_DIR, '.project-analysis', 'phase2_deep_analysis')

def load_graph():
    return json.load(open(GRAPH_FILE))

def search_data_flows(keyword):
    """Search all data_flows.json files for file paths matching keyword."""
    results = []
    keyword_lower = keyword.lower()
    for df_file in glob.glob(f'{ANALYSIS_DIR}/session_*/data_flows.json'):
        try:
            df = json.load(open(df_file))
            for flow in df.get('flows', []):
                for step in flow.get('steps', []):
                    component = step.get('component', '')
                    file_path = step.get('file_path', '')
                    if keyword_lower in component.lower() or keyword_lower in file_path.lower():
                        results.append({
                            'endpoint': f"{flow['endpoint_id']} {flow.get('http_method', '')} {flow.get('path', '')}",
                            'step': step['step'],
                            'component': component,
                            'file_path': file_path,
                            'type': step.get('type', '')
                        })
        except:
            pass
    return results

def query(keyword, depth=2):
    g = load_graph()
    keyword_lower = keyword.lower()
    
    # Search graph nodes
    matches = []
    for node in g['nodes']:
        label = node.get('label', '').lower()
        source = node.get('source_file', '').lower()
        if keyword_lower in label or keyword_lower in source:
            matches.append(node)
    
    # Traverse edges
    visited = set()
    current_ids = {n['id'] for n in matches}
    all_nodes = {n['id']: n for n in matches}
    all_edges = []
    
    for d in range(depth):
        next_ids = set()
        for edge in g['links']:
            src, tgt = edge['_src'], edge['_tgt']
            if src in current_ids and tgt not in visited:
                next_ids.add(tgt)
                all_edges.append(edge)
            elif tgt in current_ids and src not in visited:
                next_ids.add(src)
                all_edges.append(edge)
        visited.update(current_ids)
        current_ids = next_ids - visited
        for node in g['nodes']:
            if node['id'] in current_ids:
                all_nodes[node['id']] = node
    
    # Source files from graph
    graph_files = set()
    for n in all_nodes.values():
        sf = n.get('source_file', '')
        if sf and sf.endswith('.go') and 'session_' not in sf:
            graph_files.add(sf)
    
    # Source files from data flows analysis
    flow_results = search_data_flows(keyword)
    flow_files = {r['file_path'] for r in flow_results if r['file_path']}
    
    # Combine
    all_files = sorted(graph_files | flow_files)
    
    # Endpoints
    endpoints = [n for n in all_nodes.values() if '/api/v1/' in n.get('label', '')]
    
    return {
        "query": keyword,
        "direct_matches": len(matches),
        "total_nodes": len(all_nodes),
        "source_files_from_graph": sorted(graph_files),
        "source_files_from_analysis": sorted(flow_files),
        "all_source_files": all_files,
        "endpoints": [{"id": n["id"], "label": n["label"]} for n in endpoints[:20]],
        "data_flow_hits": flow_results[:10]
    }

if __name__ == "__main__":
    keyword = sys.argv[1] if len(sys.argv) > 1 else ""
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    
    if not keyword:
        print("Usage: python3 graph_query.py <keyword> [depth]")
        sys.exit(1)
    
    result = query(keyword, depth)
    print(json.dumps(result, indent=2))
