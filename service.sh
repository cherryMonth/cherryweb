pid=`cat /root/cherryweb/pid.txt`
if [ $1 ==  "start" ]
then
ps -fe|grep $pid |grep -v grep
if [ $? -ne 1 ]
then
echo "error: service cherryweb is running..."
else
nohup python /root/cherryweb/manage.py &
echo "service cherryweb has start"
fi
elif [ $1 ==  "stop" ]
then
ps -fe|grep $pid |grep -v grep
if [ $? -ne 0 ]
then
echo "error: service cherryweb has exit..."
else
kill $pid
echo "$pid was killed"
echo "service cherryweb has exit!"
fi
else
echo "unknow arugments $1 ,service cherryweb only support start and stop!"
fi
