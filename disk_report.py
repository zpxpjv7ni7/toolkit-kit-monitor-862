import os

for root, dirs, files in os.walk('.'):
    total = sum(os.path.getsize(os.path.join(root, f)) for f in files)
    if total > 0:
        print(f'{root}: {total / 1024:.1f} KB, {len(files)} files')
