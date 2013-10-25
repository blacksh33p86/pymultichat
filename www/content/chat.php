

<div  style="width: 600px; margin:0 auto">
 <p style="width:525px; text-align:center"> <a href="#" onclick="c.disconnect();" class="btn btn-primary btn-small">Disconnect</a> </p>
     
      <div id="chat"></div>
   <div  class="input-append"><input type="text" id="inp" style="width:450px" /> <a href="#" onclick="javascript:c.sendmsg();"  class="btn btn-primary ">Senden</a></div>
</div>

<script>
document.getElementById('inp').onkeypress = keyinmsg;
function keyinmsg(ev) {
	if (ev.keyCode == 13)
		c.sendmsg(document.getElementById('inp').value);
};


<?php 
if ($_SESSION['loggedin'] && $_GET['action']=="guest" || $_SESSION['username']=="")
{
	print "var loggintype='guest';\n";
	print "c.connect();\n";
	
} ?>

</script>
