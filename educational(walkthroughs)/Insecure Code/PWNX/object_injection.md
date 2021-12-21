https://play.pwnx.io/#/labs

https://developer.mozilla.org/en-US/docs/Web/HTTP

https://www.iana.org/assignments/media-types/media-types.xhtml

### index.php
```php
API Service
12
```

### register.php
```php
<?php
// Get username and input 

include_once('classes/user.php');

if (isset($_REQUEST['username']) && isset($_REQUEST['password'])){
	$username=$_REQUEST['username'];
	$password=$_REQUEST['password'];
	$user=new User();

	$user->set_password($password);
	$user->set_username($username);
	$user->set_role('user');

	//file_put_contents("/tmp/sessions.txt", $username.":".$password."\n", FILE_APPEND);
	file_put_contents("/tmp/sessions.txt", serialize($user)."\n", FILE_APPEND);
	echo 'Done';
}
else{
	echo 'Need credentials';
}

?>
534
```
== the user role is hard coded ==

### user.php
```php
<?php

class User {
  // Properties
  public $username;
  public $password;
  public $role;
  public $log = False;
  public $path = '/tmp/we'; 

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
    $this->path = '/tmp/'.rand(1,3000).'.log';
  }

  function __destruct() {
    if($this->log){
    	file_put_contents($this->path, date("H:i").$this->username.":".$this->role);
    }
  }
}

?> 
828
```
### login.php
```php
<?php
// retrieve sessions (get cookies) from sessions.txt

include_once('classes/user.php');


if (isset($_REQUEST['username']) && isset($_REQUEST['password'])){
	// search for a username and password match in file
	// get users from file
	$content = array();
	$file = fopen("/tmp/sessions.txt", "r");
	if (!$file){
		echo 'No user registered ..';
		exit();
	}
	while (!feof($file) ) {
		$line = fgets($file);
		$content[] = explode("\n", $line);
	}
	fclose($file);
	array_pop($content); // last item is empty

	
	foreach($content as $line){
		// remove newline at the end 
		$line[0] = str_replace('\n','',$line[0]);
		$user_line = new User();
		try {
			$user_line = unserialize($line[0]);
			if(!method_exists($user_line,'get_username')) {
				// we have an invalid object
				// just continue
				// DEBUG:
				//file_put_contents('/tmp/ser', $line[0]);
				continue;
			}
		} catch (Exception $e){
			// mah .....
			echo 'bad serial';
		}
		if ($user_line->get_username() == $_REQUEST['username'] && $user_line->get_password() == $_REQUEST['password']){
			echo 'Logged in';
			// no cookie? ;P
			exit();
		}
	}
	echo 'Login Failed';

}
else {
	echo 'Incorrect input';
}
?>
1182
```