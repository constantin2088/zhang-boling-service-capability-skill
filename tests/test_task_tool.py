import json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check_practice import analyze
class TaskToolTests(unittest.TestCase):
 def sample(self):return json.loads((ROOT/'examples/tool-input.json').read_text(encoding='utf-8'))
 def test_assisted_is_not_independent(self):self.assertEqual(analyze(self.sample())['independent_complete_attempts'],['b'])
 def test_repetition_not_transfer(self):
  p=self.sample();p['attempts'][1]['new_conditions']=False;self.assertEqual(analyze(p)['changed_condition_evidence'],[])
 def test_duration_does_not_certify(self):
  p=self.sample();p['attempts'][1]['met']=[];p['attempts'][1]['hours']=100;self.assertEqual(analyze(p)['independent_complete_attempts'],[])
 def test_missing_assistance_stops(self):
  p=self.sample();del p['attempts'][1]['assisted']
  with self.assertRaises(ValueError):analyze(p)
 def test_unknown_criterion_stops(self):
  p=self.sample();p['attempts'][1]['met'].append('invented')
  with self.assertRaises(ValueError):analyze(p)

if __name__=='__main__':unittest.main()
