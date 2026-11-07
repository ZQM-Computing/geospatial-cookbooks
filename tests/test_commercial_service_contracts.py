"""Fail-closed contract checks for proposed ZQM Computing service offers.

These checks verify metadata and marketing boundaries only. They do not certify
source data, professional conclusions, implementation quality or deployments.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "docs" / "commercial-service-contracts.json"
EXPECTED_IDS = (
    "preliminary-site-screening",
    "gis-automation",
    "web-gis-and-apis",
)
COMMON_EVIDENCE = {
    "agreed-scope",
    "source-provenance",
    "source-license-and-reuse-rights",
    "data-coverage-state",
    "effective-and-retrieval-dates",
    "uncertainty-and-missing-data",
    "reproducible-qa",
    "reviewer-approval",
}
ADDITIONAL_EVIDENCE = {
    EXPECTED_IDS[0]: {"jurisdiction", "boundary-and-crs-assumptions", "professional-escalation"},
    EXPECTED_IDS[1]: {"schema-contract", "row-reconciliation", "error-and-retry-behavior", "rerun-and-recovery-test"},
    EXPECTED_IDS[2]: {"access-and-authorization-model", "secret-handling-review", "security-and-regression-tests", "rollback-verification"},
}


class CommercialServiceContractsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

    def test_proposed_non_guaranteed_global_scope(self) -> None:
        self.assertEqual(self.data["schema_version"], 1)
        self.assertEqual(self.data["owner"], "ZQM Computing")
        self.assertEqual(self.data["status"], "proposed-not-launched")
        self.assertEqual(
            self.data["geographic_coverage_policy"],
            "availability-provenance-and-reuse-rights-verified-per-jurisdiction",
        )
        self.assertEqual(
            set(self.data["coverage_states"]),
            {"verified", "partial", "missing", "unavailable", "unverified"},
        )
        self.assertTrue(any("not a completeness" in note for note in self.data["policy_notes"]))
        self.assertTrue(any("not proven runtime dependencies" in note for note in self.data["policy_notes"]))

    def test_exactly_three_ordered_distinct_offers(self) -> None:
        offers = self.data["offers"]
        self.assertEqual(tuple(offer["id"] for offer in offers), EXPECTED_IDS)
        self.assertEqual([offer["launch_order"] for offer in offers], [1, 2, 3])
        self.assertEqual(len({offer["id"] for offer in offers}), 3)

    def test_no_offer_bypasses_provenance_qa_or_human_review(self) -> None:
        for offer in self.data["offers"]:
            with self.subTest(offer=offer["id"]):
                self.assertEqual(offer["status"], "scope-and-data-review-required")
                self.assertEqual(
                    offer["review_gate"], "human-approval-before-client-delivery"
                )
                evidence = offer["required_evidence"]
                self.assertEqual(len(evidence), len(set(evidence)))
                self.assertTrue(
                    COMMON_EVIDENCE | ADDITIONAL_EVIDENCE[offer["id"]] <= set(evidence),
                    f"Missing mandatory evidence for {offer['id']}",
                )
                self.assertTrue(offer["target_buyers"])
                self.assertTrue(offer["delivery_modes"])
                self.assertTrue(offer["deliverables"])
                self.assertTrue(offer["candidate_repositories"])

    def test_scorecard_has_commercial_and_engineering_metrics(self) -> None:
        scorecard = self.data["measurement"]
        self.assertIn("gross-revenue", scorecard["commercial"])
        self.assertIn("contracts-won", scorecard["commercial"])
        self.assertIn("pr-lead-time-hours", scorecard["engineering"])
        self.assertIn("ci-success-rate", scorecard["engineering"])
        for metrics in scorecard.values():
            self.assertEqual(len(metrics), len(set(metrics)))

    def test_readme_links_contract_registry(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("(docs/commercial-service-contracts.json)", readme)


if __name__ == "__main__":
    unittest.main()
