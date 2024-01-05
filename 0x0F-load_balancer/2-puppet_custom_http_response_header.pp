#creating a custom HTTP header response, but with Puppet.
package {
    'nginx':
    ensure => installed,
}

file {'/var/www/html/index.nginx-debian.html':
    ensure  => file,
    content => 'Hello World!',
}
exec { 'command':
  command  => 'sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;service nginx restart',
  provider => shell,
}
service {'nginx':
    ensure  => running,
    enable  => true,
}
