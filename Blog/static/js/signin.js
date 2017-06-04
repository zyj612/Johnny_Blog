window.global_lr = Loginregister;


function Loginregister(){


	this.oBtnSig=document.getElementById("base_sigin");
	this.oBtnReg=document.getElementById("base_register");
	
	// iContent  = document.getElementById("content"),
	//iContent = document.getElementsByClassName("container"),
	};


Loginregister.prototype={


disable_scroll:function (){
w1 = $("body").width();
//取消滚动条(如下)

document.documentElement.style.cssText = "overflow:hidden;";
w2 = window.outerWidth;
console.log(w2-w1)
	$("<style type='text/css'>.aBody{padding-right:" + (w2 - w1) + "px;}</style>").appendTo("head");
	$("<style type='text/css'>#fix-padding{padding-right:" + (w2 - w1) + "px;}</style>").appendTo("head");
},

 login_register:function(){
	
	/*H=$("html");
	w1 = $(window).width();
	H.addClass("fancybox-lock-test");
	w2 = $(window).width();
	H.removeClass('fancybox-lock-test');*/
	//$("<style type='text/css'>.fix-margin{margin:" +0+"px"+" "+0.5*(w2 - w1)+"px"+" "+0+"px"+" "+0.5*(w1 - w2)+"px"+"}</style>").appendTo("head");
	//注意appendto追加方式


	var form ="<div id='div_background'></div>"+"<div id='singin_container'>"
	+"<a id='header_close' class='glyphicon glyphicon-remove' href='javascript:;'></a>"
	+"<div id='header_signin'><a class='header_s'>登录</a><a class='header_r' href='javascript:;'>注册</a></div>"
	+"<div id ='bomp_username' class='input-group'>"
	+"<div class='input-group-addon'><span class='glyphicon glyphicon-user'></span></div>"
	+"<input id='name' name='bomp_username' class='form-control' placeholder='用户名' value='' type='text'></div>"
	+"<div id ='bomp_pwd' class='input-group'>"
	+"<div class='input-group-addon'><span class='glyphicon glyphicon-lock'></span></div>"
	+"<input id ='bomp_password' name='bomp_password' class='form-control' placeholder='密码' value='' type='password'></div>"
	+"<lable id='lable_check'  class='checkbox'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type='checkbox'>记住我</lable>"	
	+"<div id ='bomp_nickname' class='input-group' style='display: none'>"
	+"<div class='input-group-addon'><span class='glyphicon glyphicon-user'></span></div>"
	+"<input name='bomp_nickname' class='form-control' placeholder='起个昵称吧' value='' type='text'></div>"
	+"<div id ='bomp_email' class='input-group' style='display: none'>"
	+"<div class='input-group-addon'><span class='glyphicon glyphicon-envelope'></span></div>"
	+"<input name='bomp_email' class='form-control' placeholder='邮箱账户' value='' type='text'></div>"
	+"<span id='showText'></span>"
	+"<button id='bomp_submit' name='bomp_submit' class='btn btn-success btn-block' type='button'>登录</button>";
//var oBtnCheck = $(':button[name=bomp_submit]');

	if(!document.getElementById("div_background"))
	{	
	$("#form_signin").append(form);
	$("#form_signin").css("display","block");}
	else{
		$("#form_signin").css("display","block");
		$("#bomp_nickname").css("display","none");
		$("#bomp_email").css("display","none");
		$("#singin_container").height("260px");
		$("#lable_check").css("display","");
		$("#bomp_submit").text("登陆");
		$("#form_signin").attr("action","/login/");
		
	}
},



	bound_sign:function (){
		$(".header_s").on("click",function(){
		$(this).removeAttr("href");
		$(".header_r").attr("href","javascript:;");
		$("#bomp_nickname").css("display","none");
		$("#bomp_email").css("display","none");
		$("#bomp_submit").text("登录");
		$("#showText").text("");
		    if($("#bomp_submit").text()=="登录")
    	{
    		$("#bomp_submit").on('click',signin_check);
    	}
		$("#lable_check").css("display","");
		$("#singin_container").height("260px");
		$("#form_signin").attr("action","/login/");
		})

		$(".header_r").on("click",function(){
		$(this).removeAttr("href");
		$(".header_s").attr("href","javascript:;");
		$("#bomp_nickname").css("display","table");
		$("#bomp_email").css("display","table");
		$("#bomp_submit").text("注册");
		$("#showText").text("");
		if($("#bomp_submit").text()=="注册")
		{
			$("#bomp_submit").on('click',register_check);
			$(":input[name=bomp_username]").on('change',userNameCheck);
		}
		$("#singin_container").height("320px");
		$("#lable_check").css("display","none");
		$("#form_signin").attr("action","/register/");
		})
	},


	


	bound_click:function(){
		$("#header_close").on("click",function(){
			document.documentElement.style.cssText = "overflow:auto;";
			//在head标签下添加两个属性
			$("<style type='text/css'>.aBody{padding-right:" + 0 + "px;}</style>").appendTo("head");
			$("<style type='text/css'>#fix-padding{padding-right:" + 0 + "px;}</style>").appendTo("head");
			$("#form_signin").css("display","none");
		})
	},


bound_register:function(){
		$(".header_r").removeAttr("href");
		$(".header_s").attr("href","javascript:;");
		$("#bomp_nickname").css("display","table");
		$("#bomp_email").css("display","table");
		$("#lable_check").css("display","none");
		$("#bomp_submit").text("注册");
		$("#singin_container").height("320px");
		$("#form_signin").attr("action","/register/");
},




login:function() {


this.disable_scroll();
this.login_register();
this.bound_sign();
this.bound_click();
},


 register:function(){

if(!document.getElementById("div_background"))
	{
		this.disable_scroll();
		this.login_register();
		this.bound_register();
		this.bound_click();
	}

	else{
		if(document.getElementById("div_background")) 
		{
			this.disable_scroll();
			$("#form_signin").css("display","block");
			this.bound_register()
			this.bound_click();
		}
	}

this.bound_sign();


},

};


