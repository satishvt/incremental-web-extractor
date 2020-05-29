from crontab import CronTab
 
my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_business.py > /Users/satishvt/kafkaTest/logs/stdout_business.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_cricket.py > /Users/satishvt/kafkaTest/logs/stdout_cricket.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_entertainment.py > /Users/satishvt/kafkaTest/logs/stdout_entertainment.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_health.py > /Users/satishvt/kafkaTest/logs/stdout_health.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_india.py > /Users/satishvt/kafkaTest/logs/stdout_india.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_politics.py > /Users/satishvt/kafkaTest/logs/stdout_politics.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_sports.py > /Users/satishvt/kafkaTest/logs/stdout_sports.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_tech.py > /Users/satishvt/kafkaTest/logs/stdout_tech.log 2>&1')
job.minute.every(1)
my_cron.write()

my_cron = CronTab(user=True)
job = my_cron.new(command='. $HOME/.bash_profile; python /Users/satishvt/kafkaTest/producer_world.py > /Users/satishvt/kafkaTest/logs/stdout_world.log 2>&1')
job.minute.every(1)
my_cron.write()