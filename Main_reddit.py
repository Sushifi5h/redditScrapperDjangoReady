# -*- coding: utf-8 -*-

import mechanize
from bs4 import BeautifulSoup
import time
import webbrowser



links = []
titles = []
thumbnail = [] # none or thumbnail
comment_links = []
ranks = []


start_url = 'https://www.reddit.com/'
next_url = " "


def grab_everything(URL):
	
	global next_url

	global links
	global title
	global thumbnail
	global comment_links
	global ranks


	#Main browser
	br = mechanize.Browser()
	br.set_handle_robots(False)   # ignore robots
	br.set_handle_refresh(False)

	reponse = br.open(URL).read()

	all_links_on_page = ""

	
	soup = BeautifulSoup(reponse)

	#Dig soup for HTML contents
	for x in soup.findAll("div", {"id" : "siteTable"}):
		for i in x.findAll("div", {"onclick" : "click_thing(this)"}):
			ranks.append(i.find("span", { "class" : "rank"}).contents[0])
			for n in i.findAll("p", { "class" : "title"}):
				links.append(n.find('a')['href'])
				all_links_on_page += n.find('a')['href']
				titles.append(n.find('a').contents[0])

	for q in x.findAll("ul", { "class" : "flat-list buttons"}):
				comment_links.append(q.find("a")["href"])

	for x in soup.findAll("div", {"id" : "siteTable"}):
		for y in x.findAll("div", { "class" : "nav-buttons"}):
			url_for = y.find("span", {"class": "nextprev"}).contents[-1]
			fuck_me = str(url_for).split(" ")
			href = fuck_me[1]
			#href on the current page on the bottom
			next_url = href[6:-1]

	for x in soup.findAll("a", {"class" : "thumbnail may-blank "}):
		img_string = str(x["href"]) + " " + str(x.contents[0]["src"])
		if str(x["href"]) in str(all_links_on_page):
			thumbnail.append(img_string)
		else: pass

	open("/home/ctpeets/webapps/reddit_1000_static/templates/html.txt", "w").close()
	html_file_1 = open("/home/ctpeets/webapps/reddit_1000_static/templates/html.txt","r+")


	len_of_list = len(ranks)

	make_string = " "
	
	for i in thumbnail:
		make_string = make_string + i + " "

	counter = 0

	for i in range(0, len_of_list):
		if links[i] in make_string:
			get_thumb = thumbnail[counter].split(" ")
			get_thumb_url = get_thumb[1]
			pic_clean = get_thumb_url[2::]
			write_this = "|%s.| |%s| |%s| |%s| |%s| \n" % (ranks[i].encode('utf-8'), titles[i].encode('utf-8'), comment_links[i].encode('utf-8'), links[i].encode('utf-8'), pic_clean)
			html_file_1.write(write_this)
			counter = counter + 1
		else:
			write_this = "|%s.| |%s| |%s| |%s| |none| \n" % (ranks[i].encode('utf-8'), titles[i].encode('utf-8'), comment_links[i].encode('utf-8'), links[i].encode('utf-8'))
			html_file_1.write(write_this)



def print_nice():
	open("/home/ctpeets/webapps/reddit_1000_static/templates/html.txt", "w").close()
	html_file_1 = open("/home/ctpeets/webapps/reddit_1000_static/templates/html.txt","r+")


	len_of_list = len(ranks)

	make_string = " "
	
	for i in thumbnail:
		make_string = make_string + i + " "

	counter = 0

	for i in range(0, len_of_list):
		if links[i] in make_string:
			get_thumb = thumbnail[counter].split(" ")
			get_thumb_url = get_thumb[1]
			pic_clean = get_thumb_url[2::]
			write_this = "|%s.| |%s| |%s| |%s| |%s| \n" % (ranks[i].encode('utf-8'), titles[i].encode('utf-8'), comment_links[i].encode('utf-8'), links[i].encode('utf-8'), pic_clean)
			html_file_1.write(write_this)
			counter = counter + 1
		else:
			write_this = "|%s.| |%s| |%s| |%s| |none| \n" % (ranks[i].encode('utf-8'), titles[i].encode('utf-8'), comment_links[i].encode('utf-8'), links[i].encode('utf-8'))
			html_file_1.write(write_this)




	html_file_1.close()

