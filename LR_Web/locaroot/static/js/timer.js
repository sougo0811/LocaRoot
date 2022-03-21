function set_fig(num) {
  var ret;
  if( num < 10 ) { ret = "0" + num; }
  else { ret = num; }
  return ret;
}
function showClock() {
  var nowTime = new Date();
  var nowYear = set_fig( nowTime.getFullYear() );
  var nowMonth = set_fig( nowTime.getMonth() + 1 );
  var nowDay = set_fig( nowTime.getDate() );
  var nowHour = set_fig( nowTime.getHours() );
  var nowMin  = set_fig( nowTime.getMinutes() );
  var nowSec  = set_fig( nowTime.getSeconds() );
  var msg = nowYear + "年" + nowMonth + "月" + nowDay + "日" + nowHour + ":" + nowMin + ":" + nowSec;
  document.getElementById("RealtimeClockArea").innerHTML = msg;
}
setInterval('showClock()',1000);