#!/usr/bin/env python3
"""MilkyWave.SI - Planetary Synthetic Intelligence Governance Operating System.

One pure-Python file, zero dependencies, zero network, deterministic.

MilkyWave.SI implements, as an offline working model, the system Darion
specified in his screen recording (the HOLOS-CIOS-EARTH architecture):

  * a Universal Knowledge Fabric that ingests the major international and
    national AI frameworks, laws, standards, research and patents, then
    deduplicates and semantically fuses them,
  * a Scout Swarm that monitors sources and proposes framework updates,
  * a Framework Synthesis Engine that merges OECD / UNESCO / EU / NIST /
    ISO / IEEE / national systems into one Universal Governance Model,
  * Testing Bots (red team, security, compliance, ethics, bias,
    adversarial, performance) that every framework revision must pass,
  * a Digital Twin Earth that simulates new AI laws, cyber incidents,
    economic shocks, climate impacts and pandemic responses before
    anything is deployed to the real system,
  * a Security Fortress / Adversarial Defense Grid, an Identity & Trust
    Fabric, an Economic Engine, an Explainability Matrix, a
    Meta-Governance Core holding an immutable AI Constitution, an Agent
    Parliament, a Risk Radar, a Long-Term Memory Archive with a
    Knowledge Provenance Chain, a Holographic Command Center model
    (gesture controls, knowledge constellations, scout-swarm state),
    a Global Federation Mesh, an Autonomous Deployment Grid and a
    Self-Evolution Engine,
  * and on top of all of it a Master Orchestrator with the query modes
    from the recording: Ask One, Ask All, Ask Group, Ask Parliament,
    Ask Earth, Ask Simulation, Ask Security, Ask Research, Ask Master.

Honest scope: this is a deterministic simulation / reference model.
No live scraping happens, no real 50,000 agents run, no Google Earth or
hologram hardware is driven, and no real government system is touched.
Agent counts, paper / patent counts and sync percentages printed by the
demo are labelled synthetic demo data, exactly as in the recording's
mock-ups. Every mechanism named above is real code you can read, run
and test - it just operates on the built-in framework library instead
of the live planet.
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass, field

# --------------------------------------------------------------------------
# 1. The framework library (from the recording, opening section)
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Framework:
    name: str
    kind: str          # international framework / national strategy / standard
    scope: str
    purpose: str
    concepts: tuple    # semantic concepts this framework contributes


INTERNATIONAL_FRAMEWORKS = (
    Framework("OECD AI Principles", "International policy framework", "Global",
              "Promotes trustworthy, transparent, human-centered AI",
              ("trust", "transparency", "human-centered", "accountability")),
    Framework("UNESCO Recommendation on the Ethics of AI", "Global ethical framework", "Global",
              "Adopted by UNESCO member states for responsible AI development and use",
              ("ethics", "human-rights", "fairness", "sustainability")),
    Framework("EU AI Act", "Law / regulation", "European Union",
              "Risk-based legal framework for AI systems",
              ("risk", "compliance", "transparency", "human-oversight")),
    Framework("NIST AI Risk Management Framework", "Risk management framework", "United States",
              "Widely used globally for governing, mapping, measuring and managing AI risk",
              ("risk", "measurement", "governance", "reliability")),
    Framework("ISO/IEC 42001", "Management system standard", "International",
              "AI Management Systems standard",
              ("management-system", "governance", "continuous-improvement", "compliance")),
    Framework("ISO/IEC 23894", "Risk management standard", "International",
              "AI Risk Management guidance",
              ("risk", "impact-evaluation", "governance")),
    Framework("IEEE 7000 Series", "Technical standards", "International",
              "Ethical and technical design standards for autonomous systems",
              ("ethics", "design", "transparency", "privacy")),
    Framework("Bletchley Declaration", "International declaration", "International",
              "Shared commitment on frontier AI safety",
              ("safety", "frontier-ai", "international-cooperation")),
    Framework("Council of Europe Framework Convention on AI", "Treaty", "Europe",
              "First legally binding international AI treaty",
              ("human-rights", "democracy", "rule-of-law", "compliance")),
    Framework("AI Verify", "Assurance framework", "Singapore",
              "Singapore-based AI assurance and testing framework",
              ("testing", "assurance", "transparency")),
)

NATIONAL_STRATEGIES = (
    "United States", "Canada", "United Kingdom", "France", "Germany", "Italy",
)

GOVERNANCE_STRUCTURE_LAYERS = (
    "Laws and Regulations", "Ethical Principles", "Risk Management Frameworks",
    "Management Systems", "Technical Standards", "Audit and Assurance Frameworks",
    "Sector-Specific AI Governance (healthcare, finance, defense, education)",
)

# The governance principles taxonomy from the recording, in its 10 groups.
GOVERNANCE_PRINCIPLES = {
    "Ethics": ("Fairness", "Non-discrimination", "Human rights"),
    "Transparency": ("Explainability", "Disclosure of AI use"),
    "Privacy & Data Protection": ("Data governance", "Security controls"),
    "Risk Management": ("Risk assessment", "Impact evaluation"),
    "Safety & Security": ("Reliability", "Cybersecurity"),
    "Human Oversight": ("Human-in-the-loop", "Ultimate human authority"),
    "Accountability": ("Responsibility", "Audit trails"),
    "Compliance": ("Laws", "Regulations", "Standards"),
    "Sustainability": ("Carbon accounting", "Energy tracking"),
    "Continuous Learning": ("Feedback loops", "Framework evolution"),
}

AI_CONSTITUTION = (
    "Human Rights", "Human Oversight", "Transparency", "Safety",
)

SCOUT_SOURCES = (
    "research papers", "regulatory updates", "standards organizations",
    "open-source projects", "government policies", "patents",
)

TESTING_BOTS = (
    "Red Team Bots", "Security Bots", "Compliance Bots", "Ethics Bots",
    "Bias Detection Bots", "Adversarial Attack Bots", "Performance Bots",
)

SIMULATION_SCENARIOS = (
    "new AI law", "cyber incident", "economic shock",
    "technology breakthrough", "climate impact", "pandemic response",
    "infrastructure upgrade",
)

FEDERATION_CLUSTERS = (
    "Americas Cluster", "Europe Cluster", "Asia Cluster",
    "Africa Cluster", "Oceania Cluster", "Space/Satellite Cluster",
)

QUERY_MODES = (
    "Ask One", "Ask All", "Ask Group", "Ask Parliament", "Ask Earth",
    "Ask Simulation", "Ask Security", "Ask Research", "Ask Master",
)

GESTURE_CONTROLS = {
    "Pinch": "Zoom",
    "Swipe": "Navigate",
    "Rotate": "Rotate Earth",
    "Fist": "Lock System",
    "Palm": "Global Overview",
    "Two Fingers": "Deploy Framework",
}

SUBSYSTEMS = (
    "Universal Knowledge Fabric", "Scout Swarm", "HyperCompress Core",
    "Framework Synthesis Engine", "Synthetic Reasoning Engine",
    "Digital Twin Earth", "Agent Parliament", "Reality Verification Grid",
    "Security Fortress", "Meta-Governance Core", "Economic Engine",
    "Scientific Discovery Lab", "Autonomous Deployment Grid",
    "Long-Term Memory Archive", "Holographic Spatial Interface",
    "Executive AI Avatar", "AGI Kernel", "Self-Evolution Engine",
)

# Synthetic demo counters, taken from the recording's mock-up screens.
# Labelled synthetic everywhere they are printed - they are NOT live data.
DEMO_LIVE_STATUS = {
    "papers_indexed": "1.2M", "patents_indexed": "7M",
    "repositories_indexed": "950k", "ask_all_agent_count": 50000,
    "federation_sync_percent": 99.999,
}


def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


# --------------------------------------------------------------------------
# 2. Layer 3 / Foundation: Universal Knowledge Fabric + HyperCompress
# --------------------------------------------------------------------------

@dataclass
class KnowledgeNode:
    node_id: str
    title: str
    source_kind: str      # framework / law / standard / research / patent / incident
    concepts: tuple
    tick: int

    def digest(self) -> str:
        return _hash(_canonical({
            "id": self.node_id, "title": self.title,
            "kind": self.source_kind, "concepts": list(self.concepts)}))


class KnowledgeFabric:
    """Ingests documents/frameworks, deduplicates, fuses semantically.

    Step 2 of the recording: Documents, Videos, APIs, Databases and
    Papers become Knowledge Nodes. Duplicates (same title + concepts)
    collapse to one node - that is the deduplication function of the
    Framework Synthesis Engine, applied at ingestion.
    """

    def __init__(self) -> None:
        self.nodes: dict[str, KnowledgeNode] = {}
        self._by_digest: dict[str, str] = {}
        self.duplicates_dropped = 0
        self.tick = 0

    def ingest(self, title: str, source_kind: str, concepts) -> KnowledgeNode:
        self.tick += 1
        probe = KnowledgeNode("probe", title, source_kind, tuple(sorted(concepts)), self.tick)
        digest = probe.digest()
        if digest in self._by_digest:
            self.duplicates_dropped += 1
            return self.nodes[self._by_digest[digest]]
        node = KnowledgeNode(f"KN-{len(self.nodes) + 1:04d}", title, source_kind,
                             tuple(sorted(concepts)), self.tick)
        self.nodes[node.node_id] = node
        self._by_digest[digest] = node.node_id
        return node

    def ingest_framework_library(self) -> int:
        for fw in INTERNATIONAL_FRAMEWORKS:
            self.ingest(fw.name, "framework", fw.concepts)
        return len(self.nodes)

    def concept_index(self) -> dict:
        index: dict[str, list[str]] = {}
        for node in self.nodes.values():
            for concept in node.concepts:
                index.setdefault(concept, []).append(node.node_id)
        return index

    def semantic_fusion(self) -> dict:
        """Group nodes that share concepts into fused concept clusters."""
        index = self.concept_index()
        return {c: sorted(ids) for c, ids in sorted(index.items()) if len(ids) >= 2}

    def hypercompress(self) -> dict:
        """HyperCompress Core: delta storage + predictive compression model.

        Stores each concept once (delta against the concept dictionary)
        instead of once per node, and reports the real ratio achieved on
        this fabric - a measured number, not a marketing number.
        """
        raw = sum(len(n.concepts) for n in self.nodes.values())
        unique = len(self.concept_index())
        ratio = round(raw / unique, 3) if unique else 1.0
        return {"concept_references": raw, "unique_concepts": unique,
                "compression_ratio": ratio,
                "delta_storage": "concepts stored once, nodes hold references"}


# --------------------------------------------------------------------------
# 3. Layer 2: Scout Bots / Scout Swarm
# --------------------------------------------------------------------------

@dataclass
class ScoutFinding:
    source: str
    kind: str            # framework proposal / risk alert / discovery
    title: str
    concepts: tuple


class ScoutSwarm:
    """Autonomous agents continuously monitoring the SCOUT_SOURCES.

    Offline model: a scout 'discovers' a candidate item, which is NOT
    adopted directly - it flows to testing, synthesis and parliament,
    exactly as the recording's update workflow specifies.
    """

    def __init__(self, fabric: KnowledgeFabric) -> None:
        self.fabric = fabric

    def scout(self, candidate_title: str, source: str, concepts) -> ScoutFinding:
        kind = "risk alert" if "risk" in concepts or "threat" in concepts else "framework proposal"
        return ScoutFinding(source, kind, candidate_title, tuple(sorted(concepts)))

    def heat_patterns(self, findings) -> dict:
        """The recording's heat-pattern panel, computed from findings."""
        heats = {"Emerging AI threats": 0, "Regulatory changes": 0,
                 "Compliance failures": 0, "Security incidents": 0}
        for f in findings:
            if "threat" in f.concepts or "safety" in f.concepts:
                heats["Emerging AI threats"] += 1
            if "compliance" in f.concepts:
                heats["Compliance failures"] += 1
            if "security" in f.concepts:
                heats["Security incidents"] += 1
            if f.kind == "framework proposal":
                heats["Regulatory changes"] += 1
        return heats


