#fixing failed requests

exec { 'fix failed requests':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
