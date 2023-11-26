#using Puppet to make changes to our configuration file

file_line {'Declare identity file':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school'}

file_line {'Turn off password authentication':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no'}
