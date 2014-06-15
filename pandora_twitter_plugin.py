from twython import Twython
import sys

def print_module(module_name,data,is_incremental,type):
    """
    Prints a module acording to Pandora FMS syntax.
    More information at:
    http://wiki.pandorafms.com/index.php?title=Pandora:Documentation_en:Operations#Monitoring_with_the_Software_Agent
    """
    print "<module>"
    print "<name><![CDATA["+module_name+"]]></name>"
    if is_incremental:
        print "<type><![CDATA[generic_"+type+"_inc]]></type>"
    else:
        print "<type><![CDATA[generic_"+type+"]]></type>";
    print "<data><![CDATA["+data+"]]></data>"
    print "</module>"


#Enter this information from http://dev.twitter.com/
TWITTER_KEY = ''
TWITTER_SECRET = ''
TWITTER_OAUTH_TOKEN = ''
TWITTER_OAUTH_SECRET = ''

t = Twython(TWITTER_KEY,TWITTER_SECRET,TWITTER_OAUTH_TOKEN,TWITTER_OAUTH_SECRET)

#Care, we have a max. of 15 queries per 15 minutes
#More information at https://dev.twitter.com/docs/api/1.1/get/account/verify_credentials
try:
    info = t.verify_credentials(skip_status=True,include_entities=False)
except:
    print_module('Twitter plugin','0',False,'proc')
    sys.exit(1)


print_module('Followers',str(info['followers_count']),False,'data')
print_module('Following',str(info['friends_count']),False,'data')
print_module('Twitter plugin','1',False,'proc')
