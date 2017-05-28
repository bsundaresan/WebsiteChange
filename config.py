
subjectPostfix = 'A website has been updated!'

enableMailNotifications = True


sender = "mailwebsitechange@gmail.com"
smtphost = 'smtp.gmail.com'
useTLS = True
smtpport = 587
smtpusername = sender
smtppwd = "teamappcon10"
receiver = "ankur09011@gmail.com,sundaresan14791@gmail.com"

enableRSSFeed = False
rssfile = 'feed.xml'
sites = [

        {'shortname': 'mywebsite17',
         'uri': 'http://ppac.org.in/ViewAllCircular_whtnew_Reports.aspx?ModuleID=30',
         'type': 'html',
         'contentxpath': '',
          'contentregex': '',
          'encoding': 'utf-8'}

    {'shortname': 'mywebsite4',
     'uri': 'http://www.dgca.nic.in/reports/stat-ind.htm',
     'type': 'html',
     'titleregex': '',
     'contentxpath': '',
     'contentregex': '',
     'encoding': 'utf-8'},

        {'shortname': 'mywebsite7',
         'uri': 'http://www.bseindia.com/corporates/ann.aspx?expandable=3',
        'type': 'html',
        'contentxpath': '',
        'contentregex': '',
        'encoding': 'utf-8'},

    {'shortname': 'mywebsite14',
     'uri': 'http://www.cbec.gov.in/Customs-Notifications',
     'type': 'html',
     'contentxpath': '',
     'contentregex': '',
     'encoding': 'utf-8'},

        {'shortname': 'mywebsite16',
          'uri': 'http://www.cea.nic.in/index.html',
          'type': 'html',
          'contentxpath': '',
          'contentregex': '',
          'encoding': 'utf-8'},

          {'shortname': 'mywebsite2',
           'uri': 'http://www.indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,1,304,366,554,818',
           'type': 'html',
           'titleregex': '',
           'contentregex': '',
           'encoding': 'utf-8'},

           {'shortname': 'mywebsite3',
          'uri': 'http://www.indianrailways.gov.in/railwayboard/view_section.jsp?lang=0&id=0,1,304,366,554,1361',
          'type': 'html',
          'titleregex': '',
          'contentxpath': '',
          'contentregex': '',
          'encoding': 'utf-8'},

         #{'shortname': 'mywebsite5',
         # 'uri': 'http://jpcindiansteel.nic.in/pages/display/127',
         # 'type': 'html',
         # 'contentxpath': '',
         # 'contentregex': '',
         # 'encoding': 'utf-8'},

        #{'shortname': 'mywebsite6',
        #'uri': 'http://www.nhai.org/mismenu.asp',
        #'type': 'html',
        #'contentxpath': '',
        #'contentregex': '',
        #'encoding': 'utf-8'},

         #{'shortname': 'mywebsite8',
         # 'uri': 'https://www.rbi.org.in/scripts/NewLinkDetails.aspx',
         # 'type': 'html',
         # 'contentxpath': '',
         # 'contentregex': '',
         # 'encoding': 'utf-8'},

         #{'shortname': 'mywebsite9',
         # 'uri': 'https://www.rbi.org.in/Scripts/NotificationUser.aspx',
         # 'type': 'html',
         # 'contentxpath': '',
          #'contentregex': '',
          #'encoding': 'utf-8'},

         #{'shortname': 'mywebsite10',
         # 'uri': 'https://www.rbi.org.in/scripts/BS_ViewTenders.aspx',
         # 'type': 'html',
         # 'contentxpath': '',
         # 'contentregex': '',
         # 'encoding': 'utf-8'},

         #{'shortname': 'mywebsite11',
         # 'uri': 'http://eands.dacnet.nic.in/Advance_Estimates.htm',
         # 'type': 'html',
         # 'contentxpath': '',
         # 'contentregex': '',
         # 'encoding': 'utf-8'},

        # {'shortname': 'mywebsite12',
         # 'uri': 'http://www.pngrb.gov.in/complaints-disputes.html',
          #'type': 'html',
         # 'contentxpath': '',
         # 'contentregex': '',
         # 'encoding': 'utf-8'},

#         {'shortname': 'mywebsite13',
#          'uri': 'http://www.pngrb.gov.in/public-notice.html',
 #         'type': 'html',
  #        'contentxpath': '',
   #       'contentregex': '',
    #      'encoding': 'utf-8'},

         # {'shortname': 'mywebsite15',
         # 'uri': 'http://mines.nic.in/ViewData/index?mid=1438',
         # 'type': 'html',
         # 'contentxpath': '',
         # 'contentregex': '',
         # 'encoding': 'utf-8'},

    # 'uri': 'http://www.egazette.nic.in/',
    # {'shortname': 'mywebsite1',
    # 'type': 'html',
    # 'titleregex': '',
    # 'contentregex': '',
    # 'encoding': 'utf-8'},
]
maxFeeds = 100

