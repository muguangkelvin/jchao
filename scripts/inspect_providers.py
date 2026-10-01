import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/providers.json', 'r', encoding='utf-8') as f:
    providers = json.load(f)

for p in providers:
    print(f"#{p['rank']} {p['name']} ({p['slug']}): price={p.get('price')}, nodes={p.get('nodes')}")
