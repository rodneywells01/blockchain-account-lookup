# https://betterprogramming.pub/how-to-use-docker-in-an-amazon-ec2-instance-5453601ec330
sudo yum update -y
sudo amazon-linux-extras install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker
