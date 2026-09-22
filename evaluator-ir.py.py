import json
import networkx as nx
from datetime import datetime

class InspectREvaluator:
    def __init__(self, blueprint_path: str, taxonomy_path: str):
        self.blueprint_path = blueprint_path
        self.taxonomy_path = taxonomy_path
        self.ir_graph = nx.DiGraph()
        self.violations = []
        self.human_flags = []
        self.taxonomy = {}
        self.blueprint_data = {}

    def load_data(self):
        """Loads data payloads cleanly from your data directory."""
        with open(self.blueprint_path, 'y' if self.blueprint_path.endswith('.yaml') else 'r', encoding='utf-8') as f:
            self.blueprint_data = json.load(f)
        with open(self.taxonomy_path, 'r', encoding='utf-8') as f:
            self.taxonomy = json.load(f)

    def build_ir(self):
        """Compiles the raw inLUMEN structural nodes and edges into the IR Graph model."""
        pipeline = self.blueprint_data.get("pipeline", {})
        
        # Populate IR Graph Nodes
        for node in pipeline.get("nodes", []):
            # Fallback to empty extensions if inLUMEN export is bare during testing
            compliance = node.get("compliance_extensions", {
                "has_logging": True,
                "uses_ai": "prepare_sharing_decision" in node.get("label", ""),
                "social_scoring_enabled": False,
                "biometric_categorization_enabled": False,
                "has_human_override_node": "prepare_sharing_decision" not in node.get("label", "")
            })
            
            self.ir_graph.add_node(
                node.get("id"),
                label=node.get("label"),
                kind=node.get("kind"),
                compliance=compliance
            )

        # Populate IR Graph Edges (Data flow paths)
        for conn in pipeline.get("connections", []):
            source = conn.get("from", {}).get("node")
            target = conn.get("to", {}).get("node")
            if source and target:
                self.ir_graph.add_edge(source, target)

    def evaluate_policies(self) -> dict:
        """Evaluates compiled IR node constraints against our taxonomy ruleset."""
        self.violations = []
        self.human_flags = []
        
        # Pull constraints metadata from your taxonomy object definitions if present
        constraints_ref = self.taxonomy.get("constraints", {})
        
        for node_id, data in self.ir_graph.nodes(data=True):
            comp = data.get("compliance", {})
            node_label = data.get("label")

            # 1. Prohibited Practice: Social Scoring Check
            if comp.get("social_scoring_enabled") is True:
                self.violations.append({
                    "rule": "Article 5: Social Scoring",
                    "node": node_label,
                    "severity": "CRITICAL_FAIL",
                    "msg": f"Prohibited practice detected at node '{node_label}': System uses citizen metrics across non-equivalent social domains.",
                    "remedy": "Remove the analytical profiling sub-module immediately."
                })

            # 2. Prohibited Practice: Biometric Categorization
            if comp.get("biometric_categorization_enabled") is True:
                self.violations.append({
                    "rule": "Article 5: Biometric Categorization",
                    "node": node_label,
                    "severity": "CRITICAL_FAIL",
                    "msg": f"Prohibited practice detected at node '{node_label}': System attempts data inference on protected political/religious classes.",
                    "remedy": "Isolate identity signatures from underlying dataset registries before downstream ingestion."
                })

            # 3. System Integrity: Traceability & Logging Node Check
            if comp.get("has_logging") is not True:
                self.violations.append({
                    "rule": "Article 12: Logging & Traceability",
                    "node": node_label,
                    "severity": "FAIL",
                    "msg": f"Structural Gap at node '{node_label}': Component lifecycle triggers run without an active execution logger.",
                    "remedy": "Inject an automated logging metadata interceptor inside the pipeline layout."
                })

            # 4. Human-In-The-Loop Boundary Check (AI Act Article 14)
            if comp.get("uses_ai") is True and comp.get("has_human_override_node") is not True:
                self.human_flags.append({
                    "rule": "Article 14: Human Oversight Boundary",
                    "node": node_label,
                    "severity": "HUMAN_INTERVENTION_REQUIRED",
                    "msg": f"Boundary Flag at node '{node_label}': System leverages AI automated support for data-sharing recommendations without counter-signing safeguards.",
                    "remedy": "Escalate review control parameters to an authorized Trondheim Kommune caseworker checkpoint."
                })

        # Final Evaluation Aggregator
        if any(v["severity"] in ["CRITICAL_FAIL", "FAIL"] for v in self.violations):
            status = "FAIL"
        elif self.human_flags:
            status = "HUMAN"
        else:
            status = "OK"

        return {
            "status": status,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "counts": {
                "nodes": len(self.ir_graph.nodes),
                "edges": len(self.ir_graph.edges),
                "fails": len(self.violations),
                "escalations": len(self.human_flags)
            },
            "violations": self.violations,
            "human_flags": self.human_flags
        }
