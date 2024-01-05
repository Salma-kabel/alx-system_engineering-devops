#creating a custom HTTP header response, but with Puppet.
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
    line    =>  "\n\tadd_header X-Served-By $::hostname;\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n",
}

service {'nginx':
    ensure  => running,
    enable  => true,
}
