<?php 
if($_GET['url']=="logout")
 { 
 if ( isset( $_COOKIE[session_name()] ) )
	setcookie( session_name(), “”, time()-3600, “/” );
$_SESSION = array();
session_destroy();
header("Location: ".$_SERVER['PHP_SELF']);
    	exit;

 }
session_start(); ?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Multi-Chat</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="root" >

    <!-- Le styles -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 60px;
        padding-bottom: 40px;
      }
    </style>
    <link href="css/bootstrap-responsive.css" rel="stylesheet">
	<link href="css/chat.css" rel="stylesheet">
    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="ico/favicon.png">
    <?php if($_GET['url']=="chat") { print '<script language="javascript" type="text/javascript" src="js/chat.js"></script>'; } ?>
    
    
    <script>var c = new chat('inp','chat');</script>
    </head>
  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="#">Multi-Chat</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="index.php">Home</a></li>
              <li><a href="index.php?url=chat">Chat</a></li>
              <li><a href="index.php?url=about">About</a></li>
              
            </ul>
            <?php if(!isset($_SESSION['loggedin']) && !$_SESSION['loggedin'] ) { ?>
				 <form class="navbar-form pull-right">
              <input class="span2" type="text" placeholder="Email">
             
              <input class="span2" type="password" placeholder="Password"> 
          
              <button type="submit" class="btn">Sign in</button>  <button type="submit" class="btn">Register</button>
                    
            </form><?php } else {?>
            <a href="index.php?url=logout" class="btn btn-primary ">logout</a>
            <?php } ?>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

      <!-- Main hero unit for a primary marketing message or call to action -->
      <div class="hero-unit">
      
      
      <?php
				  switch($_GET['url']) {      
				    case ("chat"): if(!$_SESSION['loggedin']) include("content/login.php"); else include("content/chat.php"); break;
				    case ("login"): include("content/login.php"); break;
				    default: include("content/home.php"); 
					};           
				?>
      </div>

     

      <hr>

      <footer>
        <p>&copy; blacksh33p 2013</p>
      </footer>

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery.js"></script>
    <script src="js/bootstrap-transition.js"></script>
    <script src="js/bootstrap-alert.js"></script>
    <script src="js/bootstrap-modal.js"></script>
    <script src="js/bootstrap-dropdown.js"></script>
    <script src="js/bootstrap-scrollspy.js"></script>
    <script src="js/bootstrap-tab.js"></script>
    <script src="js/bootstrap-tooltip.js"></script>
    <script src="js/bootstrap-popover.js"></script>
    <script src="js/bootstrap-button.js"></script>
    <script src="js/bootstrap-collapse.js"></script>
    <script src="js/bootstrap-carousel.js"></script>
    <script src="js/bootstrap-typeahead.js"></script>

  </body>
</html>
