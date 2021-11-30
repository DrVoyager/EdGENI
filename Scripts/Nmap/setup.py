import os

#Get name of machine
os.system("hostname > file.txt")
temp_file = open("file.txt", "r")
name = ""
for line in temp_file:
	name = line[:line.index(".")]
print(name)
temp_file.close()
os.system("sudo rm file.txt")

#Install needed config
if "attacker" in name:
	os.system("sudo apt-get -y update")
	os.system("sudo apt-get -y install nmap")
if "server1" in name:
	os.system("sudo wget https://raw.githubusercontent.com/DrVoyager/EdGENI/master/Scripts/Nmap/setupweb.sh")
    	os.system("sudo chmod 755 setupweb.sh") 
    	os.system("sudo ./setupweb.sh")
    	os.system("sudo rm setupweb.sh")
if "server2" in name:
	os.system("sudo wget https://raw.githubusercontent.com/DrVoyager/EdGENI/master/Scripts/Nmap/setupmail.sh")
    	os.system("sudo chmod 755 setupmail.sh")    
    	os.system("sudo ./setupmail.sh")
    	os.system("sudo rm setupmail.sh")
if "server3" in name:
	os.system("sudo apt-get -y update")
    	os.system("sudo apt-get -y install samba")
    

		
