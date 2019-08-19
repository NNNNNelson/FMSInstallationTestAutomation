import time
from fabric import Connection
from invoke import Responder
from colorama import Fore, Back, Style


def print_equal_mark(test_done_message):
    for i in test_done_message:
        print('=', end='')
    print('')


def information(message):
    print_equal_mark(message)
    print(Fore.BLACK + Back.WHITE + message + Style.RESET_ALL)
    print_equal_mark(message)


information("Connecting to Docker host machine...")

# Set connection parameters
host = "10.30.168.151"
user = "root"
password = "Templ@te"
port = 22

# Connect to the host
c = Connection(host, user=user, port=port, connect_kwargs={"password": password})
print("Done\n")

# Give the docker instance name
docker_instance_name = 'nelsonRHEL7.4'

# Set console mode all responses to the console prompts
enter_roll_agreement = Responder(
    pattern=r'PRESS <ENTER> TO CONTINUE',
    response='\n',
)
accept_agreement = Responder(
    pattern=r'DO YOU ACCEPT THE TERMS OF THIS LICENSE AGREEMENT',
    response='Y\n',
)
set_install_dir = Responder(
    pattern=r'Select your installation folder',
    response='/home/test/TestInstallFMS/Foglight\n',
)
accept_the_default = Responder(
    pattern=r'ENTER THE NUMBER OF AN OPTION ABOVE, OR PRESS <ENTER> TO ACCEPT THE DEFAULT',
    response='\n',
)
accept_default_password = Responder(
    pattern=r'For default password of \"foglight\" press ENTER',
    response='\n',
)
no_secure_server = Responder(
    pattern=r'Configure as Secure Server',
    response='N\n',
)
foglight_mode = Responder(
    pattern=r'Please specify a Foglight mode',
    response='\n',
)
accept_default_db_account = Responder(
    pattern=r'Enter the user ID and password for the Foglight database account',
    response='\n',
)
choose_embedded_db = Responder(
    pattern=r'Select the Foglight database configuration',
    response='\n',
)
accept_default_db_port = Responder(
    pattern=r'Please enter the database port number',
    response='\n',
)
accept_default_cluster_multicast_port = Responder(
    pattern=r'Please enter Cluster Multi-cast Port',
    response='\n',
)
accept_default_http_port = Responder(
    pattern=r'Please enter HTTP Port',
    response='\n',
)
accept_default_https_port = Responder(
    pattern=r'Please enter HTTPS Port',
    response='\n',
)
accept_default_federation_port = Responder(
    pattern=r'Please enter Federation Port',
    response='\n',
)
accept_default_qp5_server_port = Responder(
    pattern=r'Please enter QP5 Server Port',
    response='\n',
)
set_license_path = Responder(
    pattern=r'Please enter the path to a Foglight license file',
    response='/home/test/Downloads/Foglight.license\n',
)
do_not_start_fms_server = Responder(
    pattern=r'ENTER THE NUMBER FOR YOUR CHOICE, OR PRESS <ENTER> TO ACCEPT THE DEFAULT',
    response='2\n',
)
press_enter_to_exit_installer = Responder(
    pattern=r'PRESS <ENTER> TO EXIT THE INSTALLER',
    response='\n',
)

# As running docker command need a long prefix, then is the real command, so, set a prefix variable to short the full command
command_prefix = "docker exec " + docker_instance_name + " "

# MAIN_TASK--> Download required files
# Empty the /home/test/Downloads path
information("Emptying the /home/test/Downloads/ path...")
result = c.run(command_prefix + "rm -rf /home/test/Downloads/*", warn=True)
print("Done")
# Download the installer to /home/test/Downloads path and give it execute permission
information("Downloading FMS installer...")
result = c.run(command_prefix + "wget -P /home/test/Downloads ftp://foglight:foglight@10.30.168.93/nightly/FoglightServerDist/branches/ACE.5_preview/5.9.5-201901131709-163412de-4/linux-x86_64/Foglight-5_9_5-install_linux-x86_64.bin")
information("Give execute permission to the installer...")
result = c.run(command_prefix + "chmod +x /home/test/Downloads/Foglight-5_9_5-install_linux-x86_64.bin")
print("Done\n")
# Download the Foglight.license to /home/test/Downloads path
information("Downloading Foglight.license file...")
result = c.run(command_prefix + "wget -P /home/test/Downloads ftp://foglight:foglight@10.30.168.93/nightly/FoglightServerDist/license/Foglight.license")
print('Done')

# MAIN_TASK--> Console mode install FMS with the given responses to the console prompts
information("Installing FMS in console mode with prepared responses to the console prompts...")
result = c.run('docker exec -i ' + docker_instance_name + ' sudo -u test /home/test/Downloads/Foglight-5_9_5-install_linux-x86_64.bin -i console', watchers=[enter_roll_agreement, accept_agreement, set_install_dir, accept_the_default, accept_default_password, no_secure_server, foglight_mode, accept_default_db_account, choose_embedded_db, accept_default_db_port, accept_default_cluster_multicast_port, accept_default_http_port, accept_default_https_port, accept_default_federation_port, accept_default_qp5_server_port, set_license_path, do_not_start_fms_server, press_enter_to_exit_installer])