def make_html():
	data_all = open("/home/ctpeets/webapps/reddit_1000_static/templates/html.txt","r+")
	open("/home/ctpeets/webapps/reddit_1000_static/templates/base.html", "w").close()
	example_file = open("/home/ctpeets/webapps/reddit_1000_static/templates/base.html", "r+")


	links_1 = []
	titles_1 = []
	comments_1 = []
	thumbnail_1 = []


	for i in data_all:
		
		break_it = i.split("|")

		thumbnail_1.append(break_it[-2])
		titles_1.append(break_it[3])
		comments_1.append(break_it[5])

		check_reddit = break_it[-4]

		if check_reddit[0] == "/" and check_reddit[1] == "r" and check_reddit[2] == "/":
			com_url = "http://www.reddit.com" + check_reddit
			links_1.append(com_url)
		else:
			links_1.append(break_it[-4])


		







	tagged_div = " "

	cycles_needed = len(links)


	




	for i in range(0, cycles_needed):

		if thumbnail_1[i] == "none":


			div_tagged =	 """
		 <div class="col-md-12">
		          <h2> <a href="%s">%s</a></h2>
		        <p>

		          <a class="btn btn-default btn-sm dropdown-toggle" href="%s" role="button">View details »</a>

		          <a class="btn btn-default btn-xs dropdown-toggle" href="%s" role="button">Comments »</a>
		          </p>
		        </div> 
		""" % (links_1[i], titles_1[i], links_1[i], comments_1[i])
			tagged_div = tagged_div + div_tagged

		else:


			div_tagged =	 """
		 <div class="col-md-12">
		          <h2> <a href="%s">%s</a></h2>
		        <p>
		          <a href="%s"><img src="http://%s"alt=""width="72" height="46" border="0" /></a>

		          <a class="btn btn-default btn-sm dropdown-toggle" href="%s" role="button">View details »</a>

		          <a class="btn btn-default btn-xs dropdown-toggle" href="%s" role="button">Comments »</a>
		          </p>
		        </div> 
		""" % (links_1[i], titles_1[i], links_1[i], thumbnail_1[i], links_1[i], comments_1[i])
			tagged_div = tagged_div + div_tagged







	base_html = """
	<html lang="en"><head>
	    <meta charset="utf-8">
	    <meta http-equiv="X-UA-Compatible" content="IE=edge">
	    <meta name="viewport" content="width=device-width, initial-scale=1">
	    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
	    <meta name="description" content="">
	    <meta name="author" content="">
	    <link rel="icon" href="../../favicon.ico">

	    <title>Reddit Top 1000ish</title>

	    <!-- Bootstrap core CSS -->
	    <link href="/static/css/bootstrap.min.css" rel="stylesheet">

	    <!-- Custom styles for this template -->
	    <link href="/static/css/jumbotron.css" rel="stylesheet">

	    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
	    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
	    <style>.carbonad,
	#content > #right > .dose > .dosesingle,
	#content > #center > .dose > .dosesingle,
	#carbonads-container
	{display:none !important;}</style>

	    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	    <!--[if lt IE 9]>
	      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
	      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	    <![endif]-->
	  </head>

	  <body>

	    <nav class="navbar navbar-inverse navbar-fixed-top">
	      <div class="container">
	        <div class="navbar-header">
	          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
	            <span class="sr-only">Toggle navigation</span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	          </button>
	          <a class="navbar-brand" href="#">Reddit Top 1000</a>
	        </div>
	        <div id="navbar" class="navbar-collapse collapse">
	        </div><!--/.navbar-collapse -->
	      </div>
	    </nav>

	    <!-- Main jumbotron for a primary marketing message or call to action -->
	    <div class="jumbotron">
	      <div class="container">
	        <h1>Reddit Top 1000 ish</h1>
	        <p>Updates every hour.</p>
	        
	      </div>
	    </div>

	    <div class="container">
	      <!-- Example row of columns -->
	      <div class="row">
	       



	       %s





	        </div>
	      </div>

	      <hr>
	    </div> <!-- /container -->


	    <!-- Bootstrap core JavaScript
	    ================================================== -->
	    <!-- Placed at the end of the document so the pages load faster -->
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
	    <script src="/static/js/bootstrap.min.js"></script>
	    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
	    <script src="/static/js/ie10-viewport-bug-workaround.js"></script>
	  

	</body></html>
	""" % (tagged_div)


	example_file.write(base_html)



		






	data_all.close()
	example_file.close()







if __name__ == '__main__':

	grab_everything(start_url)
	print "Let's go"
	print "Cycles: 40"
	for i in range(1, 40):
		print "Current_Cycle: " + str(i)
		try:
			time.sleep(30)
			grab_everything(next_url)
			print "Sleeping..."
		except:
			pass

	make_html()

