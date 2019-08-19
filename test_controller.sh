removeAllContainers()
{
  ssh root@10.30.168.151 'docker rm -f $(docker ps -aq)'
}

# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS7.5 -p 8080:8080 nelson-centos-7.5.1804 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/CentOS7_Python+Docker+Console+EmbeddedDB_InstallationTest.py  | tee /root/NelsonTestScripts/CentOS7_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS7.5 -p 8080:8080 nelson-centos-7.5.1804 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonOralce7.5 -p 8080:8080 nelson-oraclelinux-7.5 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/Oracle7_Python+Docker+Console+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/Oracle7_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonOracle7.5 -p 8080:8080 nelson-oraclelinux-7.5 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/Oracle7_Python+Docker+Silent+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/Oracle7_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonRHEL7.4 -p 8080:8080 nelson-rhel-7.4 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/RHEL74_Python+Docker+Console+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/RHEL74_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonRHEL7.4 -p 8080:8080 nelson-rhel-7.4 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/RHEL74_Python+Docker+Silent+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/RHEL74_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonSLES12 -p 8080:8080 nelson-sles-12 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/SLES12_Python+Docker+Console+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/SLES12_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonSLES12 -p 8080:8080 nelson-sles-12 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/SLES12_Python+Docker+Silent+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/SLES12_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu16.04 -p 8080:8080 nelson-ubuntu-16.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/Ubuntu1604_Python+Docker+Console+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/Ubuntu1604_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu16.04 -p 8080:8080 nelson-ubuntu-16.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/Ubuntu1604_Python+Docker+Silent+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/Ubuntu1604_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu18.04 -p 8080:8080 nelson-ubuntu-18.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/Ubuntu1804_Python+Docker+Console+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/Ubuntu1804_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonUbuntu18.04 -p 8080:8080 nelson-ubuntu-18.04 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/Ubuntu1804_Python+Docker+Silent+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/Ubuntu1804_Python+Docker+Silent+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS7.5 -p 8080:8080 nelson-centos-7.5.1804 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalMySQL_InstallationTest.py | tee /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalMySQL_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS7.5 -p 8080:8080 nelson-centos-7.5.1804 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalOracle_InstallationTest.py | tee /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalOracle_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS7.5 -p 8080:8080 nelson-centos-7.5.1804 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalPostgreSQL_InstallationTest.py | tee /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalPostgreSQL_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS7.5 -p 8080:8080 nelson-centos-7.5.1804 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalSQLServer_InstallationTest.py | tee /root/NelsonTestScripts/CentOS7_Python+Docker+Silent+ExternalSQLServer_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonCentOS6.10 -p 8080:8080 nelson-centos-6.10 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/CentOS6.10_Python+Docker+Console+EmbeddedDB_InstallationTest.py  | tee /root/NelsonTestScripts/CentOS6.10_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
# ssh root@10.30.168.151 'docker run -dit --name=nelsonSLES11sp4 -p 8080:8080 nelson-sles-11sp4 /bin/bash' &&
# python3.7 -u /root/NelsonTestScripts/SLES11sp4_Python+Docker+Console+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/SLES11sp4_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1 &&

# removeAllContainers &&
ssh root@10.30.168.151 'docker run -dit --name=nelsonRHEL5.11 -p 8080:8080 nelson-rhel-5.11 /bin/bash' &&
python3.7 -u /root/NelsonTestScripts/RHEL5.11_Python+Docker+Console+EmbeddedDB_InstallationTest.py | tee /root/NelsonTestScripts/RHEL5.11_Python+Docker+Console+EmbeddedDB_InstallationTest_ACE5Preview4_output.txt 2>&1