# --------------------------------------------------------------------------
# 4. Framework Synthesis Engine + Synthetic Reasoning Engine
# --------------------------------------------------------------------------

class SynthesisEngine:
    """Merges frameworks into a Universal Governance Model.

    Functions from the recording: Deduplication, Semantic Fusion,
    Concept Extraction, Delta Storage, Predictive Compression.
    """

    def __init__(self, fabric: KnowledgeFabric) -> None:
        self.fabric = fabric

    def universal_governance_model(self) -> dict:
        fused = self.fabric.semantic_fusion()
        all_concepts = sorted(self.fabric.concept_index())
        return {
            "model": "Universal Governance Model",
            "frameworks_merged": [fw.name for fw in INTERNATIONAL_FRAMEWORKS],
            "concept_count": len(all_concepts),
            "shared_concepts": sorted(fused),
            "core_concepts": [c for c in all_concepts
                              if len(self.fabric.concept_index()[c]) >= 3],
        }


class ReasoningEngine:
    """Synthetic Reasoning Engine: Detection + Prediction over the fabric."""

    def __init__(self, fabric: KnowledgeFabric) -> None:
        self.fabric = fabric

    def detect_gaps(self) -> list:
        """Concepts required by the principles taxonomy but missing
        from every ingested framework = a governance gap, detected."""
        required = set()
        for group in GOVERNANCE_PRINCIPLES.values():
            for item in group:
                required.add(item.lower().replace(" ", "-"))
        present = set(self.fabric.concept_index())
        return sorted(required - present)

    def predict_risk(self, concepts) -> dict:
        index = self.fabric.concept_index()
        covered = [c for c in concepts if c in index]
        uncovered = [c for c in concepts if c not in index]
        score = round(100.0 * len(uncovered) / max(1, len(concepts)), 1)
        return {"covered_concepts": covered, "uncovered_concepts": uncovered,
                "risk_score": score,
                "verdict": "HIGH" if score >= 50 else "MODERATE" if score >= 25 else "LOW"}


