"""Local deterministic aid; never a factual or model behavior certificate."""
def analyze(p):
 criteria=p['criteria']
 if not criteria or len(set(criteria))!=len(criteria):raise ValueError('nonempty unique criteria required')
 independent=[];transfer=[];seen=set()
 for a in p['attempts']:
  if a['id'] in seen:raise ValueError('duplicate attempt')
  seen.add(a['id'])
  if type(a.get('assisted'))!=bool or type(a.get('new_conditions'))!=bool:raise ValueError('explicit assistance and condition flags required')
  if not set(a['met']).issubset(criteria):raise ValueError('unrecognized criterion')
  if not a['assisted'] and set(a['met'])==set(criteria):
   independent.append(a['id'])
   if a['new_conditions']:transfer.append(a['id'])
 return {'independent_complete_attempts':independent,'changed_condition_evidence':transfer,'note':'User-reported evidence for listed tasks only, not a general certificate; duration is not competence.'}

if __name__=='__main__':
 import json,sys
 print(json.dumps(analyze(json.loads(open(sys.argv[1],encoding='utf-8').read())),ensure_ascii=False,indent=2))
