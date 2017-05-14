import os.path

sites = [

          {'shortname': 'egaz',
           'uri': 'http://www.egazette.nic.in/',
           'type': 'html',
           'contentcss': 'div',
           'encoding': 'utf-8'}

          # {'shortname': 'appcon',
          #  'uri': 'http://www.appcon.in/',
          #  'type': 'html',
          #  'titleregex': '',
          #  'contentregex': '',
          #  'encoding': 'utf-8'}

           # {'shortname': 'mywebsite1',
           # 'uri': 'http://www.cricbuzz.com/live-cricket-scores/18124/kxip-vs-rps-4th-match-indian-premier-league-2017',
           # 'type': 'html',
           # 'titleregex': '',
           # 'contentregex': '',
           # 'encoding': 'utf-8'}

          # {'shortname': 'mywebsite2',
          #  'uri': 'http://www.mywebsite2.com/info',
          #  'type': 'html',
          #  'contentxpath': '//*[contains(concat(\' \', normalize-space(@class), \' \'), \' news-list-container \')]',
          #  'regex': '',
          #  'encoding': 'utf-8'},
          #
          # {'shortname': 'mywebsite3',
          #  'uri': 'http://www.mywebsite3.com/info',
          #  'type': 'text',
          #  'contentxpath': '',
          #  'contentregex': 'Version\"\:\d*\.\d*',
          #  'encoding': 'utf-8'},
          #
          # {'shortname': 'lscmd',
          #  'uri': 'cmd://ls -l /home/pi',
          #  'contentregex': '.*Desktop.*'
          # }

]

subjectPostfix = 'A website has been updated!'

enableMailNotifications = True
sender = "mailwebsitechange@gmail.com"
smtphost = 'smtp.gmail.com'
useTLS = True
smtpport = 587
smtpusername = sender
smtppwd = "teamappcon10"
receiver = "ankur09011@gmail.com,sundaresan14791@gmail.com"

enableRSSFeed = True
rssfile = 'feed.xml'
maxFeeds = 100

