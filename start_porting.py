import sys
import os
import json
from sieve_common.config import *

port_folder = sys.argv[1]
build_folder = os.path.join(port_folder, "build")
deploy_folder = os.path.join(port_folder, "deploy")
test_folder = os.path.join(port_folder, "test")
oracle_folder = os.path.join(port_folder, "oracle")

os.makedirs(port_folder, exist_ok=True)
os.makedirs(build_folder, exist_ok=True)
os.makedirs(deploy_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)
os.makedirs(oracle_folder, exist_ok=True)

build_script = os.path.join(build_folder, "build.sh")
deploy_script = os.path.join(deploy_folder, "deploy.sh")
f = open(build_script, "w")
f.write("#!/bin/bash\n")
f.close()
f = open(deploy_script, "w")
f.write("#!/bin/bash\n")
f.close()
os.system("chmod +x " + build_script)
os.system("chmod +x " + deploy_script)

config_json = os.path.join(port_folder, "config.json")
controller_config_map = {
    "name": "",
    "github_link": "",
    "commit": "",
    "kubernetes_version": "",
    "client_go_version": "",
    "dockerfile_path": "",
    "controller_image_name": "",
    "annotated_reconcile_functions": {},
    "test_command": "",
    "custom_resource_definitions": [],
    "controller_pod_label": "",
    "controller_deployment_file_path": "",
}
json.dump(controller_config_map, open(config_json, "w"), indent=4)
