#fixing failed requests

exec { 'fix failed requests':
  command => "sed -i 's/worker_processes 4/worker_processes 4000/' /etc/nginx/nginx.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}

exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
