

<div  style="width: 600px; margin:0 auto">
 <p><a href="#" onclick="c.connect();" class="btn btn-primary btn-small">Connect</a> <a href="#" onclick="javscript:c.disconnect();" class="btn btn-primary btn-small">Disconnect</a> <a href="#" onclick="javscript:c.loginGuest();" class="btn btn-primary btn-small">Login as guest</a></p>
      <!--  <textarea style="width:600px" rows="10" id="chat"></textarea><br />!-->
      <div id="chat"></div>
   <div  class="input-append"><input type="text" id="inp" style="width:450px" /> <a href="#" onclick="javascript:c.sendmsg();"  class="btn btn-primary ">Senden</a></div>
</div>

<script>
document.getElementById('inp').onkeypress = keyinmsg;
function keyinmsg(ev) {
	if (ev.keyCode == 13)
		c.sendmsg(document.getElementById('inp').value);
};

</script>