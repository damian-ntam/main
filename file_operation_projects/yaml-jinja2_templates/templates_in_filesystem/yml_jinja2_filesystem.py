#!/usr/bin/python
__author__  = "Melih TEKE"
__EMAIL__   = "melihteke@gmail.com"

import yaml
from jinja2 import FileSystemLoader, Environment

with open("network_dc.yml", "r") as yaml_file:
  yaml_data = yaml.load(yaml_file)

template_dir = "C:\\Users\melih\PycharmProjects\main\\file_operation_projects\yaml-jinja2_templates\\templates_in_filesystem"

template_env = Environment(loader=FileSystemLoader(template_dir),trim_blocks=True, lstrip_blocks=True)

for device,config in yaml_data['dc1'].items():
  if config['device_template'] == "vIOSL2_Template":
    device_template = template_env.get_template("switch_template.j2")
  elif config['device_template'] == "vIOSL3_Template":
    device_template = template_env.get_template("router_template.j2")

  print("rendering now device {0}" .format(device))
  device_config = device_template.render(config)
  print(device_config)
  print("=" * 30)
  with open("generated_config.txt", "a") as file:
    file.write("\n")
    file.write(device_config)
    file.write("\n")
    file.write("==" * 30)



