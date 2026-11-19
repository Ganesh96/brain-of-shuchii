"""Adversarial structural tests. Only standard library; no model-generated answers."""
import json
import re
import unittest
from pathlib import Path

from engine.router import registry, route, validate

ROOT = Path(__file__).resolve().parents[1]


class RoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = json.loads((ROOT / 'evaluations' / 'adversarial_cases.json').read_text(encoding='utf-8'))
        cls.models = registry()

    def test_cases_are_unique_and_broad(self):
        cases = self.document['cases']
        names = [x['name'] for x in cases]
        self.assertEqual(len(names), len(set(names)))
        self.assertGreaterEqual(len(cases), 20)
        self.assertGreaterEqual(len(set(c['case']['decision']['kind'] for c in cases)), 9)

    def test_adversarial_expectations(self):
        for item in self.document['cases']:
            with self.subTest(item=item['name']):
                result = route(item['case'])
                expected = item['expected']
                self.assertEqual(result['primary_model'], expected['primary_model'])
                if 'depth' in expected:
                    self.assertEqual(result['depth'], expected['depth'])
                rejects = {x['model'] for x in result['rejected_models']}
                for model in expected.get('rejected_models_contain', []):
                    self.assertIn(model, rejects)
                for model in expected.get('supporting_models_contain', []):
                    self.assertIn(model, result['supporting_models'])
                if 'guardrail_contains' in expected:
                    self.assertTrue(any(expected['guardrail_contains'] in x for x in result['guardrails']))
                self.assertFalse(result['decision_made'])
                self.assertIn(result['primary_model'], self.models)
                self.assertTrue(result['stop_condition'])

    def test_unknown_signal_rejected(self):
        sample = json.loads((ROOT / 'examples' / 'sample_case.json').read_text())
        sample['signals']['someone_is_evil'] = True
        with self.assertRaisesRegex(ValueError, 'Unknown signals'):
            validate(sample)

    def test_ambiguous_bools_rejected(self):
        sample = json.loads((ROOT / 'examples' / 'sample_case.json').read_text())
        sample['signals']['opponent_adaptive'] = 'perhaps'
        with self.assertRaisesRegex(ValueError, 'boolean'):
            validate(sample)

    def test_missing_decision_fields_rejected(self):
        sample = json.loads((ROOT / 'examples' / 'sample_case.json').read_text())
        del sample['decision']['uncertainty']
        with self.assertRaisesRegex(ValueError, 'uncertainty'):
            validate(sample)

    def test_unknown_decision_field_rejected(self):
        sample = json.loads((ROOT / 'examples' / 'sample_case.json').read_text())
        sample['decision']['invented_risk'] = 99
        with self.assertRaisesRegex(ValueError, 'Unknown decision fields'):
            validate(sample)

    def test_schema_disallows_unexpected_top_level_data(self):
        sample = json.loads((ROOT / 'examples' / 'sample_case.json').read_text())
        sample['private_user_profile'] = {'address': 'example'}
        with self.assertRaisesRegex(ValueError, 'Unknown top-level fields'):
            validate(sample)

    def test_registry_and_rule_ids(self):
        registry_ids = list(self.models)
        self.assertEqual(len(registry_ids), len(set(registry_ids)))
        for model in self.models.values():
            self.assertIn(model['theory_type'], ['normative','descriptive','mechanistic','exploratory'])
            self.assertEqual(model['status'], 'candidate')
            self.assertTrue(all(re.fullmatch('C[0-9]{4}', x) for x in model['concept_refs']))
            self.assertGreater(len(model['method']), 10)
        rules = json.loads((ROOT / 'data' / 'rules.json').read_text())['rules']
        self.assertEqual(len({r['rule_id'] for r in rules}), len(rules))
        for rule in rules:
            self.assertTrue(rule['do_not_use_when'])
            self.assertEqual(rule['status'], 'candidate')

    def test_json_schema_definitions_exist(self):
        schema = json.loads((ROOT / 'schemas' / 'stage1.schema.json').read_text())
        self.assertTrue({'problem','model','rule','evaluation'}.issubset(schema['$defs']))
        self.assertEqual(schema['$defs']['problem']['properties']['schema_version']['const'], '1.0')
        self.assertEqual(set(schema['$defs']['problem']['properties']['signals']['properties']),
                         set(__import__('engine.router', fromlist=['SIGNALS']).SIGNALS))


if __name__ == '__main__':
    unittest.main()
