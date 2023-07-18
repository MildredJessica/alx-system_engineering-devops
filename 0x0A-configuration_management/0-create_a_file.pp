# Using Puppet, create a file in /tmp
# File path is /tmp/school, permission is 0744
# File owner is www-data
# File group is www-data and File contains I love Puppet


file { 'school file':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}
