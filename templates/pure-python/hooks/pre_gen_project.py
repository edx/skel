import json
import sys

LICENSES = ['apache', 'agpl']

context = json.load(sys.argv[1])

selected_license = context.get('license')

for license in LICENSES:
    if license == selected_license.lower():
        shutil.

    shutil.rmtree(license)

