#Using Puppet, install flask from pip3.

package { 'werkzeug':
  ensure   => installed,
  provider => 'pip',
}

package { 'Flask':
ensure   => '2.1.0',
provider => 'pip3'
}
