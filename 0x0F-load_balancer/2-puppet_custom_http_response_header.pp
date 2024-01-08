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

$host_name = "$(hostname)"

file { '/etc/nginx/sites-available/default':
    content => "
server {
    listen 80;
    listen [::]:80;

    add_header X-Served-By $host_name;

    root /var/www/html;
    index index.html index.htm;
}
",
}

exec {'restart_nginx_service':
    command => '/usr/sbin/service nginx restart'
}
