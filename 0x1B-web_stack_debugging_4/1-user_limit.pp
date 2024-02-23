# This puppet file adds a new configuration for holberton user
# By changing the number of open file limits, for warning and errors..

file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton soft nofile 4096\nholberton hard nofile 8192\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Ensure changes take effect immediately
exec { 'reload_pam':
  command     => 'sysctl -p',
  path        => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
  subscribe   => File['/etc/security/limits.d/holberton.conf'],
  refreshonly => true,
}
