# Fixes extension problem in php file

exec {'Fix-extension-error-phpp-in-php-settings':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    }
