from fabric import Connection
import time
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

# As running docker command need a long prefix, then is the real command, so, set a prefix variable to short the full command
command_prefix = "docker exec nelsonCentOS7.5 "

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
# Download the silent install properties file to /home/test/Downloads path
information("Downloading silent install properties file...")
result = c.run(command_prefix + "wget -P /home/test/Downloads https://azrepos.labs.quest.com/rmbundles/bf73d9fd-8191-4e73-8d54-dc036a94e5ba/docs/fms_silent_install.properties")
print('Done')
# Download the Foglight.license to /home/test/Downloads path
information("Downloading Foglight.license file...")
result = c.run(command_prefix + "wget -P /home/test/Downloads ftp://foglight:foglight@10.30.168.93/nightly/FoglightServerDist/license/Foglight.license")
print('Done')


# MAIN_TASK--> Modify required files
# Modify the silent install properties file content to set install DIR, license file path, External DB settings
information("Modifying silent install properties file...")
result = c.run(command_prefix + "sed -i 's/.*USER_INSTALL_DIR=.*/USER_INSTALL_DIR=\\/home\\/test\\/TestInstallFMS\\/Foglight/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/.*FMS_LICENSE_FILE=.*/FMS_LICENSE_FILE=\\/home\\/test\\/Downloads\\/Foglight.license/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/FMS_DB_USER=foglight/FMS_DB_USER=autoinstalltest/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/FMS_DB=embedded/FMS_DB=external/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/#FMS_DB_TYPE=postgresql/FMS_DB_TYPE=postgresql/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/FMS_DB_HOST=127.0.0.1/FMS_DB_HOST=10.30.168.85/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/FMS_DB_PORT=15432/FMS_DB_PORT=5432/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/#FMS_DB_NAME=foglight/FMS_DB_NAME=test/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/#FMS_DB_ADMIN_USER=/FMS_DB_ADMIN_USER=postgres/g' /home/test/Downloads/fms_silent_install.properties")
result = c.run(command_prefix + "sed -i 's/#FMS_DB_ADMIN_PASSWORD=/FMS_DB_ADMIN_PASSWORD=Rdis2fun/g' /home/test/Downloads/fms_silent_install.properties")
print("Done\n")

# MAIN_TASK--> Silent install FMS in silent mode with specufying the silent install properties file
information("Installing FMS in silent mode with the modified properties file...")
result = c.run(command_prefix + "sudo -u test /home/test/Downloads/Foglight-5_9_5-install_linux-x86_64.bin -i silent -f /home/test/Downloads/fms_silent_install.properties")

# MAIN_TASK--> Check all install log files, if abnormal message exists, print to notify user to check
# Check Foglight_x.x.x_InstallLog.log if there's none-zero Warnings/NonFatalErrors/FatalErrors, if yes, notify "FAIL --> There's Warnings/NonFatalErrors/FatalErrors in Foglight_x.x.x_InstallLog.log, please check"
# If there's no none zero Warnings/NonFatalErrors/FatalErrors, the shell command will return 1
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
