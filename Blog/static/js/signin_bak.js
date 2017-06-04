
function PopupLogin() {
	this.oMask = document.createElement("div");
	this.oWrap = document.createElement("div");
	this.oForm = document.createElement("form");
	this.oInput1 = document.createElement("input");
	this.oInput2 = document.createElement("input");
	//this.oInput3  =document.createElement("input");
	this.oButton = document.createElement("button");
	this.oLable1 = document.createElement("lable");
	this.aShow = document.createElement("span");
	this.oClose = document.createElement("a")
	
	this.cookieText = document.createTextNode("\'{% csrf_token %}\'");

};

PopupLogin.prototype = {
	//初始化
	init: function () {
		var that = this;
		this.oMask.style.position = "fixed";
		this.oMask.style.width = "100%";
		this.oMask.id="div1";
		this.oMask.style.top = this.oMask.style.left = this.oMask.style.right = this.oMask.style.bottom = 0;
		this.oMask.style.background = "#000";
		this.oMask.style.filter = "opacity=0";
		this.oMask.style.opacity = 0.6;
		this.oMask.style.zIndex = 888888;
		this.oWrap.style.position = "fixed";
		this.oWrap.style.width = "380px";
		this.oWrap.style.height = "270px";

		this.oWrap.style.top = this.oWrap.style.left = "50%";
		this.oWrap.style.margin = "-140px 0 0 -195px";
		this.oWrap.style.padding = "10px";
		this.oWrap.style.background = "#f8f6e9";
		this.oWrap.style.zIndex = 999999;
		addClass(this.oWrap, "sigin");
		this.oWrap.id = "div2";
		this.oClose.href = "javascript:;";
		this.oClose.style.position = "absolute";
		this.oClose.style.width = this.oClose.style.height = "17px";
		this.oClose.style.top = this.oClose.style.right = "5px";
		this.oClose.style.display="inline-block";
		this.oClose.innerHTML="&#xe6e9;";
		this.oClose.style.marginRight="10px";
		addClass(this.oClose,"iconfont");
		//this.oClose.style.background = "url(http://img03.taobaocdn.com/tps/i3/T1HQezXcXnXXXXXXXX-123-400.png) 0 -81px";

		this.oWrap.appendChild(this.oClose);
		//这里注意返回的还是oForm这个object
		var iForm = this.oWrap.appendChild(this.oForm);
		iForm.innerHTML="\"{% csrf_token %}\"";
		iForm.action = "/admin/login/?next=/admin/";
		//iForm.action = "/admin";
		iForm.method = "post";

		addClass(iForm, "form-signin");
		iForm.role = "form";
		var iInput1 = iForm.appendChild(this.oInput1);
		addClass(iInput1, "form-control");
		iInput1.type = "text";
		iInput1.id = "userName";
		iInput1.placeholder = "用户名";
		iInput1.name="username";
		var iInput2 = iForm.appendChild(this.oInput2);
		iInput2.type = "password";
		iInput2.id = "passWord"
			addClass(iInput2, "form-control"); ;
		iInput2.placeholder = "密码";
		iInput2.name="password";
		var iButton = iForm.appendChild(this.oButton);
		addClass(iButton, "btn");
		addClass(iButton, "btn-lg");
		addClass(iButton, "btn-block");
		iButton.type = "submit";
		iButton.id = "submitUserPass";
		iButton.innerHTML = "登录";
	//	iButton.href="javascript:;";

		var iLable1 = iForm.appendChild(this.oLable1);
		addClass(iLable1, "checkbox");
		//
		iLable1.innerHTML = "&nbsp&nbsp&nbsp&nbsp&nbsp" + "<input type=\"checkbox\" value=\"remember-me\">" + "记住我";

		var aShow= iForm.appendChild(this.aShow);
		aShow.id = "showText";

		document.body.appendChild(this.oMask);
		document.body.appendChild(this.oWrap);

		this.oClose.onclick = function () {
			
			reopen();
			//调用原型中的close方法，that就是初始化的新对象。
			that.close()
			

		};
	},

	close: function () {
		//使两个div层样式消失
		//this.oMask.style.display = this.oWrap.style.display = "none";
		removeTag();
		document.documentElement.style.cssText = "overflow:auto;";
		 
		
		$("<style type='text/css'>.aBody{padding-right:" + 0 + "px;}</style>").appendTo("head");
		$("<style type='text/css'>#fix-padding{padding-right:" + 0 + "px;}</style>").appendTo("head");
		


	},

	
};

