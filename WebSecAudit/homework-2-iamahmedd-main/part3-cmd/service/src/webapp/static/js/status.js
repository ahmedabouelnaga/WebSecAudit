
var STATUS_ENDPOINT = "/status"

function refresh_system_status(hosts,handler)
{
        for(var index = 0; index<hosts.length; index++) {
                setTimeout(function() {
                        var host = hosts[index];
                        console.log(host);
                        return function() {
                                $.post("/status", {ip: host}, handler);
                        };
                }(), 25*index);
        }
}