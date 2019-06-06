#_*_coding:utf-8_*_
import media, fresh_tomatoes
toy_story = media.Movie("Toy Story", 
	"A boy with his toys",
	"http://file.ipadown.com/uploads/news/20121215142503963.jpg",
	"http://v.youku.com/v_show/id_XMTgzOTI5OTg0.html")
avatar = media.Movie("Avatar", 
	"A Marine on an alien planet", 
	"http://pic8.nipic.com/20100722/4068536_010901449822_2.jpg",
	 "http://v.youku.com/v_show/id_XMjMwNzk2OTQw.html?tpa=dW5pb25faWQ9MTAyMjEzXzEwMDAwMl8wMV8wMQ")
xiaoaojianghu = media.Movie("笑傲江湖Ⅱ：东方不败",
	'''令孤冲（李连杰饰）在一次与师兄弟下山办事的过程中，
	意外的发现东方不败（林青霞饰）与倭寇串通有谋反之意，
	便与任盈盈（关之琳饰）、向问天及蓝凤凰（袁洁莹饰）等计划在救出任我行之后，
	联手除掉东方不败并夺回日月神教。由于令孤冲不认识东方不败，因而他误把东方不败当成一位美貌少女，
	以至于使自已的同门尽皆死于东方不败之手。于是令孤冲、任盈盈、向问天、任我行等一同去找东方不败报仇。在一场激烈的打斗中，
	令孤冲的面部被划伤，任我行一只眼被刺瞎，向问天小腿受伤，而东方不败则坠入山崖。''', 
	"http://image14.m1905.cn/uploadfile/2011/0126/20110126010557579.jpg",
	"https://v.youku.com/v_show/id_XMzQ1MzA0NjIwNA==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2")
rangzidanfei= media.Movie("让子弹飞",
	'''北洋年间，中国南部。
	一场惊天动地的火车劫案之后，
	号令山林的绿林悍匪张牧之，
	遭遇行走江湖的通天大骗老汤，
	两人从生死宿敌变成莫逆之交，
	然而真正的决战才刚刚开始。
	南国一霸黄四郎虎视眈眈镇守鹅城，
	一场场情杀命案连环上演。华南三王各自为阵，
	鹅城双艳粉墨登场，乱世枭雄的混战一触即发''',
	"https://pic.baike.soso.com/ugc/baikepic2/0/ori-20170402002400-1084855641.jpg/800", 
	"https://v.youku.com/v_show/id_XODY2NDc3ODA0.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2")
movies = [toy_story, avatar, xiaoaojianghu, rangzidanfei]
#toy_story.show_trailer()
fresh_tomatoes.open_movies_page(movies)
