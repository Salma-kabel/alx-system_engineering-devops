file { '/etc/ssh/ssh_config':
  content => 'PasswordAuthentication no
  IdentityFile ~/.ssh/school',
}