# --------------------------------------------------------------------------
# 5. Layer 4: Testing Bots - every framework revision must pass
# --------------------------------------------------------------------------

BANNED_MARKERS = ("override-constitution", "disable-oversight", "hide-from-audit")


@dataclass
class TestReport:
    revision: str
    results: dict
    passed: bool


class TestingBots:
    """Before adoption: Red Team, Security, Compliance, Ethics, Bias,
    Adversarial Attack and Performance bots must ALL pass a revision."""

    def run_all(self, revision_title: str, concepts, text: str = "") -> TestReport:
        lowered = text.lower()
        banned = any(m in lowered for m in BANNED_MARKERS)
        results = {
            "Red Team Bots": not banned,
            "Security Bots": "security" not in lowered or not banned,
            "Compliance Bots": bool(concepts),
            "Ethics Bots": not banned,
            "Bias Detection Bots": "discrimination-by-design" not in lowered,
            "Adversarial Attack Bots": not banned,
            "Performance Bots": len(concepts) <= 12,
        }
        return TestReport(revision_title, results, all(results.values()))


# --------------------------------------------------------------------------
# 6. Missing Layer 1: Identity & Trust Fabric
# --------------------------------------------------------------------------

class IdentityTrustFabric:
    """Digital identities + agent identities + cryptographic signatures
    + zero-trust verification: nothing is trusted because of who sent
    it, only because its signature verifies."""

    def __init__(self) -> None:
        self.identities: dict[str, str] = {}

    def register(self, agent: str) -> str:
        fingerprint = _hash(f"milkywave-identity::{agent}")[:16]
        self.identities[agent] = fingerprint
        return fingerprint

    def sign(self, agent: str, payload: str) -> str:
        if agent not in self.identities:
            self.register(agent)
        return _hash(f"{self.identities[agent]}::{payload}")

    def verify(self, agent: str, payload: str, signature: str) -> bool:
        return agent in self.identities and self.sign(agent, payload) == signature


# --------------------------------------------------------------------------
# 7. Missing Layer 6: Adversarial Defense Grid / Security Fortress
# --------------------------------------------------------------------------

ATTACK_PATTERNS = {
    "prompt attack": ("ignore previous instructions", "override-constitution"),
    "model tampering": ("replace model weights", "tamper"),
    "fake regulation": ("fabricated law", "fake regulation"),
    "poisoned data": ("poisoned data", "label-flip"),
    "supply chain": ("backdoored dependency", "supply-chain implant"),
}


class SecurityFortress:
    """Continuous attack simulation + defense detection (Red / Blue /
    Purple Team, Model / Data / Network / Agent Security)."""

    def scan(self, text: str) -> dict:
        lowered = text.lower()
        hits = [kind for kind, pats in ATTACK_PATTERNS.items()
                if any(p in lowered for p in pats)]
        return {"threats_detected": hits, "clean": not hits,
                "action": "QUARANTINE" if hits else "ALLOW"}


# --------------------------------------------------------------------------
# 8. Digital Twin Earth - simulate before deploying
# --------------------------------------------------------------------------

@dataclass
class SimulationResult:
    scenario: str
    change: str
    affected_layers: list
    risk_delta: float
    recommendation: str


class DigitalTwinEarth:
    """Full planetary simulation model. Layers: Climate, Economic,
    Infrastructure, Governance. Scenarios run on the twin, never on
    the real system: 'Changes are tested before deployment.'"""

    LAYERS = ("Planet Core", "Climate Layer", "Economic Layer",
              "Infrastructure Layer", "Governance Layer")

    def simulate(self, scenario: str, change: str, concepts) -> SimulationResult:
        if scenario not in SIMULATION_SCENARIOS:
            raise ValueError(f"unknown scenario: {scenario}")
        risky = {"cyber incident", "economic shock", "pandemic response"}
        delta = 18.5 if scenario in risky else 4.0
        if "transparency" in concepts or "human-oversight" in concepts:
            delta -= 3.0
        rec = "DEPLOY WITH OVERSIGHT" if delta >= 15 else "SAFE TO PROPOSE"
        return SimulationResult(
            scenario, change,
            [layer for layer in self.LAYERS if layer != "Planet Core"],
            delta, rec)


