# Fixes extension problem in php file

exec {'Fix extension error phpp int php':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    }
