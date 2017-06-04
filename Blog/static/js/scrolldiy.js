/* ========================================================================
 * Bootstrap: scrollspy.js v3.3.7
 * http://getbootstrap.com/javascript/#scrollspy
 * ========================================================================
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 * ======================================================================== */

 + function ($) {
	//'use strict';//严格模式

	// SCROLLSPY CLASS DEFINITION
	// ==========================
	//element指向属性是[data-spy="scroll"]的对象
	//options是代表element对象的data元素
	function ScrollSpy(element, options) {

		this.$body = $(document.body)
			//添加当前function的data属性的offset的值
			this.options = $.extend({}, ScrollSpy.DEFAULTS, options) 

			if ($(element).attr("id") == "content") {
				this.$scrollElement = $(window)
					this.selector = (this.options.target || '') + ' .list-group>a'
			} else {
				this.$scrollElement = $(element).is(document.body) ? $(window) : $(element)
					this.selector = (this.options.target || '') + ' .nav li > a'
			}

			// 输出的值是#navbar-example .nav li>a


			this.offsets = []
			this.targets = []
			this.activeTarget = null
			this.scrollHeight = 0
			
			//proxy的this对象会替换process函数中的this对象
			//jquery的on()函数是绑定事件
			//这里的this是要替换$.proxy之后的
			this.$scrollElement.on('scroll.bs.scrollspy', $.proxy(this.process, this))
			//this.$scrollElement.on('scroll.bs.scrollspy', this.process)
			/*$(window).on('scroll', function () {
			console.log("scroll事件被触发")
			})*/

			//function自带的方法在new一个对象的时候自动触发
			this.refresh()

			this.process()

	}

	ScrollSpy.VERSION = '3.3.7'

		ScrollSpy.DEFAULTS = {
		offset: 10
	}

	ScrollSpy.prototype.getScrollHeight = function () {
		return this.$scrollElement[0].scrollHeight || Math.max(this.$body[0].scrollHeight, document.documentElement.scrollHeight)
	}

	//refresh方法主体
	ScrollSpy.prototype.refresh = function () {
		var that = this
			var offsetMethod = 'offset'
			var offsetBase = 0
			this.offsets = []
			this.targets = []
			//这里的this调用的是ScrollSpy的对象
			this.scrollHeight = this.getScrollHeight()
			//我定义的,这里的scrollElement不是window，所以执行
			if (!$.isWindow(this.$scrollElement[0])) {
				offsetMethod = 'position'
				offsetBase = this.$scrollElement.scrollTop()
			}

			//this.$body.find(this.selector).css('color', 'red')			
			//console.log($($xxx)[0].data('target'))
			//find函数是 find()方法获得当前元素集合中每个元素的后代
			//map()把每个元素通过函数传递到当前匹配集合中
			//这里的this指代的是ScrollSpy的对象
		
			//我的理解
			//这里的this是指的是this.$body的对象
			
			//同上
		/*	this.$body.hehe = function () {
			console.log(this)
		}*/
		//匿名函数不等于自执行函数，一定是被调用了
		//this.$body.hehe(function(){console.log(this)})//102
		//this.$body.hehe()

		this.$body
		//this.selector为#navbar-example .list-group>a
		//这里find是有return
		.find(this.selector)
		// jquery的map有点奇怪，return值或return[值]得到的都是数组。return [[值]]得到的才是数组组成的数组
		//map是开始具体一个一个遍历
		.map(function () {			
			var $el = $(this)
				//href在这里取出来就是对应的id名称，例如#1
				var href = $el.data('target') || $el.attr('href')
				//test()方法把符合匹配规则的，然后$(href) 赋值给$href
				//获取对应的id元素的jquery对象
				var $href = /^#./.test(href) && $(href)

				//输出对象中元素的数目，这边是一条一条匹配，所有都为1。

				///console.log(( && $href.is(':visible')))
				//内部寒素直接访问外部函数的成员变量
				
				//console.log($(this)[offsetMethod]() === $href[offsetMethod]())
				var tptp = ($href && [
						[$href[offsetMethod]().top + offsetBase, href]
					])

				//这边花了太多时间，原来是因为这里的第一个对象是一个false，所以直接跳过不执行了，所以单独写的时候，
				//首先遍历第一个，所以才提示这不是一个function，因为第一个对象是一个空值，所以返回false直接跳过不执行了
				//console.log($href.is(':visible'))


				//直接打印一个数组


				//直接打印一个数组的数组
			
				//这里的返回值很巧使用了数组中存放数组的方式存储数据
				return ($href && $href.length && $href.is(':visible') && [
						[$(href)[offsetMethod]().top + offsetBase, href]
					]) || null
		})
		//sort函数
		.sort(
			//这里的function其实只是定义个规则，具体由底层来实现，a-b一般就是升序
			function (a, b) {
			//为什么这里的this取不到值
					
			//以素组中的第一个元素排序
		
			return a[0] - b[0]
		})
		.each(function () {
			console.log(this)
			//向数组里面添加数据
			that.offsets.push(this[0])
			that.targets.push(this[1])
			console.log(that[0])
		})
	

	}

	ScrollSpy.prototype.process = function () {
		
		
		//这里的this对象是指ScrollSpy的对象
		//scrollTop()方法返回或设置匹配元素的滚动条的垂直位置
		var scrollTop = this.$scrollElement.scrollTop() + this.options.offset

		
			

			var scrollHeight = this.getScrollHeight()
			//height()函数，获取匹配元素集合中的第一个元素的当前高度值
			console.log(window.document.body.scrollHeight)//body标签的高度
			console.log(window.document.body.clientHeight)//body标签的高度
			console.log(window.document.body.offsetHeight)//body标签的高度(高度5107)
			console.log(window.screen.height)//屏幕的高度
			console.log(window.screen.availHeight)//屏幕的高度
			console.log(document.documentElement.clientHeight)//浏览器的可见高度
            console.log(window.innerHeight)//浏览器的可见高度
            console.log(window.outerHeight)//浏览器窗口的高度(包括了地址栏还有标签栏高度)
			console.log(this.$scrollElement.height())
			console.log(this.$scrollElement[0])
			
			var maxScroll = this.options.offset + scrollHeight - this.$scrollElement.height()
			//$scrollElemen指代的是window对象
			//第一段匹配元素的高度
			console.log(maxScroll)
			console.log(this.$scrollElement.height())
			console.log(this.$scrollElement.offset())

			var offsets = this.offsets
			var targets = this.targets

			var activeTarget = this.activeTarget

			var i

			console.log(this.scrollHeight === scrollHeight)
			console.log(this.scrollHeight === scrollHeight)
			if (this.scrollHeight != scrollHeight) {
				//主要是刷新一次，防止激活错位				
				this.refresh()
			}
			//scrollTop的值是跟谁滚动监听改变的
			console.log(scrollTop)
			//console.log(activeTarget != (i = targets[targets.length - 1]) && this.activate(i))
			if (scrollTop >= maxScroll) {
				return activeTarget != (i = targets[targets.length - 1]) && this.activate(i)
			}


			if (activeTarget && scrollTop < offsets[0]) {
				this.activeTarget = null
					return this.clear()
			}
console.log(activeTarget != targets[i])
console.log(activeTarget)
console.log(targets[i])
			for (i = offsets.length; i--; ) {
				activeTarget != targets[i] && scrollTop >= offsets[i] && (offsets[i + 1] === undefined || scrollTop < offsets[i + 1]) && this.activate(targets[i])
			}
	}

	//activate 方法
	ScrollSpy.prototype.activate = function (target) {
		this.activeTarget = target

			this.clear()
//这里用的是jquery的属性选择器
			var selector = this.selector +
			'[data-target="' + target + '"],' +
			this.selector + '[href="' + target + '"]'
			
			console.log(selector)
			console.log($(selector))

	/*		var active = $(selector)
			.parents('li')
			.addClass('active')*/
			var active = $(selector).addClass('active')

			if (active.parent('.dropdown-menu').length) {
				active = active
					.closest('li.dropdown')
					.addClass('active')
			}

			//active.trigger('activate.bs.scrollspy')
	}

/*	ScrollSpy.prototype.clear = function () {
		$(this.selector)
		.parentsUntil(this.options.target, '.active')
		.removeClass('active')
	}*/
	
	ScrollSpy.prototype.clear = function () {
		$(this.selector)
		.removeClass('active')
	}
	

	// SCROLLSPY PLUGIN DEFINITION
	// ===========================

	function Plugin(option) {
		return this.each(function () {
			var $this = $(this)

				var data = $this.data('bs.scrollspy')
				var options = typeof option == 'object' && option

				if (!data)
					$this.data('bs.scrollspy', (data = new ScrollSpy(this, options)))

					if (typeof option == 'string')
						data[option]()
		})
	}

	/*  var old = $.fn.scrollspy

	$.fn.scrollspy             = Plugin
	$.fn.scrollspy.Constructor = ScrollSpy


	// SCROLLSPY NO CONFLICT
	// =====================

	$.fn.scrollspy.noConflict = function () {
	$.fn.scrollspy = old
	return this
	}
	 */

	// SCROLLSPY DATA-API
	// ==================

	//将原型对象的scroll属性赋值给old
	var old = $.fn.scrollspy
		//$.fn.scrollspy被赋值成一个function对象
		$.fn.scrollspy = Plugin

		//插件通过 Constructor 属性暴露其原始的构造函数
		$.fn.scrollspy.Constructor = ScrollSpy

		//将原来的$.fn.scrollspy值返回出来
		$.fn.scrollspy.noConflict = function () {
		$.fn.scrollspy = old
			//返回调用这个方法的对象，就是$.fn.scrollspy
			return this
	}

	$(window).on('load.bs.scrollspy.data-api', function () {

		//var contentEle = document.getElementById("content")
		/*  for (var z in contentEle)
		console.log(z)
		 */
		$('[data-spy="scroll"]').each(function () {
			var $spy = $(this)

				Plugin.call($spy, $spy.data())

				console.log("结束。。。")
		})
	})

}
(jQuery);
