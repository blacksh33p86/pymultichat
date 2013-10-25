

<?php 

if ($_POST['action'] == "registered" || $_GET['action'] == "guest")
{
	if($_POST['action']=="registered") {
		
	}

	if($_GET['action'] == "guest") {
		$_SESSION['loggedin']=true;
		$_SESSION['username']="";
		$_SESSION['privilege']=0;
		header("Location: index.php?url=chat&action=guest");
    	exit;
	}
}

else {
?>
<div  style="width: 300px; margin:0 auto">
<form method="post" action="index.php?url=login">
<fieldset>
	<legend>Sign in</legend>
	
	<label>username:</label>
        
        <div  class="input-prepend">
            <span  class="add-on">@</span>
            <input  type="text"  placeholder="username" name="user">
        </div>
        
        <label>password:</label>
        
        <div  class="input-prepend">
            <span  class="add-on">*</span>
            <input  type="password"  placeholder="password" name="pass">
        </div>
         <button  class="btn"  type="submit">Sign in</button>
</fieldset>
<input type="hidden" name="action" value="registered">
</form>
<a href="index.php?url=login&action=guest" class="btn">Sign in as guest</a>

<?php } ?>

</div>