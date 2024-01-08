# Puppet manifest for installing and configuring nginx

exec {'update_kernel':
    command => '/usr/bin/apt-get update'
}

package {'nginx':
    ensure => installed
}

exec {'mkdir_root_html':
    command => '/usr/bin/mkdir -p /var/www/html/'
}

file {'/var/www/html/index.html':
    content => 'Hello World!'
}

exec {'substitute':
    command => sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default,
    provider => shell
}

exec {'restart_nginx_service':
    command => '/usr/sbin/service nginx restart'
}