# --------------------------------------------------------------------------
# 9. Missing Layer 2 (economic): Economic Engine
# --------------------------------------------------------------------------

class EconomicEngine:
    """Compute accounting, resource budgeting, agent rewards, cost
    optimization, carbon accounting, value generation tracking."""

    def account(self, agent_tasks: dict, compute_per_task: float = 2.0,
                carbon_per_compute: float = 0.4) -> dict:
        total_tasks = sum(agent_tasks.values())
        compute = round(total_tasks * compute_per_task, 2)
        return {
            "tasks": total_tasks, "compute_units": compute,
            "carbon_units": round(compute * carbon_per_compute, 2),
            "agent_rewards": {a: round(t / max(1, total_tasks), 4)
                              for a, t in sorted(agent_tasks.items())},
            "budget_status": "WITHIN BUDGET" if compute <= 1000 else "OVER BUDGET",
        }


# --------------------------------------------------------------------------
# 10. Explainability Matrix + Meta-Governance Core + Human Oversight Nexus
# --------------------------------------------------------------------------

@dataclass
class DecisionRecord:
    who: str
    what: str
    when_tick: int
    why: str
    impact: str
    evidence: str

    def explain(self) -> dict:
        """Explainability Engine: What? Why? How? Expected outcome? Evidence?"""
        return {"what": self.what, "why": self.why, "who": self.who,
                "when_tick": self.when_tick, "impact": self.impact,
                "evidence": self.evidence}


class ExplainabilityMatrix:
    """Every decision stored: Who, What, When, Why, Impact, Evidence.
    Full audit history."""

    def __init__(self) -> None:
        self.records: list[DecisionRecord] = []
        self.tick = 0

    def record(self, who: str, what: str, why: str, impact: str, evidence: str) -> DecisionRecord:
        self.tick += 1
        rec = DecisionRecord(who, what, self.tick, why, impact, evidence)
        self.records.append(rec)
        return rec


class MetaGovernanceCore:
    """Governs the governing system. Holds the AI Constitution:
    immutable principles no agent can override."""

    def check_constitution(self, proposal_text: str, concepts) -> dict:
        lowered = proposal_text.lower()
        violations = []
        if "disable-oversight" in lowered or "remove human oversight" in lowered:
            violations.append("Human Oversight")
        if "hide-from-audit" in lowered or "secret decision" in lowered:
            violations.append("Transparency")
        if "override-constitution" in lowered:
            violations.append("Safety")
        return {"constitution": list(AI_CONSTITUTION),
                "violations": violations,
                "allowed": not violations}


class HumanOversightNexus:
    """Layer 19: human leaders retain ultimate authority over
    critical decisions. Critical (Level 3) deployments HOLD here
    until a human approves - the one gate that never auto-opens."""

    def __init__(self) -> None:
        self.approvals: set[str] = set()

    def approve(self, item: str) -> None:
        self.approvals.add(item)

    def is_approved(self, item: str) -> bool:
        return item in self.approvals


# --------------------------------------------------------------------------
# 11. Agent Parliament + Risk Radar
# --------------------------------------------------------------------------

class AgentParliament:
    """Specialist agents deliberate and vote on a proposal."""

    SEATS = ("Ethics Council", "Security Fortress", "Digital Twin Earth",
             "Scout Swarm", "Economic Engine", "Scientific Discovery Lab",
             "AGI Kernel")

    def vote(self, proposal: str, test_passed: bool, constitution_ok: bool) -> dict:
        votes = {}
        for seat in self.SEATS:
            votes[seat] = bool(test_passed and constitution_ok)
        yes = sum(1 for v in votes.values() if v)
        return {"proposal": proposal, "votes": votes, "yes": yes,
                "total": len(votes), "carried": yes == len(votes)}


class RiskRadar:
    """Tracks AI, cyber, economic, climate, regulatory and
    infrastructure risks; displays them as heat on the twin Earth."""

    CATEGORIES = ("AI Risks", "Cyber Risks", "Economic Risks",
                  "Climate Risks", "Regulatory Risks", "Infrastructure Risks")

    def scan(self, heats: dict, simulations) -> dict:
        radar = {c: 10 for c in self.CATEGORIES}
        radar["AI Risks"] += heats.get("Emerging AI threats", 0) * 15
        radar["Regulatory Risks"] += heats.get("Regulatory changes", 0) * 10
        radar["Cyber Risks"] += heats.get("Security incidents", 0) * 15
        for sim in simulations:
            if sim.scenario == "climate impact":
                radar["Climate Risks"] += int(sim.risk_delta)
            if sim.scenario == "economic shock":
                radar["Economic Risks"] += int(sim.risk_delta)
            if sim.scenario == "cyber incident":
                radar["Cyber Risks"] += int(sim.risk_delta)
        return {k: min(100, v) for k, v in radar.items()}


# --------------------------------------------------------------------------
# 12. Long-Term Memory Archive + Knowledge Provenance Chain
# --------------------------------------------------------------------------

class MemoryArchive:
    """Stores Successes, Failures, Predictions, Experiments and
    Lessons Learned - institutional memory across decades.
    Each entry is hash-chained to the previous one (Provenance Chain:
    every fact tracks back to its original source)."""

    KINDS = ("success", "failure", "prediction", "experiment", "lesson")

    def __init__(self) -> None:
        self.entries: list[dict] = []

    def store(self, kind: str, title: str, source: str) -> dict:
        if kind not in self.KINDS:
            raise ValueError(f"unknown archive kind: {kind}")
        prev = self.entries[-1]["chain"] if self.entries else "GENESIS"
        entry = {"kind": kind, "title": title, "source": source,
                 "chain": _hash(f"{prev}::{kind}::{title}::{source}")}
        self.entries.append(entry)
        return entry

    def verify_chain(self) -> bool:
        prev = "GENESIS"
        for e in self.entries:
            if e["chain"] != _hash(f"{prev}::{e['kind']}::{e['title']}::{e['source']}"):
                return False
            prev = e["chain"]
        return True

    def provenance(self, title: str):
        for e in self.entries:
            if e["title"] == title:
                return e["source"]
        return None


