https://portswigger.net/web-security/deserialization/exploiting

# Identify

## PHP
The native methods for PHP serialization are serialize() and unserialize(). If you have source code access, you should start by looking for unserialize() anywhere in the code and investigating further. 

## JAVA
serialized Java objects always begin with the same bytes, which are encoded as ac ed in hexadecimal and rO0 in Base64.

Any class that implements the interface java.io.Serializable can be serialized and deserialized. If you have source code access, take note of any code that uses the readObject() method, which is used to read and deserialize data from an InputStream. 

# Manipulation
1.  You can either edit the object directly in its byte stream form, 
2.  or you can write a short script in the corresponding language to create and serialize the new object yourself. 
    The latter approach is often easier when working with binary serialization formats.

# Magic Methods
Subsets of methods that are automatically envoked whenever an event triggers them.  They start with two underscores (double-underscores).  

https://www.php.net/manual/en/language.oop5.magic.php

The following method names are considered magical: __construct(), __destruct(), __call(), __callStatic(), __get(), __set(), __isset(), __unset(), __sleep(), __wakeup(), __serialize(), __unserialize(), __toString(), __invoke(), __set_state(), __clone(), and __debugInfo(). 

**Warning**

    All magic methods, with the exception of __construct(), __destruct(), and __clone(), must be declared as public, otherwise an E_WARNING is emitted. Prior to PHP 8.0.0, no diagnostic was emitted for the magic methods __sleep(), __wakeup(), __serialize(), __unserialize(), and __set_state().
        

**Warning**

    If type declarations are used in the definition of a magic method, they must be identical to the signature described in this document. Otherwise, a fatal error is emitted. Prior to PHP 8.0.0, no diagnostic was emitted. However, __construct() and __destruct() must not declare a return type; otherwise a fatal error is emitted.

### Constructors and Destructors
https://www.php.net/manual/en/language.oop5.decon.php#object.destruct

https://www.php.net/manual/en/function.serialize.php

https://www.php.net/manual/en/function.unserialize.php


# Object Injection
https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection

### write-up
https://medium.com/swlh/exploiting-php-deserialization-56d71f03282a

https://www.php.net/manual/en/function.phpinfo.php

https://www.w3schools.com/Php/php_oop_classes_objects.asp