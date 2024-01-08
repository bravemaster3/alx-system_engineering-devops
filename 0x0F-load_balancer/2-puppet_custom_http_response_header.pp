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

$config ="server {
    listen 80;
    listen [::]:80;

    add_header X-Served-By \"$(hostname)\";

    root /var/www/html;
    index index.html index.htm;
}"

file {'/etc/nginx/sites-available/default':
    content => $config
}

exec {'restart_nginx_service':
    command => '/usr/sbin/service nginx restart'
}
