function chat(inp,out) 
{
	var ws = null;
	var input = inp;
	var output = out;




	this.connect = function ()
	{
	  if ("WebSocket" in window)
	  {
	     
	     // Let us open a web socket
	     ws = new WebSocket("ws://localhost:9998", ['base64']);
	     ws.onopen = function()
	     {
	        // Web Socket is connected, send data using send()
	       input = document.getElementById(input);
	       output = document.getElementById(output);
	       
	       if (loggintype=="guest") {
	       	c.loginGuest();
	       }
	     };
	     ws.onmessage = function (evt) 
	     { 
	       var received_msg = evt.data;
	       
	   	 output.innerHTML  +=decodeURIComponent(escape(window.atob( received_msg )))+'<br>';
	   		
	       output.scrollTop = output.scrollHeight;
	       // document.getElementById('chat').value
	     };
	     ws.onclose = function()
	     { 
	        // websocket is closed.
	        //alert("Connection is closed..."); 
	        
	     };
	     
	  }
	  else
	  {
	     // The browser doesn't support WebSocket
	     alert("WebSocket NOT supported by your Browser!");
	  }
	 };
	 
	 this.writeToChat = function(msg){
	 	output.innerHTML  +=msg+'<br>';	 
	 }
	 
	
	 
	 this.loginGuest = function () {
	 	
	 	
	 	
	 	this.sendDirectly("['/login','guest']") ;
	 };
	 
	 this.sendDirectly = function (msg) {
	 	
	 	 ws.send(window.btoa(unescape(encodeURIComponent( msg ))));
	 	};
	 
	 this.sendmsg = function () {
	  		var t = input.value.replace(/(<([^>]+)>)/ig,"");
	  		if (t.length<1) return false;
	  		input.value ="";
	  		t=  t.replace(/\'/g,"\\'");
			this.sendDirectly("['/send','Welcome hall','"+t+"']");
			
			// document.getElementById('inp').value
		};
		
	this.disconnect = function () {
	  	
			this.sendDirectly("['/logout','me']");
			window.location.href = "index.php";
		};

}