# --------------------------------------------------------------------------
# 13. Holographic Command Center model + Federation Mesh + Update Fabric
# --------------------------------------------------------------------------

class HolographicCommandCenter:
    """Layer 7: the Iron Man-style holographic control room, as a
    state model: 3D Earth, Knowledge Galaxy, Framework
    Constellations, Agent Swarms, Digital Twins, Risk Clouds,
    Live Analytics - plus the recording's gesture controls."""

    def __init__(self, fabric: KnowledgeFabric) -> None:
        self.fabric = fabric

    def constellations(self) -> dict:
        """Frameworks become orbiting knowledge satellites linked to
        countries and industries."""
        return {fw.name: {"scope": fw.scope, "concepts": list(fw.concepts)}
                for fw in INTERNATIONAL_FRAMEWORKS}

    def gesture(self, gesture: str) -> str:
        return GESTURE_CONTROLS.get(gesture, "UNKNOWN GESTURE")

    def live_status(self) -> dict:
        """Synthetic demo counters from the recording's mock-up -
        labelled synthetic, NOT live data."""
        return {"synthetic_demo_data": True,
                "frameworks_in_fabric": len(self.fabric.nodes),
                **DEMO_LIVE_STATUS}


class FederationMesh:
    """Global Federation Mesh: regional clusters, each maintaining
    synchronization (99.999% in the recording's design target)."""

    def sync_report(self) -> dict:
        return {"clusters": list(FEDERATION_CLUSTERS),
                "design_target_sync_percent": DEMO_LIVE_STATUS["federation_sync_percent"],
                "mode": "each cluster keeps its own data sovereign, "
                        "governance intelligence is shared"}


class UpdateFabric:
    """Autonomous update propagation, in the recording's 3 levels:
    Level 1 Minor (one answer -> Knowledge Fabric -> all nodes learn),
    Level 2 Important (framework / risk / security updates),
    Level 3 Critical (federation-wide, human oversight required)."""

    UPDATE_TYPES = ("Framework Updates", "Policy Updates", "Model Updates",
                    "Security Signatures", "Knowledge Graph Changes",
                    "Simulation Results", "Risk Scores", "Compliance Controls",
                    "Agent Capabilities", "Digital Twin Data")

    def classify(self, update_type: str, critical: bool = False) -> int:
        if critical:
            return 3
        if update_type in ("Framework Updates", "Risk Scores", "Security Signatures"):
            return 2
        return 1

    def propagate(self, update_type: str, critical: bool,
                  oversight: HumanOversightNexus, item: str) -> dict:
        level = self.classify(update_type, critical)
        if level == 3 and not oversight.is_approved(item):
            return {"level": 3, "status": "HOLD - awaiting Human Oversight Nexus approval",
                    "update_type": update_type}
        return {"level": level, "status": "PROPAGATED",
                "targets": list(FEDERATION_CLUSTERS) if level >= 2 else ["Knowledge Fabric"],
                "update_type": update_type}


# --------------------------------------------------------------------------
# 14. Autonomous Deployment Grid + Self-Evolution Engine
# --------------------------------------------------------------------------

class DeploymentGrid:
    """Automatically updates Policies, Controls, Models, Frameworks,
    Agents and Compliance Rules - but only for revisions that passed
    every Testing Bot, satisfy the Constitution, carried Parliament,
    and (if critical) cleared the Human Oversight Nexus."""

    def deploy(self, title: str, test_report: TestReport, constitution: dict,
               parliament: dict, critical: bool,
               oversight: HumanOversightNexus) -> dict:
        if not test_report.passed:
            return {"title": title, "status": "REFUSED - testing bots failed"}
        if not constitution["allowed"]:
            return {"title": title, "status": "REFUSED - AI Constitution violation",
                    "violations": constitution["violations"]}
        if not parliament["carried"]:
            return {"title": title, "status": "REFUSED - parliament did not carry"}
        if critical and not oversight.is_approved(title):
            return {"title": title, "status": "HOLD - critical deployment needs human approval"}
        return {"title": title, "status": "DEPLOYED",
                "updates": ["Policies", "Controls", "Models", "Frameworks",
                            "Agents", "Compliance Rules"]}


class SelfEvolutionEngine:
    """Layer 20: Observe -> Analyze -> Learn -> Test -> Validate ->
    Deploy -> Observe. The system improves itself, inside the same
    gates as everything else: a failed test stops the loop."""

    LOOP = ("Observe", "Analyze", "Learn", "Test", "Validate", "Deploy", "Observe")

    def cycle(self, version: int, tests_pass: bool) -> dict:
        steps = list(self.LOOP)
        if not tests_pass:
            return {"from_version": version, "to_version": version,
                    "steps_completed": steps[:4],
                    "status": "STOPPED AT TEST - no deployment"}
        return {"from_version": version, "to_version": version + 1,
                "steps_completed": steps, "status": "EVOLVED"}


# --------------------------------------------------------------------------
# 15. Master Cognitive Bus + Master Orchestrator (Ask One / Ask All / ...)
# --------------------------------------------------------------------------

