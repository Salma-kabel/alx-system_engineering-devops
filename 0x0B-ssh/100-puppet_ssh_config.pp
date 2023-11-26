#using Puppet to make changes to our configuration file

file_line {'identity file':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school'}

file_line {'turn off password authentication':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no'}
