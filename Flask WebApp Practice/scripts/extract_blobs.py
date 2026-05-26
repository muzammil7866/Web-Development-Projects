import json
from pathlib import Path

pairs = [
    (Path(r"C:/Users/muzam/AppData/Roaming/Code/User/workspaceStorage/d4fb82ae7afa89cd078895c24495697b/GitHub.copilot-chat/chat-session-resources/69940b98-11bc-4470-b932-abb35d4dfa81/call_fUdNO9kULZGHOKnuzCTUYqKd__vscode-1779773791582/content.txt"), Path('docs/assets/index.png')),
    (Path(r"C:/Users/muzam/AppData/Roaming/Code/User/workspaceStorage/d4fb82ae7afa89cd078895c24495697b/GitHub.copilot-chat/chat-session-resources/69940b98-11bc-4470-b932-abb35d4dfa81/call_F7ubThH8CZVmK2BUsswXf3iX__vscode-1779773791584/content.txt"), Path('docs/assets/status.png')),
]

for src, dst in pairs:
    print('Processing', src)
    if not src.exists():
        print(' SKIP missing', src)
        continue
    text = src.read_text(errors='replace')
    # find JSON part after 'Result: '
    idx = text.find('{')
    if idx == -1:
        print(' No JSON found in', src)
        continue
    j = json.loads(text[idx:])
    if j.get('type') == 'Buffer' and 'data' in j:
        data = bytes(j['data'])
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        print(' Wrote', dst, 'size', dst.stat().st_size)
    else:
        print(' Unexpected JSON format in', src)

print('Done')
