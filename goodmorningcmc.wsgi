from datetime import datetime
import run
run.SITE = run.load_site_config("cmc")
run.SITE['the_date'] = datetime.now().strftime("%A, %B %d")
application = run.APP
