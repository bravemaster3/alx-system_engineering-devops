# Increasing the limit

exec { 'set_ulimit':
  command     => 'echo ULIMIT="-n 10000" > /etc/default/nginx',
  path        => '/bin:/usr/bin',
  onlyif      => 'test -f /etc/default/nginx',
  refreshonly => true,
  notify      => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
