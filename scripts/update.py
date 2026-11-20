"""Validate content and update publication metadata; optionally merge curated inbox entries."""
import json, pathlib, datetime, zoneinfo
root=pathlib.Path(__file__).resolve().parents[1]
path=root/'content/topics.json'
data=json.loads(path.read_text(encoding='utf-8'))
ids=set()
for item in data:
    assert all(item.get(k) for k in ('id','category','title','level','summary','sections')),item
    assert item['id'] not in ids, f"duplicate id: {item['id']}"
    ids.add(item['id'])
    assert all(s.get('heading') and s.get('body') for s in item['sections'])
inbox=root/'content/inbox.json'
if inbox.exists():
    incoming=json.loads(inbox.read_text(encoding='utf-8'))
    for item in incoming:
        assert all(item.get(k) for k in ('id','category','title','level','summary','sections'))
        if item['id'] in ids:
            idx=next(i for i,x in enumerate(data) if x['id']==item['id'])
            data[idx]=item
        else:
            data.append(item);ids.add(item['id'])
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    inbox.unlink()
now=datetime.datetime.now(zoneinfo.ZoneInfo('Asia/Singapore'))
(root/'content/status.json').write_text(json.dumps({'updated_sgt':now.strftime('%Y-%m-%d %H:%M'),'topic_count':len(data)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Validated {len(data)} topics; timestamp {now.isoformat()}')
