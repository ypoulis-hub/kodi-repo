"""Rebuild docs/addons.xml + docs/addons.xml.md5 from the ZIPs in docs/zips/.

Drop a new addon ZIP into docs/zips/<addon_id>/<addon_id>-<version>.zip,
then run:

    python scripts/build_index.py

Commit the resulting docs/addons.xml + docs/addons.xml.md5 and push.
"""

import hashlib
import os
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZIPS = ROOT / 'docs' / 'zips'
INDEX = ROOT / 'docs' / 'addons.xml'
MD5_FILE = ROOT / 'docs' / 'addons.xml.md5'


def latest_zip(addon_dir: Path) -> Path | None:
    candidates = sorted(addon_dir.glob('*.zip'))
    return candidates[-1] if candidates else None


def addon_xml_from_zip(zpath: Path) -> str:
    with zipfile.ZipFile(zpath) as z:
        for name in z.namelist():
            if name.endswith('/addon.xml') and name.count('/') == 1:
                return z.read(name).decode('utf-8').strip()
    raise RuntimeError(f'no addon.xml at <id>/addon.xml in {zpath}')


def extract_icon(zpath: Path, dest_dir: Path) -> None:
    with zipfile.ZipFile(zpath) as z:
        for name in z.namelist():
            if name.endswith('/icon.png') and name.count('/') == 1:
                with z.open(name) as src, (dest_dir / 'icon.png').open('wb') as dst:
                    dst.write(src.read())
                return


def main() -> None:
    addons: list[str] = []
    for addon_dir in sorted(p for p in ZIPS.iterdir() if p.is_dir()):
        zpath = latest_zip(addon_dir)
        if not zpath:
            print(f'! no zip in {addon_dir.name}')
            continue
        addons.append(addon_xml_from_zip(zpath))
        extract_icon(zpath, addon_dir)
        print(f'  {addon_dir.name}: {zpath.name}')

    body = '\n'.join(re.sub(r'<\?xml[^?]+\?>\s*', '', a) for a in addons)
    xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        '<addons>\n'
        f'{body}\n'
        '</addons>\n'
    )
    INDEX.write_text(xml, encoding='utf-8', newline='\n')
    md5 = hashlib.md5(xml.encode('utf-8')).hexdigest()
    MD5_FILE.write_text(md5 + '\n', encoding='utf-8', newline='\n')
    print(f'\naddons.xml: {len(xml)} bytes, {len(addons)} addons')
    print(f'md5: {md5}')


if __name__ == '__main__':
    main()
