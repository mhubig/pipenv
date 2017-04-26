import os
import sys

# Inject vendored directory into system path.

tests_path = os.sep.join(os.path.dirname(os.path.realpath(__file__)).split(os.sep)[:-1])
v_path = os.path.sep.join([tests_path, 'pipenv', 'vendor'])

sys.path.append(v_path)
