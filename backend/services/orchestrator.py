from utils.graph_utils import topological_sort
from services.rag_service import run_rag
from services.llm_service import call_llm

def run_workflow(nodes, edges, query):
    order_ids = topological_sort(nodes, edges)
    node_map = {n.id: n for n in nodes}

    # ALWAYS initialize
    current_query = query
    context = None
    response = None

    for nid in order_ids:
        node = node_map[nid]
        cfg = node.data.get("config", {})

        if node.type == "userQuery":
            current_query = query

        elif node.type == "knowledgeBase":
            context = run_rag(cfg, current_query)

        elif node.type == "llmEngine":
            response = call_llm(cfg, current_query, context)

        elif node.type == "output":
            return {
                "answer": response,
                "sources": context or []
            }

    return {"answer": response}
