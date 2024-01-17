# fix apache server error

file { '/var/www/html/wp-settings.php':
  ensure => present,
}->
file_line { 'Replace a line in /var/www/html/wp-settings.php':
  path => '/var/www/html/wp-settings.php',  
  line => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match   => "require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );",
}
