# -*- coding: utf-8 -*-
# @Time : 2022/3/15 3:00 下午
# @Author : heisenberg
# @File : merge_all.py
# @Project : sufe-cs-conf-ddl
# @Targert : concatenate all conf yaml format files.

import os
import yaml

HOME_DIR = os.path.dirname(os.path.realpath('__file__'))
all_conf_path = os.path.join(HOME_DIR,'conference')
all_conf_type = ['PDC','CGM','TC','AI','SE','DBIR','NIS']

i=0
for conf_type in all_conf_type:
    pdc_path = os.path.join(all_conf_path, conf_type)
    pdc_conf_list = [f for f in os.listdir(pdc_path) if not f.startswith('.')]
    for conf in pdc_conf_list:
        f = open(os.path.join(pdc_path,conf),'r', encoding='utf-8')
        print('now we processing %s conf in %s'%(conf,conf_type))
        c = f.read()
        x = yaml.full_load(c)
        i+=1
        with open('conference/allconf.yml','a',encoding='utf-8') as f:
            f.write(yaml.dump(x,allow_unicode=True, default_flow_style=False,sort_keys=False))
print('Sum %s confs in SUFE CS tenure conf'%i)
# Sum 108 confs in SUFE CS tenure conf


