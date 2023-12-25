#Using Puppet, install flask from pip3.

package { 'pip':
  ensure => installed,
}

package { 'werkzeug':
  ensure   => installed,
  provider => 'pip',
require  => Package['pip'],
}

package { 'Flask':
ensure   => '2.1.0',
provider => 'pip3',
require  => Package['werkzeug'],
}