# MAIN_TASK--> Check all install log files, if abnormal message exists, print to notify user to check
# Check Foglight_x.x.x_InstallLog.log if there's none-zero Warnings/NonFatalErrors/FatalErrors, if yes, notify "FAIL --> There's Warnings/NonFatalErrors/FatalErrors in Foglight_x.x.x_InstallLog.log, please check"
# If there's no none-zero Warnings/NonFatalErrors/FatalErrors, the shell command will return 1
information("Checking Foglight_x.x.x_InstallLog.log...")
result = c.run(command_prefix + "sh -c \'grep -P \"^[1-9]\\d*? (Warnings|NonFatalErrors|FatalErrors)\" /home/test/TestInstallFMS/Foglight/Foglight_*_InstallLog.log ; echo $?\'")
if result.stdout == '0\n':
    print(Fore.RED + "FAIL --> There's Warnings/NonFatalErrors/FatalErrors in Foglight_x.x.x_InstallLog.log, please check" + Style.RESET_ALL)
else:
    print(Fore.GREEN + "PASS --> No Warnings/NonFatalErrors/FatalErrors found in Foglight_x.x.x_InstallLog.log" + Style.RESET_ALL)
# Check Foglight_x.x.x_Install_yyyy-mm-dd_hhmmss_xxx.log if there's WARN/ERROR/FATAL message exists, if yes, notify "FAIL --> There's Warnings/NonFatalErrors/FatalErrors in Foglight_x.x.x_Install_yyyy-mm-dd_hhmmss_xxx.log, please check"
# If there finds "(WARN|ERROR|FATAL)   " in the log, the command will return 0, if there's no find, the shell command will return 1
information("Checking Foglight_x.x.x_Install_yyyy-mm-dd_hhmmss_xxx.log...")
result = c.run(command_prefix + "sh -c \'grep -P \"(WARN|ERROR|FATAL)   \" /home/test/TestInstallFMS/Foglight/Foglight_*_Install_2*.log ; echo $?\'")
if '0\n' in result.stdout:
    print(Fore.RED + "FAIL --> There's Warnings/NonFatalErrors/FatalErrors in Foglight_x.x.x_Install_yyyy-mm-dd_hhmmss_xxx.log, please check" + Style.RESET_ALL)
else:
    print(Fore.GREEN + "PASS --> No WARN/ERROR/FATAL message found in Foglight_x.x.x_Install_yyyy-mm-dd_hhmmss_xxx.log" + Style.RESET_ALL)

# MAIN_TASK--> Startup FMS, then check if there's abnormal meesage exists, if yes, notify user to check ManagementServer log
# Startup FMS by user 'test' (a none-root user) in Daemon mode (this will make the FMS run in background)
information("Starting the FMS...")
result = c.run(command_prefix + "sudo -u test /home/test/TestInstallFMS/Foglight/bin/fms -d")
print('\n')
# For every 5 seconds, check the ManagementServer log for "startup complete"
# If the string is not found, it means the starting is in process, rotate a line to indicate it's still running
# If the string is found, it means FMS has finished starting
# If total time exceeds 600 seconds (10 min), it's too long for FMS startup, indicates user
time_period_count = 0
rotating_slash = ['-', '\\', '|', '/']
rotate_num = 0
while 5 * time_period_count < 1800:
    result = c.run(command_prefix + "sh -c \"grep \'startup complete\' /home/test/TestInstallFMS/Foglight/logs/ManagementServer_2*.log\"", warn=True)
    rotate_count = 0
    if 'startup complete' not in result.stdout:
        while rotate_count < 10:
            rotate_order = rotate_num % 4
            print('\b' + rotating_slash[rotate_order], end='', flush=True)
            rotate_num += 1
            rotate_count += 1
            time.sleep(0.5)
    elif 'startup complete' in result.stdout:
        print('\n')
        print(Fore.BLACK + Back.WHITE + "FMS startup complete!" + Style.RESET_ALL)
        print('\n')
        break
    time_period_count += 1
    if 5 * time_period_count == 1800:
        print(Fore.YELLOW + "\nWARN --> The FMS did not complete startup in 30 minutes, please check Management Server log." + Style.RESET_ALL)
# Check ManagementServer log for WARN/ERROR/FATAL messages, if there exists, notify user to check ManagementServer log
information("Checking ManagementServer log...")
result = c.run(command_prefix + "sh -c \"grep -P \'(WARN|ERROR|FATAL).  \' /home/test/TestInstallFMS/Foglight/logs/ManagementServer_2*log\"", warn=True)
if result.stdout != '':
    print(Fore.RED + "FAIL --> There's WARN/ERROR/FATAL in ManagerServer log, please check Management Server log." + Style.RESET_ALL)
else:
    print(Fore.GREEN + "PASS --> No WARN/ERROR/FATAL message found in ManagementServer log" + Style.RESET_ALL)

# MAIN_TASK--> All test is done, print test finish message.
information('All tests are done, exit program.')

# Print a Bye text art
bye_text_art = '''░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▀▀▀▀▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▄▀░░░░░░░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░
░▄▀░░░▄▄░░░░▀▀▀▀▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄░░░░
░█░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄░░
░█░░░░██▄████▄░██▄░░░░▄██░▄████▄░░░░▀▄░
░█░░░░██▀░░▀██▄░██▄░░██▀░██▀░▄██░░░░░█░
░█░░░░██░░░░███░░█████▀░░██▄█▀▀░░░░░░█░
░█░░░░███▄▄███▀░░░▀██▀░░░▀██▄▄▄██░░░░█░
░▀▄░░░░▀▀▀▀▀▀░░░░░██▀░░░░░░▀▀▀▀▀░░░░░█░
░░▀▄░░░░░░░░░░░░░██▀░░░▄▄░░░░░░░░░▄▄▀░░
░░░░▀▀▀▀▀▀▀▀▀▄░░░▀▀░░░▄▀░▀▀▀▀▀▀▀▀▀░░░░░
░░░░░░░░░░░░░▀▄░░░░░░▄▀░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░'''
print(bye_text_art)