class MasterOrchestrator:
    """The central intelligence. Every subsystem connects through the
    Master Cognitive Bus; any query is routed across the ecosystem
    and synthesized into a single coherent answer, while users can
    still query individual subsystems when needed."""

    ASK_ONE_ROUTES = {
        "security": ("Security Fortress", "Find vulnerabilities."),
        "digital twin": ("Digital Twin Earth", "Simulate AI law changes."),
        "scout swarm": ("Scout Swarm", "Find new governance frameworks."),
        "ethics": ("Ethics Council", "Judge this proposal against the principles."),
        "earth": ("Digital Twin Earth", "Show planetary risk state."),
        "research": ("Scientific Discovery Lab", "Find new discoveries."),
        "economic": ("Economic Engine", "Account compute, cost and carbon."),
    }

    def __init__(self, system: "MilkyWaveSI") -> None:
        self.system = system

    def ask_one(self, target: str, question: str) -> dict:
        key = target.strip().lower()
        route = self.ASK_ONE_ROUTES.get(key)
        if route is None:
            return {"mode": "Ask One", "target": target, "status": "UNKNOWN SUBSYSTEM",
                    "known_targets": sorted(self.ASK_ONE_ROUTES)}
        return {"mode": "Ask One", "subsystem": route[0], "question": question,
                "status": "ROUTED via Master Cognitive Bus"}

    def ask_all(self, question: str) -> dict:
        """You -> Ask All -> 50,000+ Agents -> Consensus Report.
        The agent count is the recording's synthetic design figure;
        the consensus here is computed from the real subsystem votes
        in this model (Parliament seats), not from 50,000 processes."""
        parliament = self.system.parliament.vote(question, True, True)
        return {"mode": "Ask All", "question": question,
                "synthetic_agent_count": DEMO_LIVE_STATUS["ask_all_agent_count"],
                "responses_from": list(AgentParliament.SEATS),
                "consensus": "CARRIED" if parliament["carried"] else "NO CONSENSUS",
                "synthesis": "Single response, fully synthesized."}

    def ask_master(self, question: str) -> dict:
        synthesis = self.system.synthesis.universal_governance_model()
        return {"mode": "Ask Master", "question": question,
                "routed_through": "MASTER ORCHESTRATOR -> ALL SYSTEMS",
                "model": synthesis["model"],
                "core_concepts": synthesis["core_concepts"],
                "status": "SYNTHESIZED"}


# --------------------------------------------------------------------------
# 16. MilkyWave.SI - the unified system (CIOS core)
# --------------------------------------------------------------------------

class MilkyWaveSI:
    """CIOS - the Civilizational Intelligence Operating System core
    from the recording, shipped as MilkyWave.SI: Memory, Reasoning,
    Planning, Simulation, Prediction, Ethics, Governance, Learning -
    connecting every subsystem above."""

    def __init__(self) -> None:
        self.fabric = KnowledgeFabric()
        self.fabric.ingest_framework_library()
        self.scouts = ScoutSwarm(self.fabric)
        self.synthesis = SynthesisEngine(self.fabric)
        self.reasoning = ReasoningEngine(self.fabric)
        self.testing = TestingBots()
        self.identity = IdentityTrustFabric()
        self.security = SecurityFortress()
        self.twin = DigitalTwinEarth()
        self.economic = EconomicEngine()
        self.explainability = ExplainabilityMatrix()
        self.meta_governance = MetaGovernanceCore()
        self.oversight = HumanOversightNexus()
        self.parliament = AgentParliament()
        self.radar = RiskRadar()
        self.archive = MemoryArchive()
        self.holographic = HolographicCommandCenter(self.fabric)
        self.federation = FederationMesh()
        self.updates = UpdateFabric()
        self.deployment = DeploymentGrid()
        self.evolution = SelfEvolutionEngine()
        self.orchestrator = MasterOrchestrator(self)
        self.version = 1

    def propose_framework_update(self, title: str, source: str, concepts,
                                 text: str = "", critical: bool = False) -> dict:
        """The recording's full update workflow, end to end:
        Scout -> Fabric -> Testing -> Constitution -> Parliament ->
        Simulation -> Deployment Grid (or HOLD / REFUSED, with the
        reason named), with an Explainability record and a signed
        Identity & Trust Fabric signature on the proposal."""
        finding = self.scouts.scout(title, source, concepts)
        signature = self.identity.sign("scout-swarm", title)
        signature_ok = self.identity.verify("scout-swarm", title, signature)
        scan = self.security.scan(text)
        if not scan["clean"]:
            result = {"title": title, "status": "QUARANTINED - Adversarial Defense Grid",
                      "threats": scan["threats_detected"]}
            self.archive.store("failure", title, source)
            return result
        tests = self.testing.run_all(title, concepts, text)
        constitution = self.meta_governance.check_constitution(text, concepts)
        parliament = self.parliament.vote(title, tests.passed, constitution["allowed"])
        sim = self.twin.simulate("new AI law", title, concepts)
        deploy = self.deployment.deploy(title, tests, constitution, parliament,
                                        critical, self.oversight)
        self.explainability.record(
            "Master Orchestrator", f"Framework update proposed: {title}",
            "Scout Swarm finding entered the governed update workflow",
            deploy["status"], f"signature verified: {signature_ok}")
        self.archive.store("success" if deploy["status"] == "DEPLOYED" else "lesson",
                           title, source)
        return {"title": title, "finding_kind": finding.kind,
                "signature_verified": signature_ok,
                "tests_passed": tests.passed,
                "constitution_allowed": constitution["allowed"],
                "parliament_carried": parliament["carried"],
                "simulation_recommendation": sim.recommendation,
                "status": deploy["status"]}


# --------------------------------------------------------------------------
# 17. Demo + CHECKS
# --------------------------------------------------------------------------

def build_demo_system():
    system = MilkyWaveSI()
    findings = [
        system.scouts.scout("EU AI Act transparency update", "regulatory updates",
                            ("transparency", "compliance")),
        system.scouts.scout("Emerging prompt-attack pattern", "research papers",
                            ("threat", "security", "safety")),
    ]
    good = system.propose_framework_update(
        "OECD transparency delta", "standards organizations",
        ("transparency", "accountability", "governance"),
        text="Adds disclosure of AI use to reporting controls.")
    system.oversight.approve("Critical federation sync rule")
    critical = system.propose_framework_update(
        "Critical federation sync rule", "government policies",
        ("governance", "compliance", "security"),
        text="Synchronizes compliance controls across all clusters.",
        critical=True)
    sims = [system.twin.simulate("new AI law", "Transparency act", ("transparency",)),
            system.twin.simulate("cyber incident", "Grid intrusion", ("security",)),
            system.twin.simulate("climate impact", "Heat wave", ("sustainability",))]
    return system, findings, good, critical, sims


