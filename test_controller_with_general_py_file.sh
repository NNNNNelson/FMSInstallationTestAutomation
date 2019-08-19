removeAllContainers()
{
  ssh root@10.30.168.151 'docker rm -f $(docker ps -aq)'
}

# ssh root@10.30.168.151 'docker run -dit --name=nelsonOracleLinux5.11 -p 8080:8080 nelson-oraclelinux-5.11 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Console+EmbeddedDB_InstallationTest.py 'nelsonOracleLinux5.11' | tee /root/NelsonTestScripts/OracleLinux5.11_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonOracleLinux5.11 -p 8080:8080 nelson-oraclelinux-5.11 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Silent+EmbeddedDB_InstallationTest.py 'nelsonOracleLinux5.11' | tee /root/NelsonTestScripts/OracleLinux5.11_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
ssh root@10.30.168.151 'docker run -dit --name=nelsonOracleLinux6.10 -p 8080:8080 nelson-oraclelinux-6.10 /bin/bash' &&
python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Console+EmbeddedDB_InstallationTest.py 'nelsonOracleLinux6.10' | tee /root/NelsonTestScripts/OracleLinux6.10_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

removeAllContainers &&
ssh root@10.30.168.151 'docker run -dit --name=nelsonOracleLinux6.10 -p 8080:8080 nelson-oraclelinux-6.10 /bin/bash' &&
python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Silent+EmbeddedDB_InstallationTest.py 'nelsonOracleLinux6.10' | tee /root/NelsonTestScripts/OracleLinux6.10_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

removeAllContainers &&
ssh root@10.30.168.151 'docker run -dit --name=nelsonRHEL6.9 -p 8080:8080 nelson-rhel-6.9 /bin/bash' &&
python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Console+EmbeddedDB_InstallationTest.py 'nelsonRHEL6.9' | tee /root/NelsonTestScripts/RHEL6.9_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

removeAllContainers &&
ssh root@10.30.168.151 'docker run -dit --name=nelsonRHEL6.9 -p 8080:8080 nelson-rhel-6.9 /bin/bash' &&
python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Silent+EmbeddedDB_InstallationTest.py 'nelsonRHEL6.9' | tee /root/NelsonTestScripts/RHEL6.9_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu12.04 -p 8080:8080 nelson-ubuntu-12.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Console+EmbeddedDB_InstallationTest.py 'nelsonUbuntu12.04' | tee /root/NelsonTestScripts/Ubuntu12.04_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu12.04 -p 8080:8080 nelson-ubuntu-12.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Silent+EmbeddedDB_InstallationTest.py 'nelsonUbuntu12.04' | tee /root/NelsonTestScripts/Ubuntu12.04_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu14.04 -p 8080:8080 nelson-ubuntu-14.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Console+EmbeddedDB_InstallationTest.py 'nelsonUbuntu14.04' | tee /root/NelsonTestScripts/Ubuntu14.04_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu14.04 -p 8080:8080 nelson-ubuntu-14.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Silent+EmbeddedDB_InstallationTest.py 'nelsonUbuntu14.04' | tee /root/NelsonTestScripts/Ubuntu14.04_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS5.11 -p 8080:8080 nelson-centos-5.11 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Console+EmbeddedDB_InstallationTest.py 'nelsonCentOS5.11' | tee /root/NelsonTestScripts/CentOS5.11_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS5.11 -p 8080:8080 nelson-centos-5.11 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/General_Python+Docker+Silent+EmbeddedDB_InstallationTest.py 'nelsonCentOS5.11' | tee /root/NelsonTestScripts/CentOS5.11_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1