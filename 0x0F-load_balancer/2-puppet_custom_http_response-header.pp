#Adding a custom header

exec { 'update':
  provider => shell,
  command => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec { 'install nginx':
  provider => shell,
  command => 'sudo apt-get install -y nginx',
  before   => Exec['add_header'],
}

exec { 'add-header':
  provider => shell,
  environment => ['HOST=${hostname}'],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before   => Exec['restart Nginx'],
}

exec {'restart nginx':
  provider => shell,
  command => 'sudo service restart nginx',
}