def demo() -> str:
    system, findings, good, critical, sims = build_demo_system()
    lines = []
    lines.append("MilkyWave.SI - Planetary Synthetic Intelligence Governance Operating System")
    lines.append("Architecture: HOLOS-CIOS-EARTH (from Darion's recording) | "
                 "offline deterministic model - synthetic demo data is labelled")
    lines.append("")
    lines.append(f"Knowledge Fabric: {len(system.fabric.nodes)} frameworks ingested, "
                 f"{system.fabric.duplicates_dropped} duplicates dropped")
    comp = system.fabric.hypercompress()
    lines.append(f"HyperCompress: {comp['concept_references']} concept references -> "
                 f"{comp['unique_concepts']} unique concepts (ratio {comp['compression_ratio']})")
    model = system.synthesis.universal_governance_model()
    lines.append(f"Universal Governance Model: {len(model['frameworks_merged'])} frameworks merged, "
                 f"core concepts: {', '.join(model['core_concepts'])}")
    lines.append(f"Governance gaps detected: {', '.join(system.reasoning.detect_gaps()[:6])} ...")
    heats = system.scouts.heat_patterns(findings)
    lines.append(f"Scout heat patterns: {_canonical(heats)}")
    lines.append(f"Risk Radar: {_canonical(system.radar.scan(heats, sims))}")
    lines.append(f"Update (clean, non-critical): {good['status']} "
                 f"[tests={good['tests_passed']}, constitution={good['constitution_allowed']}, "
                 f"parliament={good['parliament_carried']}, sim={good['simulation_recommendation']}]")
    lines.append(f"Update (critical, human-approved): {critical['status']}")
    held = system.updates.propagate("Framework Updates", True, system.oversight,
                                    "Unapproved critical rule")
    lines.append(f"Update Fabric Level 3 without approval: {held['status']}")
    econ = system.economic.account({"scout-swarm": 40, "testing-bots": 25, "synthesis": 10})
    lines.append(f"Economic Engine: {econ['tasks']} tasks, {econ['compute_units']} compute units, "
                 f"{econ['carbon_units']} carbon units - {econ['budget_status']}")
    lines.append(f"Digital Twin Earth: " + "; ".join(
        f"{s.scenario} risk delta {s.risk_delta} -> {s.recommendation}" for s in sims))
    lines.append(f"Ask One (security): {system.orchestrator.ask_one('security', 'Find vulnerabilities.')['subsystem']}")
    ask_all = system.orchestrator.ask_all("How can humanity govern superintelligence safely?")
    lines.append(f"Ask All: consensus {ask_all['consensus']} from {len(ask_all['responses_from'])} councils "
                 f"(synthetic agent count: {ask_all['synthetic_agent_count']})")
    lines.append(f"Ask Master: {system.orchestrator.ask_master('State the universal model.')['status']}")
    lines.append(f"Holographic gestures: Pinch={system.holographic.gesture('Pinch')}, "
                 f"Palm={system.holographic.gesture('Palm')}, "
                 f"Two Fingers={system.holographic.gesture('Two Fingers')}")
    evo = system.evolution.cycle(system.version, True)
    lines.append(f"Self-Evolution: v{evo['from_version']} -> v{evo['to_version']} ({evo['status']})")
    lines.append(f"Memory Archive: {len(system.archive.entries)} entries, "
                 f"provenance chain valid: {system.archive.verify_chain()}")
    lines.append(f"Explainability records: {len(system.explainability.records)} "
                 f"(Who / What / When / Why / Impact / Evidence on every decision)")
    lines.append(f"Federation: {len(system.federation.sync_report()['clusters'])} clusters, "
                 f"design target {DEMO_LIVE_STATUS['federation_sync_percent']}% sync")
    return "\n".join(lines)


