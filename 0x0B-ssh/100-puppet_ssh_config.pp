# Using Puppet, configures SSH config file so that you can connect to a...
# ...server without typing a password.
# SSH client configuration configured to use the private key ~/.ssh/school
# SSH client configuration configured to refuse to authenticate using a passwd

include stdlib
file_line { 'school private key':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'remove pwd authentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
}