function hasClass(element, csName) {

	return 　element.className.match(RegExp('(\\s|^)' + csName + '(\\s|$)')); //使用正则检测是否有相同的样式

	　　　　
};

function addClass(element, csName) {

	if (!hasClass(element, csName)) {
		element.className += ' ' + csName;
		　　　　　　
	}
};

/*function ScrollbarWidth() {
this.calculateScrollbarWidth = function() {
if ($("#scrollbar-width").length > 0) return;
var a = $('<div class="modal-measure-scrollbar"/>').prependTo($("body")),
b = $('<div class="inner"/>').appendTo(a),
c = a.width() - b.width();
a.remove(),
$("head").append('<style id="scrollbar-width">        .compensate-for-scrollbar,        .modal-enabled,        .modal-enabled .global-nav-inner,        .profile-editing,        .profile-editing .global-nav-inner,        .overlay-enabled,        .overlay-enabled .global-nav-inner,        .grid-enabled,        .grid-enabled .global-nav-inner,        .gallery-enabled,        .gallery-enabled .global-nav-inner {          margin-right: ' + c + "px      }      </style>")
}
}*/

window.onload = function () {
console.log("xxxx");
	var oBtn = document.getElementById("sigin");
	// iContent  = document.getElementById("content"),
	//iContent = document.getElementsByClassName("container"),
	oBtn.onclick = login;

};

function login() {
	w1 = $("body").width();
	//取消滚动条(如下)
	document.documentElement.style.cssText = "overflow:hidden;";
	w2 = window.outerWidth;
	/*H=$("html");
	w1 = $(window).width();
	H.addClass("fancybox-lock-test");
	w2 = $(window).width();
	H.removeClass('fancybox-lock-test');*/
	//$("<style type='text/css'>.fix-margin{margin:" +0+"px"+" "+0.5*(w2 - w1)+"px"+" "+0+"px"+" "+0.5*(w1 - w2)+"px"+"}</style>").appendTo("head");
	$("<style type='text/css'>.aBody{padding-right:" + (w2 - w1) + "px;}</style>").appendTo("head");
	$("<style type='text/css'>#fix-padding{padding-right:" + (w2 - w1) + "px;}</style>").appendTo("head");
	oLogin = new PopupLogin();
	oLogin.init();

	var submitUserPass = document.getElementById("submitUserPass");
	submitUserPass.onclick = check;
};

function check() {

	var userName = document.getElementById("userName").value;
	var showText = document.getElementById("showText");
	/*showText.setAttribute("display","block");
	showText.style.marginRight="auto";
	showText.style.marginLeft="auto";*/
	showText.id="showText";
	
	
	//检验输入的用户名
	if (/^[\s\n\t\r]*$/.test(userName)) {
		showText.innerHTML = "用户名不能为空";
		return false
	} else {
		if (!/^[a-zA-Z0-9_]+$/.test(userName)) {

			showText.innerHTML = "用户名格式不正确";
			return false
		} else {
			showText.innerHTML = "";
			return true
		}
	}

};
function removeTag(){
	var div1 =document.getElementById("div1");
	var div2 =document.getElementById("div2");
	if ((div1!= null)||(div2!= null)){
	div1.parentNode.removeChild(div1);
	div2.parentNode.removeChild(div2);}
	
 };
	
	
 function reopen () {

		var oBtn = document.getElementById("sigin");

		oBtn.onclick = login;

	}
