import subprocess
import sys
from pathlib import Path

files = [Path('docs/assets/index.png'), Path('docs/assets/status.png')]

PNG_SIG = b"\x89PNG\r\n\x1a\n"

print('CWD:', Path('.').resolve())
for p in files:
    print('\nChecking', p)
    if not p.exists():
        print(' MISSING')
        continue
    size = p.stat().st_size
    print(' size:', size)
    with open(p, 'rb') as fh:
        sig = fh.read(8)
    if sig == PNG_SIG:
        print(' PNG signature OK')
    else:
        print(' Invalid PNG signature; attempting to re-encode with Pillow')
        try:
            from PIL import Image
        except Exception:
            print(' Pillow not found, installing...')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow'])
            from PIL import Image
        img = Image.open(p)
        img.save(p, format='PNG')
        print(' Re-saved as PNG')

print('\nValidation complete')
