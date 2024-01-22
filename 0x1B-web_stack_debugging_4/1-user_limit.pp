#Change the OS configuration so that it is possible to login with the holberton user
exec { 'Hard limit':
  command => "sed -i 's|holberton hard nofile 5|holberton hard nofile 5000|' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
exec { 'Soft limit':
  command => "sed -i 's|holberton soft nofile 4|holberton soft nofile 4000|' /etc/security/limits.conf",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