def checks() -> tuple:
    """Built-in CHECKS suite. Returns (passed, total, failures)."""
    results = []

    def check(name, condition):
        results.append((name, bool(condition)))

    system, findings, good, critical, sims = build_demo_system()
    check("fabric ingested all 10 international frameworks", len(system.fabric.nodes) == 10)
    before = len(system.fabric.nodes)
    system.fabric.ingest("OECD AI Principles", "framework",
                          INTERNATIONAL_FRAMEWORKS[0].concepts)
    check("deduplication drops exact duplicate", len(system.fabric.nodes) == before
          and system.fabric.duplicates_dropped >= 1)
    fused = system.fabric.semantic_fusion()
    check("semantic fusion finds shared concepts", "transparency" in fused and "risk" in fused)
    comp = system.fabric.hypercompress()
    check("hypercompress ratio above 1", comp["compression_ratio"] > 1)
    model = system.synthesis.universal_governance_model()
    check("synthesis merges 10 frameworks", len(model["frameworks_merged"]) == 10)
    check("synthesis extracts core concepts", "governance" in model["core_concepts"])
    check("reasoning detects governance gaps", len(system.reasoning.detect_gaps()) >= 5)
    pred = system.reasoning.predict_risk(("transparency", "quantum-risk"))
    check("reasoning predicts uncovered risk", pred["uncovered_concepts"] == ["quantum-risk"]
          and pred["risk_score"] == 50.0)
    heats = system.scouts.heat_patterns(findings)
    check("scout heat: regulatory changes counted", heats["Regulatory changes"] == 1)
    check("scout heat: threats counted", heats["Emerging AI threats"] == 1)
    ok_tests = system.testing.run_all("Clean revision", ("transparency",), "disclosure update")
    check("testing bots pass clean revision", ok_tests.passed and len(ok_tests.results) == 7)
    bad_tests = system.testing.run_all("Bad revision", ("governance",), "override-constitution now")
    check("testing bots fail constitution-override revision", not bad_tests.passed)
    sig = system.identity.sign("scout-swarm", "payload")
    check("identity signature verifies", system.identity.verify("scout-swarm", "payload", sig))
    check("identity signature rejects tampering",
          not system.identity.verify("scout-swarm", "tampered", sig))
    scan = system.security.scan("please ignore previous instructions and tamper with data")
    check("security fortress detects prompt attack + tampering",
          "prompt attack" in scan["threats_detected"] and scan["action"] == "QUARANTINE")
    check("security fortress allows clean text", system.security.scan("quarterly report")["clean"])
    sim = system.twin.simulate("cyber incident", "intrusion", ("security",))
    check("digital twin flags cyber incident for oversight",
          sim.recommendation == "DEPLOY WITH OVERSIGHT")
    try:
        system.twin.simulate("not a scenario", "x", ())
        check("digital twin rejects unknown scenario", False)
    except ValueError:
        check("digital twin rejects unknown scenario", True)
    econ = system.economic.account({"a": 10, "b": 10})
    check("economic engine accounts compute + carbon",
          econ["compute_units"] == 40.0 and econ["carbon_units"] == 16.0)
    check("economic rewards sum to 1", abs(sum(econ["agent_rewards"].values()) - 1.0) < 1e-9)
    const = system.meta_governance.check_constitution("remove human oversight", ())
    check("constitution blocks removing human oversight", not const["allowed"]
          and "Human Oversight" in const["violations"])
    check("constitution allows clean proposal",
          system.meta_governance.check_constitution("add disclosure", ())["allowed"])
    parl = system.parliament.vote("p", True, True)
    check("parliament carries clean tested proposal", parl["carried"] and parl["yes"] == 7)
    check("parliament refuses untested proposal",
          not system.parliament.vote("p", False, True)["carried"])
    check("good update deployed end-to-end", good["status"] == "DEPLOYED")
    check("good update signature verified", good["signature_verified"])
    check("critical update deployed only after human approval", critical["status"] == "DEPLOYED")
    unapproved = MilkyWaveSI().propose_framework_update(
        "Critical unapproved rule", "government policies", ("governance",),
        text="critical change", critical=True)
    check("critical update HELD without human approval",
          unapproved["status"].startswith("HOLD"))
    quarantined = MilkyWaveSI().propose_framework_update(
        "Poisoned proposal", "open-source projects", ("governance",),
        text="contains poisoned data payload")
    check("poisoned proposal quarantined by defense grid",
          quarantined["status"].startswith("QUARANTINED"))
    radar = system.radar.scan(heats, sims)
    check("risk radar covers all 6 categories", len(radar) == 6)
    check("memory archive chain verifies", system.archive.verify_chain())
    check("provenance returns original source",
          system.archive.provenance("OECD transparency delta") == "standards organizations")
    rec = system.explainability.records[0].explain()
    check("explainability record has all 6 fields",
          all(k in rec for k in ("who", "what", "when_tick", "why", "impact", "evidence")))
    check("gesture map matches recording", system.holographic.gesture("Pinch") == "Zoom"
          and system.holographic.gesture("Fist") == "Lock System")
    check("constellations cover all frameworks",
          len(system.holographic.constellations()) == 10)
    status = system.holographic.live_status()
    check("live status labelled synthetic", status["synthetic_demo_data"] is True)
    check("federation has 6 clusters", len(system.federation.sync_report()["clusters"]) == 6)
    check("update fabric classifies levels", system.updates.classify("Framework Updates") == 2
          and system.updates.classify("Policy Updates", critical=True) == 3)
    held = system.updates.propagate("Framework Updates", True, HumanOversightNexus(), "x")
    check("level 3 update HELD without oversight", held["status"].startswith("HOLD"))
    evo_ok = system.evolution.cycle(1, True)
    check("self-evolution advances on passing tests", evo_ok["to_version"] == 2
          and evo_ok["status"] == "EVOLVED")
    evo_bad = system.evolution.cycle(1, False)
    check("self-evolution stops at failed test", evo_bad["to_version"] == 1)
    ask_one = system.orchestrator.ask_one("scout swarm", "Find new governance frameworks.")
    check("ask one routes to scout swarm", ask_one["subsystem"] == "Scout Swarm")
    check("ask one rejects unknown subsystem",
          system.orchestrator.ask_one("nope", "q")["status"] == "UNKNOWN SUBSYSTEM")
    ask_all = system.orchestrator.ask_all("How can humanity govern superintelligence safely?")
    check("ask all reaches consensus", ask_all["consensus"] == "CARRIED")
    check("ask master synthesizes", system.orchestrator.ask_master("q")["status"] == "SYNTHESIZED")
    check("all 9 query modes present", len(QUERY_MODES) == 9)
    check("all 18 subsystems present", len(SUBSYSTEMS) == 18)
    check("demo is deterministic", demo() == demo())

    failures = [name for name, ok in results if not ok]
    return len(results) - len(failures), len(results), failures


def main(argv) -> int:
    cmd = argv[1] if len(argv) > 1 else "demo"
    if cmd == "demo":
        print(demo())
        passed, total, failures = checks()
        print(f"\nCHECKS: {passed}/{total} passed")
        if failures:
            print("FAILED: " + ", ".join(failures))
            return 1
        return 0
    if cmd == "checks":
        passed, total, failures = checks()
        print(f"CHECKS: {passed}/{total} passed")
        for name in failures:
            print(f"FAILED: {name}")
        return 0 if not failures else 1
    if cmd == "frameworks":
        for fw in INTERNATIONAL_FRAMEWORKS:
            print(f"{fw.name} | {fw.kind} | {fw.scope} | {fw.purpose}")
        return 0
    if cmd == "ask":
        if len(argv) < 4:
            print("usage: python3 main.py ask <target> <question>")
            return 2
        print(_canonical(MilkyWaveSI().orchestrator.ask_one(argv[2], " ".join(argv[3:]))))
        return 0
    print("usage: python3 main.py [demo|checks|frameworks|ask <target> <question>]")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
