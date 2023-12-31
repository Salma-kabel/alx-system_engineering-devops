#install and configure an Nginx server using Puppet instead of Bash
package {
    'nginx':
    ensure => installed,
}

file {'/var/www/html/index.nginx-debian.html':
    ensure  => file,
    content => 'Hello World!',
}

file_line {'configure redirection':
    path    =>  '/etc/nginx/sites-available/default',
    after   =>  'server_name _;',
    line    =>  "\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n",
}

service {'nginx':
    ensure  => running,
    enable  => true,
}
