import os
import sys

pro_abs_path = os.path.abspath('.')
confs = {'800x480x32_RTP', '800x480x32_CTP', '800x480x16_RTP', '800x480x16_CTP', '480x272x32_CTP', '480x272x16_CTP'}

for conf in confs:
    os.system('cd \"'+ pro_abs_path + '\" && scons -c')
    os.system('cd \"'+ pro_abs_path + '\" && cp config_' + conf + ' .config')
    os.system('cd \"'+ pro_abs_path + '\" && menuconfig --generate --silent')
    os.system('cd \"'+ pro_abs_path + '\" && scons -j 48')
    os.system('cd \"'+ pro_abs_path + '\" && cp rtthread.bin rtthread_' + conf + '.bin')